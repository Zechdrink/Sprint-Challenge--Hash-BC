#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for x in range(length):
        hash_table_insert(hashtable, tickets[x].source, tickets[x].destination)
        if tickets[x].source == "NONE":
            starting_destination = tickets[x].destination
            route[0] = starting_destination

    for x in range(length):
        currentDest = hash_table_retrieve(hashtable, starting_destination)
        if x != 0:
            route[x] = currentDest
            starting_destination = currentDest
        
    return route



    """
    YOUR CODE HERE
    """

    return route
