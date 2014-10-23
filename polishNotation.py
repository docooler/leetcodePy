class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        operation = {}
        operation['/'] = lambda x,y:int(float(x)/y)
        operation['+'] = lambda x,y:x+y
        operation['-'] = lambda x,y:x-y
        operation['*'] = lambda x,y:x*y

        numStack = []
        
        index = 0
        while  index < len(tokens):
            value = tokens[index]
            # print value
            if operation.has_key(value):
                y = numStack.pop()
                x = numStack.pop()
                result = operation[value](x, y)
                numStack.append(result)
                # print "push result" + str(result)
            else:
                numStack.append(int(value))
            index +=1
        return numStack.pop()
