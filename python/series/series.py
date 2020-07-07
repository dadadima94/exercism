def slices(series, length):
    if length <= 0:
        raise ValueError("Length is zero or negative")
    if series == "":
        raise ValueError("Series is empty")
    if length > len(series):
        raise ValueError("lenght of subsequence's element can't be longer than input series")
    else:
        return [series[x:x+length] for x in range(len(series) - length + 1)]
