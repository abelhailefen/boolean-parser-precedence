We have a custom expression parser in the file `/app/parser.py`. This parser works fine for expressions. However it has a problem with the order of operations for the `AND` and `OR` operators.

The parser treats `. And `OR` as if they have the same importance. This means it evaluates expressions from left to right. This is not how it should work. In mathematics and logic `NOT` is the important then comes `AND` and finally `OR` is the least important.

Let us take an example. The expression `OR False AND False` should be `True`. This is because `False AND False` is evaluated first which results in `True OR False`. Currently the parser says it is `False`.

We need to fix the parser class in `/app/parser.py`. Here are the things that need to be done:

1. The parser should follow the order, for the operators: `NOT` is the most important, then `AND` and `OR` is the least important.

2. When we use parentheses they should override the order of operations.

3. The parser should still be able to substitute variables correctly using the environment dictionary that is passed to the `parse` method of the `BooleanParser` class.

We should not change the name of the `BooleanParser` class. Also we should not change the way the public methods `__init__` and `parse` work.