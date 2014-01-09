#!/usr/local/bin/python
from website.models import Cart
import urllib2
import json

carts = Cart()
carts.remove_all()
host = 'http://data.cityofnewyork.us/resource/xfyi-uyt5.json'
for i in range(0, 7000, 1000):
    query = 'permit_type_description=MOBILE+FOOD+UNIT&$offset=%d' % i
    request = host + '?' + query
    data = urllib2.urlopen(request)

    results = json.loads(data.read())
    data.close()
    required_keys = ['longitude_wgs84', 'latitude_wgs84', 'street', 'address', 'zip_code', 'borough', 'license_permit_holder']
    for r in results:
        for k in required_keys:
            if not r.has_key(k):
                r[k] = None

        carts.insert(lat=r['latitude_wgs84'], lng=r['longitude_wgs84'],
                street=r['street'], address=r['address'],
                zip_code=r['zip_code'], borough=r['borough'],
                owner=r['license_permit_holder'])

out = [c for c in carts.find()]
print len(out)
