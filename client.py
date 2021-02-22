from nltk.parse.corenlp import CoreNLPParser
from nltk.tree import Tree
from rules_handler import load_rules, handler

parser = CoreNLPParser(url='http://localhost:9000')


def get_tree(sent: str) -> Tree:
    return next(parser.raw_parse(sent))


def get_response(request, rules):
    tree = get_tree(request)
    response = handler(tree, rules)
    return response


if __name__ == '__main__':

    rules = load_rules("rules2.json")

    # request = "Where can Dan buy a ticket?"
    # print("You: ", request)
    # response = get_response(request, rules)
    # print("Bot: ", response)
    #
    # request = "How much does the ticket cost?"
    # print("You: ", request)
    # response = get_response(request, rules)
    # print("Bot: ", response)
    #
    request = "How can the boy get to the library?"
    print("You: ", request)
    response = get_response(request, rules)
    print("Bot: ", response)

    request = "I want to order a hot dog."
    print("You: ", request)
    response = get_response(request, rules)
    print("Bot: ", response)
    #
    # request = "Where to get tickets to Kyiv?"
    # print("You: ", request)
    # response = get_response(request, rules)
    # print("Bot: ", response)


    while True:
        request = input("You: ")
        if request == "q":
            break
        tree = get_tree(request)
        response = handler(tree, rules)
        print("Bot: ", response)
