N = list(map(int,list(input())))

N_length = len(N)

if sum(N[:N_length//2]) == sum(N[N_length//2:]):
    print("LUCKY")
else:
    print("READY")