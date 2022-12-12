import unittest
from grammar import Grammar
from parser import Parser, ParsingStates

TEST_GRAMMAR_PATH: str = 'g3.txt'


class RecursiveDescentParserTest(unittest.TestCase):
    def setUp(self) -> None:
        self.grammar = Grammar.get_grammar_from_file(TEST_GRAMMAR_PATH)
        self.parser: Parser = Parser(self.grammar)

    def test_expand(self) -> None:
        self.parser.state = ParsingStates.NORMAL_STATE
        self.parser.input_list = ['S']
        self.parser.working_list = []
        self.parser.current_position = 0

        self.parser.expand()

        self.assertEqual(self.parser.state, ParsingStates.NORMAL_STATE)
        self.assertEqual(self.parser.input_list, ['a', 'S', 'b', 'S'])
        self.assertListEqual(self.parser.working_list, [('S', 0)])
        self.assertEqual(self.parser.current_position, 0)

    def test_advance(self) -> None:
        self.parser.state = ParsingStates.NORMAL_STATE
        self.parser.input_list = ['a', 'S', 'b', 'S']
        self.parser.working_list = [('S', 0)]
        self.parser.current_position = 0

        self.parser.advance()

        self.assertEqual(self.parser.state, ParsingStates.NORMAL_STATE)
        self.assertEqual(self.parser.input_list, ['S', 'b', 'S'])
        self.assertListEqual(self.parser.working_list, [('S', 0), ('a', 1)])
        self.assertEqual(self.parser.current_position, 1)

    def test_back(self) -> None:
        self.parser.state = ParsingStates.BACK_STATE
        self.parser.input_list = ['S', 'c', 'b', 'S', 'b', 'S']
        self.parser.working_list = [('S', 0), ('a', 1), ('S', 0), ('a', 2)]
        self.parser.current_position = 2

        self.parser.back()

        self.assertEqual(self.parser.state, ParsingStates.BACK_STATE)
        self.assertEqual(self.parser.input_list,
                         ['a', 'S', 'c', 'b', 'S', 'b', 'S'])
        self.assertListEqual(self.parser.working_list,
                             [('S', 0), ('a', 1), ('S', 0)])
        self.assertEqual(self.parser.current_position, 1)

    def test_momentary_insuccess(self) -> None:
        self.parser.state = ParsingStates.NORMAL_STATE
        self.parser.input_list = ['a', 'S', 'b', 'S']
        self.parser.working_list = [('S', 0)]
        self.parser.current_position = 0

        self.parser.momentary_insuccess()

        self.assertEqual(self.parser.state, ParsingStates.BACK_STATE)
        self.assertEqual(self.parser.input_list, ['a', 'S', 'b', 'S'])
        self.assertListEqual(self.parser.working_list, [('S', 0)])
        self.assertEqual(self.parser.current_position, 0)

    def test_success(self) -> None:
        self.parser.state = ParsingStates.NORMAL_STATE
        self.parser.input_list = ['a', 'S', 'b', 'S']
        self.parser.working_list = [('S', 0)]
        self.parser.current_position = 0

        self.parser.success()

        self.assertEqual(self.parser.state, ParsingStates.FINAL_STATE)
        self.assertEqual(self.parser.input_list, ['a', 'S', 'b', 'S'])
        self.assertListEqual(self.parser.working_list, [('S', 0)])
        self.assertEqual(self.parser.current_position, 0)

    def test_another_try(self) -> None:
        pass

    def test_parse(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
