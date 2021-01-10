# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop['name']


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

        
def add_or_remove_cash(pet_shop, amount):
    current_total_cash = pet_shop["admin"]["total_cash"] 
    pet_shop["admin"]["total_cash"] = current_total_cash + amount


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, number):
    current_pet_sold = pet_shop["admin"]["pets_sold"]
    pet_shop["admin"]["pets_sold"] = current_pet_sold + number 

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, pet_breed):
    pet_type = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == pet_breed:
            pet_type.append(pet_breed)
    return pet_type


def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet


def remove_pet_by_name(pet_shop, pet_name):
    index = 0
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            del pet_shop["pets"][index]
        index = index + 1


def add_pet_to_stock(pet_shop, pet):
    pet_shop["pets"].append(pet)


def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer, amount):
    current_cash_amount = customer["cash"]
    customer["cash"] = current_cash_amount - amount


def get_customer_pet_count(customer):
    return len(customer["pets"])

    
def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)