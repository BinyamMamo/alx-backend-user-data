#!/usr/bin/env python3
"""
Task 0. Regex-ing
Write a function called `filter_datum`
that returns the log message obfuscated
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    Filters personal data from log messages

    Parameters:
        fields (list): List of field names to redact
        redaction (str): String to replace redacted data with
        message (str): Log message to filter
        separator (str): Separator between field name and value

    Returns:
        str: Filtered log message
    """
    for field in fields:
        message = re.sub(rf"{field}=(.*?)\{separator}",
                         f'{field}={redaction}{separator}', message)
    return message


if __name__ == "__main__":
    pass
