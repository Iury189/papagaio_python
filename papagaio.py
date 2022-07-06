import naruto, seiya, goku, random

class Papagaio(naruto.Naruto, goku.Goku, seiya.Seiya):
    def repetir(self):
        random.choice((self.falaNaruto, self.falaGoku, self.falaSeiya))()
