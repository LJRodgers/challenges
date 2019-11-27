"""
This function returns the sum of numbers who 
have factors of 3 and 5
"""

def sum_of_factors_3_and_5(i , n):
    l = []
    for i in range(i,n+1):
        if (i%3 == 0 and i%5 == 0):
            l.append(i)
    return(sum(l))

print(sum_of_factors_3_and_5(1, 1000))
