# Rule Engine with Abstract Syntax Tree (AST)

## Objective

This application implements a simple rule engine using Abstract Syntax Trees (AST) to determine user eligibility based on attributes like age, department, income, and more. The system supports dynamic creation, combination, and modification of rules. The rules are represented as ASTs and stored in a database for future retrieval.

## Features

- **AST Representation**: Conditional rules are represented using a tree structure with nodes as operators (AND, OR) and operands (comparisons).
- **Rule Creation**: Create rules dynamically from strings using the `create_rule` function.
- **Rule Combination**: Combine multiple rules using the `combine_rules` function.
- **Rule Evaluation**: Evaluate the combined AST structure against a dictionary of user data.
- **Database Storage**: Rules are stored and retrieved from a SQLite database.
- **Error Handling**: Basic error handling for invalid operators and rule formats.

## Project Structure

- **rule_engine_ast.py**: The main Python script that contains the code for rule creation, combination, evaluation, and storage.
- **rules.db**: SQLite database where the rules are stored.

## Setup Instructions

### Prerequisites

Ensure that you have the following installed:

- Python 3.x
- SQLite (optional, as SQLite comes built-in with Python)
- Required Python packages (can be installed via `pip` if needed)

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone <your-repository-url>
   cd <repository-directory>
