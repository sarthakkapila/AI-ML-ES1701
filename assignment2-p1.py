import numpy as np

# Q1
array1 = np.ones(10) * 5
print("Array of 10 fives:")
print(array1)

# Q2
array2 = np.arange(10, 51)
print("\nArray of integers from 10 to 50:")
print(array2)

# Q3
array3 = np.arange(10, 51, 2)
print("\nArray of even integers from 10 to 50:")
print(array3)

# Q4
array4 = np.arange(9).reshape(3, 3)
print("\n3x3 matrix with values ranging from 0 to 8:")
print(array4)

# Q5
array5 = np.random.randn(25)
print("\nArray of 25 random numbers sampled from a standard normal distribution:")
print(array5)

# Q6
array6 = np.arange(0, 1.01, 0.01)
print("\nSpecified array:")
print(array6)

# Q7
array7 = np.linspace(0, 1, 20)
print("\nArray of 20 linearly spaced points between 0 and 1:")
print(array7)

# Q8 a)
mat = np.arange(1, 26).reshape(5, 5)
print("\nGenerated matrix:")
print(mat)

# b)
extract1 = mat[1:4, 1:5]
print("\nExtracted part 1:")
print(extract1)

extract2 = mat[[1, 2, 3], [1]]
print("\nExtracted part 2:")
print(extract2)

# c)
sum_of_all_values = np.sum(mat)
print("\nSum of all values in mat:", sum_of_all_values)

# d)
sum_of_rows = np.sum(mat, axis=1)
sum_of_columns = np.sum(mat, axis=0)
print("\nSum of rows in mat:", sum_of_rows)
print("Sum of columns in mat:", sum_of_columns)
