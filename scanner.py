from main import SymbolTable
import re

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

        self.st = SymbolTable()
        self.tokens = []
        self.defaultSeparator = "SEPARATOR"

    #region Tokens

    def filterSpacesTabsAndNewlines(self, tokens: list) -> str:
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

    def getTokens(self, file: str) -> int:
        with open(file, mode="r") as program:
            rawProgram = program.read()

            tokens = self.splitBySeparators(rawProgram)

            tokens = self.splitByOperators(tokens)

            tokens = self.filterSpacesTabsAndNewlines(tokens)

            self.tokens = tokens

    #endregion

    #region Regex

    def isIdentifier(token: str) -> bool:
        return re.match("^[$_]?[a-zA-Z_][0-9a-zA-Z_]*$", token)

    def isStringConstant(token: str) -> bool:
        pass

    def isNumericalConstant(token: str) -> bool:
        pass

    def isBooleanConstant(token: str) -> bool:
        return re.match("^true|false$", token)

    #endregion

    def run(self, file:str):
        self.getTokens()

        for token in self.tokens:
            pass

    


sc = Scanner()

sc.runProgram("p2.txt")
