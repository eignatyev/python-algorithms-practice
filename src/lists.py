def flatten_list(list_):
    '''
    Returns a 1-dimension list

        Parameters:
            list_ (list): A possibly nested list with any items

        Returns:
            (list) flattened list
    '''
    if not isinstance(list_, list):
        raise TypeError(f'The "list_" parameter is not of list type. Value: "{list_}"')

    result = []
    [result.extend(flatten_list(e)) if isinstance(e, list) else result.append(e) for e in list_]
    return result
