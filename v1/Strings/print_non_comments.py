# http://www.careercup.com/question?id=4849108141473792
# Implement a method called printNonComments() which prints out a extract of text with comments removed. 

# For example, the input: 
# hello /* this is a 
# multi line comment */ all 

# Should produce: 
# hello 
# all 

# You have access to a method called getNextLine() which returns the next line in the input string

PRINT = 0
NO_PRINT = 1
def print_non_comment(lines):
   _state = PRINT
   
   for line in lines:
       to_print = ""
       i = 0
       while i < len(line):
           if _state == PRINT:
               if line[i] == '/' and i < len(line) - 1 and line[i + 1] == '*':
                  _state = NO_PRINT
                  i += 1 # this handles the scenario for /*/
               else:
                  to_print = to_print + line[i] #TODO use stringbuffer
           else:
               if line[i] == '*' and i < len(line) - 1 and line[i + 1] == '/':
                   _state = PRINT
                   i += 1 # this handles the scenario for /*/
           i += 1
                   
       print to_print



print_non_comment(["hello /* this is a", "multi line comment */ all"])