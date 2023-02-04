from .toolsMenu import toolsMenu

def menu():
    print('\nWelcome to Helios!\n'\
   'I am here to help you automate the boring task.\n')

    print('Menu\n'\
    '1. Tools\n')

    choice =int(input('> '))

    if (choice==1):
        toolsMenu()