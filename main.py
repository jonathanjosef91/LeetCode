# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def solveA(u, v, V):
    pi = [0] * len(V)
    pi[u] = 1

    for d in V[u:v+1]:
        for w in d.In():
            pi[d] += pi[w]

    return pi[v]


def solveB_wrong(u,v, V):
    res_1 = 0
    res_2 = 0
    # Solve (1)
    for d in V[v:]:
        res_1 += solveA(v, d, V)

    # Solve (2)
    V.swap()    # need to switch .In for all v in V
    for d in V[v::-1]:
        res_2 += solveA(u, d, V[::-1])

    return res_1 * res_2 * solveA(u, v, V)


def solveB_right(u, v, V):
    # Solve (1)
    pi = [0] * len(V)
    pi[v] = 1

    for d in V[v:]:
        for w in d.In():
            pi[d] += pi[w]
    res_1 = sum(V[v:])

    # Solve (2)
    pi = [0] * len(V)
    pi[u] = 1
    V.swap()  # need to switch .In for all v in V
    for d in V[u::-1]:
        for w in d.In():
            pi[d] += pi[w]
    res_2 = sum(V[:u])

    return res_1 * res_2 * solveA(u, v, V)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
