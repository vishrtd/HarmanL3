import pandas as pd

from harman.preprocess.CleanData import CleanData
from harman.preprocess.CreateFeatures import CreateFeatures
from harman.read.ReadCsv import ReadCsv

# Read Csv

file_path = r'D:\programming\pyspark\notebook\harman\salesdaily.csv'
csv_reader = ReadCsv(file_path=file_path)
# print(csv_reader.data.head(5))
# print(csv_reader.data.columns)

# Check that the clean data class produces expected output on melt_data
cd = CleanData(csv_reader.data)
id_vars = 'datum'
value_vars = ['M01AB', 'M01AE']
cd.melt_data(id_vars=id_vars, value_vars=value_vars)
df2 = cd.get_data()
# print(cd.get_data())

features = CreateFeatures(df2)
features.calculate_rolling_average(5, 14, 50)
# print(features.get_data())
# print(features.data.columns)

# Generate ML Model
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

csv_reader = ReadCsv(file_path=file_path)

clean_data = CleanData(csv_reader.get_data())
clean_data.melt_data('datum', ['M01AB', 'M01AE'])
features = CreateFeatures(clean_data.get_data())
features.calculate_rolling_average(7*10)
print(features.get_data())

ml_df = features.get_data()
ml_df.dropna(inplace=True)

# X = ml_df['value'].values
# y = ml_df['value_70'].values

X_train, X_test, y_train, y_test = train_test_split(ml_df[['value']], ml_df[['value_70']], test_size=0.3)

# sc_X = StandardScaler()
# X_train = sc_X.fit_transform(X_train)
rfr = RandomForestRegressor()
rfr.fit(X_train, y_train)
y_pred = rfr.predict(X_test)

from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R2 Score: {r2}')

# We can check how much the data varies
from matplotlib import pyplot as plt
plt.scatter(X_test, y_test, color='black', label='Actual')
plt.scatter(X_test, y_pred, color='blue', label='Predicted')
plt.xlabel('value')
plt.ylabel('Predictions')
plt.legend('Harman Sales Predictions')
plt.show()
