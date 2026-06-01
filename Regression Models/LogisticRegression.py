# importing libraries
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# loading the iris dataset in a variable
iris = load_iris()

# creating a dataframe for the loaded data
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

# this head function prints the first five rows of the data
print("\nFirst five rows:\n",df.head())

# count of each of the target class
print("\nCount of target class:\n",df['target'].value_counts())

# dropping(deleting) all the passed student rows from x variable and loading them to y variable
x = df.drop('target', axis=1)
y = df['target']

# splitting the data using variables
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# standardizing data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# initializing Logistic Regression model using that function
model = LogisticRegression()

# training the model
model.fit(X_train, y_train)

# making predictions of data
y_pred = model.predict(X_test)

# calculating the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy}")

# creating classification report
print("\nClassification Report:\n",classification_report(y_test, y_pred))

# creating confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:\n",conf_matrix)

# visualizing confusion matrix
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
