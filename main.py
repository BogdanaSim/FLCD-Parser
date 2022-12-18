import os

from grammar import Grammar
from output import ParserOutput
from parser import Parser, ParsingStates


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


def print_parser_menu():
    print("=== Parser ===\n")
    print("1 - Parse seq.txt using g1")
    print("2 - Parse PIF.out using g2")
    print("3 - Exit")


if __name__ == '__main__':
    done = False

    while not done:
        print_parser_menu()
        option = input("Choose an option: ")
        if option == "1":
            grammar1 = Grammar.get_grammar_from_file("g1.txt")
            parser1 = Parser(grammar1)
            print("Before parsing: " + str(parser1))
            parser1.read_sequence_from_file("seq.txt")
            print("Used sequence: "+str(" ".join(parser1.w)))
            parser1.algorithm_descendent_recursive("seq.txt")
            print("After parsing: " + str(parser1))
            parser_out1 = ParserOutput(grammar1)
            if parser1.state == ParsingStates.FINAL_STATE:
                parser_out1.get_table(parser1.alpha)
                # print(parser_out.print_table())
                parser_out1.print_pretty_table()
                parser_out1.print_pretty_table_to_file("out1.txt")
        elif option == "2":
            grammar2 = Grammar.get_grammar_from_file("g2.txt")
            parser2 = Parser(grammar2)
            print("Before parsing: " + str(parser2))
            parser2.read_sequence_from_file("PIF.out")
            print("Used sequence: " + str(" ".join(parser2.w)))
            parser2.algorithm_descendent_recursive("PIF.out")
            print("After parsing: " + str(parser2))
            parser_out2 = ParserOutput(grammar2)
            if parser2.state == ParsingStates.FINAL_STATE:
                parser_out2.get_table(parser2.alpha)
                # print(parser_out.print_table())
                parser_out2.print_pretty_table()
                parser_out2.print_pretty_table_to_file("out2.txt")
        elif option == "3":
            done = True
        else:
            print("This option does not exist!\n")

    # TODO: test/print results for each function
    # parser.alpha = [('S', 1), ('a', -1), ('S', 1), ('a', -1), ('S', 1)]
    # parser.beta = "aSbSbSbS"
    # parser.current_position = 3
    # parser.state = ParsingStates.BACK_STATE
    # parser.alpha = [('S', 1), ('a', -1), ('S', 1), ('a', -1), ('S', 3), ('c', -1), ('b', -1), ('S', 3)]
    # parser.beta = "cbS"
    # parser.current_position = 5
    # parser.state = ParsingStates.BACK_STATE
    # parser.alpha = [('S', 1), ('a', -1), ('S', 2), ('a', -1), ('S', 3), ('c', -1), ('b', -1),('S', 2)]
    # parser.beta = "aS"
    # parser.current_position = 5
    # parser.state = ParsingStates.BACK_STATE
    # print(parser)
    #
    # parser.another_try()
    #
    # print(parser)

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
