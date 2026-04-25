import numpy as np 
str_arr = np.array(['Hello', 'World']) 
print("string array:", str_arr) # Creates a 1D array of strings.

import numpy as np 
str_arr = np.array(['Hello', 'World']) 
print("char.add():", np.char.add(str_arr, "!")) # Concatenates '!' to each string in the array.

import numpy as np 
str_arr = np.array(['Hello', 'World']) 
print("char.lower():", np.char.lower(str_arr)) # Converts all characters to lowercase.

import numpy as np 
str_arr = np.array(['Hello', 'World']) 
print("char.upper():", np.char.upper(str_arr)) # Converts all characters to uppercase.

import numpy as np 
str_arr = np.array(['Hello', 'World']) 
print("char.title():", np.char.title(str_arr)) # Converts the first character of each word to uppercase.

import numpy as np 
str_arr = np.array(['Hello', 'World'])
print("char.replace():", np.char.replace(str_arr, "o", "0")) # Replaces 'o' with '0' in each string.

import numpy as np 
str_arr = np.array(['Hello', 'World']) 
print("char.center():", np.char.center(str_arr, 10, '*')) # Centers each string within a width of 10, padding with '*'.

import numpy as np 
str_arr = np.array(['Hello', 'World']) 
print("char.startswith():", np.char.startswith(str_arr, 'H')) # Checks if each string starts with 'H'.

import numpy as np 
str_arr = np.array(['Hello', 'World']) 
print("char.endswith():", np.char.endswith(str_arr, 'd')) # Checks if each string ends with 'd'.

import numpy as np 
str_arr = np.array(['Hello123', 'World456']) 
print("char.isalnum():", np.char.isalnum(str_arr)) # Checks if each string contains only alphanumeric characters.

import numpy as np 
str_arr = np.array(['Hello  ', '  World']) 
print("char.isspace():", np.char.isspace(str_arr)) # Checks if each string contains only whitespace characters.

import numpy as np 
str_arr = np.array(['Hello', 'World']) 
print("char.strip():", np.char.strip(str_arr)) # Removes leading and trailing whitespace from each string.

import numpy as np 
str_arr = np.array(['Hello World', 'Python NumPy']) 
print("char.split():", np.char.split(str_arr, ' ')) # Splits each string into a list of words using space as delimiter.

import numpy as np 
str_arr = np.array(['Hello', 'World']) 
print("char.capitalize():", np.char.capitalize(str_arr)) # Capitalizes the first character of each string.
