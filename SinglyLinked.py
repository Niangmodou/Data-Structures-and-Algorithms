class Node:
    def __init__(self, data = None, next=None, prev=None):
        self.data = data;
        self.next = next;
        self.prev = prev;

def print_list(head):
    temp = head;
    while (temp is not None):
        print(temp.data);
        temp = temp.next;
    print("End of list");

head = Node();
head.data = 1;
head.prev=None;
head.next = Node();
head.next.data=2;
head.next.prev=head;
head.next.next=None;

#iterate over the list
print_list(head);

#add zero onto list
head.prev = Node(0,head);
head = head.prev;

print_list(head);

#add on to the end of the list
temp = head;
while temp.next is not None:
    temp = temp.next;
temp.next = Node(4, prev=None, next=temp);


