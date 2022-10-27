"""
json parsing
"""
import json


def keyword_callback_1(word, field):
    """
    callback print
    """
    print(f"'{word}' is found in '{field}'")


def parse_json(json_str, keyword_callback=keyword_callback_1,
               required_fields=None, keywords=None):
    """
    parse and find words
    """
    json_doc = json.loads(json_str)

    if not required_fields:
        required_fields = []
    if not keywords:
        keywords = []

    for req_field in required_fields:
        if req_field in json_doc:
            for keyword in keywords:
                if keyword in json_doc[req_field]:
                    keyword_callback(keyword, req_field)
