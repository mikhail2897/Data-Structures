class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def print_dll_fwd(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        dll_string = ''
        while itr:
            dll_string += str(itr.data) + '-->'
            itr = itr.next
        print(dll_string)

    def print_dll_rev(self):
        if self.head is None:
            print("Linked List is empty")
            return

        last_node = self.get_tail()
        itr = last_node
        dll_string = ''
        while itr:
            dll_string += str(itr.data) + '-->'
            itr = itr.prev
        print(dll_string)

    def get_tail(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1
        return count

    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(data, self.head)
            self.head = node
        else:
            node = Node(data, self.head)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            print("Index is out of range")
            return
        if index == 0:
            self.insert_at_beginning(data)
            return
        itr = self.head
        count = 0
        while itr.next:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            print("Index is out of range")
            return

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        itr = self.head
        count = 0
        while itr.next:
            if count == index:
                itr.next.prev = itr.prev
                if itr.next:
                    itr.prev.next = itr.next
                break
            itr = itr.next
            count = count + 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)




if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print_dll_fwd()
    ll.print_dll_rev()
    ll.insert_at_end("figs")
    ll.print_dll_fwd()
    ll.insert_at(0, "jackfruit")
    ll.print_dll_fwd()
    ll.insert_at(6, "dates")
    ll.print_dll_fwd()
    ll.insert_at(2, "kiwi")
    ll.print_dll_fwd()
