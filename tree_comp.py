from nltk.tree import Tree


def compare_templates(tree: Tree, templates: list):
    for template in templates:
        if compare_step(tree, template):
            return True
    return False


def compare_step(tree: Tree, template: Tree) -> bool:
    if template == '*':
        return True
    if type(template) != str and template.label() == '*':
        res_star = True
        for temp_node in template:
            res_star = res_star and compare_star_step(tree, temp_node)
        return res_star
    if type(tree) == str or type(template) == str:
        if tree == template:
            return True
        return False
    if tree.label() != template.label():
        return False
    else:
        res = False
        for t_node in template:
            nodes = get_node_by_label(tree, t_node)
            if nodes == []:
                return False
            for node in nodes:
                if compare_step(node, t_node):
                    return True
            return False
        return res


def get_node_by_label(tree: Tree, template: Tree):
    res_list = []
    if type(template) == str:
        return tree
    if template.label() == "*":
        return tree
    label = template.label()
    for node in tree:
        if type(node) != str:
            if node.label() == label:
                res_list.append(node)
    return res_list


def compare_star_step(tree: Tree, template: Tree) -> bool:
    if type(tree) == str:
        return tree == template
    res = compare_step(tree, template)
    if res == True:
        return True
    for node in tree:
        if compare_star_step(node, template):
            return True
    return False

