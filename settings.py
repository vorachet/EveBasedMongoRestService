import sys
import imp

try:
    imp.find_module('dbconf')
except ImportError:
    print("dbconf.py does not exist.  See README on https://github.com/vorachet/EveBasedMongoRestService")
    sys.exit()

import dbconf

MONGO_HOST = dbconf.CONFIG['MONGO_HOST']
MONGO_PORT = dbconf.CONFIG['MONGO_PORT']
MONGO_USERNAME = dbconf.CONFIG['MONGO_USERNAME']
MONGO_PASSWORD = dbconf.CONFIG['MONGO_PASSWORD']
MONGO_DBNAME = dbconf.CONFIG['MONGO_DBNAME']

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

schema = {
    'firstname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
    },
    'lastname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
        'required': True,
        'unique': True,
    },
    'role': {
        'type': 'list',
        'allowed': ["author", "contributor", "copy"],
    },
    'location': {
        'type': 'dict',
        'schema': {
            'address': {'type': 'string'},
            'city': {'type': 'string'}
        },
    },
    'born': {
        'type': 'datetime',
    },
}

people = {
    'item_title': 'person',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'lastname'
    },
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST'],
    'schema': schema
}

DOMAIN = {
    'people': people
}
