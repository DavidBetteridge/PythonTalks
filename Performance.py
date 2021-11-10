import timeit

def version1():
  result = 0
  for n in range(1, 1001):
    result+=n
  return result


def version2():
  return sum([n for n in range(1, 1001)])


#pip install numpy
import numpy as np
def version3():
  return np.sum(np.arange(1,1001))


print(version1())
print(version2())
print(version3())

print(1,timeit.timeit(version1, number=1000))
print(2,timeit.timeit(version2, number=1000))
print(3,timeit.timeit(version3, number=1000))















# def version4():
#   n = 1000
#   return (n + 1) * (n / 2)

# print(version4())
# print(4,timeit.timeit(version4, number=1000))



# Run mandlebrot.py