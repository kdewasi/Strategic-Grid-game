class Stack:
    # Initializes the stack with a specified capacity.
    # Creates an internal list to store stack elements and initializes the size to 0.
    def __init__(self, cap=10):
        self._capacity = cap
        self.data = [None] * self._capacity
        self.size = 0

    # Returns the current capacity of the stack.
    def capacity(self):
        return self._capacity

    # Adds a new element to the top of the stack.
    # If the stack is full, resizes the internal list to double its current capacity.
    # data: The element to be added to the stack.
    def push(self, data):
        if self.size == self._capacity:
            self.resize()
        self.data[self.size] = data
        self.size += 1

    # Removes and returns the top element of the stack.
    # Raises an IndexError if the stack is empty.
    # Returns the top element of the stack
    def pop(self):
        if self.size == 0:
            raise IndexError('pop() used on empty stack')
        self.size -= 1
        item = self.data[self.size]
        self.data[self.size] = None
        return item

    # Returns the top element of the stack without removing it.
    # Returns None if the stack is empty.
    def get_top(self):
        if self.size == 0:
            return None
        return self.data[self.size - 1]

    # Returns true if the stack is empty
    def is_empty(self):
        return self.size == 0

    # Returns the number of elements in the stack.
    def __len__(self):
        return self.size

    # Resizes the internal list to double its current capacity.
    # Copies the existing elements to the new list.
    def resize(self):
        new_capacity = self._capacity * 2
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self._capacity = new_capacity


class Queue:
    # Initializes the queue with a specified capacity.
    # Creates an internal list to store queue elements and initializes the size, front, and back pointers.
    def __init__(self, cap=10):
        self._capacity = cap
        self.data = [None] * self._capacity
        self.size = 0
        self.front = 0
        self.back = 0

    # Returns the current capacity of the queue.
    def capacity(self):
        return self._capacity

    # Adds a new element to the back of the queue.
    # If the queue is full, resizes the internal list to double its current capacity.
    # data: The element to be added to the queue 
    def enqueue(self, data): 
        if self.size == self._capacity:
            self.resize()
        self.data[self.back] = data
        self.back = (self.back + 1) % self._capacity
        self.size += 1

    # Removes and returns the front element of the queue.
    # Raises an IndexError if the queue is empty.
    # Returns the front element of the queue
    def dequeue(self):
        if self.size == 0:
            raise IndexError('dequeue() used on empty queue')
        item = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self._capacity
        self.size -= 1
        return item

    # Returns the front element of the queue without removing it.
    # Returns None if the queue is empty.
    def get_front(self):
        if self.size == 0:
            return None
        return self.data[self.front]

    # Returns true if the queue is empty
    def is_empty(self):
        return self.size == 0

    # Returns the number of elements in the queue.
    def __len__(self):
        return self.size

    # Resizes the internal list to double its current capacity.
    # Copies the existing elements to the new list and resets the front and back pointers.
    def resize(self):
        new_capacity = self._capacity * 2
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[(self.front + i) % self._capacity]
        self.data = new_data
        self.front = 0
        self.back = self.size
        self._capacity = new_capacity


class Deque:
    # Initializes the deque with a specified capacity.
    # Creates an internal list to store deque elements and initializes the size, front, and back pointers.
    def __init__(self, cap=10):
        self._capacity = cap
        self.data = [None] * self._capacity
        self.size = 0
        self.front = 0
        self.back = 0

    # Returns the current capacity of the deque.
    def capacity(self):
        return self._capacity

    # Adds a new element to the front of the deque.
    # If the deque is full, resizes the internal list to double its current capacity.
    # data: The element to be added to the front of the deque.
    def push_front(self, data):
        if self.size == self._capacity:
            self.resize()
        self.front = (self.front - 1 + self._capacity) % self._capacity
        self.data[self.front] = data
        self.size += 1

    # Adds a new element to the back of the deque.
    # If the deque is full, resizes the internal list to double its current capacity.
    # data: The element to be added to the back of the deque.
    def push_back(self, data):
        if self.size == self._capacity:
            self.resize()
        self.data[self.back] = data
        self.back = (self.back + 1) % self._capacity
        self.size += 1

    # Removes and returns the front element of the deque.
    # Raises an IndexError if the deque is empty.
    # Returns the front element of the deque
    def pop_front(self):
        if self.size == 0:
            raise IndexError('pop_front() used on empty deque')
        data = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self._capacity
        self.size -= 1
        return data

    # Removes and returns the back element of the deque.
    # Raises an IndexError if the deque is empty.
    # Returns the back element of the deque
    def pop_back(self):
        if self.size == 0:
            raise IndexError('pop_back() used on empty deque')
        self.back = (self.back - 1 + self._capacity) % self._capacity
        data = self.data[self.back]
        self.data[self.back] = None
        self.size -= 1
        return data

    # Returns the front element of the deque without removing it.
    # Returns None if the deque is empty.
    def get_front(self):
        if self.size == 0:
            return None
        return self.data[self.front]

    # Returns the back element of the deque without removing it.
    # Returns None if the deque is empty.
    def get_back(self):
        if self.size == 0:
            return None
        return self.data[(self.back - 1 + self._capacity) % self._capacity]

    # Returns true if the deque is empty
    def is_empty(self):
        return self.size == 0

    # Returns the number of elements in the deque.
    def __len__(self):
        return self.size

    # Returns the element at the specified index in the deque.
    # Raises an IndexError if the index is out of range.
    def __getitem__(self, k):
        if k < 0 or k >= self.size:
            raise IndexError('Index out of range')
        return self.data[(self.front + k) % self._capacity]

    # Resizes the internal list to double its current capacity.
    # Copies the existing elements to the new list and resets the front and back pointers.
    def resize(self):
        new_capacity = self._capacity * 2
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[(self.front + i) % self._capacity]
        self.data = new_data
        self.front = 0
        self.back = self.size
        self._capacity = new_capacity