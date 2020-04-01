# -*- coding: utf-8 -*-
import requests
import sys

import os

def get_page_text_by_url(url):
    try:
        requisicao = requests.get(url)
        if(requisicao.status_code == 404):
            print('Pokemon não encontrado.')
            return None
        else:
            return requisicao.text

    except requests.exceptions.Timeout:
        print("Site demorou muito para responder.")
        return None

    except requests.exceptions.TooManyRedirects:
        print('URL incorreta: ', url)
        return None

    except Exception as e:
        print("Um erro ocorreu: " + str(e))
        return None

def create_folder(name):
    if not os.path.exists("./"+name):
        os.makedirs("./"+name)
def remover_palavra(string, palavra):
    return string.replace(palavra,"")

def traduzir_tipo(tipo_ingles):
    TIPOS = {
        "Fire"      :   "Fogo",
        "Bug"       :   "Inseto",
        "Dark"      :   "Noturno",
        "Psychic"   :   "Psíquico",
        "Water"     :   "Agua",
        "Dragon"    :   "Dragão",
        "Electric"  :   "Elétrico",
        "Fairy"     :   "Fada",
        "Fighing"   :   "Lutador",
        "Flying"    :   "Voador",
        "Ghost"     :   "Fantasma",
        "Grass"     :   "Grama",
        "Ground"    :   "Solo",
        "Ice"       :   "Gelo",
        "Normal"    :   "Normal",
        "Poison"    :   "Venenoso",
        "Rock"      :   "Pedra",
        "Steel"     :   "Metal",
    }
    try:
        tipo_portugues = TIPOS[tipo_ingles] 
        return tipo_portugues
    except KeyError:
        return tipo_ingles

def validar_valor(valor, msg):
    if(valor is None):
        print(msg)
        sys.exit()

