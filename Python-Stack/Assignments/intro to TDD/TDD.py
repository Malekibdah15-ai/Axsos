import unittest

def ispalindrom(word):
    reversed_word = ""
    for i in range(len(word) - 1,-1,-1):
        reversed_word += word[i]
    return reversed_word == word


print(ispalindrom("aba"))


def reversed_list(list):
    left = 0
    right = (len(list)-1)
    for i in range ((len(list)) // 2):
        list[left], list[right]  = list[right], list[left]
        left += 1
        right -= 1
#     return list
print(reversed_list([1, 3, 5]))




def factorial(n):
    if n == 1:
        return 1
    fac = n*factorial(n-1)
    return fac
print(factorial(5))


class Test(unittest.TestCase):
    def test_ispalindrom(self):
        self.assertEqual(ispalindrom("aba")  ,True)
        self.assertEqual(ispalindrom("word"), False)
        self.assertFalse(ispalindrom("malek"))

    def test_reversed_list(self):
        self.assertEqual(reversed_list([1, 3, 5])  ,[5, 3, 1])
        self.assertEqual(reversed_list([2, 4, 5])  ,[5, 3, 1]) 




if __name__ =='__main__':
    unittest.main()