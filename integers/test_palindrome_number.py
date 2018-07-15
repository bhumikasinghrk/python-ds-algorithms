# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#
# Example 1:
#
# Input: 121
# Output: true
# Example 2:
#
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    num = str(x)
    return num == num[::-1]

def test_isPalindrome():
    assert isPalindrome(121)
    assert not isPalindrome(-121)

print(isPalindrome(121))
print(isPalindrome(-121))