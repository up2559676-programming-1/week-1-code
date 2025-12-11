import unittest
from unittest.mock import patch
from io import StringIO
from pract1 import (
    say_name,
    say_hello_2,
    dollars_to_pounds,
    sum_and_difference,
    change_counter,
    ten_hellos,
    zoom,
    count_to,
    count_from_to,
    weights_table,
    future_value,
)


class Tests(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_say_name(self, mock_stdout):
        say_name()
        output = mock_stdout.getvalue()
        self.assertEqual(output, "Oliver\n")

    @patch("sys.stdout", new_callable=StringIO)
    def test_say_hello_2(self, mock_stdout):
        say_hello_2()
        output = mock_stdout.getvalue()
        self.assertEqual(output, "hello\nworld\n")

    @patch("builtins.input", return_value="10")
    @patch("sys.stdout", new_callable=StringIO)
    def test_dollars_to_pounds(self, mock_stdout, mock_input):
        dollars_to_pounds()
        output = mock_stdout.getvalue()
        self.assertIn("Pounds:", output)

    @patch("builtins.input", side_effect=["3", "5"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_sum_and_difference(self, mock_stdout, mock_input):
        sum_and_difference()
        output = mock_stdout.getvalue()
        self.assertIn("Sum: 8.0", output)
        self.assertIn("Diff: -2.0", output)

    @patch("builtins.input", side_effect=["1", "2", "3"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_change_counter(self, mock_stdout, mock_input):
        change_counter()
        output = mock_stdout.getvalue()
        self.assertIn("Total: 6p", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_ten_hellos(self, mock_stdout):
        ten_hellos()
        output = mock_stdout.getvalue()
        self.assertEqual(output.strip(), ("Hello World\n" * 10).strip())

    @patch("builtins.input", return_value="3")
    @patch("sys.stdout", new_callable=StringIO)
    def test_zoom(self, mock_stdout, mock_input):
        zoom()
        output = mock_stdout.getvalue()
        self.assertIn("zoom 1", output)
        self.assertIn("zoom 2", output)
        self.assertIn("zoom 3", output)

    @patch("builtins.input", return_value="3")
    @patch("sys.stdout", new_callable=StringIO)
    def test_count_to(self, mock_stdout, mock_input):
        count_to()
        output = mock_stdout.getvalue()
        self.assertIn("1", output)
        self.assertIn("2", output)
        self.assertIn("3", output)

    @patch("builtins.input", side_effect=["3", "6"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_count_from_to(self, mock_stdout, mock_input):
        count_from_to()
        output = mock_stdout.getvalue()
        self.assertIn("3", output)
        self.assertIn("4", output)
        self.assertIn("5", output)
        self.assertIn("6", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_weights_table(self, mock_stdout):
        weights_table()
        output = mock_stdout.getvalue()
        self.assertIn("Kg", output)
        self.assertIn("Oz", output)

    @patch("builtins.input", side_effect=["1000", "5"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_future_value(self, mock_stdout, mock_input):
        future_value()
        output = mock_stdout.getvalue()
        self.assertIn("Amount after 5 years", output)


if __name__ == "__main__":
    unittest.main()
