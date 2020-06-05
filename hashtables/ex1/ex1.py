def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    if length < 2:
        return None
    weight_sums = list(
        map(lambda x: list(map(lambda y: x+y, weights)), weights))
    have_limit = list(
        map(lambda z: limit in weight_sums[z], range(length)))
    indices = [i[1] for i in list(zip(have_limit, range(limit))) if i[0]]
    return sorted(indices, reverse=True)
