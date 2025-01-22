import numpy as np

# 1-create null vectors of size 10
x = np.zeros(10)
print(x)
# 2-Create a null vector of size 10 but the fifth value which is 1
x[4] = 1
print(x)
# 3.Create a vector with values ranging from 10 to 49
arr = np.arange(10, 49)
print(arr)
# 4-Reverse a vector (first element becomes last)
arr1 = np.arange(1, 10)
print("original array: ")
print(arr1)
print("reverse array: ")
arr1 = arr1[::-1]
print(arr1)


# 6-Create a 3x3 matrix with values ranging from 0 to 8
y = np.arange(0, 9).reshape(3, 3)
print(y)

# 7.Create a 3x3 identity matrix
a = np.eye(3)
print(a)
# 8. Create a 3x3x3 array with random values
b = np.random.random((3, 3, 3))
print(b)
# 9. Create a 10x10 array with random values and find the minimum and maximum values
c = np.random.random((10, 10))
print("original array: ")
print(c)
cmin, cmax = c.min(), c.max()
print("minimum and maximum values: ")
print(cmin, cmax)
# 10. Create a random vector of size 30 and find the mean value (★☆☆)
m = np.random.random(30)
print("original array: ")
print(m)
k = m.mean()
print("the mean is: ")
print(k)

# 11 Create a 2d array with 1 on the border and 0 inside
f = np.ones((5, 5))
print("original array: ")
print(f)
f[1:-1, 1:-1] = 0
print("1 on border and 0 inside: ")
print(f)
# 12. How to add a border (filled with 0's) around an existing array?
h = np.ones((5, 5))
print("original array: ")
print(h)
h = np.pad(h, pad_width=1, mode='constant', constant_values=0)
print("0 on the border and 1 inside in the array: ")
print(h)
# 13-Create a 5x5 matrix with values 1,2,3,4 just below the diagonal
i = np.diag(1+np.arange(4), k=-1)
print(i)
# 14.Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)
j = np.random.random((5, 3))
print("first array: ")
print(j)
g = np.random.random((3, 2))
print("second array: ")
print(g)
p = np.dot(j, g)
print("dot products of two arrays: ")
print(p)

# 15. Given a 1D array, negate all elements which are between 3 and 8, in place.





# 16.How to find common values between two arrays?
array1 = np.array([10, 20, 30, 40, 50])
print("array1: ",array1)
array2 = np.array([20, 30, 35, 65])
print("array2: ",array2)
print(np.intersect1d(array1, array2))
# 17. Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆)
q = np.zeros((5, 5))
print("original array: ")
print(q)
q += np.arange(5)
print("Row values ranging from 0 to 4.")
print(q)
# 18. Create a random vector of size 10 and sort it
r = np.random.random(10)
print("original array: ")
print(r)
print("sorted array: ")
r.sort()
print(r)
# 19. Consider two random array A and B, check if they are equal
first_arr = np.random.randint(0, 2, 5)
print("first array: ")
print(first_arr)
second_arr = np.random.randint(0, 2, 5)
print("second array: ")
print(second_arr)
print("Test above two arrays are equal or not!")
array_equal = np.allclose(first_arr, second_arr)
print(array_equal)
# 20. Create random vector of size 10 and replace the maximum value by 0
v = np.random.random(10)
print("original array: ")
print(v)
v[v.argmax()] = 0
print("replace maximum value with 0 ")
print(v)
#  How to convert a float (32 bits) array into an integer (32 bits) in place
Z = np.arange(10, dtype=np.int32)
Z = Z.astype(np.float32, copy=False)
print(Z)
# 25. Subtract the mean of each row of a matrix
print("Original matrix:\n")
matrix1 = np.random.rand(5, 10)
print(matrix1)
print("\nSubtract the mean of each row of the given matrix:\n")
matrix2= matrix1 - matrix1.mean(axis=1, keepdims=True)
print(matrix2)
# 26. How to get the diagonal of a dot product?
A = np.random.randint(0,10,(3,3))
B = np.random.randint(0,10,(3,3))
C = np.diag(np.dot(A, B))
print(C)

# 28. How to swap two rows of an array?
X = np.arange(25).reshape(5, 5)
X[[0, 1]] = X[[1, 0]]
print(X)