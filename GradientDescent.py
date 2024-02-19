import numpy as np
import matplotlib.pyplot as plt


def cost_function(theta):
    return (theta - 3) ** 2  


def gradient_descent(theta_initial, learning_rate, num_iterations):
    theta = theta_initial
    theta_history = [theta]
    cost_history = [cost_function(theta)]

    for _ in range(num_iterations):

        gradient = 2 * (theta - 3)  

        theta -= learning_rate * gradient

        theta_history.append(theta)
        cost_history.append(cost_function(theta))

    return theta_history, cost_history

theta_initial = 0
learning_rate = 0.1
num_iterations = 10
theta_history, cost_history = gradient_descent(theta_initial, learning_rate, num_iterations)

plt.plot(range(num_iterations + 1), cost_history, marker='o', linestyle='-')
plt.xlabel('Iterations')
plt.ylabel('Cost Function')
plt.title('Cost Function Minimization with Gradient Descent')
plt.grid(True)
plt.show()
