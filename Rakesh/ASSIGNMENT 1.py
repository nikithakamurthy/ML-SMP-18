
# coding: utf-8

# In[2]:


# Q1:Reverse a vector (first element becomes last)
import numpy as np
a=np.array([1,2,3])
print("Original: ")
print (a)
b=a[::-1]
print("Reverse: ")
print (b)


# In[3]:


#Q2: Create a 3x3 matrix with values ranging from 0 to 8
req_matrix = np.arange(9).reshape(3,3)
print("Required Matrix :")
print(req_matrix)


# In[7]:


#Q3: Create a 2d array with 1 on the border and 0 inside
c=np.ones((int(10),int(10)),dtype=np.int8)
c[1:-1,1:-1]=0
print (c)


# In[9]:


#Q4: Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
M1=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
M2=np.array([[1,2],[3,4],[5,6]])
print("The Matrix Multiplication of M1 and M2 is : ")
print (np.dot(M1,M2))


# In[10]:


#Q5: Extract the integer part of a random array using 5 different methods
M = np.random.uniform(0,5,10)
print("Original Matrix :")
print (M)
print("Matrices with Interger Part only :")
print(M - M%1) #Method 1
print(np.floor(M)) #Method 2
print(np.rint(M)) #Method 3
print(np.ceil(M)-1) #Method 4
print(M.astype(int)) #Method 5
print(np.trunc(M)) #Method 6


# In[13]:


#Q6: Write a Python program to check two random arrays are equal or not.
A1=np.random.normal(size=6)
A2=np.random.normal(size=6)
print("Array 1 = ", A1)
print("Array 2 = ", A2)
if np.array_equal(A1,A2):
  print("EQUAL")
else:
 print("NOT EQUAL")


# In[ ]:


#Q7: Write a Python program to find the nearest value from a given value in an array.
Ar = np.random.uniform(0,1,10)
print ("Array is :-  ", Ar)
z = 0.5
m = Ar[(np.abs(Ar - z)).argmin()]
print("Nearest value : ", m)



# In[ ]:


#Q8: Write a Python program to get the n largest values of an array.
a = np.random.uniform(0,1,10)
b=-np.sort(-a)
n=5    # n largest numbers
print("The N largest numbers are :- ")
print(b[:n])


# In[ ]:


#Q9: How to find the closest value (to a given scalar) in an array?
def n_Val(array,value):
    ind=(np.abs(array-value)).argmin()
    return array[ind]
q = np.random.normal(1,15,10)
value= 5
print(n_Val(q,value))


# In[ ]:


#Q10: Write a Python program to create random vector of size 15 and replace the maximum value by -1.
a=np.random.random(size=15)
print("Original array is : ", a)
a[a.argmax()]=-1
print ("Modified array is : ", a)


# In[ ]:


#Q11: Consider a random vector with shape (100,2) representing coordinates, find point by point distances .
import scipy
import scipy.spatial
Ar = np.random.random((100,2))
D = scipy.spatial.distance.cdist(Ar,Ar)
print(D)


# In[ ]:


#Q12: How to I sort an array by the nth column?
S=np.random.normal(1,10,15).reshape(3,5)
print(S)
n = 1
R=S[S[:n].argsort()]
print(R)


# In[ ]:


#Q13: Considering a four dimensions array, how to get sum over the last two axis at once?
A=np.random.uniform(1,20,81).reshape(3,3,3,3)
print("The array is : - ", A)
print("The sum is : - " , np.sum(A,axis=(2,3)))


# In[ ]:


#Q14: How to find the most frequent value in an array?
M = np.random.randint(0,10,50)
print("The array is :- " M)
print("Most Frequent element :- ", np.bincount(M).argmax())

