# import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# create a hypothetical student dataset
data = {
    'Hours_Studied': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    'Attendance': [95, 90, 85, 80, 75, 70, 65, 60, 55, 50],
    'Previous_Grades': [88, 85, 83, 80, 78, 75, 70, 68, 65, 60],
    'Passed': [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]  # 1 = Passed, 0 = Failed
}

# convert the given data to dataframe
df = pd.DataFrame(data)

# printing first five rows
print('First few rows:')
print(df.head(),'\n')

# calculate statistics for the provided data
print('Statistics of Data Set:')
print(df.describe(),'\n')

# print information about the dataset
print('Info about Data Set:')
print(df.info(),'\n')

# separating features and target variable
x = df.drop('Passed',axis=1)
y = df['Passed']

# splitting the data into training and testing sets
x_train,x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

# using scaler for proper calculation
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

# initializing logistic regression model
model= LogisticRegression()

# training the model with the training data
model.fit(x_train, y_train)

# calculate prediction for dataset
y_pred = model.predict(x_test)

# calculate accuracy for dataset
accuracy = accuracy_score(y_test, y_pred)
print(f"\n Accuracy: {accuracy}")

# create classification report for dataset
print("\n Classification Report:\n")
print(classification_report(y_test, y_pred))

# create confusion matrix for dataset
conf_matrix = confusion_matrix(y_test, y_pred)
print("\n Confusion matrix:\n",conf_matrix)

# visualize confusion matrix for dataset
plt.figure(figsize=(8,6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues',
xticklabels = ['Failed','Passed'],yticklabels=['Failed','Passed'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
