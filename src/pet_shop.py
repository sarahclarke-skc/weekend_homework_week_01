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

# write in a customer and get their cash back

def get_customer_cash(customer):
    return customer["cash"]

# write in customer and cash to remove
# return new sum

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    pets_list = len(customer["pets"])
    return pets_list
# pass customer and pet
# return new pet count
def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:
        return True
    else:
        return False
