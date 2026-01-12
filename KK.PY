from sklearn.datasets import make_moons
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def main():
	# Create synthetic 2D data
	X, y = make_moons(n_samples=300, noise=0.3, random_state=42)

	# Scale features
	scaler = StandardScaler()
	X_scaled = scaler.fit_transform(X)

	# Range of k values to try
	k_range = range(1, 21)
	cv_scores = []
	# Evaluate each k using 5-fold cross-validation
	for k in k_range:
		knn = KNeighborsClassifier(n_neighbors=k)
		scores = cross_val_score(knn, X_scaled, y, cv=5, scoring='accuracy')
		cv_scores.append(scores.mean())

	# Best k
	best_k = 7
	print(f"Using k value: {best_k}")

	# Split into train/test and train final model
	X_train, X_test, y_train, y_test = train_test_split(
		X_scaled, y, test_size=0.2, random_state=42, stratify=y
	)
	model = KNeighborsClassifier(n_neighbors=best_k)
	model.fit(X_train, y_train)
	y_pred = model.predict(X_test)

	# Confusion Matrix
	cm = confusion_matrix(y_test, y_pred)
	disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Class 0", "Class 1"])
	disp.plot(cmap="Blues")
	plt.title(f"Confusion Matrix (k={best_k})")
	plt.grid(False)
	plt.show()
	# Detailed classification report
	print("Classification Report:")
	print(classification_report(y_test, y_pred, target_names=["Class 0", "Class 1"]))

	# Use the trained model for decision boundary plotting
	best_knn = model

	# Create a mesh grid for plotting decision boundary
	h = 0.02
	x_min, x_max = X_scaled[:, 0].min() - 0.5, X_scaled[:, 0].max() + 0.5
	y_min, y_max = X_scaled[:, 1].min() - 0.5, X_scaled[:, 1].max() + 0.5
	xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

	# Predict on mesh grid with best k
	Z = best_knn.predict(np.c_[xx.ravel(), yy.ravel()])
	Z = Z.reshape(xx.shape)

	# Plot decision boundary
	plt.figure(figsize=(8, 6))
	plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.3)
	sns.scatterplot(x=X_scaled[:, 0], y=X_scaled[:, 1], hue=y, palette="Set1", edgecolor='k')
	plt.title(f"Decision Boundary with Best k = {best_k}")
	plt.xlabel("Feature 1 (scaled)")
	plt.ylabel("Feature 2 (scaled)")
	plt.grid(True)
	plt.show()


if __name__ == '__main__':
	main()
# Z = best_knn.predict(np.c_[xx.ravel(), yy.ravel()])

 

















 