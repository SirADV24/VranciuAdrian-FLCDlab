

class Grammar:
    def __init__(self):
        self.nonterminals = []
        self.alphabet = []
        self.starting_symbol = None
        self.productions = {}

    def read(self):
        with open('G.txt', 'r') as f:
            lines = f.readlines()

            non_terminals_line = lines[0].strip()
            non_terminals_line = non_terminals_line.split('|')
            for non_terminal in non_terminals_line:
                self.nonterminals.append(non_terminal)

            alphabet_line = lines[1].strip()
            alphabet_line = alphabet_line.split('|')
            for letter in alphabet_line:
                self.alphabet.append(letter)

            self.starting_symbol = lines[2].strip()

            production_lines = lines[3:]
            for production_line in production_lines:
                production = production_line[0].strip()
                goes_into_list = production_line[5:].strip()
                goes_into_list = goes_into_list.split('|')
                result = []
                for goes_into in goes_into_list:
                    goes_into = goes_into.strip()
                    result.append(goes_into)
                self.productions[production] = result

    def printGrammar(self):
        print(self.nonterminals)
        print(self.alphabet)
        print(self.starting_symbol)
        print(self.productions)
