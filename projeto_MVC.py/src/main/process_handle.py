from .constructor.introduction_process import introdution_process
from .constructor.people_finder_contructor import people_finder_constructor
from .constructor.people_register_constructor import people_register_constructor

def start() -> None:
    while True:
        command = introdution_process()

        if command == '1': people_register_constructor()
        elif command == '2': people_finder_constructor()
        elif command == '5': exit()
        else: print('\n Comando não encontrado!! \n\n')