import re

KEYWORDS = {
    "auto", "break", "case", "char", "const", "continue",
    "default", "do", "double", "else", "enum", "extern",
    "float", "for", "goto", "if", "int", "long",
    "register", "return", "short", "signed", "sizeof",
    "static", "struct", "switch", "typedef", "union",
    "unsigned", "void", "volatile", "while"
}

TOKEN_PATTERN = re.compile(
    r"""
    (?P<COMMENT>//[^\n]*|/\*.*?\*/)
    |(?P<STRING>"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')
    |(?P<NUMBER>\b(?:\d+\.\d+|\d+)\b)
    |(?P<IDENTIFIER>[A-Za-z_][A-Za-z0-9_]*)
    |(?P<OPERATOR>==|!=|<=|>=|\+\+|--|\+=|-=|\*=|/=|&&|\|\||[+\-*/%=<>!&|^~])
    |(?P<SEPARATOR>[(){}\[\];,:])
    |(?P<WHITESPACE>\s+)
    |(?P<SPECIAL>.)
    """,
    re.DOTALL | re.VERBOSE
)


def lexical_analyzer(source_code):
    tokens = []

    for match in TOKEN_PATTERN.finditer(source_code):
        token = match.group()
        token_type = match.lastgroup

        if token_type == "WHITESPACE":
            continue

        if token_type == "COMMENT":
            tokens.append((token, "Comment"))

        elif token_type == "STRING":
            if token.startswith('"'):
                tokens.append((token, "String Literal"))
            else:
                tokens.append((token, "Constant"))

        elif token_type == "NUMBER":
            tokens.append((token, "Constant"))

        elif token_type == "IDENTIFIER":
            if token in KEYWORDS:
                tokens.append((token, "Keyword"))
            else:
                tokens.append((token, "Identifier"))

        elif token_type == "OPERATOR":
            tokens.append((token, "Operator"))

        elif token_type == "SEPARATOR":
            tokens.append((token, "Separator"))

        elif token_type == "SPECIAL":
            tokens.append((token, "Special Symbol"))

    return tokens


def count_tokens(tokens):
    counts = {
        "Keyword": 0,
        "Identifier": 0,
        "Operator": 0,
        "Constant": 0,
        "String Literal": 0,
        "Separator": 0,
        "Special Symbol": 0,
        "Comment": 0
    }

    for _, token_type in tokens:
        counts[token_type] += 1

    return counts


def main():
    filename = "sample_input.c"

    with open(filename, "r") as file:
        source_code = file.read()

    tokens = lexical_analyzer(source_code)
    counts = count_tokens(tokens)

    print("TOKEN TYPE")
    print("-" * 48)

    for token, token_type in tokens:
        print(f"{token:<25} {token_type}")

    print("\n" + "-" * 48)
    print("Token Count")

    print(f"Keywords       : {counts['Keyword']}")
    print(f"Identifiers    : {counts['Identifier']}")
    print(f"Operators      : {counts['Operator']}")
    print(f"Constants      : {counts['Constant']}")
    print(f"String Literals: {counts['String Literal']}")
    print(f"Separators     : {counts['Separator']}")
    print(f"Special Symbols: {counts['Special Symbol']}")
    print(f"Comments       : {counts['Comment']}")


if __name__ == "__main__":
    main()
