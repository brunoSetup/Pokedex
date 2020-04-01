from psycopg2 import connect, sql
import psycopg2
import json
from jsonschema2db import JSONSchemaToPostgres

schema = json.load(open('./json-schema/pokemon_schema.json'))
translator = JSONSchemaToPostgres(
    schema
)

con = psycopg2.connect('host=localhost dbname=pokedex user=postgres password=postgres')
translator.create_tables(con)




