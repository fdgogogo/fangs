""" Modified from Mezzanine's wordpress_import script

Author: Jiaan Fang <fduodev@gmail.com>

This script is used by myself to import posts from fduo.org, the compatibility
is not tested, use at your own risk.

"""

from __future__ import unicode_literals

from collections import defaultdict
from datetime import datetime, timedelta
from time import mktime, timezone
from xml.dom.minidom import parse
import re

from flask.ext.script import Command, Option
from flask.ext.script.commands import InvalidCommand
from slugify import slugify

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')


def escape(text):
    """
    Returns the given text with ampersands, quotes and angle brackets encoded
    for use in HTML.

    This function always escapes its input, even if it's already escaped and
    marked as such. This may result in double-escaping. If this is a concern,
    use conditional_escape() instead.
    """
    return text.replace('&', '&amp;'). \
        replace('<', '&lt;'). \
        replace('>', '&gt;').replace('"', '&quot;'). \
        replace("'", '&#39;')


def normalize_newlines(text):
    """Normalizes CRLF and CR newlines to just LF."""
    # text = force_text(text)
    re_newlines = re.compile(r'\r\n|\r')  # Used in normalize_newlines
    return re_newlines.sub('\n', text)


def linebreaks(value, autoescape=False):
    """Converts newlines into <p> and <br />s."""
    value = normalize_newlines(value)
    paras = re.split('\n{2,}', value)
    if autoescape:
        paras = ['<p>%s</p>' % escape(p).replace('\n', '<br />') for p in
                 paras]
    else:
        paras = ['<p>%s</p>' % p.replace('\n', '<br />') for p in paras]
    return '\n\n'.join(paras)


