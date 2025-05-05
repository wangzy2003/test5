def factorial(n):
    if n < 0:
        return "负数没有阶乘"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# 示例调用
num = 5
print(f"{num} 的阶乘是: {factorial(num)}")
