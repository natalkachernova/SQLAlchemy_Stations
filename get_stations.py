from sqlalchemy import Table, Column, Integer, String, MetaData, Float, Date
from sqlalchemy import create_engine

engine = create_engine('sqlite:///stations.db')

meta = MetaData()

clean_stations = Table(
   'clean_stations', meta,
   Column('station', String),
   Column('latitude', Float),
   Column('longitude', Float),
   Column('elevation', Float),
   Column('name', String),
   Column('country', String),
   Column('state', String),
)

clean_measure = Table(
   'clean_measure', meta,
   Column('station', String),
   Column('date', Date),
   Column('precip', Float),
   Column('tobs', Integer),
)

conn = engine.connect()
s = clean_stations.select().limit(5)
results = conn.execute(s)

for r in results:
   print(r)

conn = engine.connect()
s = clean_measure.select()
results = conn.execute(s)

for r in results:
   print(r)
