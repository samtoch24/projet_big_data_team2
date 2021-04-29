from matplotlib import pyplot as plt
import csv

file = "presidential_state_toplines_2020.csv"
x = []
with open(file, newline='\n') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        # x.append(', '.join(row))
        x.append(row)

nom = ["Trump", "Biden"]
etat = []
winstate_inc = 0
winstate_chal = 0
for i in range(1,  len(x)):
    etat.append(x[i][7])
    winstate_inc = winstate_inc + float(x[i][10])
    winstate_chal = winstate_chal + float(x[i][11])
    vote_inc = winstate_inc + float(x[i][13])
    vote_chal = winstate_chal + float(x[i][14])

v = [winstate_inc, winstate_chal]
vo= [vote_inc,vote_chal]
print(x[0])
#print(winstate_inc)
#plt.hist(winstate_inc, bins=6, range = (1,8000))
#plt.hist(winstate_chal, bins=6, range = (1,8000))
print("Trump : ", winstate_inc)
print("Biden : ", winstate_chal)

plt.figure(figsize=(12,10))
plt.hist(vo)

plt.show()
#plt.plot(nom, v, '*')
#plt.plot(nom, vo)
#plt.show()