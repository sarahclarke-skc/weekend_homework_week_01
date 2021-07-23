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

    

