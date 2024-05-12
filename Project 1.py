from typing import TypeVar, List

# for more information on type hinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")  # represents generic type
Node = TypeVar("Node")  # represents a Node object (forward-declare to use in Node __init__)
DLL = TypeVar("DLL")




class Node:
    """
    Implementation of a doubly linked list node.
    DO NOT MODIFY
    """
    __slots__ = ["value", "next", "prev", "child"]

    def __init__(self, value: T, next: Node = None, prev: Node = None, child: Node = None) -> None:
        """
        Construct a doubly linked list node.

        :param value: value held by the Node.
        :param next: reference to the next Node in the linked list.
        :param prev: reference to the previous Node in the linked list.
        :return: None.
        DO NOT MODIFY
        """
        self.next = next
        self.prev = prev
        self.value = value

        # The child attribute is only used for the application problem
        self.child = child

    def __repr__(self) -> str:
        """
        Represents the Node as a string.

        :return: string representation of the Node.
        DO NOT MODIFY
        """
        return f"Node({str(self.value)})"

    __str__ = __repr__


class DLL:
    """
    Implementation of a doubly linked list without padding nodes.
    Modify only below indicated line.
    """
    __slots__ = ["head", "tail", "size"]

    def __init__(self) -> None:
        """
        Construct an empty doubly linked list.

        :return: None.
        DO NOT MODIFY
        """
        self.head = self.tail = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        DO NOT MODIFY
        """
        result = []
        node = self.head
        while node is not None:
            result.append(str(node))
            node = node.next
            if node is self.head:
                break
        return " <-> ".join(result)

    def __str__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        return repr(self)

    def __eq__(self, other: DLL) -> bool:
        """
        :param other: compares equality with this List
        :return: True if equal otherwise False
        DO NOT MODIFY
        """
        cur_node = self.head
        other_node = other.head
        while True:
            if cur_node != other_node:
                return False
            if cur_node is None and other_node is None:
                return True
            if cur_node is None or other_node is None:
                return False
            cur_node = cur_node.next
            other_node = other_node.next
            if cur_node is self.head and other_node is other.head:
                return True
            if cur_node is self.head or other_node is other.head:
                return False

    # MODIFY BELOW #
    # Refer to the classes provided to understand the problems better#

    def empty(self) -> bool:
      """
      This function determines if the
      DLL is empty or not by returning True
      or False

      :return: True if DLL is empty, else False.
      """
      if self.head is None:
        return True
      else:
        return False

    def push(self, val: T, back: bool = True) -> None:
      """
      This function adds a node containing a 
      certain data value to the back or the front
      of the DLL and it also updates the size
      when adding the new node

      :param val: Value to be added to the DLL
      :param back: If True, add val to the back of the DLL. 
      If False, add to the front. Note that the default value is True.
      :return: None.
      """
      new_node = Node(val)
      if back:
        if self.head is None:
          self.head = new_node
          self.tail = new_node
        else:
          new_node.prev = self.tail
          self.tail.next = new_node
          self.tail = new_node
      else:
        if self.head is None:
          self.head = new_node
          self.tail = new_node
        else:
          new_node.next = self.head
          self.head.prev = new_node
          self.head = new_node
      self.size +=1
        
  
    def pop(self, back: bool = True) -> None:
      """
      This function removes a node from the back
      or the front and it updates the size of 
      the DLL when popping the node

      :param back: If True, remove from the back of the DLL.
      If False, remove from the front. Note that the default value is True.
      :return: None.
      """
      if self.head is None:
        return 
      if back:
        if self.head == self.tail:
          self.head = None
          self.tail = None
        else: 
          self.tail = self.tail.prev
          self.tail.next = None
      else:
        if self.head == self.tail:
          self.head = None
          self.tail = None
        else:
          self.head = self.head.next
          self.head.prev = None
      self.size -=1
        

    def list_to_dll(self, source: List[T]) -> None:
      """
      This function creates a Doubly linked
      List from a regular Python List and if the
      there are already nodes in the DLL it should below
      deleted and replaced from the python list

      :param source: Standard Python list from which to construct DLL.
      :return: None.
      """
      self.head = None
      self.tail = None

      for i in source:
          new_node = Node(i)
          if self.head is None:
              self.head = new_node
              self.tail = new_node
          else:
              new_node.prev = self.tail
              self.tail. next = new_node
              self.tail = new_node
          self.size = len(source)

 
    def dll_to_list(self) -> List[T]:
      """
      This function creates a python list 
      from a Doubly Linked List

      :return: list[T] containing the values of the nodes in the DLL.
      """
      emptylist = []

      current = self.head
      while current is not None:
        emptylist.append(current.value)
        current = current.next
      return emptylist

    def _find_nodes(self, val: T, find_first: bool = False) -> List[Node]:
      """
      This function makes a list of node with a 
      certain value in the Doubly Linked List and then
      it returns the associated Node object 

      :param val: Value to be found in the DLL.
      :param find_first: if True find only the first element in the DLL,
      it false find all instances of the elements in the DLL.
      :return: list of Node objects in the DLL whose value is val.
      If val does not exist in the DLL, returns empty list.
      """
      answer = []

      current = self.head
      while current is not None:
        if current.value == val:
          answer.append(current)
        current = current.next
      return answer

    def find(self, val: T) -> Node:
      """
      This function finds the first node that
      has the value passed in as a parameter
      and then it returns the associated Node
      object

      :param val: Value to be found in the DLL.
      :return: first Node object in the DLL whose value is val.
      If val does not exist in the DLL, return None.
      """
      nodes = self._find_nodes(val, find_first=True)
      if nodes:
        return nodes[0]
      else:
        return None

    def find_all(self, val: T) -> List[Node]:
      """
      This function finds all Nodes that have the 
      value of the parameter passed in and then returns
      a python list containing the Nodes that meet the
      criteria

      :param val: Value to be found in the DLL.
      :return: standard Python list of all Node objects in the DLL whose value is val.
      If val does not exist in the DLL, returns an empty list.
      """
      nodes = self._find_nodes(val, find_first=False)
      return nodes


    def _remove_node(self, to_remove: Node) -> None:
      """
      This function is given a reference to a Node
      and then that Node must be removed the Doubly
      Linked List

      :param to_remove: Node to be removed from the DLL.
      :return: None.
      """
      if to_remove:
        if to_remove.next:
          to_remove.next.prev = to_remove.prev
        else:
          self.tail = to_remove.prev
        if to_remove.prev:
          to_remove.prev.next = to_remove.next
        else:
          self.head = to_remove.next
        self.size -=1
        

    def remove(self, val: T) -> bool:
      """
      This function implements the _remove_node function
      by finding the first Node that has the value passed
      in as a paramter in the DLL and then removes it

      :param val: Value to be removed from the DLL.
      :return: True if a Node with value val was found 
      and removed from the DLL, else False.
      """
      to_remove = self.find(val)
      if to_remove:
        self._remove_node(to_remove)
        return True
      else:
        return False

    def remove_all(self, val: T) -> int:
      """
      This function calls the _remove_node function and 
      removes all Node objects that has the value val
      that is passed in as a parameter and removes them
      from the DLL

      :param val: Value to be removed from the DLL.
      :return: number of Node objects with value val removed from the DLL.
      If no node containing val exists in the DLL, returns 0.
      """
      to_remove = self.find_all(val)
      counter = 0
      for i in to_remove:
        self._remove_node(i)
        counter +=1 
      return counter

    def reverse(self) -> None:
      """
      This function reverses the DLL so it
      reverses every Node in the DLL by changing the 
      references to the Nodes and head and tail

      :return: None.
      """
      current = self.head
      while current is not None:
        temp = current.next
        current.next = current.prev
        current.prev = temp
        current = temp
        
      temp = self.head
      self.head = self.tail
      self.tail = temp





def dream_escaper(dll: DLL) -> DLL:
    """
    This function turns a multilevel DLL
    into a single level DLL and adds the children 
    into the DLl

    :param dll: A DLL where each Node holds a value of str where the string
    is the task. The Node may also hold a child in .child and store the
    child DLL to the current node
    :return: a DLL holding str representing the names of all of the tasks
    """
    current_node = dll.head
    while current_node:
        if current_node.child:
            child_head = current_node.child
            child_tail = child_head
            while child_tail.next:
                child_tail = child_tail.next

            if current_node.next:
                next_node = current_node.next
                current_node.next = child_head
                child_head.prev = current_node
                child_tail.next = next_node
                next_node.prev = child_tail
            else:
                current_node.next = child_head
                child_head.prev = current_node
                dll.tail = child_tail  

            current_node.child = None  

        current_node = current_node.next

    return dll


    

    



    