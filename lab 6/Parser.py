from Grammar import *


class Parser:
    def __init__(self):
        self.Grammar = Grammar()
        self.Grammar.read()
        self.firstSet = {}
        self.followSet = {}

    def testGrammar(self):
        self.Grammar.printGrammar()

    def first(self):
        self.firstSet = {}

        keep_parsing = False
        for x, y in self.Grammar.productions.items():
            for sample in y:
                if sample[0] in self.Grammar.alphabet:
                    if x not in self.firstSet.keys():
                        self.firstSet[x] = [sample[0]]
                    else:
                        self.firstSet[x].append(sample[0])
                else:
                    keep_parsing = True

        while keep_parsing:

            keep_parsing = False
            look_for = None
            non_terminal = None
            for x, y in self.Grammar.productions.items():
                for sample in y:
                    if sample[0] not in self.Grammar.alphabet:
                        keep_parsing = True
                        look_for = sample[0]
                        non_terminal = x

            if look_for:
                found = self.Grammar.productions[look_for]
                if found[0][0] in self.Grammar.alphabet:
                    if non_terminal not in self.firstSet.keys():
                        self.firstSet[non_terminal] = [found[0][0]]
                        break
                    else:
                        self.firstSet[non_terminal].append(found[0][0])
                        break
                else:
                    prod = self.Grammar.productions[non_terminal]

                    for i in range(0, len(prod), 1):
                        if prod[i][0] == look_for:
                            self.Grammar.productions[non_terminal][i] = found[0][0]
                    look_for = found[0][0]

    def follow(self):
        self.followSet = {i: [] for i in self.Grammar.nonterminals}
        self.followSet[self.Grammar.starting_symbol] = ["E"]

        changed = True

        while changed:
            changed = False

            for key, value in self.Grammar.productions.items():
                for rhs in value:
                    for i in range(len(rhs)):
                        if i == " ":
                            continue
                        if rhs[i] in self.Grammar.nonterminals:
                            if i == len(rhs) - 1:
                                temp = self.followSet[rhs[i]]
                                self.followSet[rhs[i]] = list(
                                    set(self.followSet[rhs[i]] + self.firstSet[key]))

                                if len(temp) != len(self.followSet[rhs[i]]):
                                    changed = True
                            else:
                                if rhs[i + 2] not in self.followSet[rhs[i]]:
                                    if rhs[i + 2] in self.Grammar.alphabet:
                                        self.followSet[rhs[i]].append(
                                            rhs[i + 2])
                                        changed = True
                                    else:
                                        temp = self.followSet[rhs[i]]
                                        self.followSet[rhs[i]] = list(
                                            set(self.followSet[rhs[i]] + self.firstSet[rhs[i + 2]]))

                                        if len(temp) != len(self.followSet[rhs[i]]):
                                            changed = True


p = Parser()

print("Grammar: \n")

p.testGrammar()

print("\nEnd grammar \n\n\n")

print("First: \n")

p.first()
print(p.firstSet)

print("\nEnd First: \n\n")

print("Follow: \n")

p.follow()
print(p.followSet)

print("\nEnd Follow: \n\n")
