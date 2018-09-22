class mane(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Give me a string:")

    def printString(self):
        print(self.s.upper())


x = mane()
print(x)

x.getString()
x.printString()



