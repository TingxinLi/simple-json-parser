#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import unittest

from parser import JsonParser, ParseResult, DataType, \
        JsonValue


parser = JsonParser()


class JsonParserTester(unittest.TestCase):

    def test_parse_null(self):
        json_value = JsonValue()
        json_value.v_type = DataType.false
        self.assertEqual(ParseResult.ok,
                parser.parse_json(json_value, 'null'))
        self.assertEqual(DataType.null,
                parser.get_type(json_value))

    def test_parse_true(self):
        json_value = JsonValue()
        json_value.v_type = DataType.false
        self.assertEqual(ParseResult.ok,
                parser.parse_json(json_value, 'true'))
        self.assertEqual(DataType.true,
                parser.get_type(json_value))

    def test_parse_false(self):
        json_value = JsonValue()
        json_value.v_type = DataType.false
        self.assertEqual(ParseResult.ok,
                parser.parse_json(json_value, 'false'))
        self.assertEqual(DataType.false,
                parser.get_type(json_value))

    def test_parse_expect_value(self):
        json_value = JsonValue()

        json_value.v_type = DataType.false
        self.assertEqual(ParseResult.expect_value,
                parser.parse_json(json_value, ''))
        self.assertEqual(DataType.null,
                parser.get_type(json_value))

        json_value.v_type = DataType.false
        self.assertEqual(ParseResult.expect_value,
                parser.parse_json(json_value, ' '))
        self.assertEqual(DataType.null,
                parser.get_type(json_value))

    def test_parse_invalid_value(self):
        json_value = JsonValue()

        json_value.v_type = DataType.false
        self.assertEqual(ParseResult.invalid_value,
                parser.parse_json(json_value, 'nul'))
        self.assertEqual(DataType.null,
                parser.get_type(json_value))

        json_value.v_type = DataType.false
        self.assertEqual(ParseResult.invalid_value,
                parser.parse_json(json_value, '?'))
        self.assertEqual(DataType.null,
                parser.get_type(json_value))

    def test_parse_root_not_singular(self):
        json_value = JsonValue()
        json_value.v_type = DataType.false
        self.assertEqual(ParseResult.root_not_singular,
                parser.parse_json(json_value, 'null x'))
        self.assertEqual(DataType.null,
                parser.get_type(json_value))

        


if __name__ == '__main__':
    unittest.main()
