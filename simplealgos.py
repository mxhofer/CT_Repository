__author__ = 'maxhofer'

# function that counts the number of vowels in a string
def countvowels(s):
    count = 0
    for c in s:
        if c in "aeiou":  # use "in"
            count += 1
    return count

# now redefine it as a recursive function
def countvowels(s):
    if s == "": return 0
    # elif s[0] in "aeiou":
        # return 1 + countvowels(s[1:])  # colone with nothing following means up to the end of the string
    else:
        return (1 if s[0] in "aeiou" else 0) + countvowels(s[1:])

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

'''Palindrome checker
Base case: isPalindrome("a") -> True
isPalindrome(" ") -> True'''
def isPalindrome(s):
	if len(s) <= 1:  # base case
		return True
	else:
		return s[0]==s[-1] and isPalindrome(s[1:-1])  # s[-1] is the last character
		

def inputNumbers(n):
    answer = []
    i = 1
    while i <= n:
        x = int(input("Enter a number: "))
        answer.append(x)
        i += 1
    return answer  # don't use print statements as part of your function


def integrate(x, start, insert, end):
    answer = x**2
    newlist = [start, insert, end]
    newlist[1] = answer
    return newlist

def integrate(start, end, dx):
    x = start
    answer = 0
    while x < end:
        area = dx * x**2
        answer += area
        x += dx
    return answer

def squareRoot(x): #finds the square root manually and stops when error < 0.01
    guess = 0
    dx = 0.01
    while abs(guess**2 - x) > 0.001:
        guess += dx
        if guess > x: #Just guess > x because it's the easiest thing to do
            return None
    return guess


def squareRoot(x, error):  # bisection search is super efficient
    low = 0
    high = x
    guess = (high+low)/2
    counter = 0
    while abs(guess**2 - x) > error:  # never goes into an infinite loop!!
        if guess**2 < x:
            low = guess
        else: high = guess
        guess = (low+high)/2
        counter += 1
    return guess, counter
