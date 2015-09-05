# -*- coding: utf-8 -*-

from backend import db


class BlogCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True)
    slug = db.Column(db.String(128), unique=True, index=True)

    order = db.Column(db.SmallInteger, default=0)

    parent_id = db.Column(db.Integer, db.ForeignKey('blog_category.id'),
                          index=True)
    parent = db.relationship(lambda: BlogCategory,
                             remote_side=id,
                             backref=db.backref('sub_categories',
                                                lazy='dynamic'))

    __mapper_args__ = {
        'order_by': order
    }

    def __repr__(self):
        return self.title


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True)
    slug = db.Column(db.String(128), unique=True, index=True)

    content = db.Column(db.Text())
    created = db.Column(db.DateTime, server_default=db.func.now(),
                        onupdate=db.func.now())
    modified = db.Column(db.DateTime, server_default=db.func.now())

    category_id = db.Column(db.Integer, db.ForeignKey('blog_category.id'),
                            index=True)
    category = db.relationship(lambda: BlogCategory,
                               backref=db.backref('posts', lazy='dynamic'))

    def __repr__(self):
        return self.title


class BlogComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now(),
                        onupdate=db.func.now())
    modified = db.Column(db.DateTime, server_default=db.func.now())

    # title = db.Column(db.String(128))
    author = db.Column(db.String(128))
    author_email = db.Column(db.String(128))
    author_website = db.Column(db.String(128), nullable=True)

    content = db.Column(db.Text)

    by_author = db.Column(db.Boolean, default=False)

    replied_to_id = db.Column(db.Integer, db.ForeignKey('blog_comment.id'),
                              index=True)
    replied_to = db.relationship(lambda: BlogComment,
                                 remote_side=id,
                                 backref=db.backref('sub_comments',
                                                    lazy='dynamic'))

    post_id = db.Column(db.Integer, db.ForeignKey(BlogPost.id), index=True)
    post = db.relationship(BlogPost,
                           backref=db.backref('comments', lazy='dynamic'))
