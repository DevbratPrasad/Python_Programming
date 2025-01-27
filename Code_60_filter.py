numbers = [1,2,3,4,5,6]
def is_even(x):
    if(x%2==0):
        return x
even_number = filter(is_even,numbers)
print(list(even_number))
