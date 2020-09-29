from preprocessing import fdf
from preprocessing import df_rio
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()


X = df_rio[['mileage','power']]
y = df_rio['price']



X_train, X_test, y_train, y_test = train_test_split(X,y)

reg = KNeighborsRegressor(n_neighbors=7).fit(X_train,y_train)
y_pred = reg.predict(X_test)
print("Правильность на обучающем наборе: {:.3f}".format(reg.score(X_train, y_train)))
print("Правильность на тестовом наборе: {:.3f}".format(reg.score(X_test, y_test)))