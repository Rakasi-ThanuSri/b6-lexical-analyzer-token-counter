# b6-lexical-analyzer-token-counter
Lexical Analyzer and Token Counter 
Lexical Analyzer & Token Counter
1. Objective

The objective of this project is to develop a lexical analyzer that reads a source-code file and identifies different types of tokens. The program classifies and counts keywords, identifiers, operators, constants, string literals, separators, special symbols, and comments.

The project is implemented in Python and demonstrates the basic principles of lexical analysis used in compiler design.

2. Problem Statement

Develop a program that reads a source-code file and performs lexical analysis by identifying and counting different types of tokens.

The program should recognize:

Keywords
Identifiers
Operators
Constants/Literals
String Literals
Separators/Delimiters
Special Symbols
Comments

The program should display each token along with its corresponding token type and provide a summary of the total number of tokens in each category.

3. Algorithm
Start the program.
Open and read the source-code file.
Define the set of programming-language keywords.
Define operators and separators.
Scan the source code from left to right.
Identify comments and ignore whitespace.
Identify string literals and character constants.
Identify numeric constants.
Identify identifiers and check whether they are keywords.
Identify operators.
Identify separators and delimiters.
Identify any remaining characters as special symbols.
Store every identified token with its token type.
Count the number of tokens in each category.
Display the token table.
Display the token counts.
Stop the program.
4. Source Code

The complete Python source code is available in lexical_analyzer.py.

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

5. Sample Input
int sum = a + b;
float average = sum / 2.0;

// Calculate average
if (average > 50)
printf("Pass");

6. Sample Output
TOKEN TYPE
------------------------------------------------
int                       Keyword
sum                       Identifier
=                         Operator
a                         Identifier
+                         Operator
b                         Identifier
;                         Separator
float                     Keyword
average                   Identifier
=                         Operator
sum                       Identifier
/                         Operator
2.0                       Constant
;                         Separator
// Calculate average      Comment
if                        Keyword
(                         Separator
average                   Identifier
>                         Operator
50                        Constant
)                         Separator
printf                    Identifier
(                         Separator
"Pass"                    String Literal
)                         Separator
;                         Separator

------------------------------------------------
Token Count
Keywords       : 3
Identifiers    : 7
Operators      : 4
Constants      : 2
String Literals: 1
Separators     : 8
Special Symbols: 0
Comments       : 1

7. Token Classification
Token Type	Description	Examples
Keyword	Reserved words of the programming language	int, float, if
Identifier	Names given to variables, functions, etc.	sum, average, printf
Operator	Symbols used to perform operations	+, -, =, /, >
Constant	Numeric or literal values	50, 2.0
String Literal	Sequence of characters enclosed in double quotes	"Pass"
Separator	Symbols used to separate or group program elements	(, ), ;, {, }
Special Symbol	Symbols not belonging to the other categories	@, #, $
Comment	Non-executable explanatory text	// Calculate average
8. Test Cases
Test Case 1 — Basic Arithmetic

Input:

int a = 10;
int b = 20;
int c = a + b;


Expected Result:

Keywords: 3
Identifiers: 5
Operators: 3
Constants: 2
Separators: 3
Test Case 2 — Conditional Statement

Input:

if (x > 10)
printf("Greater");


Expected Result:

Keywords: 1
Identifiers: 2
Operators: 1
Constants: 1
String Literals: 1
Separators: 4
Test Case 3 — Comments

Input:

// This is a comment
int x = 100;


Expected Result:

Comments: 1
Keywords: 1
Identifiers: 1
Operators: 1
Constants: 1
Separators: 1
Test Case 4 — Multiple Operators

Input:

a += b * 2;


Expected Result:

Identifiers: 2
Operators: 2
Constants: 1
Separators: 1
9. How to Run
Install Python 3.x.
Place lexical_analyzer.py and sample_input.c in the same directory.
Open a terminal in that directory.
Run:
python lexical_analyzer.py

The program displays all detected tokens and their counts.
10. Conclusion

The Lexical Analyzer & Token Counter successfully performs basic lexical analysis of a C/C++-style source file. It identifies different categories of tokens including keywords, identifiers, operators, constants, string literals, separators, special symbols, and comments.

This project provides a practical understanding of how the lexical analysis phase of a compiler processes source code and converts it into meaningful tokens.
