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
    
    def do_inverted(self, args):
        searchInverted(args)

Cli().run()