class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        ataque = ""
        if self.tipo == "mago":
            ataque = "usou magia"
        elif self.tipo == "guerreiro":
            ataque = "usou espada"
        elif self.tipo == "monge":
            ataque = "usou artes marciais"
        elif self.tipo == "ninja":
            ataque = "usou shuriken"
        else:
            print("Tipo de herói inválido")
            return
        print(f"o {self.tipo} atacou usando {ataque}")

# Exemplo de uso
mago = Heroi("Merlin", 300, "mago")
mago.atacar()

guerreiro = Heroi("Aragorn", 30, "guerreiro")
guerreiro.atacar()

monge = Heroi("Kwai Lun", 250, "monge")
monge.atacar()

ninja = Heroi("Hanzo", 200, "ninja")
ninja.atacar()