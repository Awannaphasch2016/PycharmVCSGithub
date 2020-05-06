import numpy as np


def myfunc(a, b):
    return np.sum([a, b])


vfunc = np.vectorize(myfunc)
print(vfunc([[1, 2, 3], [4, 5, 6]], [1, 2, 2]))
