# Simple example of parsing
# Bartosz Sawicki, 2014-03-13

#from scanner import *
from parser_sulej import *
from lexer_sulej import *

f = open("compose.yaml", "r")
input_string = f.read()
f.close()
print(input_string)
lexer = Lexer(input_string)
for token in lexer.tokens:
  print(token)

parser = Parser(lexer)
parser.start()
  
