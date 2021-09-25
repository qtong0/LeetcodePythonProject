import collections

class Excel:

    def __init__(self, H: int, W: str):
        self.M = [[{'v': 0, 'sum': None} for i in range(H)] for j in range(ord(W) - 64)]

    def set(self, r: int, c: str, v: int) -> None:
        self.M[r - 1][ord(c) - 65] = {'v': v, 'sum': None}

    def get(self, r: int, c: str) -> int:
        cell = self.M[r - 1][ord(c) - 65]
        if not cell['sum']:
            return cell['v']
        return sum(self.get(pos[0], pos[1]) * cell['sum'][pos] for pos in cell['sum'])

    def sum(self, r: int, c: str, strs: list[str]) -> int:
        self.M[r - 1][ord(c) - 65]['sum'] = self.parse(strs)
        return self.get(r, c)

    def parse(self, strs):
        c = collections.Counter()
        for s in strs:
            s, e = s.split(':')[0], s.split(':')[1] if ':' in s else s
            for i in range(int(s[1:]), int(e[1:]) + 1):
                for j in range(ord(s[0]) - 64, ord(e[0]) - 64 + 1):
                    c[(i, chr(j+64))] += 1
        return c


# Your Excel object will be instantiated and called as such:
# obj = Excel(H, W)
# obj.set(r,c,v)
# param_2 = obj.get(r,c)
# param_3 = obj.sum(r,c,strs)


if __name__ == '__main__':
    excel = Excel(3, 'C')
    excel.set(1, 'A', 2)
    print(excel.sum(3, 'C', ['A1', 'A1:B2']))
    excel.set(2, 'B', 2)
    print(excel.get(3, 'C'))
    print('-='*10+'-')
 
    excel = Excel(5, 'E')
    print(excel.get(1, 'A'))
    print(excel.set(1, 'A', 1))
    print(excel.get(1, 'A'))
    print(excel.sum(2, 'B', ['A1', 'A1']))
    print(excel.set(1, 'A', 2))
    print(excel.get(2, 'B'))
    print('-='*10+'-')
 
    excel = Excel(5, 'E')
    print(excel.set(1, 'A', 1))
    print(excel.sum(2, 'B', ['A1']))
    print(excel.set(2, 'B', 0))
    print(excel.get(1, 'B'))
    print(excel.set(1, 'A', 5))
    print(excel.get(2, 'B'))
    print('-='*10+'-')

    excel = Excel(3, 'C')
    print(excel.sum(1, 'A', ['A2']))
    print(excel.set(2, 'A', 1))
    print(excel.get(1, 'A'))
    print('-='*10+'-')
