# Stack
# O(n) Time
# O(n) Space
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openBrackets = "({["

        for bracket in s:
            if bracket in openBrackets:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                matchBracket = stack.pop()

                if (bracket == ")" and matchBracket == "(") or (bracket == "]" and matchBracket == "[") or (bracket == "}" and matchBracket == "{"):
                    continue
                else:
                    return False

        return len(stack) == 0
