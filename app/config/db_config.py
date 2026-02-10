import psycopg2

def get_db_connection():
    return psycopg2.connect(
        host="ep-autumn-glade-ahol7e1k-pooler.c-3.us-east-1.aws.neon.tech",
        port="5432",
        user="neondb_owner",
        password="npg_S1qynOMDXYL8",
        dbname="neondb"
    )