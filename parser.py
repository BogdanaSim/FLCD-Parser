from enum import Enum
import attrs
from typing import List

from grammar import Grammar


class ParsingStates(Enum):
    NORMAL_STATE = "q"
    BACK_STATE = "b"
    FINAL_STATE = "f"
    ERROR_STATE = "e"


@attrs.define
class Parser:
    grammar: Grammar
    state: ParsingStates = attrs.field(default=ParsingStates.NORMAL_STATE)
    current_position: int = attrs.field(default=1)  # should use 0 to be consistent?

    # list of tuples, each having the terminal/non_terminal with the position of one of its productions (position -1
    # for terminals)
    alpha: list = attrs.field(default=attrs.Factory(
        list))  # should this be also a string?, harder to maintain the string if terminals are numbers
    beta: str = attrs.field(default="S")  # kept as a string to get the head easier

    # def __attrs_post_init__(self):
    #     self.beta.append("S")

    def expand(self):
        head_input = self.beta[0]
        self.alpha.append((head_input, 1))  # non-terminal followed by the position of the production
        production = self.grammar.get_productions_for_nonterminal(head_input)[0]
        self.beta = self.beta[1:]
        self.beta = production + self.beta

    def advance(self):
        head_input = self.beta[0]
        self.current_position += 1
        self.beta = self.beta[1:]
        self.alpha.append((head_input, -1))  # terminal followed by -1

    def momentary_insuccess(self):
        self.state = ParsingStates.BACK_STATE

    def back(self):
        self.current_position -= 1
        head_working = self.alpha[-1]
        self.beta = head_working[0] + self.beta
        self.alpha = self.alpha[:-1]

    # check this for each case and the order of the conditions
    def another_try(self):

        head_working = self.alpha[-1]
        self.alpha = self.alpha[:-1]  # get rid of the terminal at the head of the working stack

        (non_terminal, index_non_terminal) = head_working
        productions = self.grammar.get_productions_for_nonterminal(non_terminal)
        self.beta = self.beta[len(
            productions[int(index_non_terminal) - 1]):]  # get rid of the previous production using its length
        index = int(index_non_terminal)  # = i+1 since the index of the productions starts at 0
        if index < len(productions):
            self.state = ParsingStates.NORMAL_STATE
            self.alpha.append((non_terminal, index + 1))
            self.beta = productions[index] + self.beta
        else:
            # should we raise an exception here?
            self.state = ParsingStates.BACK_STATE
            # self.alpha = self.alpha[:-1]
            self.beta = non_terminal + self.beta
        if self.current_position == 1 and non_terminal == "S":
            self.state = ParsingStates.ERROR_STATE

    def success(self):
        self.state = ParsingStates.FINAL_STATE

    def algorithm_descendent_recursive(self, w):
        while self.state != ParsingStates.FINAL_STATE and self.state != ParsingStates.ERROR_STATE:
            if self.state == ParsingStates.NORMAL_STATE:
                n = len(w)

                if self.current_position == n + 1 and len(self.beta) == 0:
                    self.success()
                else:
                    head_b = self.beta[0]
                    if head_b in self.grammar.nonterminals:
                        self.expand()
                    else:
                        if self.current_position - 1 < len(w) and head_b == w[self.current_position - 1]:
                            self.advance()
                        else:
                            self.momentary_insuccess()
            else:
                if self.state == ParsingStates.BACK_STATE:
                    head_a = self.alpha[-1]
                    if head_a[0] in self.grammar.terminals:
                        self.back()
                    else:
                        self.another_try()

        if self.state == ParsingStates.ERROR_STATE:
            print("Error")
        else:
            print("Sequence accepted")

    def __str__(self):
        return "(" + str(self.state.value) + ", " + str(self.current_position) + ", " + str(self.alpha) + ", " + str(
            self.beta) + ")"

    def build_string_of_prod(self):
        # TODO: how should the string look like using the list of tuples self.alpha?
        # maybe change the list to string
        return ""
