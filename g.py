from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_digits
SEED = 23
X, y = load_digits(return_X_y=True)
train_X, test_X, train_y, test_y = train_test_split(X, y,
 test_size = 0.25,
 random_state = SEED)
gbc = GradientBoostingClassifier(n_estimators=300,
 learning_rate=0.05,
random_state=100,
max_features=5 )

gbc.fit(train_X, train_y)
pred_y = gbc.predict(test_X)
acc = accuracy_score(test_y, pred_y)
print("Gradient Boosting Classifier accuracy is : {:.2f}".format(acc))

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.datasets import load_diabetes
SEED = 23
X, y = load_diabetes(return_X_y=True)
train_X, test_X, train_y, test_y = train_test_split(X, y,
 test_size = 0.25,
 random_state = SEED)
gbr = GradientBoostingRegressor(loss='absolute_error',
 learning_rate=0.1,
n_estimators=300,
max_depth = 1,
 random_state = SEED,
 max_features = 5)
gbr.fit(train_X, train_y)
pred_y = gbr.predict(test_X)
test_rmse = mean_squared_error(test_y, pred_y) ** (1 / 2)
print('Root mean Square error: {:.2f}'.format(test_rmse))

# Train model
gbc.fit(train_X, train_y)

# Predict
pred_y = gbc.predict(test_X)

# Accuracy
acc = accuracy_score(test_y, pred_y)
print("Gradient Boosting Classifier accuracy is : {:.2f}".format(acc))