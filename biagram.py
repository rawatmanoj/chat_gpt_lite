import torch 
import matplotlib.pyplot as plt

words = open('names.txt').read().splitlines()
biagram_count = {}
min(len(name) for name in words)
look_up_table = sorted(list(set(''.join(words))))
stoi = {y:x+1 for x,y in enumerate(look_up_table)}
stoi['.'] = 0
itos = {y:x for x,y in stoi.items()}
N = torch.zeros((27,27),dtype=torch.int32)
for word in words:
    ch = ['.'] + list(word) + ['.']
    #print(ch)
    for char1,char2 in zip(ch,ch[1:]):
        N[stoi[char1],stoi[char2]] += 1
# plt.imshow(N)
# plt.show()
# print(N[0])
p = N[0].float();
p = p / p.sum();
# print(p)
g = torch.Generator().manual_seed(2147483647)
# res = torch.multinomial(p,num_samples=1,replacement=True,generator=g).item()
# print(res,itos[res],"resss")
P = N.float()
P = P / P.sum(1,keepdim=True)
# print(P,"pppp")
res = []
ix = 0
for i in range(50):
 while True:
    # p = N[ix].float();
    # p = p / p.sum();
    p = P[ix]
    ix = torch.multinomial(p,1,True,generator=g).item()
    res.append(itos[ix]);
    # print(itos[ix])
    if ix == 0:
        break;

# print(P,"pppppp")

for word in words[:3]:
    ch = ['.'] + list(word) + ['.']
    #print(ch)
    for char1,char2 in zip(ch,ch[1:]):
        print(char1,char2)
        ix = stoi[char1]
        iy = stoi[char2]
        print(P[ix,iy])
        N[stoi[char1],stoi[char2]] += 1