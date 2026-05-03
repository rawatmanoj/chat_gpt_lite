import torch 

words = open('names.txt').read().splitlines()
biagram_count = {}
min(len(name) for name in words)
look_up_table = sorted(list(set(''.join(words))))
stoi = {y:x for x,y in enumerate(look_up_table)}
stoi['<S>'] = 26
stoi['<E>'] = 27
print(stoi)
for word in words:
    ch = ['<S>'] + list(word) + ['<E>']
    for char1,char2 in zip(ch,ch[1:]):
        biagram_count[(char1,char2)] = biagram_count.get((char1,char2),0) + 1
N = torch.zeros((28,28),dtype=torch.int32)
# print(biagram_count)
# print(sorted(biagram_count.items(),key = lambda x:x[1],reverse=True))