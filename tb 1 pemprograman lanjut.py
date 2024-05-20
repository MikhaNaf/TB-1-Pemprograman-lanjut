#Mikha Naftali 
#41823010047
import itertools
import re


with open('Matrix.txt', 'r') as file:
    
    dimensions = file.readline().strip().split()
    n = int(dimensions[0])
    m = int(dimensions[1])
    
    matrix = []
    
    
    for _ in range(n):
        matrix_item = file.readline().strip()
        matrix.append(matrix_item)
    
    
    encoded_string = "".join(char for group in itertools.zip_longest(*matrix, fillvalue='') for char in group)
    
    
    pat = r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])'
    decoded_string = re.sub(pat, ' ', encoded_string)
    
    print(decoded_string)
