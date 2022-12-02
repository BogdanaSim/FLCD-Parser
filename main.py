import os

from grammar import Grammar
from parser import Parser


def print_grammar_menu():
    print("=== GRAMMAR ===\n")
    print("1 - Read grammar from file")
    print("2 - Print set of non-terminals")
    print("3 - Print set of terminals")
    print("4 - Print set of productions")
    print("5 - Print set of productions for a given non-terminal")
    print("6 - Check if grammar is cfg")
    print("7 - Exit")
    print()


if __name__ == '__main__':
    grammar = Grammar.get_grammar_from_file("g1.txt")
    parser = Parser(grammar)
    # TODO: test/print results for each function
    print(parser)
    parser.expand()
    print(parser)
    # done = False
    # while not done:
    #     print_grammar_menu()
    #     option = input("Choose an option: ")
    #     if option == "1":
    #         file = input("File name: ")
    #         if os.path.exists(file):
    #             grammar = Grammar.get_grammar_from_file(file)
    #             print("Grammar file read successfully.\n")
    #         else:
    #             print("File does not exist!\n")
    #     elif option == "2":
    #         print(grammar.nonterminals)
    #     elif option == "3":
    #         print(grammar.terminals)
    #     elif option == "4":
    #         print(grammar.productions)
    #     elif option == "5":
    #         terminal = input("Non-terminal: ")
    #         try:
    #             print(grammar.get_productions_for_nonterminal(terminal))
    #             print()
    #         except Exception as e:
    #             print(e)
    #     elif option == "6":
    #         if grammar.verify_CFG():
    #             print("The given grammar is a cfg.\n")
    #         else:
    #             print("The given grammar is not a cfg.\n")
    #     elif option == "7":
    #         done = True
    #     else:
    #         print("This option does not exist!\n")
