"""Tests for most occurred symbol"""
from unittest import TestCase
from unittest.mock import (
    MagicMock,
    Mock,
    patch,
    PropertyMock,
)

from most_occurred_symbol import *

class TestMostOccurredSymbol(TestCase):
    """Test class for tzhe most occurred Symbol"""
    def setUp(self):
        pass

    @patch("builtins.print")
    @patch("builtins.input")
    def test_main(self, input_mock, print_mock):
        input_mock.side_effect = [None, "aaasdfHHhh", "", "aaasdfHHhh", "N"]
        with self.assertRaises(SystemExit):
            most_occurred_symbol.main()
        most_occurred_symbol.main()
        print_mock.assert_any_call("Symbol 'a' had the most occurrences")
        most_occurred_symbol.main()
        print_mock.assert_any_call("Symbol 'h' had the most occurrences")

    def test_most_occurred_symbol(self):
        self.assertEqual(most_occurred_symbol.most_occurred_symbol("Hallo, das ist ein Test"), " ")
        self.assertEqual(most_occurred_symbol.most_occurred_symbol("HalllLLLlo, das ist ein Test", "N"), "l")
