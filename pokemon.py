# -*- coding: utf-8 -*-

from PIL import Image

class Pokemon(object):
    def __init__(self, nome, tipos = []):
        self._nome = nome
        self._tipos = tipos
        self._evolucoes = []
        self._status = {}
        self._imagem = ""
        self._megaevolucao = None

    def get_nome(self):
        return self._nome
    
    def set_nome(self, nome):
        self._nome = nome

    def get_tipos(self):
        return self._tipos
    
    def set_tipos(self, tipos):
        self._tipos = tipos

    def get_evolucoes(self):
        return self._evolucoes
    
    def set_evolucoes(self, evolucoes):
        self._evolucoes = evolucoes

    def get_status(self):
        return self._status
    
    def set_status(self, status):
        self._status = status

    def get_imagem(self):
        return self._imagem
    
    def set_imagem(self, imagem):
        self._imagem = imagem

    def get_megaevolucao(self):
        return self._megaevolucao
    
    def set_megaevolucao(self, megaevolucao):
        self._megaevolucao = megaevolucao    

    def print_pokemon_info(self):
        print("\n")
        print("-"*80)
        print("Pokemon: " + self._nome.capitalize(), end="\n\n" )
        
        if(len(self._tipos) > 1):
            print("Tipos: ")
            for tipo in self._tipos:
                print("\t "+ tipo)
        else:
            print("Tipo: " + self._tipos[0] )
        
        print("\n")
        
        if(len(self._evolucoes) > 1):
            print("Linha Evolutiva: ",end="\n\n")
            for evolucao in self._evolucoes:
                print("\t "+ evolucao)
        else:
            print("Linha Evolutiva: " + self._evolucoes[0] )
        
        print("\n")
        print("Atributos: \n")
        for atributo in self._status:
            if(len(atributo) < 16):
                offset = 16-len(atributo)
                print("\t" + atributo+ offset*" "+ ":  " +self._status[atributo]) 

        print("\n")
        
        if(self._megaevolucao is not None):
            print("Mega Evoluções: \n")
            print(self._megaevolucao)
        
        print("\n")
        with Image.open(self._imagem) as img:
            img.show()
        
