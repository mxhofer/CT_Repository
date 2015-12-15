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
