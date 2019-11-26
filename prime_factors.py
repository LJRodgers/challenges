"""
Find the factors of numbers 
"""
def find_factors_of_num(i, n):
    l = []
    count = 0
    for i in range (i, n+1):
        if n%i==0:
            l.append(i)
        count+=1
    print("count =", count)
    return(l)

print(find_factors_of_num(1, 100))