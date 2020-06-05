def has_negatives(a):
    """
    YOUR CODE HERE
    """
    pos = list(filter(lambda i: i > 0, a))  # only positive numbers
    neg = list(filter(lambda i: i < 0, a))  # only negative numbers
    positive_count = len(pos)  # count the positives
    negative_count = len(neg)  # count the negatives
    lesser = min([positive_count, negative_count])  # choose the lesser
    check_maps = []
    # no need to check numbers without potential
    if lesser == positive_count:
        check_a = pos
        check_b = neg
    else:
        check_b = pos
        check_a = neg
    # the bitwise complement of our positive/negative pair should return -1
    check_maps = [list(map(lambda b: ~b-a == -1, check_b)) for a in check_a]
    resulting_pairs = list(zip(check_maps, check_a))  # pair results with value
    result = [abs(r[1]) for r in resulting_pairs]  # return happy results
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
