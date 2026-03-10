"""  
Lambda:
1. lambda function executes faster than normal function.
2. only small and simple logic can be implemented in lambda function
3. codes are reduced if we use lambda function
lambda arguments  : expression/logic
"""

# function1 = lambda x : x + 10
# result = function1(10)
# print(result)
# function2 = lambda x,y : x + y
# result = function2(4,5)
# print(result)
# square = lambda x : x ** 2
# result = square(4)
# print(result)
# calculate = lambda x,y,z : x * y + z
# result = calculate(2,3,4)
# print(result)
# def function1(x):
#     x = x + 10
Messages addressed to "meeting group chat" will also appear in the meeting group chat in Team Chat

Prabin Sigdel 8:48 PM
""" 
Recursive function: A function call itself
Base case and recursive case

Factorial:
4! = 4 * 3 * 2 * 1 = 24
5! = 5 * 4 * 3 * 2* 1 = 
"""
# def count(n):
#     if n == -10:
#         return
#     print(n)
#     count(n - 1)
    
# count(5)

#Factorial :
def factorial(n):
    if n == 1:
        return 1
    else:
        fact = n * factorial( n-1 )  # 4 * factorial(4-1)  ->  4 * 3 * factorial( 3-1)  -> 4 * 3 * 2 * factorial(2 -1 ) -> 4 * 3 * 2 * 1
        return fact
    
result = factorial(6)
print(result)