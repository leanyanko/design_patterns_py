class Item:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("creating new instance")
            cls._instance = super(Item, cls).__new__(cls)
        return cls._instance


print("started")

item1 = Item()
item2 = Item()

print(item1 is item2)
