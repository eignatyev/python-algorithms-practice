def flatten_list(list_):
    '''
    Returns a 1-dimension list

        Parameters:
            list_ (list): A possibly nested list with any items

        Returns:
            (list) flattened list
    '''
    result = []
    [result.extend(flatten_list(e)) if isinstance(e, list) else result.append(e) for e in list_]
    return result

""" Given a list and a number x, check for pair in list with sum as x """
class FindPairAlgorithms():

    @staticmethod
    def iteration(list_, number):

        for i, n1 in enumerate(list_[:-1]):
            for j, n2 in enumerate(list_[i + 1:]):
                if number == n1 + n2:
                    return n1, n2
        return False

    @staticmethod
    def two_pointer(list_, number):

        list_.sort()  # The list should be sorted for the 2-pointer technique
        l, r = 0, len(list_) - 1

        while l < r:
            if list_[l] + list_[r] == number:  # If the sum is equal, the solution is found
                return list_[l], list_[r]
            if list_[l] + list_[r] < number:  # Increment the left pointer if the sum is smaller
                l += 1
            else:  # Decrement the right pointer if the sum is smaller
                r -= 1
        return False

