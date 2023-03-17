from Desensos.Base import DescensoRecursivoBase
from Desensos.Movimientos import movimiento
from Desensos.Pluma import pluma
from Desensos.Util import numero, palabra, separador

# <com> ::= <mov> | <plum>
def comando(base: DescensoRecursivoBase) -> bool:
    if movimiento(base):
        return True
    elif pluma(base):
        return True
    else:
        return False

# <rep> ::= “rp [” <sep>?(<com> <sep>)* “]”
def repetir(base: DescensoRecursivoBase) -> bool:
    token = base.getToken()
    if token == "r":
        token = base.getToken()
        if token == "p":
            token = base.getToken()
            if token == " ":
                token = base.getToken()
                if token == "[":
                    if separador(base):
                        while comando(base):
                            token = base.getToken()
                            if separador(base):
                                token = base.getToken()
                                if token == "]":
                                    return True
                            elif token == "]":
                                return True
                    else:
                        while comando(base):
                            token = base.getToken()
                            if separador(base):
                                token = base.getToken()
                                if token == "]":
                                    return True
                            elif token == "]":
                                return True
    return False

# <fn> ::= “fn “ <pal> “\n”
# ((<com> | <rep>) <sep>)+
# “end”

def funcion(base = DescensoRecursivoBase) -> bool:
    token = base.getToken()
    if token == "f":
        token = base.getToken()
        if token == "n":
            token = base.getToken()
            if token == " ":
                if palabra(base):
                    token = base.getToken()
                    if token == "\n":
                        while comando(base) or repetir(base):
                            if separador(base):
                                token = base.getToken()
                        if token == "e":
                            token = base.getToken()
                            if token == "n":
                                token = base.getToken()
                                if token == "d":
                                    return True
    return False