class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for char in s:
            if char == '[' or char == '{' or char == '(':
                st.append(char)
            if len(st) == 0:
                return False
            elif char == ']':
                new_char = st[-1]
                if new_char != '[':
                    break
                else:
                    st.pop()
            elif char == '}':
                new_char = st[-1]
                if new_char != '{':
                    break
                else:
                    st.pop()
            elif char == ')':
                new_char = st[-1]
                if new_char != '(':
                    break
                else:
                    st.pop()
        if len(st) == 0:
            return True
        return False