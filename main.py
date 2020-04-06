# -*- coding: utf-8 -*-

import utils
import urls as URLS
from pokedex import Pokedex
from pokemon import Pokemon
import db

nome_do_pokemon = Pokedex.pegar_nome_pokemon_do_usuario()

pokemon = db.pegar_pokemon(nome_do_pokemon)
if not pokemon:
    pokemon = Pokemon(nome_do_pokemon)
    db.registrar_pokemon(pokemon)
else: 
    pokemon = Pokemon(nome_do_pokemon, pokemon)

pokemon.print_pokemon_info()


# atributos = Pokedex.pegar_atributos_pokemon_via_html(html_pokemon)

# utils.validar_valor(atributos,"Erro ao pegar Atributos do Pokemon.")

# pokemon.set_status(atributos)

# mega_evol = Pokedex.pegar_mega_evolucao_via_html(URL_POKEMON,html_pokemon)

# utils.validar_valor(mega_evol,"Erro ao pegar mega evoluções do Pokemon.")

# pokemon.set_megaevolucao(mega_evol)



#TO:DO
#Fazer Fraquezas

#TO:DO
#interface Gráfica X
#Colocar informações adquiridas numa interface para o usuário

#TO:DO X
#Armazenar as informações coletadas em um banco de dados 
#Primeiro consultar o banco de dados antes de ir no site

#TO:DO
#Validar se Imagem já existe para nao baixar novamente

#TO:DO
#Fazer um funcionamento em modo continuo até o usuário decidir parar 

