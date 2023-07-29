# Database Connection

from sqlobject.mysql import builder
conn = builder()(user='root', password='123',
                 host='mysql', db='falcon1')
