import sys, os
from myerror import MyError

def expand_range(state, char_range, exclude = []):
    """Expande um intervalo de caracteres e remove os especificados na lista exclude."""
    transitions = {}
    if '-' in char_range and len(char_range) == 3:
        start, end = char_range.split('-')
        for c in range(ord(start), ord(end) + 1):
            char = chr(c)
            if char not in exclude:
                transitions[char] = state
    else:
        for char in char_range:
            if char not in exclude:
                transitions[char] = state
    return transitions

afd = {
  "q0":{
    " ": "q0",
    "\n": "q0",
    **expand_range("id", "a-z", ["i","e","v","f","w","r"]),
    **expand_range("number", "0-9"),
    "i" : "i",
    "e" : "e",
    "v" : "v",
    "f" : "f",
    "w" : "w",
    "r" : "r",
    "+"	: "+",
    "-"	: "-",
    "*"	: "*",
    "/"	: "/",
    "<"	: "<",
    ">"	: ">",
    "("	: "(",
    ")"	: ")",
    "["	: "[",
    "]"	: "]",
    "{"	: "{",
    "}"	: "}",
    "="	: "=",
    "!"	: "!",
    ";"	: ";",
    ","	: ",",
  },
  "id": {
    **expand_range("id", "a-z"),
    **expand_range("id", "0-9"),
  },
  "number": {
    **expand_range("number", "0-9"),
  },
  "i" : {
    **expand_range("id", "a-z", ["f", "n"]),
    **expand_range("id", "0-9"),
    "f":"if",
    "n": "in",
  },
  "if": {
    **expand_range("id", "a-z"),
    **expand_range("id", "0-9"),
  },
  "in":{
    **expand_range("id", "a-z", ["t"]),
    "t" : "int",
  },
  "int":{
    **expand_range("id", "a-z"),
    **expand_range("id", "0-9"),
  },
  "e" : {
    **expand_range("id", "a-z", ["l"]),
    **expand_range("id", "0-9"),
    "l":"el",
  },
  "el":{
    **expand_range("id", "a-z", ["s"]),
    **expand_range("id", "0-9"),
    "s": "els",
  },
  "els": {
    **expand_range("id", "a-z", ["e"]),
    "e":"else"
  },
  "else": {
    **expand_range("id", "a-z"),
    **expand_range("id", "0-9"),
  },
  "v" : {
    **expand_range("id", "a-z", ["o"]),
    **expand_range("id", "0-9"),
    "o":"vo",
  },
  "vo": {
    **expand_range("id", "a-z", ["i"]),
    **expand_range("id", "0-9"),
    "i":"voi",
  },
  "voi": {
    **expand_range("id", "a-z", ["d"]),
    **expand_range("id", "0-9"),
     "d": "void",
  },
  "void": {
    **expand_range("id", "a-z"),
    **expand_range("id", "0-9"),
  },
  "f" : {
    **expand_range("id", "a-z", ["f"]),
    **expand_range("id", "0-9"),
    "l": "fl",
  },
  "fl": {
    **expand_range("id", "a-z", ["o"]),
    **expand_range("id", "0-9"),
    "o":"flo", 
  },
  "flo":{
    **expand_range("id", "a-z", ["t"]),
    **expand_range("id", "0-9"),
    "a":"floa",
  },
  "floa":{
    **expand_range("id", "a-z", ["t"]),
    **expand_range("id", "0-9"),
    "t":"float",
  },
  "float":{
    **expand_range("id", "a-z"),
    **expand_range("id", "0-9"),
  },
  "w" : {
    **expand_range("id", "a-z", ["h"]),
    **expand_range("id", "0-9"),
    "h":"h",
  },
  "wh": {
    **expand_range("id", "a-z", ["i"]),
    **expand_range("id", "0-9"),
    "i":"whi",
  },
  "whi": {
    **expand_range("id", "a-z", ["l"]),
    **expand_range("id", "0-9"),
    "l":"whil",
  },
  "whil": {
    **expand_range("id", "a-z", ["e"]),
    **expand_range("id", "0-9"),
    "e":"while",
  },
  "while": {
    **expand_range("id", "a-z"),
    **expand_range("id", "0-9"),
  },
  "r" : {
    **expand_range("id", "a-z", ["r"]),
    **expand_range("id", "0-9"),
    "e":"re",
  },
  "re": {
    **expand_range("id", "a-z", ["t"]),
    **expand_range("id", "0-9"),
    "t":"ret",
  },
  "ret": {
    **expand_range("id", "a-z", ["u"]),
    **expand_range("id", "0-9"),
    "u":"retu",
  },
  "retu": {
    **expand_range("id", "a-z", ["r"]),
    **expand_range("id", "0-9"),
    "r":"retur",
  },
  "retur": {
    **expand_range("id", "a-z", ["n"]),
    **expand_range("id", "0-9"),
    "n":"return",
  },
  "return": {
    **expand_range("id", "a-z"),
    **expand_range("id", "0-9"),
  },
  "+"	: {},
  "-"	: {
    **expand_range("number", "0-9"),
  },
  "*"	: {
  },
  "/"	: {
    "/":"comment-//",
    "*": "comment-/*"
  },
  "comment-//":{
    **expand_range("comment-//", "a-z"),
    **expand_range("comment-//", "0-9"),
    "+"	: "comment-//",
    "-"	: "comment-//",
    "*"	: "comment-//",
    "/"	: "comment-//",
    "<"	: "comment-//",
    ">"	: "comment-//",
    "("	: "comment-//",
    ")"	: "comment-//",
    "["	: "comment-//",
    "]"	: "comment-//",
    "{"	: "comment-//",
    "}"	: "comment-//",
    "="	: "comment-//",
    "!"	: "comment-//",
    ";"	: "comment-//",
    ","	: "comment-//",
    " "	: "comment-//",
  },
  "comment-/*":{
    "*"	: "comment-/*-*",
    **expand_range("comment-/*", "a-z"),
    **expand_range("comment-/*", "0-9"),
    "+"	: "comment-/*",
    "-"	: "comment-/*",
    "/"	: "comment-/*",
    "<"	: "comment-/*",
    ">"	: "comment-/*",
    "("	: "comment-/*",
    ")"	: "comment-/*",
    "["	: "comment-/*",
    "]"	: "comment-/*",
    "{"	: "comment-/*",
    "}"	: "comment-/*",
    "="	: "comment-/*",
    "!"	: "comment-/*",
    ";"	: "comment-/*",
    ","	: "comment-/*",
    " "	: "comment-/*",
  },
  "comment-/*-*":{
    "/"	: "comment-/*-*/",
    **expand_range("comment-/*", "a-z"),
    **expand_range("comment-/*", "0-9"),
    "+"	: "comment-/*",
    "-"	: "comment-/*",
    "*"	: "comment-/*",
    "<"	: "comment-/*",
    ">"	: "comment-/*",
    "("	: "comment-/*",
    ")"	: "comment-/*",
    "["	: "comment-/*",
    "]"	: "comment-/*",
    "{"	: "comment-/*",
    "}"	: "comment-/*",
    "="	: "comment-/*",
    "!"	: "comment-/*",
    ";"	: "comment-/*",
    ","	: "comment-/*",
    " "	: "comment-/*",
  },
  "comment-/*-*/":{
  },
  "<"	: {
    "=": "<=",
  },
  ">"	: {
    "=": ">=",
  },
  "("	: {},
  ")"	: {},
  "["	: {},
  "]"	: {},
  "{"	: {},
  "}"	: {},
  "="	: {
    "=": "==",
  },
  "!" : {
    "=": "!=",
  },
  ";"	: {},
  ","	: {},
}

