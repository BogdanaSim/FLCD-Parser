"""Implementation of grammar abstraction"""

from __future__ import annotations
from enum import Enum
import attrs
from typing import List, Dict


class GrammarParseSeparators(Enum):
    LINE_SEPARATOR = ' '
    RIGHT_SIDE_SEPARATOR = '|'
    ASSIGNMENT_OPERATOR = '::='


@attrs.define
class Grammar:
    """This class implements the basic functionality of working with a grammar,
    including parsing a grammar specification file written in a reduced
    form of EBNF.
    """
    starting_symbol: str
    """Initial state symbol (S)"""
    terminals: List[str] = attrs.Factory(list)
    """List of terminals"""
    nonterminals: List[str] = attrs.Factory(list)
    """List of nonterminals"""
    productions: Dict[str, List[str]] = attrs.Factory(dict)
    """Mapping of nonterminals to lists of coresponding productions"""

    @staticmethod
    def get_grammar_from_file(file_name: str) -> Grammar:
        """Reads grammar specification from a file and returns
        the coresponding Grammar.

        Raises:
            The grammar specification must be written in the specified reduced
        EBNF form and the file must exist (see example specification).
        Otherwise, an exception is thrown.

        Args:
            file_name: Path to the file containing the grammar definition

        Returns:
            Coresponding Grammar if file exists and contains a valid definition
        """
        production_lines: List[str] = []
        with open(file_name) as f:
            nonterminals = f.readline().strip().split(
                GrammarParseSeparators.LINE_SEPARATOR.value)
            terminals = f.readline().strip().split(
                GrammarParseSeparators.LINE_SEPARATOR.value)
            starting_symbol = f.readline().strip()

            production_lines = [line.strip().removesuffix(';')
                                for line in f.readlines()]

        productions: Dict[str, List[str]] = {}
        for line in production_lines:
            production_left, production_right = line.split(
                GrammarParseSeparators.ASSIGNMENT_OPERATOR.value)
            productions[production_left.strip()] = [
                x.strip() for x in production_right.split(
                    GrammarParseSeparators.RIGHT_SIDE_SEPARATOR.value)]

        return Grammar(starting_symbol, terminals, nonterminals, productions)

    def get_productions_for_nonterminal(self, nonterminal: str) -> List[str]:
        """Returns the productions coresponding to a given nonterminal.

        Args:
            nonterminal: The nonterminal to get productions for
        """
        return self.productions[nonterminal]

    def verify_CFG(self) -> bool:
        """Checks if the Grammar is context-free."""
        return not any(
            len(production_left.split(
                    GrammarParseSeparators.LINE_SEPARATOR.value)) > 1
            for production_left in self.productions.keys())
