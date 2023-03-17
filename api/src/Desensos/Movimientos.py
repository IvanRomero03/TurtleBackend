from Desensos.Base import DescensoRecursivoBase
from Desensos.Util import numero

# <go> ::= "go " <numero>
def avanzar(base: DescensoRecursivoBase) -> bool:
    token = base.getToken()
    if token == "g":
        token = base.getToken()
        if token == "o":
            token = base.getToken()
            if token == " ":
                return numero(base)
    return False

# <gi> ::= “gi ” <numero>
def girarIzquierda(base: DescensoRecursivoBase) -> bool:
    token = base.getToken()
    if token == "g":
        token = base.getToken()
        if token == "i":
            token = base.getToken()
            if token == " ":
                return numero(base)
    return False

# <gd> ::= “gd ” <numero>
def girarDerecha(base: DescensoRecursivoBase) -> bool:
    token = base.getToken()
    if token == "g":
        token = base.getToken()
        if token == "d":
            token = base.getToken()
            if token == " ":
                return numero(base)
    return False

# <dir> ::= “dir ” <numero>
def direccion(base: DescensoRecursivoBase) -> bool:
    token = base.getToken()
    if token == "d":
        token = base.getToken()
        if token == "i":
            token = base.getToken()
            if token == "r":
                token = base.getToken()
                if token == " ":
                    return numero(base)
    return False

# <mov> ::= <go> | <gi> | <gd> | <dir>
def movimiento(base: DescensoRecursivoBase) -> bool:
    if avanzar(base):
        return True
    elif girarIzquierda(base):
        return True
    elif girarDerecha(base):
        return True
    elif direccion(base):
        return True
    else:
        return False
    
# <movs> ::= <mov> | <mov> <sep> <movs>
def movimientos(base: DescensoRecursivoBase) -> bool:
    def movimientos_rec() -> bool:
        if movimiento(base):
            movimientos_rec()
            return True
        else:
            return False
    return movimientos_rec()

