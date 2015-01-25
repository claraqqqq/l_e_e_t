# Evaluate Reverse Polish Notation
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
# Some examples:
# 
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for element in tokens:
        	if element not in "+-*/":
        		stack.append(element)
        	else:
        		num2 = int(stack.pop())
        		num1 = int(stack.pop())

        		if element == "+":
        			stack.append(str(num1 + num2))
        		elif element == "-":
        			stack.append(str(num1 - num2))
        		elif element == "*":
        			stack.append(str(num1 * num2))
        		elif element == "/":
        			if num1 * num2 > 0:
        				stack.append(str(num1 / num2))
        			else:
        				stack.append(str(-(abs(num1) / abs(num2))))
        return int(stack[0])



        			  
