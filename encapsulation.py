

class transportation :
    def travel(self):
        print('modes of traveling')

    # child class/subclass/derived class


class aeroplane (transportation ):
    def flying(self):
        print('aeroplane is flying')


class train(transportation):
    def moves(self):
        print('train is moving')


tr = transportation
a = aeroplane()
a.travel()

t = train()
t.moves()






