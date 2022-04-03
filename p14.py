# create csv file from dataframe given that dataframe contains information (name, age, gender, hobbies, number of mutual friends)
import pandas as pd
dict = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'age': [12, 13, 10, 14, 15, 12, 13, 10, 14, 15],
    'gender': ['f', 'm', 'f', 'm', 'f', 'm', 'f', 'm', 'f', 'm'],
    'hobbies': ['football', 'swimming', 'chess', 'football', 'swimming', 'chess', 'football', 'swimming', 'chess', 'chess'],
    'mfriend': [2, 3, 1, 4, 5, 2, 3, 0, 4, 5],
}
df = pd.DataFrame(dict)
df.to_csv('q5.csv', index=False)
# print first 3 rows 
print(df.head(3))
# print last 3 rows
print(df.tail(3))
