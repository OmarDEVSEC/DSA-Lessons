# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# # Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000



# intilize function
def romanToInt(self, s: str) -> int:
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
            res -= roman[s[i]]
        else:
            res += roman[s[i]] #Algo for checking if the character in front is smaller then the next character and subtracting
            # the smaller value from the result, if not, adding the values to each other.

    if s == '':
        return 0
    
    if s == 'IV':
        return 4
    
    if s == 'IX':
        return 9
    
    if s == 'XL':
        return 40
    
    if s == 'XC':
        return 90
    
    if s == 'CD':
        return 400
    
    if s == 'CM':
        return 900

    