class ImportWordpress(Command):
    """
    Implements a Wordpress importer. Takes a file path or a URL for the
    Wordpress Extended RSS file.
    """
    option_list = (
        Option('--input-xml', '-i', dest='input_xml'),
        Option('--flush', '-f', action='store_true', dest='flush')
    )

    def run(self, input_xml, flush, **kwargs):

        self.handle_import({'url': input_xml, 'flush': flush})

    def get_text(self, xml, name, nodetype):
        """
        Gets the element's text value from the XML object provided.
        """
        nodes = xml.getElementsByTagName("wp:comment_" + name)[0].childNodes
        return "".join([n.data for n in nodes if n.nodeType == nodetype])

    def handle_import(self, options):
        """
        Gets the posts from either the provided URL or the path if it
        is local.
        """
        url = options.get("url")
        flush = options.get('flush')
        if flush:
            from backend.blog.models import BlogCategory, BlogComment, BlogPost
            BlogComment.query.delete()
            BlogPost.query.delete()
            BlogCategory.query.delete()

        if url is None:
            raise InvalidCommand("Usage is import_wordpress ")
        try:
            import feedparser
        except ImportError:
            raise InvalidCommand("Could not import the feedparser library.")
        feed = feedparser.parse(url)

        # We use the minidom parser as well because feedparser won't
        # interpret WXR comments correctly and ends up munging them.
        # xml.dom.minidom is used simply to pull the comments when we
        # get to them.
        xml = parse(url)
        xmlitems = xml.getElementsByTagName("item")

        for (i, entry) in enumerate(feed["entries"]):
            # Get a pointer to the right position in the minidom as well.
            xmlitem = xmlitems[i]
            content = linebreaks(self.wp_caption(entry.content[0]["value"]))

            # Get the time struct of the published date if possible and
            # the updated date if we can't.
            pub_date = getattr(entry, "published_parsed", entry.updated_parsed)
            if pub_date:
                pub_date = datetime.fromtimestamp(mktime(pub_date))
                pub_date -= timedelta(seconds=timezone)

            # Tags and categories are all under "tags" marked with a scheme.
            terms = defaultdict(set)
            for item in getattr(entry, "tags", []):
                terms[item.scheme].add(item.term)
            if entry.wp_post_type == "post":
                post = self.add_post(title=entry.title, content=content,
                                     pub_date=pub_date, tags=terms["post_tag"],
                                     categories=terms["category"],
                                     old_url=entry.id)

                # Get the comments from the xml doc.
                for c in xmlitem.getElementsByTagName("wp:comment"):
                    name = self.get_text(c, "author", c.CDATA_SECTION_NODE)
                    email = self.get_text(c, "author_email", c.TEXT_NODE)
                    url = self.get_text(c, "author_url", c.TEXT_NODE)
                    body = self.get_text(c, "content", c.CDATA_SECTION_NODE)
                    pub_date = self.get_text(c, "date_gmt", c.TEXT_NODE)
                    fmt = "%Y-%m-%d %H:%M:%S"
                    pub_date = datetime.strptime(pub_date, fmt)
                    pub_date -= timedelta(seconds=timezone)
                    self.add_comment(post=post, name=name, email=email,
                                     body=body, website=url,
                                     pub_date=pub_date)

                    # elif entry.wp_post_type == "page":
                    #     old_id = getattr(entry, "wp_post_id")
                    #     parent_id = getattr(entry, "wp_post_parent")
                    #     self.add_page(title=entry.title, content=content,
                    #                   tags=terms["tag"], old_id=old_id,
                    #                   old_parent_id=parent_id)
    @staticmethod
    def content_processor(content):
        content, count = re.subn(r'\[cci\]', '<code>', content)
        content, count = re.subn(r'\[/cci\]', '</code>', content)
        content, count = re.subn(r'\[ccb.*?\]', '<pre><code>', content)
        content, count = re.subn(r'\[/ccb.*?\]', '</code></pre>', content)
        return content

    def add_post(self, **kwargs):
        from backend.blog.models import BlogPost, BlogCategory
        from backend import db

        post = BlogPost()
        title = kwargs.get('title')
        post.title = title[:128]
        post.slug = slugify(title)[:128]
        post.content = self.content_processor(kwargs.get('content'))

        post.created = kwargs.get('pub_date')
        post.tags = kwargs.get('tags')

        categories = kwargs.get('categories')

        if categories:
            for category_name in categories:
                category_obj = BlogCategory.query.filter_by(
                    title=category_name).first()
                if not category_obj:
                    category_obj = BlogCategory()
                    category_obj.title = category_name[:128]
                    category_obj.slug = slugify(category_name)
                    db.session.add(category_obj)
                    db.session.commit()
                post.category = category_obj

        db.session.add(post)
        db.session.commit()

        return post

    def add_comment(self, **kwargs):
        from backend.blog.models import BlogComment
        from backend import db
        post = kwargs.get('post')

        comment = BlogComment()
        comment.post = post
        comment.website = kwargs.get('website')
        comment.author = kwargs.get('name')
        comment.author_email = kwargs.get('email')
        comment.content = kwargs.get('body')
        comment.created = kwargs.get('pub_date')

        db.session.add(comment)
        db.session.commit()

    def wp_caption(self, post):
        """
        Filters a Wordpress Post for Image Captions and renders to
        match HTML.
        """
        for match in re.finditer(r"\[caption (.*?)\](.*?)\[/caption\]", post):
            meta = '<div '
            caption = ''
            for imatch in re.finditer(r'(\w+)="(.*?)"', match.group(1)):
                if imatch.group(1) == 'id':
                    meta += 'id="%s" ' % imatch.group(2)
                if imatch.group(1) == 'align':
                    meta += 'class="wp-caption %s" ' % imatch.group(2)
                if imatch.group(1) == 'width':
                    width = int(imatch.group(2)) + 10
                    meta += 'style="width: %spx;" ' % width
                if imatch.group(1) == 'caption':
                    caption = imatch.group(2)
            parts = (match.group(2), caption)
            meta += '>%s<p class="wp-caption-text">%s</p></div>' % parts
            post = post.replace(match.group(0), meta)
        return post
