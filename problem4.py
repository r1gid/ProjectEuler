#checks if an integer is a palindromic number
def num_reverse(n):
    string = list(str(n))
    for i in range(len(string)):
        if(string[i] != string[len(string) - 1 - i]):
           return False
    else:
        return True

#finds all palindrome numbers that are made from the product of 3-digit numbers
def find_all():
    a = 999
    b = 999
    results = []
    while a > 99:
        for i in range(100, a + 1):
            print(b)
            if(num_reverse(a * b)):
                results.append(a * b)
            b -= 1
        a -= 1
        b = 999
    return results

#prints the largest found palindrome number
print(max(find_all()))
