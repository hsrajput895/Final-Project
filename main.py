import re
from string import printable
from operation import *
import random


class Foodcounter():

 def start():
    while True:
        try:
            choice = int(input("Enter \n1.Register \n2.Login \n3.Exit \n"))
        except ValueError:
            print("Please enter valid choice!")
            continue

        if choice == 1:
            try:
                register_choice = int(input("Enter \n1.Register as Admin \n2.Register as User \n3.Exit \n"))
            except ValueError:
                print("Please enter valid choice!")
                continue

            if register_choice == 1:
                name = input("Enter your name : ")                
                mobile = input("Enter your mobile : ")
                email = input("Enter your email : ") 
                address = input("Enter your address : ")               
                password = input("Enter your password : ")                

                name_re = re.findall(r'^[A-Za-z]{2,15}\s[A-Za-z]{2,15}$', name)
                mobile_re = re.findall(r'^[1-9]{1}[0-9]{9}$' , mobile)
                email_re = re.findall("^[A-z][a-zA-Z0-9._]+[@][a-z]+[.][a-z]+$",email)
                address_re=re.findall(r'^[A-Za-z]{2,15}\s[A-Za-z]{2,15}$', address)
                password_re = re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$" , password)

                if name_re and mobile_re and email_re and password_re and address_re:
                    flag = register("admin.json",name,mobile,email,address,password)
                    
                    if flag:
                        print("Successfully Registered!")
                    else:
                        print("Registeration Unsuccessful")
                else:
                    if not name_re:
                        print("Entered name format is incorrect")
                        continue
                    if not mobile_re:
                        print("Entered mobile format is incorrect")
                        continue
                    if not email_re:
                        print("Entered email format is incorrect")
                        continue
                    if not address_re:
                        print("Entered address format is incorrect")
                        continue 
                    if not password_re:
                        print("Entered passward format is incorrect")
                        continue

            if register_choice == 2:
                name = input("Enter your name : ")                
                mobile = input("Enter your mobile : ")
                email = input("Enter your email : ")  
                address=input("Enter your address : ")               
                password = input("Enter your password : ") 
                name_re = re.findall(r'^[A-Za-z]{2,15}\s[A-Za-z]{2,15}$', name)
                mobile_re = re.findall(r'^[1-9]{1}[0-9]{9}$' , mobile)
                email_re = re.findall("^[A-z][a-zA-Z0-9._]+[@][a-z]+[.][a-z]+$",email)
                address_re=re.findall(r'^[A-Za-z]{2,15}\s[A-Za-z]{2,15}$', address)
                password_re = re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$" , password)

                if name_re and mobile_re and email_re and password_re and address_re:
                    flag = register("User.json",name,mobile,email,address,password)
                    
                    if flag:
                        print("Successfully Registered!")
                    else:
                        print("Registeration Unsuccessful")
                else:
                    if not name_re:
                        print("Entered name format is incorrect")
                        continue
                    if not mobile_re:
                        print("Entered mobile format is incorrect")
                        continue
                    if not email_re:
                        print("Entered email format is incorrect")
                        continue
                    if not address_re:
                        print("Entered address format is incorrect")
                        continue
                    if not password_re:
                        print("Entered passward format is incorrect")
                        continue

            if register_choice == 3:
                print("***Bye****")
                exit()
        
        if choice == 2:
            login_choice = int(input("Enter \n1.Login as Admin \n2.Login User \n3.Exit : \n"))
            if login_choice == 1:
                email_id = input("Enter your email ID : ")
                password = input("Enter your password : ")
                flag = login("admin.json",email_id,password)
                if flag:
                    print("Login Successful")
                    while True:
                        admin_choice = int(input("Enter \n1.Add new food item \n2.View list of food item \n3.Edit food item\n4.Revove food item\n5.Continue to main Menu : \n"))
                        # Create Module
                        if admin_choice == 1:
                            
                            food_ID = random.randint(10000,20000)
                            food_name = input("Enter Food Name : ")
                            food_quantity  = input("Enter food quantity (it should be 100ml, 250gm, 4pieces) : ")
                            food_price  = input("Enter food price : ")
                            food_discount= input("Enter Discount given on food : ")
                            food_stock= input("Enter Available food stock: ")

                            if food_ID and food_name and food_quantity and food_price and food_discount and food_stock :
                                flag = add_new_food_item("food_item.json",food_ID,food_name,food_quantity,food_price,food_discount,food_stock)
                                if flag:
                                    print("food Item Addred Sucessfully is added successfully")
                                else:
                                    print("food item did not get added")
                        # View food item
                        if admin_choice == 2:
                            data = view_food_item("food_item.json")
                            for i in data:
                                print(i)

                        # Update Module
                        if admin_choice == 3:
                            food_ID = random.randint(10000,20000)
                            food_name = input("Enter Food Name : ")
                            food_quantity  = input("Enter food quantity (it should be 100ml, 250gm, 4pieces) : ")
                            food_price  = input("Enter food price : ")
                            food_discount= input("Enter Discount given on food : ")
                            food_stock= input("Enter Available food stock: ")

                            flag =update_food_item("food_item.json",food_ID,food_name,food_quantity,food_price,food_discount,food_stock)
                            if flag:
                                print("Food Item Updated")
                            else:
                                print("food item did not get updated!")

                        # Delete Module
                        if admin_choice == 4:
                            food_ID = int(input("Enter food ID : "))
                            flag = remove_food("food_item.json",food_ID)
                            if flag:
                                print("Food item Deleted")
                            else:
                                print("food item did not get deleted!")
                        if admin_choice == 5:
                           Foodcounter.start()
                else:
                    print("Login Unsuccessful")
            if login_choice == 2:
                email_id = input("Enter your email ID : ")
                password = input("Enter your password : ")
                flag = login("user.json",email_id,password)
                if flag:
                    print("Login Successful")
                    while True:
                        admin_choice = int(input("Enter \n1.Place New Order \n2.Order History \n3.Update Profile\n4.Continue to main Menu : \n"))
                        # Create Module
                        if admin_choice == 1:
                            lst=[]
                            data = view_food_item("food_item.json")
                            count=0
                            while True :
                             for i in data:
                                  count+=1
                                  print("Please Enter" ,count,"to Selected this item",i)
                           
                             try:
                              _selected_first_food_item=int(input("Enter first Food item : "))
                              _selected_second_food_item=int(input("Enter second Food item : "))
                             except ValueError:
                               print("Please enter valid choice!")
                               continue
                             details1={"food_ID":data[_selected_first_food_item-1]["food_ID"],
                                      "food_name":data[_selected_first_food_item-1]["food_name"],
                                     "food_quantity":data[_selected_first_food_item-1]["food_quantity"],
                                     "food_price":data[_selected_first_food_item-1]["food_price"],
                                     "food_discount":data[_selected_first_food_item-1]["food_discount"],
                                     "food_stock":data[_selected_first_food_item-1]["food_stock"],
                                    }
                             details2={"food_ID":data[_selected_second_food_item-1]["food_ID"],
                                      "food_name":data[_selected_second_food_item-1]["food_name"],
                                     "food_quantity":data[_selected_second_food_item-1]["food_quantity"],
                                     "food_price":data[_selected_second_food_item-1]["food_price"],
                                     "food_discount":data[_selected_second_food_item-1]["food_discount"],
                                     "food_stock":data[_selected_second_food_item-1]["food_stock"],
                                    }
                             lst.append(details1)
                             lst.append(details2)
                             print("selected item")
                             for q in lst:
                                print(q)
                             print("Please enter 1 to exit this loop  or press 2 continue")  
                             num1=int(input("Enter your choice : ")) 
                             if num1==1:
                                break
                             if num1==2:
                                continue
                             else:
                                continue


                            for  l in lst:
                                add_new_food_item("selected food item.json",l["food_ID"],l["food_name"],l["food_quantity"],l["food_price"],l["food_discount"],l["food_stock"])
                            # food_ID = random.randint(10000,20000)
                            # food_name = input("Enter Food Name : ")
                            # food_quantity  = input("Enter food quantity (it should be 100ml, 250gm, 4pieces) : ")
                            # food_price  = input("Enter food price : ")
                            # food_discount= input("Enter Discount given on food : ")
                            # food_stock= input("Enter Available food stock: ")

                            # if food_ID and food_name and food_quantity and food_price and food_discount and food_stock :
                            #     flag = add_new_food_item("food_item.json",food_ID,food_name,food_quantity,food_price,food_discount,food_stock)
                            #     if flag:
                            #         print("food Item Addred Sucessfully is added successfully")
                            #     else:
                            #         print("food item did not get added")
                        # View food item
                        if admin_choice == 2:
                            data = view_food_item("ordered_histroy_item.json")
                            for i in data:
                                print(i)

                        # Update Module
                        if admin_choice == 3:
                            name = input("Enter your name : ")                
                            mobile = input("Enter your mobile : ")
                            email = input("Enter your email : ")  
                            address=input("Enter your address : ")               
                            password = input("Enter your password : ") 
                            name_re = re.findall(r'^[A-Za-z]{2,15}\s[A-Za-z]{2,15}$', name)
                            mobile_re = re.findall(r'^[1-9]{1}[0-9]{9}$' , mobile)
                            email_re = re.findall("^[A-z][a-zA-Z0-9._]+[@][a-z]+[.][a-z]+$",email)
                            address_re=re.findall(r'^[A-Za-z]{2,15}\s[A-Za-z]{2,15}$', address)
                            password_re = re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$" , password)

                            if name_re and mobile_re and email_re and password_re and address_re:
                               flag = register("User.json",name,mobile,email,address,password)
                    
                               if flag:
                                  print("Successfully Updated!")
                               else:
                                   print("Updation Unsuccessful")
                            else:
                              if not name_re:
                                 print("Entered name format is incorrect")
                                 continue
                              if not mobile_re:
                                 print("Entered mobile format is incorrect")
                                 continue
                              if not email_re:
                                  print("Entered email format is incorrect")
                                  continue
                              if not address_re:
                                  print("Entered address format is incorrect")
                                  continue
                              if not password_re:
                                 print("Entered passward format is incorrect")
                                 continue

                                                
                        if admin_choice == 4:
                           Foodcounter.start()
                else:
                    print("Login Unsuccessful")
    if register_choice == 3:
        print("***Bye****")
        exit()
if __name__ == "__main__":
    obj_Foodcounter=Foodcounter()
    Foodcounter.start()