from svg_turtle import SvgTurtle

lexema_nArgs = {
    "go": 1, # avanzar
    "gd": 1, # girar derecha
    "gi": 1, # girar izquierda
    "dir": 1, # direccion
    "pa": 0, # pluma arriba
    "pb": 0, # pluma abajo
    "lp": 0, # limpiar pantalla
    "cc": 1, # Cambiar color
}

class Parser:
    query = []

    def __init__(self):
        self.turtle = SvgTurtle()

    def queryArgToCommand(self, commandName, commandArgs):
        if commandName == "go": # avanzar
            self.query.append(lambda: self.turtle.forward(int(commandArgs[0])))
        elif commandName == "gd": # girar derecha
            self.query.append(lambda: self.turtle.right(int(commandArgs[0])))
        elif commandName == "gi": # girar izquierda
            self.query.append(lambda: self.turtle.left(int(commandArgs[0])))
        elif commandName == "dir": # direccion
            self.query.append(lambda: self.turtle.setheading(int(commandArgs[0])))
        elif commandName == "pa": # pluma arriba
            self.query.append(lambda: self.turtle.penup())
        elif commandName == "pb": # pluma abajo
            self.query.append(lambda: self.turtle.pendown())
        elif commandName == "lp": # limpiar pantalla
            self.query.append(lambda: self.turtle.clear())
        elif commandName == "cc": # Cambiar color 
            self.query.append(lambda: self.turtle.pencolor(commandArgs[0]))
    
    def parse(self, text: str):
        splittedText = text.split(" ")
        print(splittedText)
        currentCommand = ""
        currentCommandArgs = []
        stringQuery = []
        while splittedText:
            print(splittedText)
            lexema = splittedText.pop(0)
            if lexema in lexema_nArgs:
                for i in range(lexema_nArgs[lexema]):
                    currentCommandArgs.append(splittedText.pop(0))
                self.queryArgToCommand(lexema, currentCommandArgs)
                stringQuery.append(lexema + " " + " ".join(currentCommandArgs))
                currentCommandArgs = []
            else:
                print("Error: Lexema no reconocido")
                break
        return stringQuery
                
    def execute(self):
        for command in self.query:
            print(command)
            command()
        
    def save(self, filename: str):
        self.turtle.save_as(filename)
    
    def getSVG(self):
        return self.turtle.to_svg()


if __name__ == "__main__":
    parser = Parser()
    parser.parse("go 100 gd 90 go 100 gd 90 go 100")
    parser.execute()
    parser.save("temp10.svg")





