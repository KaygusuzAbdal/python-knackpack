import random as rd

itemList = []


class Item:
    def __init__(self, profits=None, weight=None):
        if profits is None:
            self.profits = rd.randint(1, 20)
        else:
            self.profits = profits
        if weight is None:
            self.weight = rd.randint(1, 10)
        else:
            self.weight = weight
        self.pW = profits / weight


class Knakpack:
    def __init__(self, limit=None):
        if limit is None:
            self.limit = rd.randint(10, 20)
        else:
            self.limit = limit
        self.storedItems = []
        self.usedCapacity = 0

    def add_item(self, item):
        if (self.usedCapacity + item.weight) <= self.limit:
            self.storedItems.append(item)
            self.usedCapacity = self.usedCapacity + item.weight
            print("Item added (weight = {0})".format(item.weight))
        else:
            print("Item tried to added (weight = {0})".format(item.weight))
            print("Out of Bound")


# example

package = Knakpack(15)

element1 = Item(10, 2)
element2 = Item(5, 3)
element3 = Item(15, 5)
element4 = Item(7, 7)
element5 = Item(6, 1)
element6 = Item(18, 4)
element7 = Item(3, 1)

itemList.append(element1)
itemList.append(element2)
itemList.append(element3)
itemList.append(element4)
itemList.append(element5)
itemList.append(element6)
itemList.append(element7)

for i in itemList:
    print("{} değerinde, {} ağrırlığındaki ürün".format(i.profits, i.weight))

newItemList = sorted(itemList, key=lambda item: item.pW, reverse=True)

print(package.limit)
print("used = {}".format(package.usedCapacity))

for element in newItemList:
    print("{} değerinde, {} ağrırlığındaki ürün için".format(element.profits, element.weight))
    package.add_item(element)
    print("used = {}".format(package.usedCapacity))
