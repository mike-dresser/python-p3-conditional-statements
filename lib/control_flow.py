#!/usr/bin/env python3

def admin_login(username, password):
    response = 'Access granted' if (
        password == '12345' and 
        (username == 'admin' or username == 'ADMIN')
     ) else 'Access denied'
    return response

def hows_the_weather(temperature):
    if temperature <  40: return "It's brisk out there!"
    elif temperature < 65: return "It's a little chilly out there!"
    elif temperature < 85: return "It's perfect out there!"
    else: return "It's too dang hot out there!"
    

def fizzbuzz(num):
    if num % 15 == 0: return 'FizzBuzz'
    if num % 5 == 0: return 'Buzz'
    if num % 3 == 0: return 'Fizz'
    return num

def calculator(operation, num1, num2):
    function_map = {
        '+': lambda num1,num2: num1 + num2,
        '-': lambda num1,num2: num1-num2,
        '*': lambda num1,num2: num1* num2,
        '/': lambda num1,num2: num1 / num2
    }

    def default_response(a,b):
            print('Invalid operation!')
            return None

    return function_map.get(operation, default_response)(num1, num2)