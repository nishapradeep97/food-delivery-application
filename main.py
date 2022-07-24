import admin as aa
from user import User

je = User(str, str, str, str, str)
p = 1
q = True
r = True
while r:

    inp = int(
        input(
            "Where You want to login select 1.Admin and 2.User and 3.User Registration 4.Exit"
        ))
    if p == 0:
        q = True
    if inp == 1:
        Username = input("Enter the username of admin: ")
        Password = input("Enter the password of admin: ")
        if aa.admin_keys[Username] == Password:
            print("*****You're successfully logged inn*****")
            r = True
            while r:
                adm_choice = int(
                    input(
                        "Choose the options of admin panel 1.ADD NEW ITEM 2.EDIT ITEM 3.VIEW INVENTORY 4.REMOVE ITEM 5.EXIT"
                    ))
                if adm_choice == 1:
                    aa.add_new_item()
                elif adm_choice == 2:
                    aa.edit_from_item()
                elif adm_choice == 3:
                    aa.show_item()
                elif adm_choice == 4:
                    aa.remove_item()
                elif adm_choice == 5:
                    print(f"You're Exit to the admin panel{Username}")
                    r = False
                else:
                    print(
                        "This is the wrong selection please select valid option"
                    )
        else:
            print("These are the wrong credentials! SORRY!!!")
    elif inp == 2:
        print("Welcome to the user panel")
        email = input("Enter the email here: ")
        password = input("Enter the password here: ")
        if User.login(email, password):
            print(f"You are logged in successfully {email}")
            #p= True
            while p:
                usr_choice = int(
                    input(
                        f"{email}, Enter the option1.Place new order 2.Order history 3.Update profile 4.Exit"
                    ))
                if usr_choice == 1:
                    je.place_order()
                elif usr_choice == 2:
                    print(f"Here is your order history, {email}")
                    print(je.order_history)
                elif usr_choice == 3:
                    je.update()
                elif usr_choice == 4:
                    user_crawler = False
                    print("You're Successfully looged out")
                else:
                    print("You choose the invalid option")
        else:
            print("These are the wrong credentials! SORRY!!!")
    elif inp == 3:
        new_email = input("Enter the email:")
        if new_email in User.login_info.keys():
            print("Email already registered!!")
        else:
            nname = input("Enter your name:")
            nphoneno = int(input("Enter your Phone no:"))
            naddress = input("Enter the Address:")
            npassword = input("Enter the Password:")
            userr = User(new_email, nname, nphoneno, naddress, npassword)
            print("Registered successfully!! now you can log in!!")

    elif inp == 4:
        r = False
        exit()

else:
    exit()
