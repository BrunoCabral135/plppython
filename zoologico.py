
from abc import ABC, abstractmethod

# 1. Classe abstrata Animal
class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def falar(self):
        pass

    @abstractmethod
    def mover(self):
        pass


# 2. Classes com herança simples

class Cachorro(Animal):
    def falar(self):
        print(f"{self.nome}: Au au")

    def mover(self):
        print(f"{self.nome} corre")


class Gato(Animal):
    def falar(self):
        print(f"{self.nome}: Miau")

    def mover(self):
        print(f"{self.nome} pula")


class Vaca(Animal):
    def falar(self):
        print(f"{self.nome}: Muuu")

    def mover(self):
        print(f"{self.nome} caminha")


# 3. Classes para herança múltipla

class Voador:
    def voar(self):
        print(f"{self.nome} voa")


class Nadador:
    def nadar(self):
        print(f"{self.nome} nada")


class Pato(Animal, Voador, Nadador):
    def falar(self):
        print(f"{self.nome}: Quack")

    def mover(self):
        print(f"{self.nome} anda, ", end="")
        print(f"{self.nome} voa e ", end="")
        print(f"{self.nome} nada")


# 4. Desafio: Jacaré que anda e nada

class Jacare(Animal, Nadador):
    def falar(self):
        print(f"{self.nome}: Grrr")

    def mover(self):
        print(f"{self.nome} anda e nada")


# 5. Funções polimórficas

def fazer_som(animal):
    animal.falar()


def fazer_movimento(animal):
    animal.mover()


# 6. Testando o sistema

rex = Cachorro("Rex")
mimi = Gato("Mimi")
mimosa = Vaca("Mimosa")
donald = Pato("Donald")
jacare = Jacare("Jacare")

animais = [rex, mimi, mimosa, donald, jacare]

for animal in animais:
    fazer_som(animal)
    fazer_movimento(animal)
    print()
