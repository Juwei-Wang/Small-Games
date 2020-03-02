import random


a = []
for i in range(10):
    a += [random.randrange(1,100)]
def find_index_of_minimun(a, start, stop):
    min_index = start
    min_value = a(start)
    for index in range(start,stop):
        if a[index] < min_value:
            min_value = a[index]
            min_index = index
    return min_index
""" 
Insertion sort
repeat for sucessive indices of my array
find the index of the minimun element between the current index and end
exchange the element at current index with the minimun found

"""

def exchange_elemets(a, index1, index2):
    temp = a[index1]
    a[index1] = a[index2]
    a[index2] = temp

print(a)

num_elements = len(a)
for current_index in range(len(a)):
    index_of_min = find_index_of_minimun(a, current_index,num_elements)
    exchange_elemets(a,current_index,index_of_min)

b = sorted(a)

print(a)
print(b)
random.shuffle(b)
print(b)
"""2 dementional arrays
array is sequence of homogeneous data values(int str float bool)
2D array  is an array of arrays(usually the same size
a=[[1,2],[3,4]]
[1,2]
[3,4]
print(a[0])   #[1,2]
print(a[0][1])  2
       row column
creat 9*16 array of 
a = [[0]*16] * 9
a = []
for i in range (9):
    row = []
    for j in range(16):
        row += [0]
        a += [row]
import stdarry
a = stdarray create2D(9,16,0)
System of Equatians
3x + 7y = 15
2x + 5x = 11
det (a) = ad -bc
A ** -1 = 1/den(a) [d -b]
                   [-c a]
[x] = a ** -1 b
[y]
AB = [ae + bf]   A = [ a b ]    b =  [e]
      ce + df          c d            f

"""
def determinant_2x2(A):
    """claculate the determinant 2x2 matrix A"""
    return 1.0/(A[0][0] * A[1][1] - A[0][1] * A[1][0])
def inverse_2x2(A):
    detA = determinant_2x2(A)
    a = A[0][0] 
    b = A[0][1]
    c = A[1][0]
    d = A[1][1]
    B = [ [d, -b], [-c, a] ]
    for i in range(2):
        for j in range(2):
            B[i][j] = (1.0/ detA) * B[i][j]
    return B
def multiply_matrix_with_vector(A.b):
    rows = len(A)
    C = []
    for i in range (rows):
        C += [inner_product(A[i], b)]
    return C



