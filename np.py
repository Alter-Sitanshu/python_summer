import numpy as np

# np.linspace(start, end, number of elements total)
# np.arange(start, end, step) works similar to a range function
# np.array(list) takes a list as an argument and turns it into array, can make multidim arrays by nesting
# np.zeros(size) , np.ones(size) , np.empty(size) --> some important useful funcs
#  --> while instanciating these arrays we can also typecast the entries by "dtype" pos arg


# a = np.array([[8,3,4,2,1,9,10,5,7,6],[1,2,7,3,9,4,8,6,10,5]])
# a2 = np.sort(a,axis=1, kind='mergesort')
# here the kind field takes thesorting algo
# for axis = None output = [ 1  1  2  2  3  3  4  4  5  5  6  6  7  7  8  8  9  9 10 10]
# for axis = -1(last index: col) output = [[ 1  2  3  4  5  6  7  8  9 10]
#                                          [ 1  2  3  4  5  6  7  8  9 10]]
# for axis = 0(first index: row) output = [[ 1  2  4  2  1  4  8  5  7  5]
#                                          [ 8  3  7  3  9  9 10  6 10  6]]

# array_example = np.array([[[0, 1, 2, 3],
                        #    [4, 5, 6, 7]],

                        #   [[0, 1, 2, 3],
                        #    [4, 5, 6, 7]],

                        #   [[0 ,1 ,2, 3],
                        #    [4, 5, 6, 7]]])
# this has the array_example.shape() = (3,2,4) --> (height, breadth, length)
# we can reshape an array by arr.reshape(dimensions as parameter)
# it flattens the initial nd array and then groups the arrays according to the dimensions given


# we can add new axes to our array by new_vector = arr[:, np.newaxis] --> makes it col vector as the shape is now (6,1)

# filtering can be done as a2 = a[condition] returns the new filtered array

import matplotlib.pyplot as plt
rng = np.linspace(np.pi,3*np.pi,10)

plt.plot(np.sin(rng), marker='x')
plt.grid(True)
plt.show()

