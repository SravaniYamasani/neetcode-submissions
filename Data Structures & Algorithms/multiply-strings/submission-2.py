class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        def convertStringToNum(c: str)->int:
            num = 0  
            for i in range(len(c)):
                digit = ord(c[i]) - ord("0")
                print("digit:", digit)
                num = num + (digit * pow(10,(len(c) - i -1)))

            print(num)

            return num        

        ans = convertStringToNum(num1) * convertStringToNum(num2)
        print("ans",ans)

        return str(ans)