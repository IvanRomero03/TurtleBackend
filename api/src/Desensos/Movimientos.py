from .Base import DescensoRecursivoBase
from .Util import numero, separador

# <go> ::= "go " <numero>
def avanzar(base: DescensoRecursivoBase) -> tuple[bool, DescensoRecursivoBase]:
    token = base.getToken()
    if token == "g":
        token = base.getToken()
        if token == "o":
            token = base.getToken()
            if token == " ":
                return numero(base)
    return False, base

# <gi> ::= “gi ” <numero>
def girarIzquierda(base: DescensoRecursivoBase) -> tuple[bool, DescensoRecursivoBase]:
    token = base.getToken()
    if token == "g":
        token = base.getToken()
        if token == "i":
            token = base.getToken()
            if token == " ":
                return numero(base)
    return False, base

# <gd> ::= “gd ” <numero>
def girarDerecha(base: DescensoRecursivoBase) -> tuple[bool, DescensoRecursivoBase]:
    token = base.getToken()
    if token == "g":
        token = base.getToken()
        if token == "d":
            token = base.getToken()
            if token == " ":
                return numero(base)
    return False, base

# <dir> ::= “dir ” <numero>
def direccion(base: DescensoRecursivoBase) -> tuple[bool, DescensoRecursivoBase]:
    token = base.getToken()
    if token == "d":
        token = base.getToken()
        if token == "i":
            token = base.getToken()
            if token == "r":
                token = base.getToken()
                if token == " ":
                    return numero(base)
    return False, base

# <mov> ::= <go> | <gi> | <gd> | <dir>
def movimiento(base: DescensoRecursivoBase) -> tuple[bool, DescensoRecursivoBase]:
    copy_base = base.copy()
    res, temp = avanzar(copy_base)
    if res:
        return res, temp
    copy_base = base.copy()
    res, temp = girarIzquierda(copy_base)
    if res:
        return res, temp
    copy_base = base.copy()
    res, temp = girarDerecha(copy_base)
    if res:
        return res, temp
    res, temp = direccion(base)
    if res:
        return res, temp
    return False, base

# FIXME: <sep>? esto no jala creo q ya
# <movs> ::= <mov> | <mov> <sep> <movs> 
def movimientos(base: DescensoRecursivoBase) -> tuple[bool, DescensoRecursivoBase]:
    def mov_rec(base: DescensoRecursivoBase) -> tuple[bool, DescensoRecursivoBase]:
        res, temp = movimiento(base)
        if res:
            res, temp = separador(temp)
            if res:
                return mov_rec(temp)
            return True, temp
        return False, base
    
    return mov_rec(base)