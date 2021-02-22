from nltk.parse.corenlp import CoreNLPParser
from nltk.tree import Tree
from rules_handler import load_rules, handler

parser = CoreNLPParser(url='http://localhost:9000')


def get_tree(sent: str) -> Tree:
    """Return a tree from the lexical parser."""
    return next(parser.raw_parse(sent))


def get_response(request: str, rules: str) -> str:
    """Return a response from the request due to rules."""
    tree = get_tree(request)
    response = handler(tree, rules)
    return response


if __name__ == '__main__':

    rules = load_rules("rules.json")

    while True:
        request = input("You: ")
        if request == "q":
            break
        tree = get_tree(request)
        response = handler(tree, rules)
        print("Bot: ", response)
