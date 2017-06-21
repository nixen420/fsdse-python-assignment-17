import operator
dic={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

def solution_asc(dic):
    sorted_x = sorted(dic.items())
    return sorted_x
solution_asc(dic)

def solution_desc(dic):
    return sorted(dic.items(),key=operator.itemgetter(0),reverse=True)
    return sorted_x
solution_desc(dic)
