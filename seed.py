import utils
import urls as URLS
from pokedex import Pokedex
import sys

def seed_pokemon_images():
    for pkm_number in range(1,889):
        URL_POKEMON = URLS.POKEDEX_URL_INICIAL + str(pkm_number)
        html_pokemon = utils.get_page_text_by_url(URL_POKEMON)
        Pokedex.baixar_imagem_pokemon_via_html(html_pokemon)
        print("Foto do pokemon n*: " + str(pkm_number)+ " baixada com sucesso.")

def list_all_seeds():
    print ("python3 seed.py seed_pokemon_images -> download all images of pokemon avaliable.")

if __name__ == '__main__':
    try:
        globals()[sys.argv[1]]()
    except KeyError as keyError:
        print("Task: '" + sys.argv[1] + "' not exist")
        print("Use 'python3 seed.py list_all_seeds' to see all tasks.")
    except IndexError as e:
        print("You need to pass a task name: 'python3 seed.py task_name'")
        print("Use 'python3 seed.py list_all_seeds' to see all tasks.")
    except Exception as e:
        print(e)