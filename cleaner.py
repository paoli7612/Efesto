import os, re

class Cleaner:
    def __init__(self, IN_FOLDER, OUT_FILE):
        self.w = open(OUT_FILE, 'w',encoding='utf8')
        for filename in os.listdir(IN_FOLDER):
            with open(os.path.join(IN_FOLDER, filename), 'r',encoding='utf8') as f:
                self.chord = set()
                self.calculate(f, filename)
    
    def calculate(self, f, filename):
        name = ".".join(filename.split('.')[:2])
        self.w.write(name+" { } ")
        for row in f:
            row = row.strip()
            
            # salta riga vuota
            if not row:
                continue

            # salta la riga di accordi/tablature/Intro...
                # conservando gli accordi nel set self.chord
            if self.isWrong(row):
                continue

            # sostituisco gli apostrofi con degli spazi (evitare [ all'alba -> allalba ])
            row = row.replace("'", " ")

            # rimuovi spazi e punteggiatura
            row = re.sub(r'[^\w\s]','', row)

            # rendi tutto minuscolo
            row = row.lower()
            self.w.write(row + " ")
        self.w.write(" { } ")
        for c in self.chord:
            self.w.write(c + " ")
        self.w.write("\n")

    def isWrong(self, row):
        for w in ['Intro', '---']:
            if w in row:
                return True

        chords = set()
        for w in ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI']:
            if w in row:
                ww = row.split()
                for c in ww:
                    chords.add(c)
        if chords:
            for c in chords:
                self.chord.add(c)
            return True
        return False


if __name__ == '__main__':
    c = Cleaner('canzoni', 'testi.txt')