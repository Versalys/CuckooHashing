
Cuckoo Hashing
CSE 331 honors option fall of 2020
Written By Aidan Erickson (The cool dude with a cool attitude)
Under supervision of Professor Sebnam Onsay

The following data structure CuckooHashMap utilizes cuckoo hashing to achieve O(1*)
amortized insertion. The variability, of course, comes from the need to
rehash as well as the cuckoo hashing process.

Cuckoo hashing is a hashing algorithm that utilizes two hashtables with different hash functions.
When an element is added, the first hashtable is checked. If an element exists in that
hashtable, it is booted to the second hash table with its position determined by its own hash
function. If an element exists there, its own spot is taken by the new arrival and it is booted
to the first where it is, of course, hashed by the first's algorithm. This process continues until
every item has found a spot or it reaches a cycle (detected by a set max iterations).

With this in mind, replacing buckets, it has a O(1) lookup time for all elements.

For fun, I modified this algorithm to support k-ary cuckoo hashing to allow for an arbitrary number
of tables. This of course is accounted for by going down the line and rolling over onto the first
table.

Cuckoo hashing is explained quite well here: https://en.wikipedia.org/wiki/Cuckoo_hashing

I had a lot of fun on this project. Some bugs along the way, but solving them is the most fun part
of computer science.

from collections import MutableMapping

class MapBase(MutableMapping):
  Our own abstract base class that includes a nonpublic _Item class.

  #------------------------------- nested _Item class -------------------------------
  class _Item:
    Lightweight composite to store key-value pairs as map items.

    __init__(self, k, v):
      
      Initializes items with key value pair
      :param k: key
      :param v: value
      
      

    __eq__(self, other):
      
      compares two items for equality
      :param other: other item
      :return: True if equal false otherwise
      
      

    __ne__(self, other):
      
      compares two items for equality
      :param other: other item
      :return: True if unequal false otherwise
      
      

    __lt__(self, other):
      
      compares two keys to determine ordering
      :param other: other item
      :return: True if less than false otherwise
      
      

    get_key(self):
      
      returns key of item
      :return: key
      
      

    get_value(self):
      
      returns value of item
      :return: value
      
      

    __str__(self):
      
      Returns item in string representation
      :return: item string representation
      
      

    __repr__(self):
      
      Returns item in string representation
      :return: item string representation
      
      


class CuckooHashMap(MapBase):
    
    Implements a hashtable utilizing cuckoo hashing
    
    __init__(self, capacity=13, prime=309345133, table_num=2):
        
        Create empty Cuckoo hash-table map
        :param capacity: capacity of table
        :param prime: prime number used for MAD compression
        
        
     _hash_function(self, key, t):
        
        Hashes key depending on tables hash function determined by t.
        :param key: inserted key
        :param t: table number
        :return: hashed result
        

      __len__(self):
        
        Returns number of elements in all tables
        :return: number of elements
        
        

    __getitem__(self, key):
        
        Returns item associated with key
        :param key: hash key
        :return: item associated with key
        

    _rehash(self, new_item=None):
        
        Rehashes the table based on the current number of elements by adding capacity
        :param new_item: new item to be added if failed on insert
        


    __setitem__(self, key, value):
        
        Adds item to hash table. If item is already in the first table
        kick 'em out into table 2 and insert into table 1. Keep doing this until
        all items are accounted for or a cycle is found
        :param key: hashing key
        :param value: value to add
        

    __delitem__(self, key):
        
        Deletes item from hashtable
        :param key: deleted key
        
    
    __str__(self):
        
        Creates the string representation of the cuckoo hashtable
        :return: string representation
        
    
    __iter__(self):
        
        Prepare for iteration
        :return: self
        
    
    __next__(self):
        
        Cycle through next iteration
        :return: next items value
        
    
