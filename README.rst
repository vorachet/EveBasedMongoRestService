Eve Based Mongo Restful Service Template
=========================================

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

Learn more aobut Eve http://python-eve.org/