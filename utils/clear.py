#!/usr/local/bin/python
from website.models import Collection
from website.settings import COLLECTIONS

models = Collection()

for key in COLLECTIONS:
    val = COLLECTIONS[key]
    if val != 'ignore':
        models.db[val].drop()

models.db.fs.drop()
