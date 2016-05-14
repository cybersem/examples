#!
"""Программа для работы с базой данных
"""

import datetime
import pymongo

logfile = open('mus.log', 'a')
dbserver = 'mongodb://localhost:27017'
dbname = 'exdb'
clname = 'unicorns'

#Подключение к БД:
client = pymongo.MongoClient(dbserver)
dbs = client.database_names()
db = client[dbname]
cls = db.collection_names(include_system_collections=False)
cl = db[clname]
sstate = 'Ok' if cl else 'Error'
strlog = '%s - Подсоединение к БД --> %s' % (datetime.datetime.now().strftime('%d.%m.%Y %I:%M:%S %P'), sstate)
print(strlog, file=logfile)

#Добавление группы:
class Group:
    def __init__(self):
        pass

group = Group()    
group.name = input('Введите название группы >>')
group.year = input('Введите год создания группы >>')
group.style = input('Введите музыкальный стиль >>')

group.album = None

input('Название альбома >>')
input('Год выпуска альбома >>')

"""
Альбом 1. 1980
    трек 1
    трек 2
    трек 3

Альбом 2. 1983
    трек 1
    трек 2

Альбом 3.1988
    трек 1
    трек 2
    трек 3

[{'name': 'al1', 'year': '1980'},
{'name': 'al2', 'year': '1983'}]

"""


#Завершение программы:
logfile.close()

#test:
if __name__ == '__main__':
    print(cl.find_one({}))
