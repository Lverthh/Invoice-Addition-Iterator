import itertools

# Add all invoices here
inv = []
# Add the objective pay here
pay = 0


res = []
i_temp = [round(i * 100) for i in inv]
p_temp = round(pay * 100)
r_temp = [seq for i in range(len(i_temp), 0, -1)
          for seq in itertools.combinations(i_temp, i) if sum(seq) == p_temp]
for t in r_temp:
    res.append(list(t))
for i in range(len(res)):
    for j in range(len(res[i])):
        res[i][j] = (res[i][j]) / 100
print(sum(i_temp) / 100)
print(res)
