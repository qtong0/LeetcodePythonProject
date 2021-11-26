from typing import List


class Person:
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.childrenList = []
        self.isDead = False


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = Person(kingName)
        self.hashmap = {kingName: self.root}


    def birth(self, parentName: str, childName: str) -> None:
        parent = self.hashmap[parentName]
        child = Person(childName)
        parent.children[childName] = child
        parent.childrenList.append(child)
        self.hashmap[childName] = child


    def death(self, name: str) -> None:
        person = self.hashmap[name]
        person.isDead = True


    def getInheritanceOrder(self) -> List[str]:
        res = []
        self.inhertianceHelper(self.root, res)
        return res

    def inhertianceHelper(self, person, res):
        if not person.isDead:
            res.append(person.name)
        for child in person.childrenList:
            self.inhertianceHelper(child, res)


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()


if __name__ == '__main__':
    t = ThroneInheritance('king')
    # ["king","andy"],["king","bob"],["king","catherine"],["andy","matthew"],["bob","alex"],["bob","asha"],
    t.birth("king","andy")
    t.birth("king","bob")
    t.birth("king","catherine")
    t.birth("andy","matthew")
    t.birth("bob","alex")
    t.birth("bob","asha")
    print(t.getInheritanceOrder())
    t.death("bob")
    print(t.getInheritanceOrder())
