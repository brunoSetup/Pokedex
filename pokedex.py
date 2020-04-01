from bs4 import BeautifulSoup
import utils
# from translate import Translator
import utils as nome_utils
import requests 
import os

class Pokedex(object):
 
    @classmethod
    def pegar_nome_pokemon_do_usuario(self):
        nome = input("Digite o nome do pokemon: ")
        return nome 

    @classmethod
    def pegar_tipos_pokemon_via_html(self,html):
        try:
            soup = BeautifulSoup(html, 'html.parser')
            div_de_tipo = soup.findAll("div", {"class": "dtm-type"})[0].findAll("a")
            tipos = []
            # try:
            #     translator= Translator(to_lang="pt")
            #     tipo = translator.translate(tipo_ingles)
            # except Exception:
            #     print("Tipo em Ingles mantido...")
            #     tipo = tipo_ingles
            for tipo_ingles in div_de_tipo:
                tipo_temp = nome_utils.remover_palavra(tipo_ingles.text,"Type").strip()
                tipos.append(nome_utils.traduzir_tipo(tipo_temp))

            return tipos
        except Exception as e:
            print("Erro ocorreu: " + str(e))
            return None

    @classmethod
    def pegar_evolucoes_pokemon_via_html(self,html):
        try:
            evolucoes = []
            soup = BeautifulSoup(html, 'html.parser')
            ul_de_evolucoes = soup.findAll("ul", {"class": "evolution-profile"})
            nome_primeiro = ul_de_evolucoes[0].findAll("li",{"class":"first"})[0].find("img")["alt"]
            evolucoes.append(nome_primeiro)
            if(ul_de_evolucoes[0].findAll("li",{"class":"middle"}) != []):
                nome_segundo = ul_de_evolucoes[0].findAll("li",{"class":"middle"})[0].find("img")["alt"]
                evolucoes.append(nome_segundo)
            if(ul_de_evolucoes[0].findAll("li",{"class":"last"}) != []):
                imagens_ultimo = ul_de_evolucoes[0].findAll("li",{"class":"last"})[0].findAll("img")
                nome_ultimo = ""
                if(len(imagens_ultimo) > 1 ):
                    for imagem in imagens_ultimo:
                        nome_ultimo += imagem["alt"] + " ou "
                    nome_ultimo = nome_ultimo[:-4]
                else:
                    nome_ultimo = imagens_ultimo[0]["alt"]
                evolucoes.append(nome_ultimo)
            return evolucoes

        except Exception as e:
            print("Erro ocorreu: " + str(e))
            return None


    @classmethod
    def baixar_imagem_pokemon_via_html(self,html):
        try:
            soup = BeautifulSoup(html, 'html.parser')
            imagem_tag = soup.findAll("div", {"class": "profile-images"})
            imagem_url = imagem_tag[0].findAll("img")[0]["src"]
            imagem_name = imagem_tag[0].findAll("img")[0]["alt"]
            r = requests.get(imagem_url, stream=True)
            utils.create_folder("pokemon_images")
            path = "./pokemon_images/" + imagem_name + ".png"
            has_imagem = os.path.isfile(path)    # True
            if not has_imagem:
                if r.status_code == 200:
                    with open(path, 'wb') as f:
                        for _bytes in r:
                            f.write(_bytes)
            return path
        except Exception as e:
            print("Erro ocorreu: " + str(e))
            return None


    @classmethod
    def pegar_atributos_pokemon_via_html(self,html):
        try:
            atributos = {}
            attr_order = ["","HP", "Ataque", "Defesa", "Ataque Especial", "Defesa Especial", "Velocidade"]
            soup = BeautifulSoup(html, 'html.parser')
            div_de_atributos = soup.findAll("div", {"class": "pokemon-stats-info"})[0]
            li_atributos = div_de_atributos.select('.pokemon-stats-info li:first-child')
            for atributo_index in range(1,len(li_atributos)):
                atributos[attr_order[atributo_index]] = str(int(li_atributos[atributo_index]["data-value"]) * 10) +"%" 
            return atributos
        except Exception as e:
            print("Erro ocorreu: " + str(e))
            return None
    
    @classmethod
    def pegar_mega_evolucao_via_html(self,URL_POKEMON, html):
        try:
            from selenium import webdriver
            import warnings
            warnings.filterwarnings('ignore')
            browser = webdriver.PhantomJS(executable_path='./phantomjs/bin/phantomjs')
            browser.get(URL_POKEMON)
            html = browser.page_source
            soup = BeautifulSoup(html, 'lxml')
            label_de_mega = soup.findAll("div", {"class": "custom-select-menu"})

            megaevolucao = ""
            if(label_de_mega != []):
                label_de_mega = label_de_mega[0].findAll("li")
                for me in label_de_mega[1:]:
                    megaevolucao+= me.text + " ou "
                megaevolucao = megaevolucao[:-4]
                return megaevolucao
            else:
                return megaevolucao
        except Exception as e:
            print("Erro ocorreu: " + str(e))
            return None