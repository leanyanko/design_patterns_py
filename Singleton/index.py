class Item:

    _instance = None

    def __init__(self):
        raise RuntimeError("call instance() instead")

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print("creating new instance")
            cls._instance = cls.__new__(cls)
        return cls._instance


# item = Item()

print("started")

item1 = Item.instance();
item2 = Item.instance();

print(item1 is item2)
