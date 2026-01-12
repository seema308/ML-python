
"""import numpy as np
import time

SIZE = 100000
L1 = range(SIZE)
L2 = range(SIZE)
A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

# List addition
start = time.time()
result = [x + y for x, y in zip(L1, L2)]
print("List addition time (ms):", (time.time() - start) * 1000)

# NumPy addition
start = time.time()
result = A1 + A2
print("NumPy addition time (ms):", (time.time() - start) * 1000)"""


"""import pandas as pd
import numpy as np
dict={'First Score':[100,90,np.nan,95],
      'Second Score':[30,45,56,np.nan],
      'Third Score':[np.nan,40,80,90]}
df=pd.DataFrame(dict)
df.isnull()"""


# import pandas as pd
# dicr= {'name':["aparna","pankaj","sudhir","geeku"],
#       'degree':["MBA","BCA","M.Tech","MCA"],
#       'score':[90,40,80,98]}
# df=pd.DataFrame(dict)
# for i,j in df.iterrows():
#     print(i,j)
#     print()





# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# # Load CSV files (make sure they exist in the same folder)
# df1 = pd.read_csv('df1.csv', index_col=0)
# df2 = pd.read_csv('df2.csv')

# # Inspect the data
# print(df1.head())
# print(df2.info())

# # Plot as bar chart (only numeric columns will be plotted)
# df2.plot.bar()
# df1.plot.scatter(x ='A', y ='B')
# df1.plot(style=['-', '--', '-.', ':'], title='Line Plot with Different Styles', xlabel='Index', ylabel='Values', grid=True)
# # Show the plot
# plt.show()



# import matplotlib.pyplot as plt

# # Data for the pie chart
# labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
# sizes = [25, 30, 20, 25]   # percentage values
# colors = ['green', 'yellow', 'pink', 'brown']
# explode = (0, 0.1, 0, 0)   # "explode" the 2nd slice (Bananas)

# # Create the pie chart
# plt.pie(
#     sizes, 
#     labels=labels, 
#     colors=colors, 
#     explode=explode, 
#     autopct='%1.1f%%',   # show percentages
#     shadow=True, 
#     startangle=140
# )

# plt.title("Fruit Distribution")
# plt.axis('equal')  # Equal aspect ratio ensures the pie is circular
# plt.show()

  

# import seaborn as sns
# import matplotlib.pyplot as plt

# # Example dataset
# data = [12, 15, 14, 10, 18, 20, 22, 19, 17, 16, 15, 14, 13, 12, 11]

# # Kernel Density Plot
# sns.kdeplot(data, fill=True, color="blue", linewidth=2)

# # Labels
# plt.title("Kernel Density Plot")
# plt.xlabel("Values")
# plt.ylabel("Density")

# plt.show()


# import seaborn as sns
# import matplotlib.pyplot as plt

# # Set Seaborn style
# sns.set_style("darkgrid")

# # Example plot
# data = [1, 2, 3, 4, 5]
# plt.plot(data)
# plt.show()


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import warnings as wr
# wr.filterwarnings('ignore')
# df = pd.read_csv('WineQT.csv')
# print(df.head())
# df.shape
# df.info()
# df.describe().T
# df.columns.tolist()
# quality_counts = df['quality'].value_counts()

# plt.figure(figsize=(8, 6))
# plt.bar(quality_counts.index, quality_counts, color='deeppink')
# plt.title('Count Plot of Quality')
# plt.xlabel('Quality')
# plt.ylabel('Count')
# plt.show()

# sns.set_style("darkgrid")

# numerical_columns = df.select_dtypes(include=["int64", "float64"]).columns

# plt.figure(figsize=(14, len(numerical_columns) * 3))
# for idx, feature in enumerate(numerical_columns, 1):
#     plt.subplot(len(numerical_columns), 2, idx)
#     sns.histplot(df[feature], kde=True)
#     plt.title(f"{feature} | Skewness: {round(df[feature].skew(), 2)}")
# import matplotlib.pyplot as plt

# plt.plot([1, 2, 3], [4, 5, 6])
# plt.show(block=False)
# plt.tight_layout()
# plt.show()


# plt.figure(figsize=(10, 8))
# sns.swarmplot(x="quality", y="alcohol", data=df, palette='viridis')
# plt.title('Swarm Plot for Quality and Alcohol')
# plt.xlabel('Quality')
# plt.ylabel('Alcohol')
# plt.show()


# sns.set_palette("Pastel1")
# plt.figure(figsize=(10, 6))
# sns.pairplot(df)
# plt.suptitle('Pair Plot for DataFrame')
# plt.show()


# df['quality'] = df['quality'].astype(str)  
# plt.figure(figsize=(10, 8))
# sns.violinplot(x="quality", y="alcohol", data=df, palette={
# '3': 'lightcoral', '4': 'lightblue', '5': 'lightgreen', '6': 'gold', '7': 'lightskyblue', '8': 'lightpink'}, alpha=0.7)
# plt.title('Violin Plot for Quality and Alcohol')
# plt.xlabel('Quality')
# plt.ylabel('sulphates')
# plt.show()

# sns.boxplot(x='quality', y='alcohol', data=df)


# plt.figure(figsize=(15, 10))
# sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap='Pastel2', linewidths=2)
# plt.title('Correlation Heatmap')
# plt.show()


# Linear Regression using scikit-learn
# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt

# # Example dataset
# # X = independent variable (hours studied)
# # y = dependent variable (exam score)
# X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
# y = np.array([1.5, 3.7, 4.2, 5.0, 7.1])

# # Create and train model
# model = LinearRegression()
# model.fit(X, y)

# # Predict
# y_pred = model.predict(X)

# # Print coefficients
# print("Slope (m):", model.coef_[0])
# print("Intercept (b):", model.intercept_)

# # Plot
# plt.scatter(X, y, color="blue", label="Data points")
# plt.plot(X, y_pred, color="red", label="Regression line")
# plt.xlabel("Hours studied")
# plt.ylabel("Exam score")
# plt.legend()
# plt.show()







