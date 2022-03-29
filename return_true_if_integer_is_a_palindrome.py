def findPalindrome(x: int) -> bool:
    
    if x < 0:
        return False
        
    number = x
    reversedNumber = 0
    
    while number:
        
        lastDigit = number % 10
        
        reversedNumber = reversedNumber * 10 + lastDigit
        
        number //= 10
    return reversedNumber == x
    
print(findPalindrome(123)) #returns False
print(findPalindrome(131)) #returns True
