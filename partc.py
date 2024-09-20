class HashTable:
    class Node:
        def __init__(self, key, record):
            """
            Initializing a node in a table where key is associated with record and record is associated with key.
            """
            self.key = key
            self.record = record
            self.next = None

    def __init__(self, capacity=32):
        """
        Initializing table with given capacity.
        - Capacity: Initial capacity of the table is set as default 32.
        - Limitations: Capacity must be a positive intiger.
        - Functionality: The table is initialized with its default capacity, its size is set to 0 and its initialized as a list of None values.
        """
        self._capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key):
        """
        The key value pair will be saved at the index determined by the hash function.
        - Return integer (hash) value.
        - Functionality: The hash value for a perticular key is calculated using python's built- in hash function.
        """
        return hash(key) % self._capacity

    def insert(self, key, value):
        """
        Insert a key value pair into the table and it will return True if insertion is successful and false if the key already exists.
        - Return Value: True if Insertion is successful and False if key already existes.
        - Functionality: A new Key value pair is added to the hash table.
        """
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = []
        for i in self.table[index]:
            if i.key == key:
                return False
        self.table[index].append(self.Node(key, value))
        self.size += 1
        if self.size > 0.7*self._capacity:
            self.resize()
        return True

    def modify(self, key, value):
        """
        Modify the value associated with a given key.
        - Return Value: True if modification is successful, False Otherwise.
        - Functionality: Changes the value associated with a specified key.
        """
        index = self._hash(key)
        if self.table[index] is not None:
            for node in self.table[index]:
                if node.key == key:
                    node.record = value
                    return True
        return False

    def remove(self, key):
        """
        Remove a key value pair from the hash table.
        - Return value: It returns true if removal is successful or else false.
        - Functionality: A key value pair is removed from the hashtable. if the key is discovered, it is deleted from the related node.
        """
        index = self._hash(key)
        if self.table[index] is not None:
            for i, node in enumerate(self.table[index]):
                if node.key == key:
                    del self.table[index][i]
                    self.size -= 1
                    return True
        return False

    def search(self, key):
        """
        Search for the value associated with a given key in the hash table.
        - key: It returns the value associated with the key if found, otherwise it will return false.
        - Functionality: If the value is discovered, it is returned, otherwise it is none.
        """
        index = self._hash(key)
        if self.table[index] is not None:
            for node in self.table[index]:
                if node.key == key:
                    return node.record
        return None

    def capacity(self):
        """
        Get the current capacity of the hash table.
        - return Value: Integer
        - Functionality: returns the current capacity of the hash table.
        """
        return self._capacity

    def __len__(self):
        """
        - Functionality: returns the number of elements in the hash table.
        - Return Value: Integer.
        """
        return self.size

    def resize(self):
        """
        Resize the hash table when the load factor exceeds 0.7.
        - Functionality: This function doubles the capacity of the hash table and reuse all the elements.
        """
        new_capacity = self._capacity * 2
        new_table = [None] * new_capacity
        for chain in self.table:
            if chain:
                for node in chain:
                    new_index = hash(node.key) % new_capacity
                    if new_table[new_index] is None:
                        new_table[new_index] = []
                    new_table[new_index].append(node)
        self.table = new_table
        self._capacity = new_capacity
