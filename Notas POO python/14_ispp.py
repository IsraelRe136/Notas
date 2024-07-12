# from abc import ABC, abstractclassmethod

# class trabajor (ABC):
    
#     @abstractclassmethod
#     def comer(self):
#         pass
#     @abstractclassmethod
#     def trabajar(self):
#         pass
#     @abstractclassmethod
#     def dormir(self):
#         pass  

# class humano(trabajor):
#     def comer(self):
#         print("comer")

#     def trabajar(self):
#         print("trabajar")

#     def dormir(self):
#         print("dormir")

# class Robot(trabajor):

#     def trabajar(self):
#         print("trabajar")


# robot=Robot()

from abc import ABC, abstractclassmethod

class trabajor (ABC):
    
    @abstractclassmethod
    def trabajar(self):
        pass

class comedor (ABC):
    @abstractclassmethod
    def comer(self):
        pass
class dormilon (ABC):
    @abstractclassmethod
    def dormir(self):
        pass  

class humano(trabajor,comedor,dormilon):
    def comer(self):
        print("comer")

    def trabajar(self):
        print("trabajar")

    def dormir(self):
        print("dormir")

class Robot(trabajor):

    def trabajar(self):
        print("trabajar")


robot=Robot()