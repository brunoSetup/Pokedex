# -*- coding: utf-8 -*-

import utils
import urls as URLS
from pokedex import Pokedex
from pokemon import Pokemon

nome_do_pokemon = Pokedex.pegar_nome_pokemon_do_usuario()

pokemon = Pokemon(nome_do_pokemon)

URL_POKEMON = URLS.POKEDEX_URL_INICIAL + nome_do_pokemon

html_pokemon = utils.get_page_text_by_url(URL_POKEMON)

utils.validar_valor(html_pokemon, "Erro ao pegar HMTL do pokemon.")

tipos_do_pokemon = Pokedex.pegar_tipos_pokemon_via_html(html_pokemon)

utils.validar_valor(tipos_do_pokemon, "Erro ao pegar Tipo(s) do Pokemon.")

pokemon.set_tipos(tipos_do_pokemon)

evolucoes_do_pokemon = Pokedex.pegar_evolucoes_pokemon_via_html(html_pokemon)

utils.validar_valor(evolucoes_do_pokemon, "Erro ao pegar Evoluções do Pokemon.")

pokemon.set_evolucoes(evolucoes_do_pokemon)

path_imagem = Pokedex.baixar_imagem_pokemon_via_html(html_pokemon)

utils.validar_valor(path_imagem,"Erro ao pegar Imagem do Pokemon.")

pokemon.set_imagem(path_imagem)

# atributos = Pokedex.pegar_atributos_pokemon_via_html(html_pokemon)

# utils.validar_valor(atributos,"Erro ao pegar Atributos do Pokemon.")

# pokemon.set_status(atributos)

mega_evol = Pokedex.pegar_mega_evolucao_via_html(URL_POKEMON,html_pokemon)

utils.validar_valor(mega_evol,"Erro ao pegar mega evoluções do Pokemon.")

pokemon.set_megaevolucao(mega_evol)

pokemon.print_pokemon_info()



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

