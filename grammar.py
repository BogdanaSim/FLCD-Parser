class Grammar:
    # TODO : check if grammar is cfg
    def __init__(self, filename):
        self.N = []  # non-terminals
        self.E = []  # terminals
        self.P = {}  # set of productions
        self.S = None  # start symbol
        self.read_input_file(filename)

    def read_input_file(self, filename):
        with open(filename) as file:
            self.N = file.readline().strip().replace(" ", "")[3:-1].split(',')
            self.E = file.readline().strip().replace(" ", "")[3:-1].split(',')
            self.S = file.readline().strip().replace(" ", "").split("=")[1]
            file.readline()
            for line in file:
                if line != '}' and len(line) > 0:
                    pair = line.strip().replace(" ", "").split('->')
                    production_left = pair[0]
                    production_right = pair[1]
                    target = line.strip().replace(" ", "").split('->')[1].strip()
                    productions = production_right.split("|")
                    if production_left in self.P.keys():
                        self.P[production_left].append(target)
                    else:
                        self.P[production_left] = productions

    def get_set_terminals_str(self):
        return "N = {" + ", ".join([str(x) for x in self.N]) + "}\n"

    def get_set_non_terminals_str(self):
        return "E = {" + ", ".join([str(x) for x in self.E]) + "}\n"

    def get_set_productions_str(self):
        P = ""
        for production_left in self.P.keys():
            production_right = self.P[production_left]
            P += str(production_left) + " -> "
            for p in production_right:
                P += p + " | "
            P = P[:-3] + "\n"
        return "P = {\n" + P + "}\n"

    def get_set_productions_for_non_terminal_str(self, terminal):
        if terminal not in self.N:
            raise Exception("The input is not a valid terminal!")
        set_productions = str(terminal) + " -> "
        production_right = self.P[terminal]
        for p in production_right:
            set_productions += p + " | "
        set_productions = set_productions[:-3] + ",\n"
        return set_productions

    def __str__(self):
        P = ""
        for production_left in self.P.keys():
            production_right = self.P[production_left]
            P += str(production_left) + " -> "
            for p in production_right:
                P += p + " | "
            P = P[:-3] + ",\n"

        return "N = {" + ", ".join([str(x) for x in self.N]) + "}\n" + "E = {" + ", ".join(
            [str(x) for x in self.E]) + "}\n" + "S = " + str(
            self.S) + "\n" + "P = {\n" + P + "}\n"
