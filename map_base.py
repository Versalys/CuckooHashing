"""
Mapbase.py
CSE331 Honors Project for fall 2020
Written by Professor Onsay
Modified by Aidan Erickson

Defines numerous basics and abstractions to be utilized by the data
structure in cuckoo_hashmap.py
"""

from collections import MutableMapping

class MapBase(MutableMapping):
  """Our own abstract base class that includes a nonpublic _Item class."""

  #------------------------------- nested _Item class -------------------------------
  class _Item:
    """Lightweight composite to store key-value pairs as map items."""
    __slots__ = '_key', '_value'

    def __init__(self, k, v):
      """
      Initializes items with key value pair
      :param k: key
      :param v: value
      """
      self._key = k
      self._value = v

    def __eq__(self, other):
      """
      compares two items for equality
      :param other: other item
      :return: True if equal false otherwise
      """
      return self._key == other._key   # compare items based on their keys

    def __ne__(self, other):
      """
      compares two items for equality
      :param other: other item
      :return: True if unequal false otherwise
      """
      return not (self == other)       # opposite of __eq__

    def __lt__(self, other):
      """
      compares two keys to determine ordering
      :param other: other item
      :return: True if less than false otherwise
      """
      return self._key < other._key    # compare items based on their keys

    def get_key(self):
      """
      returns key of item
      :return: key
      """
      return self._key

    def get_value(self):
      """
      returns value of item
      :return: value
      """
      return self._value

    def __str__(self):
      """
      Returns item in string representation
      :return: item string representation
      """
      return "Item:" + str((self._key, self._value))

    def __repr__(self):
      """
      Returns item in string representation
      :return: item string representation
      """
      return self.__str__()
