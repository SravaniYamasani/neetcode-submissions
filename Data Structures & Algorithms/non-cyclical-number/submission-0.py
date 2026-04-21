class Solution:
    def isHappy(self, n: int) -> bool:
        mySet = set()

        def integerSquares(num: int)-> int:
            sum = 0
            i = 1
            while num:
                rem = num % 10
                num = num // 10 
                sum += pow(rem, 2)
                print(sum)
                i += 1

            return sum


        while n!= 1:
            n = integerSquares(n)
            if n in mySet:
                return False
            else:
                mySet.add(n)

        return True


        