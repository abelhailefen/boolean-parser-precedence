import pytest
import sys
sys.path.append('/app')
from parser import BooleanParser

def test_basic_evaluation():
    assert BooleanParser("True").parse() is True
    assert BooleanParser("False").parse() is False
    assert BooleanParser("NOT True").parse() is False
    assert BooleanParser("NOT False").parse() is True

def test_and_operations():
    assert BooleanParser("True AND True").parse() is True
    assert BooleanParser("True AND False").parse() is False
    assert BooleanParser("False AND True").parse() is False
    assert BooleanParser("False AND False").parse() is False

def test_or_operations():
    assert BooleanParser("True OR True").parse() is True
    assert BooleanParser("True OR False").parse() is True
    assert BooleanParser("False OR True").parse() is True
    assert BooleanParser("False OR False").parse() is False

def test_operator_precedence():
    # Buggy parser treats AND and OR with equal precedence, evaluating left-to-right.
    # "True OR False AND False" should parse as "True OR (False AND False)" -> True
    assert BooleanParser("True OR False AND False").parse() is True
    assert BooleanParser("False AND False OR True").parse() is True

def test_parentheses():
    assert BooleanParser("(True OR False) AND False").parse() is False
    assert BooleanParser("NOT (True AND False)").parse() is True
    assert BooleanParser("((True))").parse() is True

def test_variables():
    env = {"x": True, "y": False}
    assert BooleanParser("x AND NOT y").parse(env) is True
    assert BooleanParser("x OR y").parse(env) is True

def test_syntax_errors():
    with pytest.raises(ValueError):
        BooleanParser("True AND").parse()
    with pytest.raises(ValueError):
        BooleanParser("(True AND False").parse()
    with pytest.raises(ValueError):
        BooleanParser("").parse()
    with pytest.raises(ValueError):
        BooleanParser("True True").parse()