import admin as ad

class User:
    login_info = {}

    def __init__(self,email, name, phoneno, address, password):
        self.email=email
        self.name = name
        self.phoneno = phoneno
        self.address = address
        self.password = password
        User.login_info[self.email] ={'Email':self.email,'Name':self.name,'Phone':self.phoneno,'Address':self.address,'Password':self.password}
        self.order_history = {}

    @classmethod
    def login(cls, email, password):
      if email in cls.login_info.keys():
          if cls.login_info.get(email)['Password'] == password:
            print("You're are successfully logged in.....")
            return True
          else:
            print("SORRY! These are the Wrong Credentials")
            return 
      else:
        print(f"{email} not yet registered...First you need to register  ")

    def place_order(self):
        print("What you want to order here in the food menu")
        print(ad.show_item())
        user_choice = int(input("If you want to order then select 1.YES 2.NO"))
        if user_choice == 1:
            n=int(input("Enter how many items do you want to Order"))
            x=0
            for i in range(n):
             
             itemid = int(input("Enter the Item id here: "))
             quan = int(input("Enter the quantity of the item: "))
             x += ad.itemlist[itemid]["price"] * quan
             self.order_history[itemid] = {
                    "Item Name": ad.itemlist[itemid]["itemName"],
                    "price": ad.itemlist[itemid]["price"],
                    "quantity": quan
                } 
            again_ask = input("Are you still want to order this Enter YES or NO")
            if again_ask == "YES":
             
                print(f"It costs you {x}INR in total")
                print("You're all set for this order")


                print("You're order is successfully placed")

            elif again_ask == "NO":
                print("This Order is cancelled!! You can look once more")
            else:
                print("Invalid choice")
        elif user_choice == 2:
            print("You select 2 option so we cancelled this")
        else:
            print("Enter the invalid choice")

    def display_ordr_history(self):
      print(self.order_history)

    def update(self):
      #print("Enter the updations:")
      email=input("Enter the email id for the user to be updated:")
      if email in User.login_info.keys():
        print(" Exitss!!")
        del User.login_info[email]
        nemail=input("Enter new email id:")
        nname=input("Enter new name:")
        nphone=int(input("Enter new phone no:"))
        npass=input("Enter new password:")
        User.login_info[nemail]={'Email':nemail,'Name:':nname,'phone':nphone,'Password':npass}
        print("User Profile updated Successfully!!")
      else:
        print("Email does not Matches,Try again with a valid Email")
       





