import json
from nltk.tree import Tree
from tree_comp import compare_templates
from tree_extract import extract_words

file_path = "rules.json"


def load_rules(file_path):
    rules_json = []
    with open(file_path, 'r') as file:
        rules_json = json.loads(file.read())
    rules = []
    for rule_json in rules_json:
        rule = {}
        rule['if'] = []
        for condition in rule_json['if']:
            rule['if'].append(Tree.fromstring(condition))
        rule['then'] = {}
        vars = {}
        vars_json = rule_json['then']['var']
        for v in vars_json:
            vars[v] = Tree.fromstring(vars_json[v])
        rule['then']['var'] = vars
        rule['then']['answer'] = rule_json['then']['answer']

        rules.append(rule)

    return rules


def handler(sent_tree: Tree, rules: list):
    for rule in rules:
        res = None
        try:
            res = simple_handler(sent_tree, rule)
        except:
            pass
        if type(res) == str:
            return res
    return "Sorry, I don't get it"


def simple_handler(sent_tree: Tree, rule):
    if not (compare_templates(sent_tree, rule['if'])):
        return False

    var = {}

    gen_ans = rule['then']

    for var_name in gen_ans['var']:
        var[var_name] = extract_words(sent_tree, gen_ans['var'][var_name])

    answer_list = []
    for ans_part in gen_ans['answer']:
        if ans_part[0] == "~":
            answer_list.append(var[ans_part[1:]])
        else:
            answer_list.append(ans_part)
    answer = "".join(answer_list)
    answer = answer[0].upper() + answer[1:]
    return answer


