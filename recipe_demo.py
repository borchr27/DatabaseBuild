import pandas as pd
import sqlite3
from Ingredient import Ingredient

conn = sqlite3.connect('ingredients.db')

c = conn.cursor()

#df = pd.read_excel ('Ingredients.xlsx')

def insert_ingredient(item):
    with conn: #closes the connection w the db when finished
        c.execute("INSERT INTO ingredients VALUES (:recipe, :ingredient, :amt )", {'recipe': item.recipe, 'ingredient': item.ingredient, 'amt': item.amt})
'''
# Adds all items from excel file into database (maybe delete items afterwards?)
for i in range(len(df)):
    new  = Ingredient(str(df.loc[i][0]), str(df.loc[i][1]), str(df.loc[i][2]))
    insert_ingredient(new)
'''

def show_all():
    with conn:
        c.execute("SELECT * FROM ingredients")
    return print(c.fetchall()) 

show_all()
conn.close()