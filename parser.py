#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import enum
from functools import partial

import lazy_object_proxy

whitespace = ('\s', '\t', '\n', '\r')


@enum.unique
class DataType(enum.Enum):

    null = '_null'
    true = '_true'
    false = '_false'
    num = '_decimal'
    string = '_string'
    array = '_array'
    obj = '_obj'


@enum.unique
class ParseResult(enum.IntEnum):

    ok = 0
    except_value = 10
    invalid_value = 20
    root_not_singular = 30


class JsonValue(object):

    v_type = None


class ParserContext(object):

    def __init__(self, json):
        self.json = json 
        self.pos = 0

        # result parts are saved as a list of <JsonValue>
        self.result = []

    @property
    def current_char(self):
        if self.pos < len(self.json):
            return self.json[self.pos]

    def current_n_char_till_end(self, n):
        upper_limit = self.pos + n if self.pos + n < \
                len(self.json) else len(self.json)-1
        return self.json[self.pos: upper_limit]


class JsonParser(object):

    def parse_json(self, json_value, json):
        # Not allown imput args as None 
        assert(json_value is not None)
        assert(json is not None)
        json_value.v_type = DataType.null
        parser_context = ParserContext(json)
        self.parse_whitespace(parser_context)
        return self.parse_value(parser_context, json_value)

    def parse_value(self, parser_context, json_value):
        # NOTE: Should parse_whitespace move here??
        print("current_char is:")
        print(parser_context.current_char)
        parser_dict = {
            None: ParseResult.ok,
            'n': self.parse_null(parser_context, json_value),
            't': self.parse_true(parser_context, json_value),
            'f': self.parse_false(parser_context, json_value),
            # TODO: More here 
        }
        return parser_dict.get(parser_context.current_char,
                ParseResult.invalid_value)
    
    @lazy_object_proxy.Proxy
    def parse_whitespace(self, parser_context):
        """
        white_space = (%x20 / %x09 / %x0A / %x0D) 

        """
        while(parser_context.current_char in whitespace):
            parser_context.pos += 1

    @lazy_object_proxy.Proxy
    def parse_null(self, parser_context, json_value):
        """
        null = "null"

        """
        assert(parser_context.current_char=='n')
        if parser_context.current_n_char_till_end(4) != 'null':
            return ParseResult.invalid_value
        parser_context.pos += 4
        json_value.v_type = DataType.null
        return ParseResult.ok

    @lazy_object_proxy.Proxy
    def parse_true(self, parser_context, json_value):
        """
        true = "true"

        """
        assert(parser_context.current_char=='t')
        if parser_context.current_n_char_till_end(4) != 'true':
            return ParseResult.invalid_value
        parser_context.pos += 4
        json_value.v_type = DataType.true
        return ParseResult.ok

    @lazy_object_proxy.Proxy
    def parse_false(self, parser_context, json_value):
        """
        false = "false"

        """
        assert(parser_context.current_char=='f')
        if parser_context.current_n_char_till_end(5) != 'false':
            return ParseResult.invalid_value
        parser_context.pos += 5 
        json_value.v_type = DataType.false
        return ParseResult.ok
    
    @staticmethod
    def get_type(json_value):
        return json_value.v_type 
