Eve-Based Restful Service Template
===================================

Hi!

Eve-based Restful service project template. This project helps me to setup an Eve-based backend in a minute.


Eve (http://python-eve.org/) is an open source Python REST API framework designed for human beings. It allows to effortlessly build and deploy highly customizable, fully featured RESTful Web Services.

Get the tempalte
.. code::
  git clone https://github.com/vorachet/EveBasedMongoRestService.git
  cd EveBasedMongoRestService

Create dbconf.py
.. code::
  CONFIG = {
    'MONGO_HOST': 'YourMongoDBHost',
    'MONGO_PORT': 'YourMongoDBPort',
    'MONGO_USERNAME': 'user',
    'MONGO_PASSWORD': 'password',
    'MONGO_DBNAME': 'database'
  }

Run server
.. code::
  pip install eve
  python run.py

Create new data
.. code::
  curl -d '[{"firstname": "barack", "lastname": "obama"}, {"firstname": "miney"}]' -H 'Content-Type: application/json'  http://127.0.0.1:5000/people

Get new data
.. code::
  curl http://127.0.0.1:5000/people

  {"_items": [{"_id": "5aa7f1060074b339afb32787", "firstname": "barack", "lastname": "obama", "_updated": "Tue, 13 Mar 2018 15:40:51 GMT", "_created": "Tue, 13 Mar 2018 15:40:51 GMT", "_etag": "bd7f8dcbff70fce70701964593751a48017abe66", "_links": {"self": {"title": "person", "href": "people/5aa7f1060074b339afb32787"}}}, {"_id": "5aa7f1060074b339afb32788", "firstname": "mitt", "lastname": "romney", "_updated": "Tue, 13 Mar 2018 15:40:51 GMT", "_created": "Tue, 13 Mar 2018 15:40:51 GMT", "_etag": "cea69abae1dfb128809ad0c94286020c186a2e62", "_links": {"self": {"title": "person", "href": "people/5aa7f1060074b339afb32788"}}}], "_links": {"parent": {"title": "home", "href": "/"}, "self": {"title": "people", "href": "people"}}, "_meta": {"page": 1, "max_results": 25, "total": 2}}

