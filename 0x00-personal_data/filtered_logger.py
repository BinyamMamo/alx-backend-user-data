#!/usr/bin/env python3
"""
Task 0. Regex-ing
Write a function called `filter_datum`
that returns the log message obfuscated
"""
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        """ Initialize the RedactingFormatter object
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ Format the log record by filtering sensitive data
        """
        return filter_datum(self.fields, self.REDACTION,
                        super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
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
