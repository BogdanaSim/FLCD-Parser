import os

from grammar import Grammar


def print_grammar_menu():
    print("Menu grammar")
    print("1 - Read grammar from file")
    print("2 - Print set of non-terminals")
    print("3 - Print set of terminals")
    print("4 - Print set of productions")
    print("5 - Print set of productions for a given non-terminal")
    print("6 - Check if grammar is cfg")
    print("7 - Exit")


if __name__ == '__main__':
    grammar = Grammar("g1.txt")
    done = False
    while not done:
        print_grammar_menu()
        option = input("Choose an option:")
        if option == "1":
            file = input("Write file name:")
            if os.path.exists(file):
                grammar.read_input_file(file)
                print("Grammar file read successfully.\n")
            else:
                print("File does not exist!")
        elif option == "2":
            print(grammar.get_set_non_terminals_str())
        elif option == "3":
            print(grammar.get_set_terminals_str())
        elif option == "4":
            print(grammar.get_set_productions_str())
        elif option == "5":
            terminal = input("Enter a terminal:")
            try:
                print(grammar.get_set_productions_for_non_terminal_str(terminal))
            except Exception as e:
                print(e)
        elif option == "6":
            print("\n")
        elif option == "7":
            done = True
        else:
            print("This option does not exist!")
