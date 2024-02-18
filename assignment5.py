import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class LinearRegression:
    # part of gradient descent
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None
    
    def fit(self, X, y):
        n_samples, n_features = X.shape

        # Initialize weights and bias
        # self.weights is initialized as a NumPy array of zeros with a length equal to the number of features (n_features).
        # self.bias is initialized to zero. It represents the intercept term in the linear regression equation.
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # Gradient descent to minimize the mean squared error loss.
        for _ in range(self.n_iterations):
            y_predicted = np.dot(X, self.weights) + self.bias

            # Compute gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)

            # Update weights and bias
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias


    def evaluate(self, X, y):
        y_predicted = self.predict(X)
        mae = np.mean(np.abs(y_predicted - y))
        mse = np.mean((y_predicted - y) ** 2)
        rmse = np.sqrt(mse)
        return mae, mse, rmse

if __name__ == "__main__":
    data = pd.read_csv('USA_Housing.csv')

    X = data[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms', 'Area Population']]
    y = data['Price']

    # Training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scaling features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = LinearRegression(learning_rate=0.01, n_iterations=1000)
    model.fit(X_train_scaled, y_train)

    mae, mse, rmse = model.evaluate(X_test_scaled, y_test)

    print("Mean Absolute Error (MAE):", mae)
    print("Mean Squared Error (MSE):", mse)
    print("Root Mean Squared Error (RMSE):", rmse)
