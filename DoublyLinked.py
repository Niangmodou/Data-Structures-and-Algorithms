class LinkedList:
    class Node:
        def __init__(self, data = None, next=None, prev=None):
            self.data = data;
            self.next = next;
            self.prev = prev;
        def disconnect(self):
            self.data=None;
            self.next=None;
            self.prev=None;
    def __init__(self):
        self.head = LinkedList.Node();
        self.tail = LinkedList.Node();
        self.head.next = self.tail;
        self.tail.prev = self.head;
        self.size=0;
    def __len__(self):
        return self.size;
    def is_empty(self):
        return len(self) ==0;
    def first_node(self):
        if (self.is_empty()):
            raise Exception("List is empty");
        return self.head.next;
    def last_node(self):
        if (self.is_empty()):
            raise Exception("List is empty");
        return self.tail.prev;
    def add_after(self, node, data):
        new_node = LinkedList.Node(data);
        follower = node.next;
        node.next = new_node;
        new_node.next = follower;
        new_node.prev=node;
        follower.prev = new_node;
        self.size+=1;
        return new_node;
    '''
        node.next = node.next.prev = LinkedList.Node(data,next=node.next, prev=node);
        return node.next;
    '''
    def add_first(self, data):
        return self.add_after(self.head, data);
    def add_last(self,data):
        return self.add_after(self.tail.prev,data);
    def delete_node(self, node):
        if (self.is_empty()):
            raise Exception("List is empty");
        node.prev.next = node.next;
        node.next.prev = node.prev;
        self.size-=1;
        retval = node.data;
        node.disconnect();
        return retval;
    def delete_first(self):
        return self.delete_node(self.first_node());
    def delete_last(self):
        return self.delete_node(self.last_node());

    def __iter__(self):
        if (self.is_empty()):
            return;
        cursor = self.first_node();
        while cursor is not self.tail:
            yield cursor.data;
            cursor = cursor.next;

    def __repr__(self):
        return "[" + " <--> ".join([str(item) for item in self]) +"]";
    def clear(self):
        while not self.is_empty():
            self.delete_first();

    def __getitem__(self,i):
        if i >= self.size:
            raise Exception("List index is out of range")
        mid_ind = self.size//2
        if i > mid_ind:#Iterate from the Back
            curr = self.size-1
            curr_node = self.last_node()
            while curr > i:
                curr_node = curr_node.prev
                curr-=1
            return curr_node.data
        else:#Iterate from the front
            curr = 0
            curr_node = self.first_node()
            while i > curr:
                curr_node = curr_node.next
                curr+=1
            return curr_node.data

dl = LinkedList();
dl.add_last(3);
dl.add_last(5);
dl.add_last(7);
print(dl[2]);

def remove_value(llist, val):
    if llist.is_empty():
        return;
    cursor = llist.first_node();
    while cursor is not llist.tail:
        if cursor.data == val:
            temp = cursor;
            cursor = cursor.next;
            llist.delete_node(temp);
        else:
            cursor = cursor.next();
