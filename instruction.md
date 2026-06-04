We have a custom boolean expression parser located in `/app/parser.py`. It works for basic expressions, but it is evaluating operator precedence incorrectly.

Specifically, it treats `AND` and `OR` with equal precedence, parsing expressions strictly from left to right. This breaks standard mathematical/logical operator precedence, where `NOT` takes the highest precedence, followed by `AND`, and finally `OR` (lowest precedence).

For example, the expression:
`True OR False AND False`
should evaluate to `True` (since `False AND False` is computed first, yielding `True OR False`). However, it currently evaluates to `False`.

Please refactor/fix the parser class in `/app/parser.py` so that:
1. Operator precedence matches the standard logical order: `NOT` (highest) > `AND` > `OR` (lowest).
2. Parentheses correctly override standard precedence.
3. Variable substitution continues to work correctly using the environment dictionary argument passed to `.parse(env)`.

Do not modify the class name `BooleanParser` or change its public method signatures (`__init__` and `parse`).