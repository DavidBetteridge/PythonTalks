import timeit

def version1():
  l = ["a"] * 10000
  for _ in range(100):
    l = l + ["b"]
  assert len(l) == 10100

def version2():
  l = ["a"] * 10000
  for _ in range(100):
    l.append("b")
  assert len(l) == 10100
  
print(timeit.timeit(version1, number=100))
print(timeit.timeit(version2, number=100))