class Solution:
    def isValid(self, s: str) -> bool:
        openParanthesis = {"(", "{", "["}
        closedParanthesis = {")", "}", "]"}
        paranthesisPair = { ")" :"(", "}" : "{", "]" : "["}
        sk = []
        ans = False

        if s == "" or len(s) == 1:
            return False
        
        for c in s:
            if c in openParanthesis:
                sk.append(c)
            elif c in closedParanthesis:
                if sk:
                    if paranthesisPair[c] == sk[-1]:
                        sk.pop()
                    else:
                        return ans
                else:
                    return ans
                

        if not sk:
            ans = True

        return ans


