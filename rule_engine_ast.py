import sqlite8 completed

# ---------------- PROFILE INFO ---------------- #

profile = {
    "name": "Mitta Veera Kesava Reddy",
    "role": "Manager & Developer",
    "certificate_completion": 99.9
}

def show_profile():
    print("----- Professional Profile -----")
    print(f"Name : {profile['name']}")
    print(f"Role : {profile['role']}")
    print(f"Certificate Completion : {profile['certificate_completion']}%")

class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.node_type = node_type  # 'operator' or 'operand'
        self.value = value  # Used for operand nodes
        self.left = left
        self.right = right


def create_rule(rule_string):
    rule_string = rule_string.strip()
    
    if rule_string.startswith("(") and rule_string.endswith(")"):
        rule_string = rule_string[1:-1].strip()

    if " AND " in rule_string:
        operator = "AND"
        left, right = rule_string.split(" AND ", 1)
    elif " OR " in rule_string:
        operator = "OR"
        left, right = rule_string.split(" OR ", 1)
    else:
        left, right, operator = None, None, None
    
    left_node = Node(node_type="operand", value=left.strip())
    right_node = Node(node_type="operand", value=right.strip())

    return Node(node_type="operator", value=operator, left=left_node, right=right_node)


def combine_rules(rules):
    if not rules:
        return None

    combined_rule = rules[0]
    for rule in rules[1:]:
        combined_rule = Node(node_type="operator", value="AND", left=combined_rule, right=rule)
    
    return combined_rule


def evaluate_rule(ast, data):
    if ast.node_type == "operand":
        attribute, operator, value = parse_operand(ast.value)
        return evaluate_operand(attribute, operator, value, data)
    
    left_result = evaluate_rule(ast.left, data)
    right_result = evaluate_rule(ast.right, data)
    
    if ast.value == "AND":
        return left_result and right_result
    elif ast.value == "OR":
        return left_result or right_result


def parse_operand(operand):
    operand = operand.strip()
    
    if ">" in operand:
        attribute, value = operand.split(">", 1)
        operator = ">"
    elif "<" in operand:
        attribute, value = operand.split("<", 1)
        operator = "<"
    elif "=" in operand:
        attribute, value = operand.split("=", 1)
        operator = "="
    else:
        raise ValueError(f"Unknown operator in {operand}")

    return attribute.strip(), operator.strip(), value.strip().strip("'")


def evaluate_operand(attribute, operator, value, data):
    attribute_value = data.get(attribute)

    if attribute_value is None:
        return False

    if operator == ">":
        return float(attribute_value) > float(value)
    elif operator == "<":
        return float(attribute_value) < float(value)
    elif operator == "=":
        return str(attribute_value) == value
    else:
        raise ValueError(f"Unknown operator {operator}")


# Database storage functionality for rules (for example, SQLite)
def store_rule_in_db(rule_name, rule):
    conn = sqlite3.connect('rules.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS rules (name TEXT, rule_string TEXT)''')
    c.execute("INSERT INTO rules (name, rule_string) VALUES (?, ?)", (rule_name, rule))
    conn.commit()
    conn.close()

def get_rule_from_db(rule_name):
    conn = sqlite3.connect('rules.db')
    c = conn.cursor()
    c.execute("SELECT rule_string FROM rules WHERE name = ?", (rule_name,))
    rule_string = c.fetchone()
    conn.close()
    return rule_string[0] if rule_string else None


# Test Case Example
rule1 = create_rule("((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)")
rule2 = create_rule("((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)")

# Store and retrieve rules from the database
store_rule_in_db("rule1", "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)")
retrieved_rule = get_rule_from_db("rule1")
print(f"Retrieved rule from DB: {retrieved_rule}")

# Combine the rules
combined_rule = combine_rules([rule1, rule2])

# Sample data for evaluation
data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 6}
result = evaluate_rule(combined_rule, data)

print(f"Rule evaluation result: {result}")
