"""
"""
from collections import deque


def bfs_two_water_jug(jugOneCap, jugTwoCap, target):
    def fillJugOne(jugState):
        jugOne, jugTwo = jugState
        return (jugOneCap, jugTwo)

    def fillJugTwo(jugState):
        jugOne, jugTwo = jugState
        return (jugOne, jugTwoCap)

    def emptyJugOne(jugState):
        jugOne, jugTwo = jugState
        return (0, jugTwo)

    def emptyJugTwo(jugState):
        jugOne, jugTwo = jugState
        return (jugOne, 0)

    def pourJugOne2Two(jugState):
        jugOne, jugTwo = jugState
        delta = min(jugOne, jugTwoCap-jugTwo)
        return (jugOne - delta, jugTwo + delta)

    def pourJugTwo2One(jugState):
        jugOne, jugTwo = jugState
        delta = min(jugOneCap-jugOne, jugTwo)
        return (jugOne + delta, jugTwo - delta)

    # initialisation
    initialState = (0,0)
    targetStates = [(0, target), (target, 0)]
    seen = set()
    queue = deque([initialState])
    operations = [fillJugOne, fillJugTwo, emptyJugOne, emptyJugTwo,
                  pourJugOne2Two, pourJugTwo2One]

    # run bfs in search space
    seen.add(initialState)
    while queue:
        jugState = queue.popleft()

        print(jugState)

        if jugState in targetStates:
            print("Found")
            return

        for nextState in [operation(jugState) for operation in operations]:
            if nextState in seen: continue
            queue.append(nextState)
            seen.add(nextState)

    else:
        print("Not Found")

    return


if __name__ == '__main__':
    bfs_two_water_jug(4, 3, 2)