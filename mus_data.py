#!
"""Программа для работы с базой данных
"""

import pymongo

dbserver = 'mongodb://localhost:27017'
dbname = 'exdb'
clname = 'unicorns'
client = pymongo.MongoClient(dbserver)
dbs = client.database_names()
db = client[dbname]
cls = db.collection_names(include_system_collections=False)
cl = db[clname]

#test:
if __name__ == '__main__':
    print(cl.find_one({}))
