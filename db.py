# -*- coding: utf-8 -*-

import pymongo
from copy import deepcopy

# client = pymongo.MongoClient("mongodb+srv://<user>:<password>@cluster0-fcmso.mongodb.net/test?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb+srv://pedroblandim:ZRzxCYvatpqV7pvl@cluster0-fcmso.mongodb.net/test?retryWrites=true&w=majority")
db = client.Pokedex
collection = db.Pokemon
    
def registrar_pokemon(pokemon):
    dicionario_do_pokemon = deepcopy(pokemon.__dict__)
    dicionario_do_pokemon["_id"] = pokemon.get_nome()
    return collection.insert_one(dicionario_do_pokemon).inserted_id

def pegar_pokemon(nome):
    return collection.find_one({"_nome":nome})