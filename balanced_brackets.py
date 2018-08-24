# Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
#
# For example, given the string "([])[]({})", you should return true.
#
# Given the string "([)]" or "((()", you should return false.


# assumes that only bracket characters will be passed in
def balanced_brackets(s):
    open_brackets = []
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}',
    }
    for char in s:
        if char in brackets:
            open_brackets.append(char)
        else:
            currently_open_bracket = open_brackets.pop()
            if brackets[currently_open_bracket] != char:
                return False
    if open_brackets:
        return False
    return True
