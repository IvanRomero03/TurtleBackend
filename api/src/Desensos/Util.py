from Desensos.Base import DescensoRecursivoBase

# <digito> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
def digito(base: DescensoRecursivoBase) -> bool:
    token = base.getToken()
    if token in "0123456789":
        return True
    
# <numero> ::= <digito> | <numero> <digito>
def numero(base: DescensoRecursivoBase) -> bool:
    def numero_rec() -> bool:
        token = base.getToken()
        if digito(token):
            numero_rec()
            return True
        else:
            return False
    return numero_rec()

# <entero> ::= <numero> | "-" <numero>
def entero(base: DescensoRecursivoBase) -> bool:
    token = base.getToken()
    if token == "-":
        return numero(base.getToken())
    else:
        return numero(base.s)

# <let> ::= [a-zA-Z]
def letra(base: DescensoRecursivoBase) -> bool:
    token = base.getToken()
    if token in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return True
    
# <pal> ::= <let>+
def palabra(base: DescensoRecursivoBase) -> bool:
    def palabra_rec() -> bool:
        if letra(base):
            palabra_rec()
            return True
        else:
            return False
    return palabra_rec()

# <sep> ::= " " | "\n"
def separador(base: DescensoRecursivoBase) -> bool:
    token = base.getToken()
    if token == "\n":
        return True
    elif token == None:
        return True
    elif token == " ":
        return True
    else:
        return False
    



