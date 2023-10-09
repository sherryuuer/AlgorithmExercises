class hash_table():
    def __init__(self, size):  # Initialize the size
        self.size = size
        self.data = [None] * self.size
        # Initialize an array of size 'size' with None

    def __str__(self):
        # Print the attributes of the class object in a dictionary format
        return str(self.__dict__)

    def _hash(self, key):  # A functiont to give the data a place to hold.
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % self.size
            # ord(key[i]) gives the unicode code point of the character key[i]
        return hash  # The hashed value/where to hold the data set.

    def sets(self, key, value):  # Function to insert a new key, value pair
        address = self._hash(key)
        if not self.data[address]:
            # If the 'hash' position of the data array is empty, we insert the key, value pair as a list
            self.data[address] = [[key, value]]
        else:
            # If the 'hash' position is not empty, implying a collision, we simply append the list of key,value pair to the lists already present
            self.data[address].append([key, value])
        print(self.data)

    def get(self, key):  # Function to return the value of the key
        address = self._hash(key)
        # Hash value of the key is calculated by passsing key to the _hash
        if self.data[address]:
            # Multiple items may exist in the position of the hash value returned by the hash function, so we have to chceck all of them
            for i in range(len(self.data[address])):
                # We loop over the entire list of lists that may be present in the 'hash' position of the data array
                if self.data[address][i][0] == key:
                    # For every list in the list of lists(extracted by 'i'), we match the first element of the list with the given key
                    return self.data[address][i][1]
                    # If we get a match, we return the second element of that list, which is the value
        return None  # If we don't find the key, we return None

    def keys(self):  # without collision
        # Function to return all the keys
        keys_array = []  # Array to hold the keys
        for i in range(self.size):
            if self.data[i]:  # If we find a non-empty bucket, we go in and loop over all the key,value pairs that might be in it
                if len(self.data[i]) > 1:
                    for j in range(len(self.data[i])):  # Looping over all the lists(key,value pairs) in the current bucket
                        keys_array.append(self.data[i][j][0])
                else:
                    keys_array.append(self.data[i][0][0])
        return keys_array

    def values(self):
        # Function to return all the values, with exactly the same logic as the keys function
        values_array = []
        for i in range(self.size):
            if self.data[i]:
                for j in range(len(self.data[i])):
                    values_array.append(self.data[i][j][1])  # Only difference from the keys function is instead of appending the first element, we are appending the last element of each list
        return values_array


new_hash = hash_table(2)
# #{'size': 2, 'data': [None, None]}

new_hash.sets('one', 1)
new_hash.sets('two', 2)
new_hash.sets('three', 3)
new_hash.sets('four', 4)
new_hash.sets('five', 5)
# print(new_hash)
# #{'size': 2, 'data': [[['one', 1], ['five', 5]], [['two', 2], ['three', 3], ['four', 4]]]}

print(new_hash.get('one'))
# #1

print(new_hash.keys())
# #['one', 'five', 'two', 'three', 'four']
print(new_hash.values())
# #[1, 5, 2, 3, 4]


# Another solution
class Hashtable:
    def __init__(self):

        self.bucket = 16
        self.hashmap = [[] for i in range(self.bucket)]

    def __str__(self):
        return str(self.__dict__)

    def _hash(self, key):
        return len(key) % self.bucket

    def put(self, key, value):
        """
        value may already be present
        """
        address = self._hash(key)
        reference = self.hashmap[address]
        for i in range(len(reference)):
            if reference[i][0] == key:
                reference[i][1] = value
                return None
        reference.append([key, value])
        return None

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        address = self._hash(key)
        reference = self.hashmap[address]
        for i in range(len(reference)):
            if reference[i][0] == key:
                return reference[i][1]
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        address = self._hash(key)
        reference = self.hashmap[address]
        for i in range(len(reference)):
            if reference[i][0] == key:
                reference.pop(i)
                return None
        return None


h = Hashtable()
h.put('grapes', 1000)
h.put('apples', 10)
h.put('ora', 300)
h.put('banan', 200)
print(h.get('grapes'))
print(h)
h.remove('apples')
print(h)
