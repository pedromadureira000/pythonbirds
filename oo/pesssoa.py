class Pessoa:
    def __init__(self, *filhos, nome=None, idade=0):
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f"ola {id(self)}"

if __name__ == '__main__':
    pedro = Pessoa(nome="Pedro")
    henrique = Pessoa(pedro, nome="Henrique")
    print(henrique.filhos)
    for filhos in henrique.filhos:
        print(filhos.nome)

    print("Pessoa.cumprimentar(pedro)", Pessoa.cumprimentar(pedro))
    print("id(pedro)", id(pedro))
    print("pedro.cumprimentar()", pedro.cumprimentar())
    print("pedro.nome", pedro.nome)
    print("pedro.cumprimentar", pedro.cumprimentar)
    henrique.sobrenome = "Pedro"
    print(henrique.__dict__)
    print(pedro.__dict__)
    del henrique.sobrenome      #vc pode deletar atributos dinamicamente, msm sendo um atributo definido em __init__
    print(henrique.__dict__)    #isso não é uma boa pratica
