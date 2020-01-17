import pandas as pd

df = pd.read_excel ('Ingredients.xlsx')
print (df.loc[1,:])

# Next steps add all to a ingredients database