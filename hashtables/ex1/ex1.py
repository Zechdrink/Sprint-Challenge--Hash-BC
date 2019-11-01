#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    #    x gets the index
    #    weights[x] gets the value
    #    limit - weights[x] can produce a temporary limit
    #    if another value brings that temporary limit to 0 we have found our two numbers

    for x in range(length):
    # inserts the array of weights and indexes into the hash table
        hash_table_insert(ht, weights[x], x)
        
        
    for x in range(length):
        temp = limit - weights[x]
        retrieved_pair = hash_table_retrieve(ht, temp)
        if retrieved_pair:
            return (retrieved_pair, x)
            


    """
    YOUR CODE HERE
    """

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

# arrray = [5, 2, 3, 7, 5, 6]

# for x in range(len(arrray)):
#     print(x)
#     print(arrray[x])