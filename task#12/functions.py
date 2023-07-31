# Excersize 1
def greetUser(name):
    print("hello", name)

greetUser("jaihoon")


# Excersize 2
def calculatRectangleArea(witdth , height):
    print(witdth * height)

calculatRectangleArea(5, 8)


# Excersize 3
def celsiusToFahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(fahrenheit)

celsiusToFahrenheit(25)


# Excersize 4
def isEven(number1):
    if number1 % 2 == 0:
        print("true")
    else:
        print("false")

isEven(10)


# Excersize 5
def maxOfTwo(number1, number2):
    if number1 > number2:
        print(number1)
    else: 
        print(number2)

maxOfTwo(32 , 78)


# Excersize 6
def is_vowel(character):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    if character in vowels:
        return true
    else:
        return false
    characters = ["a" "b", "E", "Z"]
    for char in characters:
        result = is_vowel(char)
        print(f"{char} is a vaowel: {result}")
        


# Excersize 7
def factorial(b):
    if b <=1:
        return 1
    else:
        return b * factorial(b-1)
    
print(factorial(5))

# 5 * 4 * 3 * 2 * 1 = 120


#  Excersuze 9
def sum_multiple(n, f):
    num1 = range(n,100,n)
    num2 = range(f,100,f)
    nu1 = list(num1)
    nu2 = list(num2)
    print(sum(nu1))
    print(sum(nu2))
    print(sum(nu1+nu2))

sum_multiple(3,5)


# Excersize 10
def triangle(n):
    x = 0
    while x <= n:
        print("#"*x)
        x+=1
triangle(8)


