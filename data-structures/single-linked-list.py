class ListNode:
    def __init__(self, data):
        "constructor to initiate this object"
        self.data = data
        self.next = None
        return

    def has_value(self, value):
        "method to compare the value with the node data"
        if self.data == value:
            return True
        else:
            return False


if __name__ == '__main__':
    node1 = ListNode(15)
    node2 = ListNode(8.2)
    node3 = ListNode("Canada")
