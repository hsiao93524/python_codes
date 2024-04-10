
# load width and height of card to N, amount of picking number to K
N, K = list(map(int, input().split(" ")))
# load card
card = [] # card in 1D format
idx_bingo = []
for i in range(N):
    row = list(map(int, input().split(" ")))
    card += row
# load picking number
num_bingo = list(map(int, input().split(" ")))

# get picking number's index on card
for e in num_bingo:
    if e in card:
        idx_bingo.append(card.index(e))
idx_bingo.append(card.index(0))
idx_bingo.sort()

# generate all bingo lines with index list
rows = [[i*N+j for j in range(0, N)] for i in range(0, N)]
cols = [[j*N+i for j in range(0, N)] for i in range(0, N)]
diags = [[i*N+i for i in range(0, N)], [i*N+N-1-i for i in range(0, N)]]
idx_lines = rows + cols + diags

# check_bingo
counter = 0
for line in idx_lines:
    if sum([idx in line for idx in idx_bingo]) == N:
        counter += 1

# print result
print(counter)