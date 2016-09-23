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

#    def test_parse_expect_value(self):
#        json_value = JsonValue()
#        json_value.v_type = 


if __name__ == '__main__':
    unittest.main()
