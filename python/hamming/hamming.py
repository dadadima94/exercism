def distance(strand_a, strand_b):
    if (len(strand_a) != len(strand_b) and (strand_a or strand_b)):
        raise ValueError("The two DNA strands have different lengths.")
    else:
        return sum(j != k for j, k in zip(strand_a, strand_b))
