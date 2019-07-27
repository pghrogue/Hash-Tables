

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return "(" + self.key + ", " + self.value + ") "


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381

    for character in string:
        hash = ((hash << 5) + hash) + ord(character)

    return hash % max


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    current_pair = hash_table.storage[index]

    while current_pair is not None and current_pair.key is not key:
        current_pair = current_pair.next

    if current_pair is None:
        # We reached the end of the linked list - no matching keys
        new_pair = Pair(key,value)
        new_pair.next = hash_table.storage[index]
        hash_table.storage[index] = new_pair
    else:
        current_pair.value = value  


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)

    if hash_table.storage[index] is None:
        print(f"Warning: Index {index} does not exist! Cannot remove key {key}.")
        return

    current_pair = hash_table.storage[index]
    last_pair = None

    # Loop through linked list till it hits None or finds the key
    while current_pair is not None and current_pair.key is not key:
        last_pair = current_pair
        current_pair = current_pair.next

    if current_pair is not None:
        # key found - remove it
        if last_pair is not None:
            last_pair.next = current_pair.next
            current_pair = None
        else:
            hash_table.storage[index] = None
    else:
        # Key not found - print warning
        print(f"Warning: key {key} was not found.")



# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    
    if hash_table.storage[index] is None:
        print(f"Warning: Index {index} does not exist! Cannot retrieve key {key}.")
        return None

    current_pair = hash_table.storage[index]

    # Loop through linked list till it finds the key or runs out of nodes
    while current_pair is not None and current_pair.key is not key:
        current_pair = current_pair.next

    if current_pair is not None:
        # Key found, return it
        return current_pair.value
    else:
        # Key not found
        print(f"Warning: Key {key} was not found!")


def Testing():
    # ht = BasicHashTable(16)

    # hash_table_insert(ht, "line", "Here today...\n")

    # hash_table_remove(ht, "line")

    # if hash_table_retrieve(ht, "line") is None:
    #     print("...gone tomorrow (success!)")
    # else:
    #     print("ERROR:  STILL HERE")
    # ht = BasicHashTable(8)

    # hash_table_insert(ht, "key-0", "new-val-0")
    # print(ht.storage)
    # return_value = hash_table_retrieve(ht, "key-0")
    # print(f"Return value: {return_value}")
    ht = BasicHashTable(8)

    hash_table_insert(ht, "key-1", "new-val-1")
    print(f"After insert: {ht.storage}")
    hash_table_remove(ht, "key-1")
    print(ht.storage)
    return_value = hash_table_retrieve(ht, "key-1")
    print(return_value)

Testing()
