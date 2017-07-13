# Approach 1
# from itertools import combinations
# from collections import OrderedDict
# print("\n".join(OrderedDict.fromkeys(map(lambda x:" ".join(map(str,x)),
#                                          sorted(map(lambda x: sorted(x),
#                                                     filter(lambda x:sum(x)==0,
#                                                            combinations(map(int, input("").split(' ')), 3))))))))

# Approach 2 - Doesnt do formatting but a console based solution
print(set(filter(lambda x: sum(x) == 0, __import__('itertools').combinations(map(int, input("").split(' ')), 3))))
