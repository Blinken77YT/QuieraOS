import regex as re

def lexer(contents):
    lines = contents.split('\n')
    for line in lines:
        chars = list(line)
        tokens = []
        temp_str = ""
        quote_count = 0
        for char in chars:
            if char == '"' or char == "'":
                quote_count += 1
            if quote_count % 2 == 0:
                in_quotes = False
            else:
                in_quotes = True

            if char == " " and in_quotes == False:
                tokens.append(temp_str)
                temp_str = ""
            else:
                temp_str += char 

        tokens.append(temp_str)
        items = []
        for token in tokens:
            if token[0] == '"' or token[0] == "'":
                if token[-1] == '"' or token[-1] == "'":
                    items.append(("string", token))
                else:
                    break
            elif re.match(r"[.a-zA-Z]+", token):
                items.append(("symbol", token))
            elif token in "+-*/":
                items.append(("expresion", token))
            elif re.match(r"[.0-9]+", token):
                items.append(("number", token))

        if items and items[0][0] == 'symbol' and items[0][1] == 'echo':
            if items[1][0] == 'string':
                string = items[1][1]
                string = string[1:-1]
                print(string)

        if items and items[0][0] == 'symbol' and items[0][1] == 'input':
            user_input = input("Enter your input: ")
            items.append(("input", user_input))

        print(items)

def parse(file):
    contents = open(file, "r").read()
    tokens = lexer(contents)
    return tokens