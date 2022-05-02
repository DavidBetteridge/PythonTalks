# Count number of A's in a string
import timeit
from typing import Counter

text = "sdfklasjdfsdjfkdsAsdfjsdjkfAdklfjdsklA"
text = 'Abcde' * 1000

def version1(text):
  # Loop O(N)
  count = 0
  for c in text:
    if c == 'A':
      count += 1
  return count


def version2(text):
  # Loop O(N)
  count = 0
  for i in range(len(text)):
    if text[i] == 'A':
      count += 1
  return count


def version3(text):
  # List comprehension (using sum over iteration)
  return sum(1 for c in text if c == 'A')

def version4(text):
  # List comprehension (using length over an array)
  return len([1 for c in text if c == 'A'])


def version5(text):
  # Count all letter frequences and return just A
  cnts = Counter(text)
  return cnts["A"]

print(version1(text))
print(version2(text))
print(version3(text))
print(version4(text))
print(version5(text))

print(1,timeit.timeit(lambda: version1(text), number=1000))
print(2,timeit.timeit(lambda: version2(text), number=1000))
print(3,timeit.timeit(lambda: version3(text), number=1000))
print(4,timeit.timeit(lambda: version4(text), number=1000))
print(5,timeit.timeit(lambda: version5(text), number=1000))