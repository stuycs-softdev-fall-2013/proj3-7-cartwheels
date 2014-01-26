#!/usr/local/bin/python
from website import carts
import urllib2
import json


def load():
    carts.remove_all()
    request = 'http://data.cityofnewyork.us/resource/akqf-qv4n.json'

    for i in range(0, 24000, 1000):
        query = '?$offset=%d' % i
        data = urllib2.urlopen(request + query)

        results = json.loads(data.read())
        data.close()
        required_keys = ['license_permit_holder', 'license_permit_holder_name',
                'license_permit_number', 'permit_issuance_date',
                'permit_expiration_date', 'longitude_wgs84', 'latitude_wgs84',
                'zip_code', 'borough']

        for r in results:
            for k in required_keys:
                if not r.has_key(k):
                    r[k] = ''

            carts.insert(name=r['license_permit_holder'],
                    owner=r['license_permit_holder_name'],
                    permit_number=r['license_permit_number'],
                    issuance=r['permit_issuance_date'],
                    expiration=r['permit_expiration_date'],
                    loc=[ float(r['longitude_wgs84']),
                        float(r['latitude_wgs84']) ],
                    zip_code=r['zip_code'], borough=r['borough'])

    out = [c for c in carts.find()]
    print len(out)
