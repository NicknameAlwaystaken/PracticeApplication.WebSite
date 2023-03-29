#Generated by ChatGPT

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Load the iris dataset
iris = load_iris()

# Define the features and labels
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=2)

# Create a K-Nearest Neighbors classifier
knn = KNeighborsClassifier(n_neighbors=5, metric='manhattan')

# Train the classifier on the training dataset
knn.fit(X_train, y_train)

# Use the classifier to make a prediction
prediction = knn.predict([[5, 2, 1, 1]])

# Print the predicted label
print("The predicted label is:", iris.target_names[prediction[0]])

# Test the classifier on the testing dataset and print the accuracy score
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}%".format(accuracy * 100))
