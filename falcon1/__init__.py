# from sqlobject import sqlhub, connectionForURI

# connect_string = "mysql://roci:root-roci@localhost/falcon1"
# conn = connectionForURI(connect_string)
# sqlhub.processConnection = conn

from sqlobject.mysql import builder
conn = builder()(user='root', password='123',
                 host='mysqldb', db='falcon1')
# conn = builder()(user='roci', password='root-roci',
#                  host='localhost', db='falcon1')
