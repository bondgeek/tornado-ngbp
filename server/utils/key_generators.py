#!/usr/bin/env python
"""
From:  https://gist.github.com/didip/823887

"""

import base64
import uuid


def cookie_secret():
    return unicode(
        base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
    )
