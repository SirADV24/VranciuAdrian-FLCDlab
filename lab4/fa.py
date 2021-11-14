class FiniteAutomata:

    def __init__(self, filename: str):
        self.Q = [] # States
        self.E = [] # Alphabet
        self.q0 = None # initial state
        self.F = None # Final state
        self.S = {} # Transitions

        with open(filename, "r") as file:
            lines = file.readlines()

            self.Q = self.computeLine(lines[0])
            self.E = self.computeLine(lines[1])
            self.q0 = self.computeLine(lines[2])[0]
            self.F = self.computeLine(lines[3])
            self.S = self.computeTransitions(lines[4])
        
        self.validateFA()

    def computeLine(self, line: str):
        return line.strip().split(':')[1].split(" ")

    def computeTransitions(self, line):
        states = line.split(":")[1:]
        states = states[0].split(",")

        result = {}

        for state in states:
            state = state.strip().split(" ")
            key = (state[0], int(state[1]))

            if key in result.keys():
                result[key].append(state)
            else:
                result[(state[0], int(state[1]))] = [state[2]]

        return result

    def validateFA(self):
        return self.checkIfq0() and self.checkF() and self.checkS()

    def checkIfq0(self):
        return self.q0 in self.Q
    
    def checkF(self):
        return all(f in self.Q for f in self.F)
    
    def checkS(self):
        for key in self.S.keys():
            state = key[0]
            symbol = key[1]

            if state not in self.Q:
                return False
            if symbol not in self.E:
                return False
            for dest in self.S[key]:
                if dest not in self.Q:
                    return False
        return True


    def isDeterministicFA(self):
        return all(len(self.S[k]) == 1 for k in self.S.keys())        

    def isAccepted(self, seq):
        # check if we can reach the final state
        if not self.isDeterministicFA():
            return False;

        crt = self.q0
        for symbol in seq:
            symbol = int(symbol)
            if (crt, symbol) in self.S.keys():
                crt = self.S[(crt, symbol)][0]
            else:
                return False
        return crt in self.F

    def __str__(self):
        return "FA states: " + str(self.Q) + "\n" +\
            "FA alhabet: " + str(self.E) + "\n" + \
            "FA initial state: " + self.q0 + "\n" +\
            "FA initial states: " + str(self.F) + "\n" + \
            "FA transitions: " + str(self.S) + "\n"