import json
import psycopg2
from datetime import datetime


with open('../json/us_states.json', 'r') as f:
    d = json.load(f)
f = d['features']
sql = '''INSERT INTO news_app_region (name, created_on, updated_on,
         region_category_id, census_area, geo_id, state_number)
         VALUES (%s, %s, %s, %s, %s, %s, %s);'''
cnxn = psycopg2.connect(dbname='news_app',
                        user='postgres',
                        password='mysecretpassword',
                        host='localhost')
crsr = cnxn.cursor()
for feature in f:
    crsr.execute(sql, [feature['properties']['NAME'],
                       datetime.now(),
                       datetime.now(),
                       1,
                       feature['properties']['CENSUSAREA'],
                       feature['properties']['GEO_ID'],
                       feature['properties']['STATE']])
crsr.execute('commit')

with open('../json/north_america.json', 'r') as f:
    d = json.load(f)
f = d['features']
sql = '''INSERT INTO news_app_region (name, created_on, updated_on,
         region_category_id, census_area, geo_id, state_number)
         VALUES (%s, %s, %s, %s, %s, %s, %s);'''
cnxn = psycopg2.connect(dbname='news_app',
                        user='postgres',
                        password='mysecretpassword',
                        host='localhost')
crsr = cnxn.cursor()
for feature in f:
    crsr.execute(sql, [feature['properties']['name'],
                       datetime.now(),
                       datetime.now(),
                       3,
                       None,
                       feature['properties']['adm0_a3'],
                       None])
crsr.execute('commit')
