import string



def high(x):
    list_enumerate = dict(i for i in enumerate(string.ascii_lowercase, 1))
    num = 0
    score = []

    for i in x.rsplit():
        for a in i:
            for key, value in list_enumerate.items():
                if value == a:
                    num+= key
        score.append(num)
        num = 0

    return x.rsplit()[score.index(max(score))]

print(high("what time are we climbing up the volcano"))