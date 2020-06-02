class Node:
    def __init__(self, number=None):
        self.number = number
        self.nextNode = None


class BigInt():
    def __init__(self):
        self.head = None

    def insertNumber(self, number):
        for x in range(len(str(number))):
            self.insert(int(str(number)[x]))

    def insert(self, number):
        NewNode = Node(number)
        NewNode.nextNode = self.head
        self.head = NewNode

    def listprint(self):
        printval = self.head
        value = ""
        while printval is not None:
            value += str(printval.number)
            printval = printval.nextNode

        return value#[::-1]
    
    def __add__(self, other):
        carry = 0
        result = BigInt()
        head = self.head
        head2 = other.head
        while head != None and head2 != None:
            temp = head.number + head2.number + carry
            if (temp >= 10):
                temp -= 10
                carry = 1
            else:
                carry = 0
            result.insert(temp)
            head = head.nextNode
            head2 = head2.nextNode
        if (head == None):
            while(head2 != None):
                if(carry == 1):
                    if(head2.number + 1 >= 10):
                        result.insert(head2.number + 1 - 10)
                        carry = 1
                    else:
                        carry = 0
                        result.insert(head2.number + 1)
                else:
                    result.insert(head2.number)
                head2 = head2.nextNode
        else:
            while(head != None):
                if(carry == 1):
                    if(head.number + 1 >= 10):
                        result.insert(head.number + 1 - 10)
                        carry = 1
                    else:
                        carry = 0
                        result.insert(head.number + 1)
                else:
                    result.insert(head.number)
                head = head.nextNode
        if carry == 1:
            result.insert(1)
        return result