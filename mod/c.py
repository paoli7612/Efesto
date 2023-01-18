

class Boss:
    def __init__(self, fname):
        with open(fname + ".txt", "r") as f:
            self.text = f.read()
        self.preprocessing()

    def preprocessing(self):
        pass


if __name__ == '__main__':
    b = Boss('ww1')