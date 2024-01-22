class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        itr = self.head
        string_of_linked_list = ''
        while itr is not None:
            string_of_linked_list += str(itr.data) + '-->' if itr.next else str(itr.data)
            itr = itr.next
        print(string_of_linked_list)
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if (self.head is None):
            self.head = Node(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    def length_of_linked_list(self):
        itr = self.head
        counter = 0
        while itr:
            counter += 1
            itr = itr.next
        return counter

    def insert_at(self, index, data):
        if index < 0 or index > self.length_of_linked_list():
            raise Exception("Index out of range")
        if index == 0:
            self.insert_at_beginning(data)
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            count = count + 1
            itr = itr.next

    def remove_at(self, index):
        if index < 0 or index > self.length_of_linked_list():
            raise Exception("index out of range")
        if index == 0:
            self.head = self.head.next()
            return

        counter = 0
        itr = self.head
        while itr.next:
            if counter == index - 1:
                itr.next = itr.next.next
                break
            counter = counter + 1
            itr = itr.next

    def insert_array(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            raise Exception("The list was empty")
        if self.head == data_after:
            node = Node(data_to_insert, self.head.next)
            self.head = node
            return
        itr = self.head
        while itr.next:
            if itr.data == data_after:
                node = Node(data_after, itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            raise Exception("List is empty")
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.data == data:
                itr.next = itr.next.next
                break

            itr = itr.next


'''ll1 = LinkedList()
ll1.insert_at_beginning(2)
ll1.print_ll()
ll1.insert_at_beginning(4)
ll1.print_ll()
ll1.insert_at_beginning(1)
ll1.print_ll()
ll1.insert_at_end(100)
ll1.print_ll()
ll1.length_of_linked_list()
ll1.insert_at(2, 2000)
ll1.print_ll()
ll1.remove_at(4)
ll1.print_ll()
ll1.insert_array([100, 200, 300])
ll1.print_ll()'''


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_array(["banana","mango","grapes","orange"])
    ll.print_ll()
    ll.insert_after_value("mango","apple")
    ll.print_ll()
    ll.remove_by_value("orange")
    ll.print_ll()
    ll.remove_by_value("figs")
    ll.print_ll()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print_ll()




