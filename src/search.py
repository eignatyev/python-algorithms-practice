def do_binary_search(list_, value, start_index=0):
    '''
    Returns value's index if it's in the list, otherwise - False

        Constraints:
            The input list is sorted ASC

        Parameters:
            list_ (list): A sorted list of numbers (ASC)
            value (int/float): A number
            start_index (int): Index of the 0th element in the parent list

        Returns:
            value's index (int) if it's in the list, otherwise - False
    '''
    if list_:

        mid_index = len(list_) // 2
        mid_element = list_[mid_index]

        if value == mid_element:
            return start_index + mid_index

        if value < mid_element:
            return do_binary_search(list_[:mid_index], value, start_index)
        return do_binary_search(list_[mid_index + 1:], value, start_index + mid_index + 1)

    return False
