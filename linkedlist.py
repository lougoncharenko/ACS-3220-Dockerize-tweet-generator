#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions?"""
        count = 0
        if not self.is_empty():
            current_item = self.head  
            while current_item is not None:
                count += 1
                current_item = current_item.next 
        return count 
       
    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node 
            self.tail = new_node
        else: 
            self.tail.next = new_node #inserting after the tail
            self.tail = new_node # telling the code the new_node is now tail


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node 
            self.tail = new_node
        else: 
            new_node.next = self.head #putting it in front of the head
            self.head = new_node #assigning the role of head to the new node

    def find(self, matcher):
        """Return an item from this linked list if it is present.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        if self.is_empty():
            return False
        current_item = self.head
        while current_item is not None:
            if current_item.data == matcher:
                return True
            current_item = current_item.next
        return False

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        if not self.is_empty():
            current_item = self.head
            previous_item = None
            while current_item  is not None:
                if current_item.data == item:
                    # if this node is the only node
                    if previous_item is None and current_item.next is None:
                        self.tail = None
                        self.head = None
                    # if this node is the head
                    elif previous_item is None:
                        self.head = current_item.next
                    # if this node is the tail
                    elif current_item.next is None:
                        self.tail = previous_item #previous item is now the tail
                        self.tail.next = None #deletion
                    # every other case
                    else:
                        previous_item.next = current_item.next
                    return(item)
                else:
                    #how i move down the linked list
                    previous_item = current_item 
                    current_item = current_item.next

            raise ValueError(f'Item not found: {item}')
        else:
            raise ValueError(f'Item not found: {item}')

    def replace(self, original_item, new_item):
        node = self.head
        while node is not None:
            if node.data == original_item:
                node.data = new_item
                return
            node = node.next

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))
    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