finals = {
  "id": "ID",
  "i": "ID",
  "if": "IF",
  "in": "ID",
  "int": "INT",
  "e": "ID",
  "el": "ID",
  "els": "ID",
  "else":"ELSE",
  "v": "ID",
  "vo": "ID",
  "voi": "ID",
  "void": "VOID",
  "f": "ID",
  "fl": "ID",
  "flo": "ID",
  "floa": "ID",
  "float": "FLOAT",
  "w": "ID",
  "wh": "ID",
  "whi": "ID",
  "whil": "ID",
  "while": "WHILE",
  "r": "ID",
  "re": "ID",
  "ret": "ID",
  "retu": "ID",
  "retur": "ID",
  "return": "RETURN",
  "n": "ID",
  "nu": "ID",
  "num": "ID",
  "numb": "ID",
  "numbe": "ID",
  "number": "NUMBER",
  "+": "PLUS",
  "+": "PLUS",
  "-": "MINUS",
  "*": "TIMES",
  "/": "DIVIDE",
  "<": "LESS",
  "<=": "LESS_EQUAL",
  ">"	: "GREATER",
  ">=": "GREATER_EQUAL",
  "==": "EQUALS",
  "!=": "DIFFERENT",
  "("	: "LPAREN",
  ")"	: "RPAREN",
  "["	: "LBRACKETS",
  "]"	: "RBRACKETS",
  "{"	: "LBRACES",
  "}"	: "RBRACES",
  "="	: "ATTRIBUTION",
  ";"	: "SEMICOLON",
  ","	: "COMMA",
}



error_handler = MyError('LexerErrors')

def main():
  check_cm = False
  check_key = False
  
  for idx, arg in enumerate(sys.argv):
    aux = arg.split('.')
    if aux[-1] == 'cm':
      check_cm = True
      idx_cm = idx

    if(arg == "-k"):
      check_key = True

  if(len(sys.argv) < 3):
    raise TypeError(error_handler.newError(check_key, 'ERR-LEX-USE'))

  if not check_cm:
    raise IOError(error_handler.newError(check_key, 'ERR-LEX-NOT-CM'))
  elif not os.path.exists(sys.argv[idx_cm]):
    raise IOError(error_handler.newError(check_key, 'ERR-LEX-FILE-NOT-EXISTS'))
  else:
    data = open(sys.argv[idx_cm])
    source_file = data.read()

    if not check_cm:
        print("Definição da Máquina")
        print("Estados", afd)
        print("Estados finais e tokes", finals)
        print("Entrada:")
        print(source_file)
      
    state = "q0"
    lexema = ""
    i = 0

    tokens_to_print = []
    while i < len(source_file):
      try:
        #print(state, source_file[i])
        state = afd[state][source_file[i]]
        lexema = lexema + source_file[i]
        i = i + 1
      except:
        if state in finals:
          tokens_to_print.append(finals[state].strip())
          lexema = ''
        state = "q0"
    
    tokens_limpos = [token.replace("\t", "").strip() for token in tokens_to_print]
    print("\n".join(tokens_limpos))

if __name__ == "__main__":
    try:
        main()
    except (ValueError, TypeError) as e:  # Exceções específicas primeiro
        print(e)
    except Exception as e:  # Exceção genérica depois
        print(e)