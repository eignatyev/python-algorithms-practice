"""Given a string S, the task is to output a string with the first
letter of every word in the string."""
def get_first_letters_as_string(S):
    return ''.join([w[0] for w in S.split()])
