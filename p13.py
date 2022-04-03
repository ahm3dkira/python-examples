# write panda program to select 'name' and 'score' from the following dataframe:
from cProfile import label
import pandas as pd
data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9.0, 16.5, 4, 9.5, 20.0, 14.5, 8, 8.0, 19.0],
        'attempts': [1, 3, 2, 2, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'yes', 'yes', 'no', 'yes', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data, index=labels)
# print(df)
# print(df.loc[['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], ['name', 'score']])
print(df.loc[labels, ['name', 'score']])
