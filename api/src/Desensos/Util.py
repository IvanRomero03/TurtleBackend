from Base import DescensoRecursivoBase

# <digito> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
def digito(base: DescensoRecursivoBase) -> tuple[bool, DescensoRecursivoBase]:
    print(base, "base")
    token = base.getToken()
    print(token, "token")
    try:
        if token in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            return True, base
        print("Expected a digit, got: " + token)
        return False, base
    except:
        return False, base
    
#FIXME: no jala
# <numero> ::= <digito> | <numero> <digito>
def numero(base: DescensoRecursivoBase) -> tuple[bool, DescensoRecursivoBase]:
    def numero_rec(base: DescensoRecursivoBase) -> tuple[bool, DescensoRecursivoBase]:
        res, base = digito(base)
        if res:
            if base.i == base.n:
                return True, base
            return numero_rec(base)
        else:
            print(base, "base")
            base.i -= 1
            token = base.getToken()
            print(token, "token2")
            if token in (" ", "\n", None, "]"):
                return True, base
            else:
                print("Expected a number, got: " + token)
                return False, base
    
    return numero_rec(base)

# <entero> ::= <numero> | "-" <numero>
def entero(base: DescensoRecursivoBase) -> tuple[bool, DescensoRecursivoBase]:
    copy_base = base.copy()
    token = copy_base.getToken()
    if token == "-":
        return numero(copy_base)
    else:
        return numero(base)
    
# <let> ::= [a-zA-Z]
def letra(base: DescensoRecursivoBase) -> tuple[bool, DescensoRecursivoBase]:
    token = base.getToken()
    if token in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return True, base
    return False, base
    
#FIXME: no jala
# <pal> ::= <let>+
def palabra(base: DescensoRecursivoBase) -> tuple[bool, DescensoRecursivoBase]:
    def palabra_rec(base: DescensoRecursivoBase) -> tuple[bool, DescensoRecursivoBase]:
        res, base = letra(base)
        if res:
            if base.i == base.n:
                return True, base
            return palabra_rec(base)
        else:
            base.i -= 1
            token = base.getToken()
            if token in (" ", "\n", None):
                base.i -= 1
                return True, base
            else:
                return False, base
    return palabra_rec(base)

# <sep> ::= " " | "\n"
def separador(base: DescensoRecursivoBase) -> tuple[bool, DescensoRecursivoBase]:
    if base.i == base.n:
        return True, base
    token = base.getToken()
    if token == "\n":
        return True, base
    elif token == None:
        return True, base
    elif token == " ":
        return True, base
    else:
        return False, base
    



