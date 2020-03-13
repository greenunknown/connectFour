import numpy as np
import collections

def copyQ(q, actionSpace):
    newq = collections.defaultdict(lambda: np.zeros(actionSpace))
    for item in q.items():
        newq[item[0]] = np.copy(item[1])
    return newq


def main():
    actionSpace = 5
    q = collections.defaultdict(lambda: np.zeros(actionSpace))
    q['poop'][2] = 5.0
    print(q['poop'])
    q2 = copyQ(q, actionSpace)
    print(q2['poop'])
    q2['poop'][1] = 9.0
    print(q['poop'])
    print(q2['poop'])

main()