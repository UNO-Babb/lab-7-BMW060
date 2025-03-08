#Problem3.py
#Problem 3 Largest Prime Factor
#Brennan Wood
#3/7/25


from NumberTests import isPrime
from NumberTests import getFactors




def main(): 
  number = 84
  factors = getFactors(number)
  print(factors)

  primeFactors = []
  for f in factors:
    if isPrime(f):
      primeFactors.append(f)
  
  print(primeFactors)
  print(primeFactors[-1]) #used this to grab the biggest value in the prime factors list
  print("The largest prime factor of",number,"is",primeFactors[-1])
if __name__ == '__main__':
  main()
