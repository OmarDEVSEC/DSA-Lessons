# given an integer x, return true if x is a palindrome, and false otherwise. An
# integer is a palindrome when it reads the same backwards, 121 and 121

def isPalindrome(self,x:int) -> bool:
    if x < 0: return False

    div = 1
    while x >= 10 * div:
        div *= 10

    while x:
        right = x % 10
        left = x // div

        if left != right: return False
        
        x = (x % div) // 10
        div = div / 100

    return True


# complete palindrome algorithm, review and study later