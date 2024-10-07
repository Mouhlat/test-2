file_path = "file1.txt"

content = "Line 1\nLine 2\nLine 3"

# Writing content using write() method
with open(file_path, 'w') as file:
    file.write(content)

a = open(file_path,'r')
print(a.read())


#%%
import numpy as np

data = np.genfromtxt('C:\Work\Python\customer_data.csv', delimiter=',')

print(data)