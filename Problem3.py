#Problem3.py
#Problem 3 Largest Prime Factor
#Brennan Wood
#3/7/25


from NumberTests import isPrime
from NumberTests import fibonacciSequence



def factors(p):
  for i in range(2,p):
    if p % i == 0:
      return False
    else:
      return True
  return factors
def main(): 
  p = int(input("Enter a number: "))
  fac = factors(p)
  print(fac)
  
  #p = int(input("Enter a number: "))
  #length = []
  #for i in range(p):
  #  length.append(i+1)
  #print(length)


if __name__ == '__main__':
  main()
