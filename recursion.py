def find_fact(num):
    if num == 1:
        return 1
    return (num * find_fact(num-1))
n=7
print(find_fact(n))

def find_fact_one(num):
    factorial = 1

    for i in range(1, num+1):
        factorial = factorial*i
    return factorial
n=7
print(find_fact_one(n))