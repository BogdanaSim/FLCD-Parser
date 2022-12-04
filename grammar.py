from enum import Enum
import attrs
from typing import List, Dict


class GrammarSymbols(Enum):
    LINE_SEPARATOR = ' '
    RIGHT_SIDE_SEPARATOR = '|'
    ASSIGNMENT_OPERATOR = '::='


@attrs.define
class Grammar:
    starting_symbol: str
    terminals: List[str] = attrs.Factory(list)
    nonterminals: List[str] = attrs.Factory(list)
    productions: Dict[str, List[str]] = attrs.Factory(dict)

    @staticmethod
    def get_grammar_from_file(file_name: str):
        production_lines: List[str] = []
        with open(file_name) as f:
            nonterminals = f.readline().strip().split(
                GrammarSymbols.LINE_SEPARATOR.value)
            terminals = f.readline().strip().split(
                GrammarSymbols.LINE_SEPARATOR.value)
            starting_symbol = f.readline().strip()

            production_lines = [line.strip().removesuffix(';')
                                for line in f.readlines()]

        productions: Dict[str, List[str]] = {}
        for line in production_lines:
            production_left, production_right = line.split(
                GrammarSymbols.ASSIGNMENT_OPERATOR.value)
            productions[production_left.strip()] = [
                x.strip() for x in production_right.split(
                    GrammarSymbols.RIGHT_SIDE_SEPARATOR.value)]

        return Grammar(starting_symbol, terminals, nonterminals, productions)

    def get_productions_for_nonterminal(self, nonterminal: str) -> List[str]:
        return self.productions[nonterminal]

    def verify_CFG(self) -> bool:
        return not any(
            len(production_left.split(GrammarSymbols.LINE_SEPARATOR.value)) > 1
            for production_left in self.productions.keys())
