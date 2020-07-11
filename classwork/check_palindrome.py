def isPalindrome(s):
    # print(s)
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    # if s[0] == s[-1] and len(s) == 2:
    #     return True
    return isPalindrome(s[1:-1])  # trim 1st and last character and recurse


if __name__ == "__main__":
    assert isPalindrome("racecar") == True
    assert isPalindrome("abba") == True
    assert isPalindrome("a") == True
    assert isPalindrome("hello") == False
    assert isPalindrome("ax") == False
