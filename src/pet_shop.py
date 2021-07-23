# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(petshop):
    return petshop["name"]

def get_total_cash(petshop):
    return petshop["admin"]["total_cash"]

def add_or_remove_cash(petshop, number_to_add):
    petshop["admin"]["total_cash"] += number_to_add
    return petshop["admin"]["total_cash"]

def get_pets_sold(petshop):
    return petshop["admin"]["pets_sold"]
