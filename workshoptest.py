def get_strong_word(w1, w2):
    words1 = list(w1)
    words2 = list(w2)

    value1 = 0
    for i in words1:
        value1 += ord(i)

    value2 = 0
    for j in words2:
        value2 += ord(j)

    if value1 > value2:
        return w1
    elif value1 < value2:
        return w2
    else:
        return (w1, w2)


print(get_strong_word('delilah', 'dixon'))
