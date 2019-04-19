#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""
import re

from config import HTTP_HEADER

__product__ = "AdNovum nevisProxy"


def detect(resp):
    headers = resp.headers

    retval = re.search(r"^Navajo.*?$", headers.get(HTTP_HEADER.SET_COOKIE, ""), re.I) is not None
    
    return retval
