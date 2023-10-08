#!/usr/bin/env python3
"""
Personal data
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ function called filter_datum returns the log message obfuscated """
    lst = message.split(separator)

    for f in fields:
        for i in range(len(lst)):
            if lst[i].startswith(f):
                subst = f + '=' + redaction
                lst[i] = re.sub(lst[i], '', lst[i])
                lst[i] = subst
    return separator.join(lst)
