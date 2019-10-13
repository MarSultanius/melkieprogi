def sum_square_difference(n):
    r = range(1, n+1)  # first n natural numbers
    return sum(i**2 for i in r) 
n=int(input())
print(sum_square_difference(n))
