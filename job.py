import pandas as pd
data = pd.read_html("https://en.wikipedia.org/wiki/List_of_United_States_cities_by_area")
df = data[1]
print(df)
df.to_csv("Users\jashu\Desktop\HNew.csv",sep = '\t', encoding='utf-8', index = False)