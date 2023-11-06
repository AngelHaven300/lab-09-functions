def factorial(n):
    for i in range(n - 1, 0, -1):
        n *= i
    return n
userint = input("number please...")
userinput = int(userint)
print(factorial(userinput))

        