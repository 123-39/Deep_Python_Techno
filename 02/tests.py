""" parser function tests """
import json
import random
import unittest
from unittest.mock import patch
from faker import Faker
from parse import keyword_callback_1, parse_json


def json_creating(dict_size=10):
    """
    Fake json creating
    """
    fake = Faker()

    json_dict = {'name': [fake.name() for _ in range(dict_size)],
                 'adress': [fake.address() for _ in range(dict_size)],
                 'date_of_birth': [fake.date() for _ in range(dict_size)],
                 'credit_card_number': [fake.credit_card_number()
                                        for _ in range(dict_size)]}
    return json_dict


class TestParser(unittest.TestCase):
    """
    Implementation of the parse function tests
    """

    @patch('parse.keyword_callback_1')
    def test_1_key_1_word_callback(self, callback_func):
        """
        One key one keyword callback test
        """
        json_dict = json_creating(dict_size=20)
        required_fields = ["name"]
        keywords = [json_dict.get('name')[1]]

        parse_json(json.dumps(json_dict), callback_func,
                   required_fields, keywords)
        self.assertEqual(callback_func.call_count, 1)

    @patch('parse.keyword_callback_1')
    def test_2_key_1_word_callback(self, callback_func):
        """
        Two key one keyword callback test
        """
        json_dict = json_creating(dict_size=20)
        json_dict['ex_name'] = json_dict['name']
        required_fields = ["name", "ex_name"]
        keywords = [json_dict.get('name')[1]]

        parse_json(json.dumps(json_dict), callback_func,
                   required_fields, keywords)

        self.assertEqual(callback_func.call_count, 2)

    @patch('parse.keyword_callback_1')
    def test_1_key_1_word_zero_callback(self, callback_func):
        """
        One key one keyword zero callback test
        """
        json_dict = json_creating(dict_size=5)
        required_fields = ["adress"]
        keywords = [json_dict.get('name')[1]]

        parse_json(json.dumps(json_dict), callback_func,
                   required_fields, keywords)
        self.assertEqual(callback_func.call_count, 0)

    @patch('parse.keyword_callback_1')
    def test_check_faker_callback(self, callback_func):
        """
        Faker generation callback test
        """
        numb_key = 30
        numb_val = 20

        json_dict = json_creating(dict_size=10)

        req_fields_ = list(set([random.choice(list(json_dict))
                                for _ in range(numb_key)]))
        keywords_ = list(set(sum([[random.choice(json_dict[req_fields_[i]])
                                  for _ in range(numb_val)]
                                 for i in range(len(req_fields_))], [])))

        parse_json(json.dumps(json_dict), callback_func,
                   req_fields_, keywords_)
        self.assertEqual(len(keywords_), callback_func.call_count)

    @patch('parse.keyword_callback_1')
    def test_check_faker_zero_callback(self, callback_func):
        """
        Zero key zero keyword zero callback test
        """
        json_dict = json_creating(dict_size=10)
        parse_json(json.dumps(json_dict), callback_func)
        self.assertEqual(callback_func.call_count, 0)

    @patch('builtins.print')
    def test_print(self, mock_print):
        """
        Print callback test
        """
        json_str = '{"key1": "word1 word2", "key2": "word2 word3"}'
        req_fields = ["key1"]
        keywords = ["word2"]

        parse_json(json_str, keyword_callback_1,
                   req_fields, keywords)

        output = f"'{keywords[-1]}' is found in '{req_fields[-1]}'"
        mock_print.assert_called_with(output)


if __name__ == "__main__":

    unittest.main()
