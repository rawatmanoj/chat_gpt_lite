from openai import OpenAI
import torch 
import os
from dotenv import load_dotenv

# api_key = os.getenv("OPENAI_API_KEY")
# client = OpenAI(api_key)



# def get_embeddings(chunks):
#     response = client.embeddings.create(
#     input=chunks,
#     model="text-embedding-3-small",
#     )

#     return [x.embedding for x in response.data]

# def chunk(fileData, chunkSize, overlap):
#     # Validate input
#     if overlap >= chunkSize:
#         raise ValueError("overlap must be smaller than chunkSize")

#     chunks = []
#     curr = 0

#     while curr < len(fileData):
#         data = fileData[curr:curr + chunkSize]
#         chunks.append(data)

#         curr += (chunkSize - overlap)

#     return chunks


# Usage
with open('test2.txt') as file:
    fData = file.read()
    # chunks = chunk(file.read(), 200, 50)
    # print(get_embeddings(chunks))

chars = sorted(list(set(fData)))
stoi = {fruit:index for index, fruit in enumerate(chars)}
itos = {index:fruit for index, fruit in enumerate(chars)}
# print(itos)
encode = lambda s: [stoi[c] for c in s ]
decode = lambda l: ''.join([itos[num] for num in l])
# print(decode(encode('manoj')))
data = torch.tensor(encode(fData), dtype=torch.long)
# print(data,len(data))

n = int(0.9*len(data))
train_data = data[:n]
val_data = data[n:]
# print(len(list(set(data))))
block_size = 8

# block_size_data = train_data[:block_size]
# block_size_data_plus = train_data[1:block_size+1]
# for index in range(block_size):
#     print(block_size_data[:index+1],block_size_data_plus[index])

torch.manual_seed(42)

 
block_size = 8
batch_size = 4

def get_batch(split):

    # print(torch.randint(0,7,(4,)))
    ix = torch.randint(0,len(train_data)-block_size,(batch_size,))
    print(ix,"starting index")
    list = [train_data[index:index+block_size] for index in ix]
    list2 = [train_data[index+1:index+block_size+1] for index in ix]
    return list,list2

xb, yb = get_batch('train')
print(torch.stack(xb),'\n',torch.stack(yb))



