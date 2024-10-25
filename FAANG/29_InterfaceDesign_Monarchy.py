# Constraints:
# Can we implement helper classes or methods? YES
# Case:
class Monarch:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.isAlive = True


class Monarchy:
    def __init__(self, king):
        self.king = Monarch(king)

    def birth(self, child_name, parent_name):
        parent = self.findPerson(self.king, parent_name)
        if parent:
            monarchChild = Monarch(child_name)
            parent.children.append(monarchChild)
        else:
            print(f"Parent {parent_name} not found!")

    def findPerson(self, root, name):
        if root.name == name:
            return root
        for child in root.children:
            found = self.findPerson(child, name)
            if found:
                return found
        return None

    def death(self, person_name):
        person = self.findPerson(self.king, person_name)
        if person:
            person.isAlive = False
        else:
            print(f"Person {person_name} not found!")

    def getOrderOfSuccession(self):
        order = []
        if not self.king:
            return order
        self.orderHelper(self.king, order)
        return order

    def orderHelper(self, root, order):
        if root.isAlive:
            order.append(root.name)
        for branch in root.children:
            self.orderHelper(branch, order)


# use hashmap to improve the solution
class Monarchy:
    def __init__(self, king_name):
        self.king = Monarch(king_name)
        self.person_map = {king_name: self.king}  # Hash map for quick lookup

    def birth(self, child_name, parent_name):
        parent = self.person_map.get(parent_name)
        if parent:
            monarch_child = Monarch(child_name)
            parent.children.append(monarch_child)
            self.person_map[child_name] = monarch_child  # Add child to the map
        else:
            print(f"Parent {parent_name} not found!")

    def death(self, person_name):
        person = self.person_map.get(person_name)
        if person:
            person.isAlive = False
        else:
            print(f"Person {person_name} not found!")

    def getOrderOfSuccession(self):
        order = []
        self.orderHelper(self.king, order)
        return order

    def orderHelper(self, root, order):
        if root.isAlive:
            order.append(root.name)
        for child in root.children:
            self.orderHelper(child, order)


monarchy = Monarchy("King Arthur")
monarchy.birth("Prince Charles", "King Arthur")
monarchy.birth("Prince Lily", "Prince Charles")
monarchy.birth("Prince William", "Prince Charles")
monarchy.birth("Prince Harry", "Prince Charles")
print(monarchy.getOrderOfSuccession())


monarchy.death("Prince Charles")
print(monarchy.getOrderOfSuccession())
