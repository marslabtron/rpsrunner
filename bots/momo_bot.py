# http://www.rpscontest.com/entry/320008

import random, math

def highest(v):
    return random.choice([i for i in range(len(v)) if max(v) == v[i]])

def lowest(v):
    return random.choice([i for i in range(len(v)) if min(v) == v[i]])

def best(c):
    return highest([c[1]-c[2], c[2]-c[0], c[0]-c[1]])

def mean(c):
    return sum(c)/length(c)

def beat(c):
    return (c + 2) % 3

def dblbeat(c):
    return (c + 1) % 3

if (input == ""):

        N = 1
        states = ["R","S","P"]
        st = [0,1,2]
        st1 = [1,2,0]
        st2 = [2,0,1]
        sdic = {"R":0, "S":1, "P":2}
        res = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]

        table = {}

        AR1 = .85

        MEM = [3,4,5]

        M = len(MEM) *2
        EX = 2
        MEX = M*EX


        yo = random.choice(st)
        tu = random.choice(st)

        state = [0]*MEX

        model = [1,0.7, 0.5, 0.5]*(M/2)
        prognosis = [random.choice(st) for i in range(MEX)]


        pa = (yo, tu)
        hi = [pa]
else:
        tu = sdic[input]
        pa = (tu,yo)
        hi += [pa]

        for i in MEM:
            if N + 2 > i and i > 0:
                k = tuple(hi[N-i-2:N-2])
                if k in table:
                    table[k] = table[k] + [N-1]
                else:
                    table[k] = [N-1]


        state = [ AR1 * state[i] + model[i]+res[prognosis[i]][tu] for i in range(MEX)]


        J = -EX
        #J += EX; prognosis[J] = 0
        ns = range(N)
        for i in MEM:
            if N > i and i > 0:
                k = tuple(hi[N-i-1:N-1])
                if (k in table):
                    ns = table[k]
            n = max(random.choice(ns), random.choice(ns))
            p = [hi[n][0], hi[n][1]]

            J += EX; prognosis[J] = beat(p[0])
            J += EX; prognosis[J] = dblbeat(p[1])

        J += EX; assert(J==MEX)




        for j in range(M):
           prognosis[j*EX + 1] = beat(prognosis[j*EX])
           #prognosis[j*3 + 2] = (prognosis[j*3] + 1) % 3




best = highest(state)
yo = prognosis[best]
#if random.random() < .3: yo = random.choice(st)
output = states[yo]


N = N + 1
