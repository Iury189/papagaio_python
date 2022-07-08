import naruto, seiya, goku, yusuke, random

class Papagaio(naruto.Naruto, goku.Goku, seiya.Seiya, yusuke.Yusuke):
    def repetir(self):
        random.choice((self.falaNaruto, self.falaGoku, self.falaSeiya, self.falaYusuke))()
