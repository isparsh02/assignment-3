def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        return fact

num = int(input("Enter a number: "))

if num >= 0:
    print(f"Factorial of {num} is:", factorial(num))
else:
    print(factorial(num))