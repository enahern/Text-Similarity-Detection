import os

def find_paragraphs(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        
    paragraphs = text.split('\n\n')  
    p_list = []
    for p in paragraphs:
        if p.strip():
            p_list.append(p.strip())
    
    return p_list
# os.chdir('/drive/data/')
# print(os.getcwd()) 
file_path = '/Users/emilyahern/Documents/Sophomore Year/Big Data Analytics/similarity.txt'  

parag = find_paragraphs(file_path)
# print(len(parag))


import re

def create_shingles(paragraphs, k):
    shingle_sets = []

    #splitting the paragraphs into a set of words
    for para in paragraphs:
        just_words = re.sub(r'[^\w\s]', '', para.lower())
        words = just_words.split() 
        shingles = set()

        # creating the shingles
        for i in range(len(words) - k + 1):
            shingle = tuple(words[i:i + k])  
            shingles.add(shingle)

        shingle_sets.append(shingles)

    return shingle_sets
shin = create_shingles(parag,5)
# print(shin)
# print(len(shin))

def assign_num(set_name):
    dword = {}
    numlst = []
    for para in set_name:
        tmplst = []
        for words in para:
            if words in dword:
                tmplst += [dword[words]]
            else:
                dword[words] = len(dword) + 1
                tmplst += [dword[words]]
        numlst += [tmplst]
    return numlst

anum = assign_num(shin)
# print(anum)

def find_max(lst):
    maxlst = []
    for i in lst:
        maxlst += [max(i)]
    return max(maxlst)
max_l = find_max(anum)
# print(max_l)
def bit_vector(num_lst):
    vec = []
    for para in num_lst:
        v1 = []
        for i in range(1, find_max(num_lst)+1):
            if i in para:
                v1.append(1)
            else:
                v1.append(0)
        vec.append(v1)
    return vec
bvec = bit_vector(assign_num(create_shingles(find_paragraphs(file_path),5)))
# print(len(bvec))
# print(bvec)
import random as rn

def rand_perm(max_num):
    lstofperm = []
    i = 0
    while i < 100:
        perm1 = list(range(1,max_num+1))
        rn.shuffle(perm1)
        if perm1 not in lstofperm:
            lstofperm +=[perm1.copy()]
            i +=1
        
    return lstofperm
ranper = rand_perm(find_max(assign_num(create_shingles(find_paragraphs(file_path),5))))
# print(len(ranper))
# print(ranper)

def signature(rand_perm, bit_v):
    sig = []
    for bit in bit_v:
        lst = []
        for perm in rand_perm:
            for num in perm:
                if bit[num-1] == 1:
                    lst += [num]
                    break
        sig += [lst]
    return sig
s =  signature(ranper,bvec)                 

def jaccard(x,y):
    return len(x.intersection(y))/ len(x.union(y))

def splitv(sig, b):
    row = int(len(sig)/b)
    spv = []
    for i in range(0,len(sig), row):
        spv += [sig[i:i+ row]]
    return spv

spl_v_fin = []
for i in s:
    spl_v_fin += [splitv(i, 20)]

import hashlib
def hashband(band):
    return hashlib.md5(str(band).encode('utf-8')).hexdigest()
buckets = {}
for i, para in enumerate(spl_v_fin):
    for j, bin in enumerate(para):
        hb = hashband(bin)
        spl_v_fin[i][j] = hb
        if hb not in buckets:
            buckets[hb] = []
        buckets[hb].append(i)



from itertools import combinations
c = set()
for b in buckets.values():
    if len(b) > 1:
        for pair in combinations(b,2):
            c.add(pair)


sim = []
for p1,p2 in c:
    sim.append([(p1,p2),jaccard(set(shin[p1]),set(shin[p2]))])
high2low = sorted(sim, key=lambda x: x[1], reverse=True)
print(high2low[0:5])


for i in high2low[0:5]:
    print((parag[i[0][0]]))
    print((parag[i[0][1]]))


