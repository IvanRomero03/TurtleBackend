from .Base import DescensoRecursivoBase
from .Movimientos import movimiento
from .Pluma import pluma
from .Util import numero, palabra, separador

# <com> ::= <mov> | <plum>
def comando(base: DescensoRecursivoBase) -> tuple[bool, DescensoRecursivoBase]:
    base1 = base.copy()
    res, temp = movimiento(base)
    if res:
        return res, temp
    res, temp = pluma(base1)
    temp.getToken()
    if res:
        return res, temp
    return False, base

# <inner> ::= <sep>?(<com> <sep>) <inner>? | <sep>?(<com> <sep>)*
def inner(base: DescensoRecursivoBase) -> tuple[bool, DescensoRecursivoBase]:
    res, temp = separador(base)
    if res:
        res, temp = comando(base)
        if res:
            base = temp
            base.i -= 1
            res, temp = separador(base)
            if res:
                res, temp = inner(base)
                if res:
                    return res, temp
                else:
                    return True, base
            else:
                return True, base
    else:
        base.i -= 1
        res, temp = comando(base)
        if res:
            base = temp
            base.i -= 1
            res, temp = separador(base)
            if res:
                res, temp = inner(base)
                if res:
                    return res, temp
                else:
                    return True, base
            else:
                base.i -= 1
                if base.getToken() == "]":
                    return True, base
                return True, base
    return False, base

# <rep> ::= “rp numero [” <sep>?(<com> <sep>)* “]”
def repetir(base: DescensoRecursivoBase) -> tuple[bool, DescensoRecursivoBase]:
    token = base.getToken()
    if token == "r":
        token = base.getToken()
        if token == "p":
            token = base.getToken()
            if token == " ":
                res, temp = numero(base)
                if res:
                    base = temp
                    token = base.getToken()
                    if token == "[":
                        res, temp = inner(base)
                        if res:
                            base = temp 
                            base.i -= 1
                            token = base.getToken()
                            if token == "]" or None:
                                return True, base
    return False, base

# <fn> ::= “fn “ <pal> “\n”
# ((<com> | <rep>) <sep>)+
# “end”

def funcion(base: DescensoRecursivoBase) -> bool:
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

# Valid input:
# por el momento no se aceptarán funciones
# <valid_input> ::= (<com> | <rep>) | ((<com> | <rep>) <sep>)* <valid_input>
def valid_input(base: DescensoRecursivoBase) -> tuple[bool, DescensoRecursivoBase]:
    def valid_rec(base1: DescensoRecursivoBase):
        cop = base1.copy()
        token = cop.getToken()
        print(token)
        if token == "" or token == None:
            return True, base1
        base2 = base1.copy()
        res, temp = comando(base1)
        if res:
            base1 = temp
            return valid_rec(base1)
        res, temp = repetir(base2)
        if res:
            base2 = temp
            return valid_rec(base2)
        return False, base1
    return valid_rec(base)


if __name__ == "__main__":
    # test
    # input = "go 10"
    input = "go 10 rp 10 [go 10 gd 90]"
    base = DescensoRecursivoBase(input)
    print(valid_input(base))


