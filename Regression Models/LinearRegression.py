import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
import matplotlib.pyplot as plt

np.random.seed(0)
x = 2 * np.random.rand(100,1)
y = 4 + 3 * x + np.random.randn(100,1)
# Y = 4+3x + noise

#y = mx+b

plt.scatter(x,y)
plt.title('Scatter plot of the synthetic data')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

# Coefficient (slope of the line) shows how much y changes for a unit change in x
# Intercept shows the point where the line crosses the y-axis (the constant in the equation y = mx + b)
# Mean Squared Error is a measure of how far off the predictions are from the actual values on average
print(f'Coefficient: {model.coef_[0][0]}') # Coefficient = slope of the line (3 in the equation y = 4 + 3x)
print(f'Intercept: {model.intercept_[0]}') # Intercept = y-intercept (4 in the equation y = 4 + 3x)
print(f'Mean Squared Error: {mse}') # Mean Squared Error = average squared difference between actual and predicted values

plt.scatter(x_test, y_test, color='black', label='Actual data')
plt.plot(x_test, y_pred, color='blue', linewidth=3, label='Regression line')
plt.title('Linear Regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
