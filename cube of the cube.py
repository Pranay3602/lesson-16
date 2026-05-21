def cube(number):
    return number*number*number
def by3(number):
    if number%3==0:
        return cube(number)
    else:
        return False
number=int(input("what is your number you wnat to find the cube of"))
print(by3(number))