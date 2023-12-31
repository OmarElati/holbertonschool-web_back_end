#!/usr/bin/env python3
"""
Personal data
"""
import re
from typing import List
import logging
import os
import mysql.connector


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Filter values in incoming log records using filter_datum """
        message = super(RedactingFormatter, self).format(record)
        for field in self.fields:
            message = filter_datum(
                [field],
                self.REDACTION,
                message,
                self.SEPARATOR
                )
        return message


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """ Returns a Logger object """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    formatter = RedactingFormatter(list(PII_FIELDS))
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Get database credentials from environment variables with default values
    """
    user = os.getenv("PERSONAL_DATA_DB_USERNAME", 'root')
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", '')
    host = os.getenv("PERSONAL_DATA_DB_HOST", 'localhost')
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    db = mysql.connector.connect(
        host=host,
        database=db_name,
        user=user,
        password=password
    )

    return db


def main():
    db = get_db()
    
    if db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users;")
        
        logger = get_logger()
        
        for row in cursor:
            filtered_data = filter_datum(
                PII_FIELDS,
                RedactingFormatter.REDACTION,
                "; ".join(map(lambda x: "{}={}".format(x[0], x[1]), zip(PII_FIELDS, row))),
                RedactingFormatter.SEPARATOR
            )
            logger.info(filtered_data)

        cursor.close()
        db.close()


if __name__ == "__main__":
    main()
