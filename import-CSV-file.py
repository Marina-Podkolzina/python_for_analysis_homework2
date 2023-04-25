import pandas as pd
df = pd.read_csv(r'C:/Users/obluch/Downloads/kc_house_data.csv', encoding='latin-1')
df.head()
print(df.head()) # Вывести на экран первые 5 строк

# Задание 2
# Проведите первичный анализ данных
#Изучите типы данных
#Найдите количество пропущенных ячеек в данных
#Посчитайте основные статистики по всем признакам и поизучайте их
#Пишите выводы

df.info()

df.describe()
print(df.describe())
# В таблице   числовые типы данных int64(15), float64(5)и  данные типа object(1).
#Таблица не содержит пустых ячеек.

#Задание 3

#3.1  В каком диапазоне изменяются стоимости недвижимости?
df['price'].min(), df['price'].max()
print(df['price'].min(),df['price'].max()) #  Ответ: 75000.0,    7700000.0

#3.2  Какую долю в среднем занимают жилая площадь от всей площади по всем домам?

df['sqft_living'].mean() * 100/ df['sqft_lot'].mean()
print(df['sqft_living'].mean() * 100/ df['sqft_lot'].mean()) # ответ: 13.76781757959227

#3.3  Как много домов с разными этажами в данных?

df['floors'].value_counts()
print(df['floors'].value_counts())

#3.4  Насколько хорошие состояния у домов в данных?

df['condition'].value_counts()
print(df['condition'].value_counts())

#3.5  Найдите года, когда построили первый дом, когда построили последний дом в данных?

df['yr_built'].min(), df['yr_built'].max()
print(df['yr_built'].min(),df['yr_built'].max()) # Ответ: 1900 год,  2015 год

# Задание 4
#4.1 Сколько в среднем стоят дома, у которых 2 спальни?

df[df['bedrooms'] == 2] ['price'].mean()
print(df[df['bedrooms'] == 2] ['price'].mean())  # Ответ: 401372.681884058

#4.2 Какая в среднем общая площадь домов, у которых стоимость больше 600 000?

df[df['price'] > 600000]['sqft_lot'].mean()
print(df[df['price'] > 600000]['sqft_lot'].mean()) # ответ: 20442.524776214832

#4.3 Как много домов коснулся ремонт?

df[(df['yr_renovated'] != 0)].shape[0]
print(df[(df['yr_renovated'] != 0)].shape[0]) # ответ: 914


#4.4 Насколько в среднем стоимость домов с оценкой grade домов выше 10 отличается от стоимости домов с оценкой grade меньше 4?

p_10 = df[df['grade'] > 10]['price'].mean()
print(p_10)                                # ответ: 1678635.1175298805
p_4 = df[df['grade'] < 4]['price'].mean()
print(p_4)                                 # ответ: 189750.0
a = p_10 - p_4
print(a)                                   # ответ: 1488885.1175298805

# Задание 5 
# 5.1 Выберите дом клиенту
#Клиент хочет дом с видом на набережную, как минимум с тремя ванными и с подвалом. Сколько вариантов есть у клиента? 

df[(df['waterfront']== 1) & (df['bathrooms'] >= 3) & (~(df['sqft_basement'] == 0)) ].shape[0]
print(df[(df['waterfront']== 1) & (df['bathrooms'] >= 3) & (~(df['sqft_basement'] == 0)) ].shape[0]) # ответ: 41

#5.2 Выберите дом клиенту
#Клиент хочет дом либо с очень красивым видом из окна, либо с видом на набережную, в очень хорошем состоянии и год постройки не меньше 1980 года. В какой ценовом диапазоне будут дома?

choice = ((df['view'] == 4) | (df['waterfront'] == 1)) & (df['condition'] == 5) & (df['yr_built'] >= 1980)
client_choice = df[choice]
client_choice['price'].min(), client_choice['price'].max()
print(client_choice['price'].min(), client_choice['price'].max()) # Ответ: 1295000.0 3000000.0

#5.3 Выберите дом клиенту
#Клиент хочет дом без подвала, с двумя этажами, стоимостью до 150000. Какая оценка по состоянию у таких домов в среднем?

client_choice = df[(df['sqft_basement'] == 0) & (df['floors'] == 2) & (df['price'] < 150000)]
client_choice['condition'].mean()
print(client_choice['condition'].mean()) # Ответ: 2.8333333333333335