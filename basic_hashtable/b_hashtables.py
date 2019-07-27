

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


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

    if hash_table.storage[index] is not None:
        print(f"Warning: overwriting key {hash_table.storage[index].key} with value {hash_table.storage[index].value}")

    hash_table.storage[index] = Pair(key, value)


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)

    if hash_table.storage[index] is None:
        print(f"Warning: Index {index} does not exist! Cannot remove key {key}.")

    hash_table.storage[index] = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    
    if hash_table.storage[index] is None:
        print(f"Warning: Index {index} does not exist! Cannot retrieve key {key}.")
        return None

    return hash_table.storage[index].value


def Testing():
    # ht = BasicHashTable(16)

    # hash_table_insert(ht, "line", "Here today...\n")

    # hash_table_remove(ht, "line")

    # if hash_table_retrieve(ht, "line") is None:
    #     print("...gone tomorrow (success!)")
    # else:
    #     print("ERROR:  STILL HERE")
    ht = BasicHashTable(8)

    hash_table_insert(ht, "key-0", "new-val-0")
    print(ht.storage)
    return_value = hash_table_retrieve(ht, "key-0")
    print(f"Return value: {return_value}")
    

Testing()
