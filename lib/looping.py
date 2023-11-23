#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print('Happy New Year!')  


happy_new_year()    



def square_integers(int_list):
    return[number ** 2 for number in int_list]
   
result = square_integers([1,2,3,4,5,6])
print(result)
def fizzbuzz():
    # code goes here!
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz')        
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)    



fizzbuzz()