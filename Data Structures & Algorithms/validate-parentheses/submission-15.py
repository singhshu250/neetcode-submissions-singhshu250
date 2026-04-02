class Solution:
    def isValid(self, s: str) -> bool:
        # my sol
        # st = []
        # for char in s:
        #     if char == '[' or char == '{' or char == '(':
        #         st.append(char)
        #     if len(st) == 0:
        #         return False
        #     elif char == ']':
        #         new_char = st[-1]
        #         if new_char != '[':
        #             break
        #         else:
        #             st.pop()
        #     elif char == '}':
        #         new_char = st[-1]
        #         if new_char != '{':
        #             break
        #         else:
        #             st.pop()
        #     elif char == ')':
        #         new_char = st[-1]
        #         if new_char != '(':
        #             break
        #         else:
        #             st.pop()
        # if len(st) == 0:
        #     return True
        # return False

        #---------------------------------------------------------------

        # Sol
        st = []
        check = {')':'(',']':'[','}':'{'}

        for c in s:
            if c in check:
                if st and st[-1] == check[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)
        return True if not st else False