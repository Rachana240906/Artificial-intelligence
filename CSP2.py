from itertools import permutations

letters = ('S','E','N','D','M','O','R','Y')

for p in permutations(range(10), len(letters)):
    S,E,N,D,M,O,R,Y = p

    # Leading digit constraint
    if S == 0 or M == 0:
        continue

    send = 1000*S + 100*E + 10*N + D
    more = 1000*M + 100*O + 10*R + E
    money = 10000*M + 1000*O + 100*N + 10*E + Y

    if send + more == money:
        print(f"SEND={send}, MORE={more}, MONEY={money}")
        break
