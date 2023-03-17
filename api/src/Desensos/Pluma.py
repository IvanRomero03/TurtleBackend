from Desensos.Base import DescensoRecursivoBase

# <pa> ::= “pa”
def plumaArriba(base: DescensoRecursivoBase) -> bool:
    token = base.getToken()
    if token == "p":
        token = base.getToken()
        if token == "a":
            return True
    return False

# <pb> ::= “pb”
def plumaAbajo(base: DescensoRecursivoBase) -> bool:
    token = base.getToken()
    if token == "p":
        token = base.getToken()
        if token == "b":
            return True
    return False

# <lp> ::= “lp”
def limpiarPantalla(base: DescensoRecursivoBase) -> bool:
    token = base.getToken()
    if token == "l":
        token = base.getToken()
        if token == "p":
            return True
    return False

# <cp> ::= “cp”
def centrarPluma(base: DescensoRecursivoBase) -> bool:
    token = base.getToken()
    if token == "c":
        token = base.getToken()
        if token == "p":
            return True
    return False

# <color> ::= ["red" | "green" | "blue" | "yellow" | "black" | "white" | "purple" | "orange" | "brown" | "pink" | "gray" | "cyan"]
def color(base: DescensoRecursivoBase) -> bool:
    s = base.getToken()
    if s == "r":
        s += base.getToken()
        if s == "re":
            s += base.getToken()
            if s == "red":
                return True
    elif s == "g":
        s += base.getToken()
        if s == "gr":
            s += base.getToken()
            if s == "gre":
                s += base.getToken()
                if s == "gree":
                    s += base.getToken()
                    if s == "green":
                        return True
    elif s == "b":
        s += base.getToken()
        if s == "bl":
            s += base.getToken()
            if s == "blu":
                s += base.getToken()
                if s == "blue":
                    return True
            elif s == "bla":
                s += base.getToken()
                if s == "blac":
                    s += base.getToken()
                    if s == "black":
                        return True
        elif s == "br":
            s += base.getToken()
            if s == "bro":
                s += base.getToken()
                if s == "brow":
                    s += base.getToken()
                    if s == "brown":
                        return True
    elif s == "y":
        s += base.getToken()
        if s == "ye":
            s += base.getToken()
            if s == "yel":
                s += base.getToken()
                if s == "yell":
                    s += base.getToken()
                    if s == "yello":
                        s += base.getToken()
                        if s == "yellow":
                            return True
    elif s == "w":
        s += base.getToken()
        if s == "wh":
            s += base.getToken()
            if s == "whi":
                s += base.getToken()
                if s == "whit":
                    s += base.getToken()
                    if s == "white":
                        return True
    elif s == "p":
        s += base.getToken()
        if s == "pu":
            s += base.getToken()
            if s == "pur":
                s += base.getToken()
                if s == "purr":
                    s += base.getToken()
                    if s == "purpl":
                        s += base.getToken()
                        if s == "purple":
                            return True
        elif s == "pi":
            s += base.getToken()
            if s == "pin":
                s += base.getToken()
                if s == "pink":
                    return True
    elif s == "o":
        s += base.getToken()
        if s == "or":
            s += base.getToken()
            if s == "ora":
                s += base.getToken()
                if s == "oran":
                    s += base.getToken()
                    if s == "orang":
                        s += base.getToken()
                        if s == "orange":
                            return True
    elif s == "c":
        s += base.getToken()
        if s == "cy":
            s += base.getToken()
            if s == "cya":
                s += base.getToken()
                if s == "cyan":
                    return True
    elif s == "g":
        s += base.getToken()
        if s == "gr":
            s += base.getToken()
            if s == "gra":
                s += base.getToken()
                if s == "gray":
                    return True
    return False

# <cc> ::= “cc ” <color>
def cambiarColor(base: DescensoRecursivoBase) -> bool:
    token = base.getToken()
    if token == "c":
        token = base.getToken()
        if token == "c":
            token = base.getToken()
            if token == " ":
                return color(base)
    return False

# <pluma> ::= <pa> | <pb> | <lp> | <cp> | <cc>
def pluma(base: DescensoRecursivoBase) -> bool:
    if plumaArriba(base):
        return True
    elif plumaAbajo(base):
        return True
    elif limpiarPantalla(base):
        return True
    elif centrarPluma(base):
        return True
    elif cambiarColor(base):
        return True
    return False