def remove_duplications(given_list: list):
    seen = set()
    result = []
    for item in given_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result