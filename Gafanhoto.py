import pandas as pd

'''Frutas = pd.DataFrame({'Apples':[35,41], 'Bananas':[21,34]},
 index= ['2017 sales', '2018 sales'])
print(Frutas)'''


Ingredientes = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index= ['flour', 'milk', 'eggs', 'spam'], name = 'dinner')
print(Ingredientes)

Ingredientes.to_csv("Ingredientes.csv", header=False)



 