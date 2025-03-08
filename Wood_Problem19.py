# Wood_Problem19
# Lab 7 Counting Sundays
# Brennan Wood
# 3/8/25

from NumberTests import isPrime
from NumberTests import isEven

def primeSum(num):

  prime = []
  for p in range(2, num): # num is non inclusive, I'm assuming becuase it's "belox 2000000" then we leave it like that
    if isPrime(p):
      prime.append(p)
  s = sum(prime)
      
  print(s)

 

def main():
  num = 2000000
  primeSum(num)

if __name__ == '__main__':
  main()