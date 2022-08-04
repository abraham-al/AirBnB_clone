#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print("Name = {} , Id = {} , created at = {}, updated at ={}, numer = {}".format(my_model.name, my_model.id, my_model.created_at, my_model.updated_at, my_model.my_number))
print("________________________________________________________________________________________________")
print(my_model)
print("________________________________________________________________________________________________")
my_model.save()
print(my_model)
print("________________________________________________________________________________________________")
my_model_json = my_model.to_dict()
print(my_model_json)
print("________________________________________________________________________________________________")
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
    
my_model1 = BaseModel()
my_model1.name = "My First Model"
my_model1.my_number = 89
print(my_model1)
my_model1.save()
print(my_model1)
my_model_json1 = my_model1.to_dict()
print(my_model_json1)
print("JSON of my_model:")
for key in my_model_json1.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json1[key]), my_model_json1[key]))