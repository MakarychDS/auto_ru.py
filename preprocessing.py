import json
import numpy as np
import pandas as pd
import sklearn

dict_data = {}
with open('data.json','r', encoding='utf8') as f:
    data = json.load(f)

df = pd.read_json('data.json',encoding='utf8')



ndf = pd.DataFrame()

# обработка json, получаем цену в рублях и добавляем в датасет
dict_p = {}
n = 0
price_list = []

for i in data:
    dict_p[n] = i
    n+= 1

for i in range(len(dict_p)):
    try:

        price_list.append(dict_p[i]['price_info']['price'])
    except:
        price_list.append(np.NaN)




# собираем пробег
mileage_list = []
for i in range(len(dict_p)):
    try:
        mileage_list.append(dict_p[i]['state']['mileage'])
    except:
        mileage_list.append(np.NaN)



#print(ndf.isna().sum())

# собираем название модели
model_list = []
for i in range(len(dict_p)):
    try:
        model_list.append(dict_p[i]['vehicle_info']['model_info']['code'])
    except:
        model_list.append(np.NaN)


# собираем мощность в л.с.
power_list = []
for i in range(len(dict_p)):
    try:
        power_list.append(dict_p[i]['vehicle_info']['tech_param']['power'])
    except:
        power_list.append(np.NaN)

#добавим в датасет колонки в том порядке, в котором удобно на них смотреть
ndf['model'] = model_list
ndf['mileage'] = mileage_list
ndf['power'] = power_list
ndf['price'] = price_list

'''
теперь нам необходимо заменить названия моделей на числа, чтобы
наша обучающаяся модель могла работать с моделями автомобилей
'''
dict_model = {}
k = 0
modeli = ndf.model.unique()
for i in modeli:
    dict_model[i] = k
    k+=1

model_numbers = []
for i in ndf['model']:
    for j in dict_model.keys():
        if i == j:
            model_numbers.append(dict_model[j])
        else:
            continue

ndf['model_number'] = model_numbers

#запишем все в новый датасет вмете с новой колонкой идентификатора модели

df = ndf[['model','model_number','mileage','power','price']]

''' 
print(df.model.value_counts())

RIO         250
CEED        132
SPORTAGE     90
SORENTO      78
CERATO       56
OPTIMA       46
SOUL         15
VENGA        12
QUORIS        9
CEED_GT       7
PICANTO       7
CARNIVAL      4
MOHAVES       3

Видно, что, начиная с модели "SOUL", количество машин очень мало и строить
регресиию по этим моделям будет сложно. Предлагаю выбросить из датасета все модели, 
которые находятся ниже "OPTIMA".
'''
fdf = df
na_vibros = ['SOUL', 'VENGA', 'QUORIS', 'CEED_GT', 'PICANTO', 'CARNIVAL', 'MOHAVES']
for i in na_vibros:
    fdf = fdf[fdf['model'] != i]

# мы получили финальный датасет 'fdf'. С ним можно рабоать, если мы захотим
# провести кластеризацию. Для построения регрессионной модели будет лучше,
# если мы разделим датасет для каждой модели автомобиля

''' выбросим пропуски '''
fdf = fdf.dropna(axis = 0)


df_rio = fdf[fdf['model'] == 'RIO']
df_ceed = fdf[fdf['model'] == 'CEED']
df_sportage = fdf[fdf['model'] == 'SPORTAGE']
df_sorento = fdf[fdf['model'] == 'SORENTO']
df_cerato = fdf[fdf['model'] == 'CERATO']
df_optima = fdf[fdf['model'] == 'OPTIMA']



