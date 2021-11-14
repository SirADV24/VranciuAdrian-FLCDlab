from fa import FiniteAutomata

class Menu:
    def __init__(self):
        self.filename = "fa.txt"
        self.fa = FiniteAutomata(self.filename)

    def displayFa(self):
        print(self.fa)

    def displayStates(self):
        print(self.fa.Q)

    def displayAlphabet(self):
        print(self.fa.E)

    def displayTransitions(self):
        print(self.fa.S)

    def displayFinalStates(self):
        print(self.fa.F)

    def deterministic(self):
        print(self.fa.isDeterministicFA())

    def sequence(self):
        seq = input()
        print(self.fa.isAccepted(seq))

    def __displayMenu(self):
        print("1: FA")
        print("2: FA States")
        print("3: FA Alphabet")
        print("4: FA transitions")
        print("5: FA final states")
        print("6: Check Deterministic")
        print("7: Sequence")

    def run(self):
        menu = {
            '1':self.displayFa,
            '2':self.displayStates,
            '3':self.displayAlphabet,
            '4':self.displayTransitions,
            '5':self.displayFinalStates,
            '6':self.deterministic,
            '7':self.sequence
        }

        while True:
            self.__displayMenu()
        
            print(": ")
        
            cmd = input()
            if cmd in menu:
                menu[cmd]()
            elif cmd == "exit":
                break
            else:
                continue