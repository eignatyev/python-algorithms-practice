""" Given a string S, the task is to output a string with the first
letter of every word in the string """
def get_first_letters_as_string(string):
    '''
    Returns first letters of every word as a string with no whitespaces

        Constraints:
            input string contains words separated with single whitespaces

        Parameters:
            string (str): a string of words separated with single whitespaces

        Returns:
            (str)
    '''
    if not isinstance(string, str):
        raise TypeError('"string" parameter is not of str type')

    return ''.join([w[0] for w in string.split()])

""" Given a string, verify if brackets in this string are properly nested and balanced """
def is_brackets_balanced(string):
    '''
    Returns True if brackets in the string are properly nested and balanced, otherwise - False

        Parameters:
            string (str): a string with or without 3 types of brackets - {}, [], ()

        Returns:
            (bool)
    '''

    if not isinstance(string, str):
        raise TypeError('"string" parameter is not of str type')

    open_brackets = ['(', '[', '{']
    close_brackets = [')', ']', '}']
    open_brackets_history = []

    for c in string:

        if c in open_brackets:
            open_brackets_history.append(c)

        elif c in close_brackets:
            if not open_brackets_history or any([
                c == ')' and open_brackets_history[-1] != '(',
                c == ']' and open_brackets_history[-1] != '[',
                c == '}' and open_brackets_history[-1] != '{'
            ]):
                return False
            else:
                open_brackets_history.pop()

    return not open_brackets_history
