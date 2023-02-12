from cmd import Cmd
from boss import searchWhoosh, searchInverted
from myDisplay import display

class Cli(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = "> "
        self.run = self.cmdloop

    def do_whoosh(self, _):
        chords = input("Accordi: ")
        tokens = input("Testo: ")
        artist = input("Artista: ")
        searchWhoosh(artist, tokens, chords)
    
    def help_whoosh(self):
        print("Prepara una ricerca sull'indice di whoosh")

    def help_inverted(self):
        print("Effettua una ricerca su una parola tramite l'inverted index")

    def do_inverted(self, args):
        searchInverted(args)

Cli().run()