# Wood_Problem20.py
# Factorial Digit Sum
# Brennan Wood
# 3/8/25

from NumberTests import digSum, factorial


def main():
    num = 100

    factorial(num)
    fac = factorial(num)
    digSum(fac)
    added = digSum(fac)

    print(num,"factorial is:",fac)
    print("The sum of the factorial digits is:",added)

if __name__ == "__main__":
    main()

