class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class RoleHierarchy:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("List is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Role is not present in List")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def delete_by_value(self, x):
        if self.head is None:
            print("Can't delete List is empty!")
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("Role is not present!")
        else:
            n.ref = n.ref.ref


def add_user(x):

    arr = []
    for i in range(x):
        name = input("Enter User Name: ")
        role = input("Enter role: ")
        arr.append(str(name+" - "+role))
    return arr


def display_user(arr):
    for i in arr:
        print(i)


LL1 = RoleHierarchy()

a = input("Enter root role name: ")
LL1.add_begin(a)
while True:
    print()
    print("-----Operations----")
    print("0. Quit")
    print("1. Add sub role")
    print("2. Display roles")
    print("3. Delete Role")
    print("4. Add User")
    print("5. Display Users")
    print()
    b = int(input("Enter operation to be performed: "))
    if b == 0:
        break
    elif b == 1:
        c = input("Enter sub role name: ")
        d = input("Enter reporting to role name: ")
        LL1.add_end(c)
    elif b == 2:
        LL1.print_LL()
        print()
    elif b == 3:
        e = input("Enter the role to be deleted: ")
        f = input("Enter the role to be transferred: ")
        LL1.delete_by_value(e)
    elif b == 4:
        x = int(input("How many Users Do you want to add: "))
        arr = add_user(x)
    else:
        display_user(arr)


############################################################ ASHOK KUMAR S ##########################################################
