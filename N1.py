"""import pandas as pd

# Read CSV from same folder as your .py file
df = pd.read_csv('heart.csv')

X = df.drop('target', axis=1)
y = df['target']

print(df.head())"""


from sklearn.preprocessing import MinMaxScaler

# Features to normalize
features = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']

# Initialize scaler
scaler = MinMaxScaler()

# Copy original data
X_normalized = X.copy()

# Apply Min-Max scaling
X_normalized[features] = scaler.fit_transform(X[features])

# View result
X_normalized.head()


"""from sklearn.preprocessing import StandardScaler

# Features to standardize
features = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']

# Initialize StandardScaler
scaler_z = StandardScaler()

# Copy original data
X_standardized = X.copy()

# Apply StandardScaler to selected features
X_standardized[features] = scaler_z.fit_transform(X[features])

# View the first rows
X_standardized.head()"""