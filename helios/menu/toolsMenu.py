import helios.tools.urlshortner as urlshortner

def toolsMenu():
    print('\nTools:\n'\
    '1. URL shortner\n')

    choice =int(input('> '))

    if (choice == 1):
        urlshortner.run()