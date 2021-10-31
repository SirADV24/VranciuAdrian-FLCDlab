import re

from symbolTable import SymbolTable


class Scanner:
    def __init__(self):
        with open("lab 2/token.txt", mode="r") as file:
            lines = file.readlines()
            self.reservedWords = lines[0].strip().split(" ")
            self.operators = lines[1].strip().split(" ")
            self.separators = lines[2].strip().split(" ")

            for separator in self.separators:
                if separator == "space":
                    self.separators.remove(separator)
                    self.separators.append(" ")

                if separator == "\\n":
                    self.separators.remove(separator)
                    self.separators.append("\n")

        self.symbolTable = SymbolTable()
        self.pif = []
        self.defaultSeparator = "SEPARATOR"

    # region Tokens

    def filterSpacesTabsAndNewlines(self, tokens: list) -> list:
        sanitiezedResult = []

        for token in tokens:
            sanitizedToken = token.strip("\t").strip("\n").strip(" ")
            if sanitizedToken != '' and sanitizedToken != ' ' and sanitiezedResult != '\n' and sanitiezedResult != '\t':
                sanitiezedResult.append(sanitizedToken)

        return sanitiezedResult

    def splitBySeparators(self, text: str) -> list:
        for separator in self.separators:
            text = text.replace(
                separator, self.defaultSeparator + separator + self.defaultSeparator)

        return list(filter(lambda x: x != " " or x != "", text.split(self.defaultSeparator)))

    def splitByOperators(self, tokens: list) -> list:
        splitted = []

        for token in tokens:
            sanitizedToken = token
            for operator in self.operators:
                sanitizedToken = sanitizedToken.replace(
                    operator, self.defaultSeparator + operator + self.defaultSeparator)

            tokens = sanitizedToken.split(self.defaultSeparator)

            splitted = splitted + tokens

        return splitted

    def getTokens(self, line: str):
        tokens = self.splitBySeparators(line)
        tokens = self.splitByOperators(tokens)
        tokens = self.filterSpacesTabsAndNewlines(tokens)

        return tokens

    # endregion

    # region Regex

    def isIdentifier(self, token: str) -> bool:
        return re.match("^[$_]?[a-zA-Z_][0-9a-zA-Z_]*$", token)

    def isStringConstant(self, token: str) -> bool:
        return re.match('^"[a-zA-Z0-9 ]+"$', token)

    def isNumericalConstant(self, token: str) -> bool:
        return re.match('^[-]?[1-9][0-9]*$', token) or re.match('0', token)

    def isBooleanConstant(self, token: str) -> bool:
        return re.match("^true|false$", token)

    def isConstant(self, token: str) -> bool:
        return self.isStringConstant(token) \
            or self.isNumericalConstant(token) \
            or self.isBooleanConstant(token)

    # endregion

    # region Write to file

    def writeToFile(self, file):
        
        with open("results/{0}.symbolTable.txt".format(file), "w") as symbolTableFile:
            symbolTableFile.write(str(self.symbolTable))

        with open("results/{0}.pif.txt".format(file), "w") as pifFile:
            pifString = ""

            for pair in self.pif:
                pifString =  pifString + str(pair) + "\n"

            pifFile.write(pifString)

    # endregion

    def run(self, file: str):
        self.pif = []
        self.symbolTable = SymbolTable()
        errors = []

        with open(file, "r") as program:
            lines = program.readlines()

            for index, line in enumerate(lines):
                tokens = self.getTokens(line)
                if line == []:
                    continue

                for token in tokens:
                    if token in self.reservedWords or token in self.separators or token in self.operators:
                        self.pif.append((token, -1))

                    elif self.isConstant(token) or self.isIdentifier(token):
                        if self.symbolTable.get(token) == -1:
                            self.symbolTable.add(token)

                        self.pif.append((token, self.symbolTable.get(token)))


                    else:
                        errors.append(
                            "Error on line {0}, invalid token {1}".format(index, token))
                        break

        if len(errors) == 0:
            print("lexically correct {0}".format(file))
            self.writeToFile(file)
        else:
            print("lexical error {0}".format(file))
            for error in errors:
                print(error)


sc = Scanner()

# sc.run("p1.txt")
# sc.run("p2.txt")
sc.run("p3.txt")
# sc.run("p1error.txt")
