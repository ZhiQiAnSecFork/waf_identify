#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from config import HTTP_HEADER

__product__ = "Imunify360 (CloudLinux Inc.)"


def detect(resp):
    page = resp.text
    headers = resp.headers

    retval = re.search(r"\Aimunify360", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
    retval |= any(
        _ in (page or "") for _ in ("protected by Imunify360", "Powered by Imunify360", "imunify360 preloader"))
    
    return retval
