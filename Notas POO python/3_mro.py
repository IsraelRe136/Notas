class A:
    def hablar(self):
        print("hola desde A")

class B(A):
    def hablar(self):
        print("hola desde B")

class C(A):
    def hablar(self):
        print("hola desde C")

class D(B,C):
    pass
    # def hablar(self):
    #     print("hola desde D")

d = D()

d.hablar()
# B.hablar(d)
print(D.mro())