
# coding: utf-8

# In[206]:

import csv
import numpy as np
from random import shuffle, sample, choice
from math import floor


# In[242]:

fname = 'kittens.in'


# In[243]:

ans = open(fname).read().splitlines()


# ## Parameters:

# In[244]:

video_num, endpoint_num, request_num, cache_num, cache_size_limit = map(int, ans[0].split())


# In[245]:

video_sizes = list(enumerate(map(int, ans[1].split())))


# ## Endpoints

# In[246]:

rest = ans[2:]
endpoints = []
point = 0
for endpoint in range(endpoint_num):
    end_latent, num_connected = map(int,rest[point].split())
    caches = []
    for l in range(num_connected):
        caches.append(map(int,rest[point+l+1].split()))
    endpoints.append([end_latent, num_connected, caches])
    point += 1 + num_connected


# ## Requests

# In[247]:

rest = rest[point:]

requests = []
for l in range(request_num):
    requests.append(map(int, rest[l].split()))


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[249]:

def fill_server(capacity, videos):
    curr = 0
    ret = set()
    indices = list(enumerate(videos))
    shuffle(indices)
    for i, size in indices:
        if curr + size > capacity:
            continue
        ret.add(i)
        curr += size
    return ret


# In[250]:

def initial_guess():
    guess = []
    for c in range(cache_num):
        sh = sample(video_sizes, len(video_sizes))
        ans = []
        size = cache_size_limit
        while len(sh) > 0:
            if sh[0][1] < size:
                ans.append(sh[0][0])
                size -= sh[0][1]
            del sh[0]
        guess.append([c,ans])
    return guess


# In[251]:

def mutate(instance):
    cacheToReplace = choice(instance)
    videoToReplace = choice(cacheToReplace[1])
    for l in range(mutateRetry):
        newVid = choice(video_sizes)[1]
        if newVid not in cacheToReplace and newVid != videoToReplace:
            cacheToReplace[1].remove(videoToReplace)
            cacheToReplace[1].append(newVid)
            if sum([l[1] for l in video_sizes]) <= cache_size_limit:
                return 
            cacheToReplace[1].remove(newVid)
            cacheToReplace[1].append(videoToReplace)


# In[252]:

def mate(inst1, inst2):
    cut = int(min(len(inst1), len(inst2))/2.0)
    return inst1[:cut] + inst2[cut:]


# In[254]:

def fit(solution):
    saved_time = 0 # in ms
    total_watches = 0
    
    for video_id, endpoint_id, times in requests:
        endpoint = endpoints[endpoint_id]
        # dc latency
        min_latency = endpoint[0]
        # iterate caches
        for cache, latency in endpoint[2]:
            if video_id in solution[cache]:
                min_latency = min(min_latency, latency)
        
        saved_latency = endpoint[0] - min_latency

#         print 'adding saved time: %i * %i' % (times, saved_latency)
        saved_time += saved_latency * times
#         print 'adding times: %i' % (times, )
        total_watches += times

    # average
    return floor(1000.0 * saved_time / total_watches)


# In[ ]:




# In[ ]:




# In[ ]:




# In[255]:

couples = 20
pop_size = couples**2
generations = 10
mutate_prob = 0.1


# In[240]:

def run_evol():
    pop = [initial_guess() for a in range(pop_size)]
    for gen in range(generations):
#         print pop
        fited = [[p,fit(p)] for i,p in enumerate(pop)]
        fited.sort(key = lambda x: x[1])
        best = fited[:20]
        print fited[0]
        best = [l[0] for l in best]
        new_pop = []
        for a in best:
            for b in best:
                new_pop.append(mate(a,b))
        for i,a in enumerate(new_pop):
            if np.random.rand() < mutate_prob:
                mutate(new_pop[i])
                
        pop = new_pop
        
#     print init


# In[ ]:




# In[241]:

run_evol()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# ## Output

# In[ ]:

def write_out(fout='output.in', cache_list):
    with open(fout, 'w') as f:
        f.write(len(cache_list))

