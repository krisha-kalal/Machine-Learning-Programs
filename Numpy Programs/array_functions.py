import numpy as np 

arr = np.array([1,2,3]) # Creates a 1D array.
a = np.array([4,5,6]) # Creates another 1D array.
arr2d = np.array([(1, 5, 6), (8, 2, 4)]) # Creates a 2D array.
arr3d = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)]) # Creates a 3D array.

print("array1:", arr) 
print("array2:", a) 
print("2d array:\n", arr2d)
print("3d array:\n", arr3d)

arr = np.array([1, 2, 3]) 
print("arr[2]:", arr[2]) # Accesses the third element of the array.

arr = np.array([1, 2, 3]) 
print("arr[-2]:", arr[-2]) # Accesses the second-to-last element of the array.

arr2d = np.array([(1, 5, 6), (8, 2, 4)]) 
print(arr2d[1:3]) # Slices the 2D array.

arr3d = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)]) 
print(arr3d[2:6]) # Slices the 3D array.

print("concatenate():", np.concatenate((arr, a))) # Concatenates two arrays.

print("vstack():\n", np.vstack((arr, a))) # Stacks arrays vertically.

print("hstack():", np.hstack((arr, a))) # Stacks arrays horizontally.

print("split():", np.split(arr, 1)) # Splits the array into sub-arrays.

arr = np.array([1, 2, 3]) 
print("all():", np.all(arr)) # Checks if all elements in the array are True.
 
arr = np.array([1, 2, 3]) 
print("any():", np.any(arr)) # Checks if any element in the array is True.

arr = np.array([1, 2, 3]) 
np.put(arr, [2], [-9]) 
print("put():", arr) # Replaces elements in the array at specified indices.

print("arange():", np.arange(1, 10, 2)) # Creates an array with a range of values.

print("zeros():", np.zeros(4)) # Creates an array filled with zeros.

print("ones():", np.ones(4)) # Creates an array filled with ones.

print("empty():", np.empty((4, 3))) # Creates an uninitialized array.

print("linspace():", np.linspace(1, 3, 5)) # Creates an array with linearly spaced values.

print("random.rand():", np.random.rand(5)) # Generates an array of random values.

print("random.randint():", np.random.randint(1, 9, 3)) # Generates an array of random integers.

arr = np.array([1, 2, 3]) 
print("max():", np.max(arr)) # Returns the maximum value in the array.

arr = np.array([1, 2, 3]) 
print("min():", np.min(arr)) # Returns the minimum value in the array.

arr = np.array([1, 2, 3]) 
print("mean():", np.mean(arr)) # Returns the mean of the array.

arr = np.array([1, 2, 3]) 
print("median():", np.median(arr)) # Returns the median of the array.

arr = np.array([1, 2, 3]) 
print("std():", np.std(arr)) # Returns the standard deviation of the array.

arr = np.array([1, 2, 3]) 
print("var():", np.var(arr)) # Returns the variance of the array.

arr = np.array([1, 2, 3]) 
print("sum():", np.sum(arr)) # Returns the sum of the array elements.

arr = np.array([1, 2, 3]) 
print("cumsum():", np.cumsum(arr)) # Returns the cumulative sum of the array elements.

arr = np.array([1, 2, 3]) 
a = np.array([4, 5, 6]) 
print("dot():", np.dot(arr, a)) # Computes the dot product of two arrays.

arr2d = np.array([(1, 5, 6), (8, 2, 4)]) 
b = arr2d.reshape(3, 2) 
print("reshape(): ", b) # Reshapes the array to the specified dimensions.

arr = np.array([1, 2, 3]) 
print("reverse:", arr[::-1]) # Reverses the array.

print("deleting element:", np.delete(a, 1)) # Deletes the element at the specified index.

print("power():", np.power(a, 2)) # Raises the array elements to the specified power.

print("remainder():", np.remainder(a, 3)) # Computes the element-wise remainder.

print("random.choice():", np.random.choice(arr)) # Generates a random sample from the array.

arr = np.array([1, 2, 3, 4]) 
np.random.shuffle(arr) 
print("random.shuffle():", arr) # Shuffles the elements of the array in place.