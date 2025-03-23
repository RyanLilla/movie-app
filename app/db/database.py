import sqlite3
import csv
import pandas as pd


def fetch_one_movie():
    with sqlite3.connect("database.db") as conn:
        
        cur = conn.cursor()
        
        # Drop the table if it exists
        # cur.execute("DROP TABLE IF EXISTS movie")
        # cur.execute("CREATE TABLE movie(id, genre_ids, overview, popularity, release_date, title, vote_average, vote_count)")

        # Execute a query to fetch one row
        cur.execute("SELECT * FROM movie LIMIT 1")
        
        # Fetch one row
        row = cur.fetchone()
        
        if row:
            print("Fetched movie:", row)
        else:
            print("No movie found")