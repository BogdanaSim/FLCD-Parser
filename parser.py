from enum import Enum
import attrs
import abc
from typing import List, Tuple

from grammar import Grammar


class ParsingStates(Enum):
    NORMAL_STATE = 'q'
    BACK_STATE = 'b'
    FINAL_STATE = 'f'
    ERROR_STATE = 'e'


@attrs.define
class Parser:
    grammar: Grammar
    state: ParsingStates = ParsingStates.NORMAL_STATE
    current_position: int = 0

    input_list: List[str] = attrs.Factory(list)
    working_list: List[Tuple[str, int]] = attrs.Factory(list)

    def reset_config(self):
        self.state = ParsingStates.NORMAL_STATE
        self.current_position = 0
        self.working_list = []
        self.input_list = [self.grammar.starting_symbol]

    def expand(self):
        input_head = self.input_list.pop(0)

        self.working_list.append((input_head, 0))

        productions = self.grammar.get_productions_for_nonterminal(
            input_head)[0]

        for production in reversed(productions):
            self.input_list.insert(0, production)

    def advance(self):
        input_head = self.input_list.pop(0)

        self.current_position += 1
        self.working_list.append((input_head, self.current_position))

    def back(self):
        working_tail = self.working_list.pop()

        self.current_position -= 1
        self.input_list.insert(0, working_tail[0])

    def another_try(self):
        nonterminal, nonterminal_index = self.working_list.pop()

        if self.current_position == 0 and \
                nonterminal == self.grammar.starting_symbol:
            self.state = ParsingStates.ERROR_STATE

            return

        productions = self.grammar.get_productions_for_nonterminal(
            nonterminal)

        self.input_list = self.input_list[len(productions[nonterminal_index]):]

        if nonterminal_index < len(productions):
            self.state = ParsingStates.NORMAL_STATE
            self.working_list.append((nonterminal, nonterminal_index + 1))

            for production in reversed(productions[nonterminal_index]):
                self.input_list.insert(0, production)
        else:
            self.state = ParsingStates.BACK_STATE
#            self.working_list.pop()
            self.input_list.insert(0, nonterminal)

    def momentary_insuccess(self):
        self.state = ParsingStates.BACK_STATE

    def success(self):
        self.state = ParsingStates.FINAL_STATE

    def build_string_of_prod(self):
        return str(self.working_list)

    def parse(self, word: str):
        self.reset_config()

        while self.state not in [
                ParsingStates.FINAL_STATE, ParsingStates.ERROR_STATE]:
            if self.state == ParsingStates.NORMAL_STATE:
                if self.current_position == len(word) and not self.input_list:
                    self.success()
                else:
                    if self.input_list[0] in self.grammar.nonterminals:
                        self.expand()
                    elif self.current_position < len(word) and \
                            self.input_list[0] == word[self.current_position]:
                        self.advance()
                    else:
                        self.momentary_insuccess()

            elif self.state == ParsingStates.BACK_STATE:
                if self.working_list[0][0] in self.grammar.terminals:
                    self.back()
                else:
                    self.another_try()

        if self.state == ParsingStates.ERROR_STATE:
            raise RuntimeError(f'Could not parse sequence {word}')

        return self.build_string_of_prod()

    def __str__(self):
        return '\n'.join([
            f'STATE: {self.state}',
            f'CURRENT POSITION: {self.current_position}',
            f'WORKING LIST: {self.working_list}',
            f'INPUT LIST: {self.input_list}'
        ])
