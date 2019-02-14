import os
import psycopg2

DATABASE_URI = os.getenv("DATABASE_PROC_URL",'')
con = psycopg2.connect(DATABASE_URI)
cur = con.cursor()


"""Delete database"""
schema = """DROP SCHEMA IF EXISTS politico CASCADE;"""
cur = con.cursor()
cur.execute(schema)
con.commit()