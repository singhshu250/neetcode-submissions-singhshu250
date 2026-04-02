class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sum = 0
        st = []
        for i, char in enumerate(operations):
            if char.lstrip('-').isdigit() :
                sum += int(char)
                st.append(int(char))
            elif char == "+":
                sum += st[-1] + st[-2]
                st.append(st[-1] + st[-2])
            elif char == "D":
                sum += (2 * st[-1])
                st.append(2 * st[-1])
            elif char == "C":
                sum -= st.pop()
        return sum

        