class Solution(object):
    def calculate(self, s: str) -> int:
        if not s: return 0
        queue = []
        for c in s:
            queue.append(c)
        queue.append('+')
        return self.cal(queue)

    def cal(self, queue):
        sign = '+'
        num = 0
        stack = []
        while queue:
            c = queue.pop(0)
            if c == ' ':
                continue
            if c.isdigit():
                num = 10*num + ord(c) - ord('0')
            elif c == '(':
                num = self.cal(queue)
            else:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    tmp = stack.pop()
                    if tmp % num != 0 and tmp*num < 0:
                        stack.append(tmp // num+1)
                    else:
                        stack.append(tmp // num)
                num = 0
                sign = c
                if c == ')':
                    break
        sumVal = 0
        while stack:
            sumVal += stack.pop()
        return sumVal
    
    def test(self):
        testCases = [
            "5 - 3/2",
            " 6-4 / 2 ",
            "1 + 1",
            "2*(5+5*2)/3+(6/2+8)",
            "(2+6* 3+5- (3*14/7+2)*5)+3",
            "-1+4*3/3/3",
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.calculate(s)
            print('result: %s' % result)
            print('-='*30+'-')

if __name__ == '__main__':
    Solution().test()
