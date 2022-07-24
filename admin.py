admin_keys = {"nisha": "nisha123"}

itemlist = {1: {'itemName': 'biriyani', 'itemID': 1,'price':140,'quantity':500 ,'discount':50 ,'stock': 14},
        2: {'itemName': 'chicken curry', 'itemID': 2,'price':100,'quantity':250 ,'discount':20 ,'stock': 4},
        3: {'itemName': 'beef fry', 'itemID': 3,'price':120,'quantity':500 ,'discount':40 ,'stock': 10}}
id=3
#nested dict

def add_new_item():
    global id
    id=id+1
    itemname = input("Enter the itemname")
    price = int(input("Enter the price of the item: "))
    quant=int(input("Enter the quantity"))
    dis=int(input("Enter the discount"))
    stock = int(input("Enter the stock value of item: "))
    itemlist[id] = {
        "itemName": itemname,
        "itemID": id,
        "price": price,
        "quantity":quant,
        "discount":dis,
        "stock": stock
    }
    print("The food Item"+itemname+ "is successfully added")
    return itemlist


def edit_from_item():
    item = int(input("Enter the itemid which you want to edit: "))
    a = input("Enter the item name:")
    b = int(input("Enter the price of item:"))
    c=int(input("Enter the quantity:"))
    d=int(input("Enter the discount:"))
    e =int(input("Enter the stock of the item:"))
    itemlist[item]["itemName"] = a
    itemlist[item]["price"] = b
    itemlist[item]["quantity"] = c
    itemlist[item]["discount"]=d
    itemlist[item]["stock"]=e
    print("*****Edited item successfully*****")
    return itemlist

def show_item():
    print("*****HERE IS THE FOODMENU*****")
    for i in itemlist:
        print("item Name: ",itemlist[i]["itemName"])
        print("price: ",itemlist[i]["price"],"INR")
        print("item ID: ",itemlist[i]["itemID"])
        print("quantity ",itemlist[i]["quantity"])
        print("discount: ",itemlist[i]["discount"])
        print("stock: ",itemlist[i]["stock"])

      

def remove_item():
    d = int(input("Enter the Item id which you want to exit"))
    itemlist.pop(d)
    print("Remove item successfully ")
    return itemlist






