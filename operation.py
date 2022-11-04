from asyncio.windows_events import NULL
from contextlib import nullcontext
import json

def register(filename,name,mobile,email,address,password):
    details={
            "Full Name":name,
            "Mobile Number":mobile,
            "Email":email,
            "Address":address,
            "Password":password,
        }
        
    file = open(filename,"w+")
    try:
        data=json.load(file)
        if details not in data:
            data.append(details)
            file.seek(0)
            file.truncate()
            json.dump(data,file)
            file.close()
            return True
    except json.decoder.JSONDecodeError:
        lst=[]
        lst.append(details)
        json.dump(lst,file)
        file.close()
        return True
    finally:
        file.close()
    return False

def login(filename,email_id,password):
    file = open(filename,"r+")
    try:
        data = json.load(file)
        for i in data:
            if i["Email"] == email_id and i["Password"] == password:
                return True
            else:
                return False
    except json.decoder.JSONDecodeError:
        return False
    finally:
        file.close()
    return False

def add_new_food_item(filename,food_ID,food_name,food_quantity,food_price,food_discount,food_stock):
    details={
            "food_ID":food_ID,
            "food_name":food_name,
            "food_quantity":food_quantity,
            "food_price":food_price,
            "food_discount":food_discount,
            "food_stock":food_stock,
        }
    #details=Food(food_ID,food_name,food_quantity,food_price,food_discount,food_stock)
    file = open(filename,"r+")
    try:
        data=json.load(file)
        if details not in data:
            data.append(details)
            file.seek(0)
            file.truncate()
            json.dump(data,file)
            file.close()
            return True
    except json.decoder.JSONDecodeError:
        lst=[]
        lst.append(details)
        json.dump(lst,file)
        file.close()
        return True
    finally:
        file.close()
    return False

def update_food_item(filename,food_ID,food_name,food_quantity,food_price,food_discount,food_stock):
    file = open(filename,"r+")
    data = json.load(file)
    for i in range(len(data)):
        if data[i]["food_ID"] == food_ID:
            data[i]["food_name"] = food_name
            data[i]["food_quantity"] = food_quantity
            data[i]["food_price"] = food_price
            data[i]["food_discount"] = food_discount
            data[i]["food_stock"] = food_stock
            file.seek(0)
            file.truncate()
            json.dump(data,file)
            file.close()
            return True
    return False

def view_food_item(filename):
    file = open(filename,"r+")
    data = json.load(file)
    if data==NULL:
        return []
    else:
     return data


def remove_food(filename,food_ID):
    file = open(filename,"r+")
    data = json.load(file)
    for i in range(len(data)):
        if data[i]["food_ID"] == food_ID:
            data.pop(i)
            file.seek(0)
            file.truncate()
            json.dump(data,file)
            file.close()
            return True
    return False