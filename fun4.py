#Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a,b,c):
    return max(a,b,c)
print(max_num(5,10,40))
print(max_num(8,4,6))

#Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(*args):
    prod = 1
    for num in args:
        prod *= num
    return prod
print(mult_list(2,4,6,8))
print(mult_list(4,9,2,16))

#Write a Python function called rev_string() to reverse a string.
def rev_string(my_string):
    return my_string[::-1]
print(rev_string("Marshall"))
print(rev_string("Lorhan"))

#Write a Python function called num_within() to check whether a number falls in a given range.
#The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
#Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

def num_within(d,e,f):
    distance_from_d = abs(f-d)
    distance_from_e = abs(f-e)

    if distance_from_d <= e:
        return True
    elif distance_from_e <= e:
        return True
    else:
        return False

print(num_within(3,2,4))
print(num_within(3,1,3))
print(num_within(10,2,5))

#Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
#The function accepts the number n, the number of rows to print
#Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.

def pascal(num_rows):
    if num_rows <= 0:
        print("Must be atlease 1 row")
        return None
    
    triangle = []
    for row_num in range(num_rows):
            row = [1] * (row_num + 1)
            for g in range(1, row_num):
                row[g] = triangle[row_num - 1][g - 1] + triangle[row_num - 1][g]
            triangle.append(row)
    return triangle
    
num_rows = 7
pascals_triangle = pascal(num_rows)
for row in pascals_triangle:
    print(row)