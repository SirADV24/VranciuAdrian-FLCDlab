class Production:
    def __init__(self, LHS, RHS) -> None:
        self.LHS = LHS
        self.RHS = RHS

    def __str__(self) -> str:
        return self.LHS + " -> " + str(self.RHS)


class Grammar:
    assignment = '  1.b. ll(1) '

    def __init__(self) -> None:
        self.nonterminals = []
        self.alphabet = []
        self.productions = []
        self.startingSymbol = None

        self.file = "g1-test.txt"

        with open(self.file, "r") as file:
            lines = file.readlines()
            self.readNonTerminals(lines[0].strip())
            self.readAlphabet(lines[1].strip())
            self.readStartingSymbol(lines[2].strip())

            productionLines = lines[4:]
            self.readProductions(productionLines)

    def readNonTerminals(self, line: str) -> None:
        rawTerminalsString = line.split(":")[1:][0].strip()
        self.nonterminals = rawTerminalsString.split("|")

    def readAlphabet(self, line: str) -> None:
        rawAlhabetString = line.split(":")[1:][0].strip()
        self.alphabet = rawAlhabetString.split("|")

    def readStartingSymbol(self, line: str) -> None:
        self.startingSymbol = line.split(":")[1:][0]

    def readProductions(self, lines: str) -> None:
        for line in lines:
            line = line.strip().split("->")
            LHS = line[0].strip()
            RHS = []
            RHSraw = line[1].split("|")

            for x in RHSraw:
                x = x.strip()
                x = x.split(" ")
                RHS.append((x[0], x[1]))

            self.productions.append(Production(LHS, RHS))

    def printNonTerminals(self) -> None:
        print("Non terminals " + str(self.nonterminals))

    def printAlhabet(self) -> None:
        print("Alhabet " + str(self.alphabet))

    def printStartingSymbol(self) -> None:
        print("Starting symbol " + str(self.startingSymbol))

    def printProductions(self) -> None:
        for production in self.productions:
            print(str(production))

    def printAll(self) -> None:
        # for testing
        self.printNonTerminals()
        self.printAlhabet()
        self.printStartingSymbol()
        self.printProductions()

    def checkCFG(self) -> bool:
        for production in self.productions:
            if production.LHS not in self.nonterminals:
                return False
            for pair in production.RHS:
                x = pair[0]
                y = pair[1]

                if x not in self.alphabet:
                    return False

                if y not in self.nonterminals:
                    return False
        return True

    def getProductionForNonTerminal(self, nonTerminal):
        if nonTerminal not in self.nonterminals:
            return []
        result = []

        for production in self.productions:
            if production.LHS == nonTerminal:
                result.append(production.RHS)

        return result


g = Grammar()

g.printAll()

print(g.checkCFG())

result1 = g.getProductionForNonTerminal("S")
result2 = g.getProductionForNonTerminal("A")
result3 = g.getProductionForNonTerminal("B")
result4 = g.getProductionForNonTerminal("C")

print(result1)
print(result2)
print(result3)
print(result4)
