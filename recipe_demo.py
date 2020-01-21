import pandas as pd
import sqlite3
from Ingredient import Ingredient
from Direction import Direction

conn_i = sqlite3.connect('ingredients.db')
conn_d = sqlite3.connect('directions.db')

c_i = conn_i.cursor()
c_d = conn_d.cursor()


def insert_ingredient(item):
    with conn_i: #closes the connection w the db when finished
        c_i.execute("INSERT INTO ingredients VALUES (:recipe, :ingredient, :amt )", {'recipe': item.recipe, 'ingredient': item.ingredient, 'amt': item.amt})

def insert_direction(item):
    with conn_d:
        c_d.execute("INSERT INTO directions VALUES (:recipe, :source, :direc )", {'recipe': item.recipe, 'source': item.source, 'direc': item.direc})

def show_ingredients_table():
    with conn_i:
        c_i.execute("SELECT * FROM ingredients")
    return print(c_i.fetchall()) 

def show_directions_table():
    with conn_d:
        c_d.execute("SELECT * FROM directions")
    return print(c_d.fetchall())

x = input("Search for recipes that have these ingredients: ")
# High probability search relevance (search: egg, return: egg)
spec = c_i.execute("SELECT * FROM ingredients WHERE ingredient LIKE '{}' ".format(x))
# Low + high probability search relevance (search: egg, return: egg, veggies, eggplant)
#gen = c_i.execute("SELECT * FROM ingredients WHERE ingredient LIKE '%{}%' ".format(x))

for _ in spec:
    print(_)

#c_d.execute("SELECT recipe FROM directions WHERE recipe LIKE '%{}%' ".format(x))
#print(c_i.fetchall())
#print(c_d.fetchall())

#show_directions_table()
#show_ingredients_table()
c_i.close()
c_d.close()