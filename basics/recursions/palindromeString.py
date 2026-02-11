str1 = "Malayalam"

def palindrome(text):
    original = str1.lower()
    palindrome = text.lower()
    checkStr =  text[-1]
    palindrome(checkStr)
    if original == palindrome:
        return True
    else:
        return False
palindrome(str1)