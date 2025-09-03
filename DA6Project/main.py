import pandas as pd
import numpy as np
from sqlalchemy import create_engine


engine = create_engine('mysql+mysqlconnector://root:root123@localhost/sakila')


def simulate_sql_query():
    actor = pd.read_sql('SELECT * FROM actor', engine)
    film_actor = pd.read_sql('SELECT * FROM film_actor', engine)
    film = pd.read_sql('SELECT * FROM film', engine)
    film_category = pd.read_sql('SELECT * FROM film_category', engine)
    category = pd.read_sql('SELECT * FROM category', engine)

    result = (actor
              .merge(film_actor, on='actor_id', how='left', suffixes=('_actor', '_film_actor'))
              .merge(film, on='film_id', how='left', suffixes=('', '_film'))
              .merge(film_category, on='film_id', how='left', suffixes=('', '_film_category'))
              .merge(category, on='category_id', how='left', suffixes=('', '_category'))
              .groupby(['actor_id', 'first_name', 'last_name', 'name'])
              .agg(category_count=('category_id', 'count'))
              .reset_index()
              .rename(columns={'name': 'category_name'}))

    return result



final_df = simulate_sql_query()
print("RESULT:")
print(final_df.head(15))


