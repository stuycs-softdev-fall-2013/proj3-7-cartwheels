#!/usr/local/bin/python
from website.settings import COLLECTIONS
from website import models


def clear():
    for key in COLLECTIONS:
        val = COLLECTIONS[key]
        if val != 'ignore':
            models.db[val].drop()

    models.db.fs.drop()
