import re

class BooleanParser:
    def __init__(self, expression):
        self.expression = expression
        self.tokens = self._tokenize(expression)
        self.pos = 0

    def _tokenize(self, expr):
        token_specification = [
            ('TRUE',    r'\b(?i:true)\b'),
            ('FALSE',   r'\b(?i:false)\b'),
            ('AND',     r'\b(?i:and)\b'),
            ('OR',      r'\b(?i:or)\b'),
            ('NOT',     r'\b(?i:not)\b'),
            ('LPAREN',  r'\('),
            ('RPAREN',  r'\)'),
            ('ID',      r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ('WS',      r'\s+'),
        ]
        tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
        tokens = []
        for mo in re.finditer(tok_regex, expr):
            kind = mo.lastgroup
            value = mo.group()
            if kind != 'WS':
                tokens.append((kind, value))
        return tokens

    def parse(self, env=None):
        self.env = env or {}
        self.pos = 0
        if not self.tokens:
            raise ValueError("Empty expression")
        result = self._expr()
        if self.pos < len(self.tokens):
            raise ValueError("Unexpected extra tokens")
        return result

    def _expr(self):
        # BUG: Evaluates left-to-right without respecting operator precedence.
        val = self._primary()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] in ('AND', 'OR'):
            op = self.tokens[self.pos][0]
            self.pos += 1
            right = self._primary()
            if op == 'AND':
                val = val and right
            elif op == 'OR':
                val = val or right
        return val

    def _primary(self):
        if self.pos >= len(self.tokens):
            raise ValueError("Unexpected end of input")
        kind, val = self.tokens[self.pos]
        if kind == 'NOT':
            self.pos += 1
            return not self._primary()
        elif kind == 'TRUE':
            self.pos += 1
            return True
        elif kind == 'FALSE':
            self.pos += 1
            return False
        elif kind == 'LPAREN':
            self.pos += 1
            res = self._expr()
            if self.pos >= len(self.tokens) or self.tokens[self.pos][0] != 'RPAREN':
                raise ValueError("Unmatched parenthesis")
            self.pos += 1
            return res
        elif kind == 'ID':
            self.pos += 1
            if val not in self.env:
                raise ValueError(f"Undefined variable: {val}")
            return bool(self.env[val])
        else:
            raise ValueError(f"Unexpected token: {val}")