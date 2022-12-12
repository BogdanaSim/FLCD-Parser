from prettytable import PrettyTable,ALL


class Row:
    def __init__(self, info, parent, right_sibling):
        self.info = info
        self.parent = parent
        self.right_sibling = right_sibling

    def return_data(self):
        return [self.info, self.parent, self.right_sibling]

    def __str__(self):
        return "{ info = " + str(self.info) + ", parent = " + str(self.parent) + ", right_sibling = " + str(
            self.right_sibling) + " }"


class ParserOutput:
    def __init__(self, grammar):
        self.grammar = grammar
        self.table = {}

    def get_string_products(self, alpha):
        products = []
        non_terminals = self.grammar.nonterminals
        for (value, i) in alpha:
            if value in non_terminals:
                products.append((value, i))
        return products

    def get_table(self, alpha):
        string_products = self.get_string_products(alpha)
        products_stack = [self.grammar.starting_symbol]
        index = 1
        parent = 0
        right_sibling = 0
        self.get_recursive_table(index, parent, right_sibling, string_products, products_stack)

    def get_recursive_table(self, index, parent, right_sibling, string_products, products_stack):
        while len(string_products) != 0 or len(products_stack) != 0:
            if len(products_stack) == 0:
                return index, string_products
            head_status = products_stack[0]
            products_stack = products_stack[1:]
            if head_status[0] in self.grammar.terminals:
                self.table[index] = Row(head_status[0], parent, right_sibling)
                right_sibling = index
                index += 1
            else:
                self.table[index] = Row(head_status[0], parent, right_sibling)
                head_products = string_products[0]
                product = self.grammar.get_productions_for_nonterminal(head_products[0])[head_products[1] - 1]
                product = [*product]
                right_sibling = index
                new_index = index + 1
                index, string_products = self.get_recursive_table(new_index, index, 0, string_products[1:], product)
        return index + 1, []

    def print_table(self):
        string = ""
        for key in self.table:
            # print(str(self.table[key]))
            string += str(key) + "->" + str(self.table[key]) + "\n"
        return string

    def print_pretty_table(self):
        table = [['Index', 'Info', 'Parent', 'Right Sibling']]
        tab = PrettyTable(table[0])
        tab.hrules =ALL
        for key in self.table:
            tab.add_row([key] + self.table[key].return_data())
        print(tab)
