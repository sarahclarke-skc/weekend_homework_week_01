# WRITE YOUR FUNCTIONS HERE
from os import remove


def get_pet_shop_name(petshop):
    return petshop["name"]

def get_total_cash(petshop):
    return petshop["admin"]["total_cash"]

def add_or_remove_cash(petshop, number_to_add):
    petshop["admin"]["total_cash"] += number_to_add
    return petshop["admin"]["total_cash"]

def get_pets_sold(petshop):
    return petshop["admin"]["pets_sold"]

def increase_pets_sold(petshop, num):
    petshop["admin"]["pets_sold"] =+ num
    return get_pets_sold(petshop)

def get_stock_count(petshop):
    return len(petshop["pets"])

def get_pets_by_breed(petshop, breed):
    breed_count = []
    for animal in petshop["pets"]:
        if animal ["breed"] == breed:
            breed_count.append(animal)
    return breed_count

def find_pet_by_name(petshop, petname):
    for animal in petshop["pets"]:
        if animal["name"] == petname:
            return animal 

def remove_pet_by_name(petshop, petname):
    for_removal = find_pet_by_name(petshop, petname)
    petshop["pets"].remove(for_removal)

def add_pet_to_stock(petshop, newpet):
    petshop["pets"].append({
        "name": "Fenya",
        "pet_type": "cat",
        "breed": "Tabby",
        "price": 10000,
    })
    get_stock_count(petshop)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    pets_list = len(customer["pets"])
    return pets_list

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:
        return True
    else:
        return False

# pass the petshop, the pet, and the customer
# update the dictionaries to show that a pet has 
# been sold to a customer

# does the petshop have the pet?
# if yes, check the customer
# if no, no sale
# can the customer afford the pet?
# if yes, update the customer(cash-, pets+)
#         update the petshop(cash +, pets -)
# if no, no sale

# remember the functions already created


# def sell_pet_to_customer(petshop, pet, customer):
#     for item in petshop:
#         if find_pet_by_name(petshop, pet) == pet:
#             if customer_can_afford_pet(customer, pet):
#                 add_pet_to_customer(customer, pet)
#                 remove_pet_by_name(petshop, pet)
#                 increase_pets_sold(petshop, 1)
#                 get_stock_count(petshop)
#                 get_total_cash(petshop)
#                 get_customer_cash(customer)
#                 get_customer_pet_count(customer)
#                 get_pets_sold(petshop)


# get_customer_pet_count
# get_pets_sold
# get_customer_cash
# get_total_cash