from Base import DescensoRecursivoBase

# <pa> ::= “pa”
def plumaArriba(base: DescensoRecursivoBase) -> tuple[bool, DescensoRecursivoBase]:
    token = base.getToken()
    if token == "p":
        token = base.getToken()
        if token == "a":
            return True, base
    return False, base

# <pb> ::= “pb”
def plumaAbajo(base: DescensoRecursivoBase) -> bool:
    token = base.getToken()
    if token == "p":
        token = base.getToken()
        if token == "b":
            return True, base
    return False, base

# <lp> ::= “lp”
def limpiarPantalla(base: DescensoRecursivoBase) -> tuple[bool, DescensoRecursivoBase]:
    token = base.getToken()
    if token == "l":
        token = base.getToken()
        if token == "p":
            return True, base
    return False, base

# <cp> ::= “cp”
def centrarPluma(base: DescensoRecursivoBase) -> tuple[bool, DescensoRecursivoBase]:
    token = base.getToken()
    if token == "c":
        token = base.getToken()
        if token == "p":
            return True, base
    return False, base

# <color> ::= ["red" | "green" | "blue" | "yellow" | "black" | "white" | "purple" | "orange" | "brown" | "pink" | "gray" | "cyan"]
def color(base: DescensoRecursivoBase) -> tuple[bool, DescensoRecursivoBase]:
    s = base.getToken()
    if s == "r":
        s += base.getToken()
        if s == "re":
            s += base.getToken()
            if s == "red":
                return True, base
    elif s == "g":
        s += base.getToken()
        if s == "gr":
            s += base.getToken()
            if s == "gre":
                s += base.getToken()
                if s == "gree":
                    s += base.getToken()
                    if s == "green":
                        return True, base
    elif s == "b":
        s += base.getToken()
        if s == "bl":
            s += base.getToken()
            if s == "blu":
                s += base.getToken()
                if s == "blue":
                    return True, base
            elif s == "bla":
                s += base.getToken()
                if s == "blac":
                    s += base.getToken()
                    if s == "black":
                        return True, base
        elif s == "br":
            s += base.getToken()
            if s == "bro":
                s += base.getToken()
                if s == "brow":
                    s += base.getToken()
                    if s == "brown":
                        return True, base
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
                            return True, base
    elif s == "w":
        s += base.getToken()
        if s == "wh":
            s += base.getToken()
            if s == "whi":
                s += base.getToken()
                if s == "whit":
                    s += base.getToken()
                    if s == "white":
                        return True, base
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
                            return True, base
        elif s == "pi":
            s += base.getToken()
            if s == "pin":
                s += base.getToken()
                if s == "pink":
                    return True, base
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
                            return True, base
    elif s == "c":
        s += base.getToken()
        if s == "cy":
            s += base.getToken()
            if s == "cya":
                s += base.getToken()
                if s == "cyan":
                    return True, base
    elif s == "g":
        s += base.getToken()
        if s == "gr":
            s += base.getToken()
            if s == "gra":
                s += base.getToken()
                if s == "gray":
                    return True, base
    return False, base

# <cc> ::= “cc ” <color>
def cambiarColor(base: DescensoRecursivoBase) -> tuple[bool, DescensoRecursivoBase]:
    token = base.getToken()
    if token == "c":
        token = base.getToken()
        if token == "c":
            token = base.getToken()
            if token == " ":
                return color(base)
    return False, base

# <pluma> ::= <pa> | <pb> | <lp> | <cp> | <cc>
def pluma(base: DescensoRecursivoBase) -> tuple[bool, DescensoRecursivoBase]:
    copy_base = base.copy()
    res, temp = plumaArriba(copy_base)
    if res:
        return True, temp
    copy_base = base.copy()
    res, temp = plumaAbajo(copy_base)
    if res:
        return True, temp
    copy_base = base.copy()
    res, temp = limpiarPantalla(copy_base)
    if res:
        return True, temp
    copy_base = base.copy()
    res, temp = centrarPluma(copy_base)
    if res:
        return True, temp
    copy_base = base.copy()
    res, temp = cambiarColor(copy_base)
    if res:
        return True, temp
    return False, base