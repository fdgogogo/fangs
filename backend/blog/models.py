# -*- coding: utf-8 -*-
__author__ = 'fdgogogo'

from backend import db


class BlogCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True)
    order = db.Column(db.SmallInteger, default=0)

    __mapper_args__ = {
        'order_by': order
    }

    def __repr__(self):
        return self.title


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True)
    content = db.Column(db.Text())
    created = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    modified = db.Column(db.DateTime, server_default=db.func.now())

    category_id = db.Column(db.Integer, db.ForeignKey(BlogCategory.id))
    category = db.relationship(BlogCategory, backref=db.backref('posts', lazy='dynamic'))

    def __repr__(self):
        return self.title


class BlogComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    modified = db.Column(db.DateTime, server_default=db.func.now())

    post_id = db.Column(db.Integer, db.ForeignKey(BlogPost.id))
    post = db.relationship(BlogPost, backref=db.backref('comments', lazy='dynamic'))


