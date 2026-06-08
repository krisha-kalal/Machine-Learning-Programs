import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

iris = load_iris()
x,y = iris.data,iris.target

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test,y_pred)
print(f'Accuracy: {accuracy:2f}')

print('\nClassification Report:')
print(classification_report(y_test,y_pred,target_names=iris.target_names))

new_samples = np.array([
    [5.1,3.5,1.4,0.2], #setosa
    [6.7,3.0,5.2,2.3], #virginica
    [5.9,3.0,4.2,1.5] #versicolor
])

# Predict the class for new samples
new_predictions = model.predict(new_samples)
print('\nPredictions for new samples:')
for sample, prediction in zip(new_samples, new_predictions):
    print(f'Sample: {sample} -> Predicted class: {iris.target_names[prediction]}')
