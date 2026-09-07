class Solution:
    def isValid(self, s: str) -> bool:
        lista_stack = []
        if len(s)%2 != 0:
            return False
        for char in s:
            if char == '(' or char == '{' or char =='[':
                lista_stack.append(char)
            elif len(lista_stack) > 0 and (lista_stack[-1] == '(' and char == ')' or lista_stack[-1] == '{' and char == '}' or lista_stack[-1] == '[' and char == ']'):
                lista_stack.pop()
            else:
                return False
        return True if len(lista_stack) == 0 else False
        