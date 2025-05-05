def factorial(n):
    if n < 0:
        return "wrong"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

num = 5
print(f"{num} = {factorial(num)}")
