#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from lib.url import Url
from templates.profile import Profile
from templates.update import Update
from templates.comment import Comment
from templates.repost import Repost

class Template(object):

    def build(self, module, method, response):
        shortener = Url()
        constructor = globals()[module]
        instance = constructor(response, shortener, method)
        if method == 'post':
            return instance.post_text()
        elif method == 'delete':
            return instance.delete_text()
        else:
            return instance.get_text()
