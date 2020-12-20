from cuckoo_hashmap import CuckooHashMap

def main():
    print("Welcome to the test case E X P E R I E N C E")
    print("Written by Aidan Erickson (the cool dude with a cool attitude)\n")
    cuckoo = CuckooHashMap()
    print("Hashing 0-29...")
    for i in range(30):
        cuckoo[i] = i
    print(cuckoo)
    cuckoo = CuckooHashMap()
    for i in range(1000):  # __setitem__
        cuckoo[i] = i
    # print(cuckoo)
    print("Get each item from hashtable...")
    test_list = []   # __getitem__
    for i in range(1000):
        # print(i)
        t = cuckoo[i]
        test_list.append(t)
    print("Equal to ranged list?:", test_list == list(range(1000)))

    del cuckoo[7]
    print("\nlets delete 7!")
    print("len after deletion of 7:", len(cuckoo))
    print("lets try to get 7...")
    try:
        print(cuckoo[7])
    except Exception as e:
        print(e)

    cuckoo = CuckooHashMap()
    print("you can even iterate thorugh!!!")
    for i in range(30):
        cuckoo[i] = i
    print(cuckoo)

    test_list = []
    print("== iteration through == ")
    for key, val in cuckoo:
        print("Key:", key, "Value:", val)
        test_list.append(key)
    test_list.sort()
    y = list(range(30))
    print("ranged list:", test_list == y)

    print("""\n\nThe data structure also allows for k-ary cuckoo hashing.
Meaning that an arbitrary number of tables can be stipulated other than 2
(2 is the default value) Lets look at that now (with 5 tables)! Groovy huh?""")

    cuckoo = CuckooHashMap(table_num=5)
    for i in range(100):
        cuckoo[i] = i
    print(cuckoo)

    test_list = []   # __getitem__
    for i in range(100):
        # print(i)
        t = cuckoo[i]
        test_list.append(t)
    print("ranged list:", test_list == list(range(100)))

if __name__ == "__main__":
    main()
