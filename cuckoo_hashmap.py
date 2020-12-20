"""
Cuckoo Hashing
CSE 331 honors option fall of 2020
Written By Aidan Erickson (The cool dude with a cool attitude)
Under supervision of Professor Sebnam Onsay

Hashmap that utilizes the cuckoo hashing method.
"""
from random import randrange

from map_base import MapBase


class CuckooHashMap(MapBase):
    """
    Implements a hashtable utilizing cuckoo hashing
    """
    def __init__(self, capacity=13, prime=309345133, table_num=2):
        """
        Create empty Cuckoo hash-table map
        :param capacity: capacity of table
        :param prime: prime number used for MAD compression
        """
        self._n = 0
        self._tables = [capacity * [None] for i in range(table_num)]
        self._prime = prime
        self._scaling_facts = [1 + randrange(prime-1) for _ in range(table_num)]
        self._shifts = [randrange(prime) for _ in range(table_num)]
        self._max_iter = int(capacity * table_num)  # for cycle detecting

    def _hash_function(self, key, t):
        """
        Hashes key depending on tables hash function determined by t.
        :param key: inserted key
        :param t: table number
        :return: hashed result
        """
        return (hash(key)*self._scaling_facts[t]+self._shifts[t]) % self._prime % len(self._tables[t])

    def __len__(self):
        """
        Returns number of elements in all tables
        :return: number of elements
        """
        return self._n

    def __getitem__(self, key):
        """
        Returns item associated with key
        :param key: hash key
        :return: item associated with key
        """
        for i in range(len(self._tables)):
            j = self._hash_function(key, i)
            if self._tables[i][j] and self._tables[i][j].get_key() == key:
                return self._tables[i][j].get_value()
        raise KeyError("Key not found in either table.")

    def _rehash(self, new_item=None):
        """
        Rehashes the table based on the current number of elements by adding capacity
        :param new_item: new item to be added if failed on insert
        """
        all_items = []
        for table in self._tables:
            all_items.extend(item for item in table if item is not None)
        self._tables = [len(self._tables[0]) * 2 * [None] for i in range(len(self._tables))]
        self._n = 0

        for item in all_items:
            self.__setitem__(item.get_key(), item.get_value())

        if new_item:
            self.__setitem__(new_item.get_key(), new_item.get_value())


    def __setitem__(self, key, value):
        """
        Adds item to hash table. If item is already in the first table
        kick 'em out into table 2 and insert into table 1. Keep doing this until
        all items are accounted for or a cycle is found
        :param key: hashing key
        :param value: value to add
        """
        item = self._Item(key, value)
        iterations = 0
        table_num = 0
        while iterations < self._max_iter:  # for table jumping
            index = self._hash_function(item.get_key(), table_num)
            if not self._tables[table_num][index] or self._tables[table_num][index] == item:
                if not self._tables[table_num][index]:
                    self._n += 1
                self._tables[table_num][index] = item
                return
            tmp = self._tables[table_num][index]
            self._tables[table_num][index] = item
            item = tmp
            iterations += 1
            table_num = table_num + 1 if table_num < len(self._tables)-1 else 0

        self._rehash(item)

    def __delitem__(self, key):
        """
        Deletes item from hashtable
        :param key: deleted key
        """
        for t, table in enumerate(self._tables):
            index = self._hash_function(key, t)
            if table[index] and table[index].get_key() == key:
                table[index] = None
                self._n -= 1
                return
        raise KeyError("Key not in hashmap")

    def __str__(self):
        """
        Creates the string representation of the cuckoo hashtable
        :return: string representation
        """
        ret = "size: " + str(self._n) + '\n'
        for t, table in enumerate(self._tables):
            ret += "Table #" + str(t) + ':' + '\n'
            for i, item in enumerate(table):
                if item:
                    ret += '\t' + str(i) + ', ' + str(item) + '\n'
        return ret

    def __iter__(self):
        """
        Prepare for iteration
        :return: self
        """
        self._last = (0,0)
        return self

    def __next__(self):
        """
        Cycle through next iteration
        :return: next items value
        """
        table, index = self._last
        while table < len(self._tables):
            if index >= len(self._tables[0]):
                table += 1
                index = 0
                continue
            if self._tables[table][index]:
                self._last = table, index + 1
                return self._tables[table][index].get_key(), self._tables[table][index].get_value()
            index += 1
        raise StopIteration

