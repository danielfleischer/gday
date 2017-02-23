#!/usr/bin/python2

from math import floor

#endpoints:
#[
#  [1013, 3, [[0, 170], [1, 22], [2, 224]]],
#  [696, 2, [[0, 7], [1, 50]]],
#  [1114, 3, [[1, 202], [4, 175], [5, 2]]],
#  ...
#]
# latency, number of connected caches, [ [cache, latency], ...]

# requests:
#[
#  [27, 4, 340],
#  [13, 8, 249],
#  ...
#]
# video, endpoint, times

# solution - list of sets (set is a cache server)
def fit(endpoints, requests, solution):
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

        saved_time += saved_latency * times
        total_watches += times

    # average
    return floor(1000.0 * saved_time / total_watches)

if __name__ == '__main__':
    endpoints = [
        [1000, 3, [[0, 100], [1, 300], [2, 200]]],
        [500, 0, []]
    ]
    
    requests = [
        [0, 1, 1000],
        [1, 0, 1000],
        [3, 0, 1500],
        [4, 0, 500]
    ]
    
    solution = [
        set([2]),
        set([1, 3]),
        set([0, 1])
    ]
    
    print fit(endpoints, requests, solution)
    
    endpoints = [
            [1013, 3, [[0, 170], [1, 22], [2, 224]]],
            [696, 2, [[0, 7], [1, 50]]],
            [1114, 3, [[1, 202], [4, 175], [5, 2]]],
            [464, 2, [[1, 24], [8, 25]]],
            [522, 5, [[3, 216], [5, 155], [6, 139], [7, 208], [8, 145]]],
            [321, 4, [[0, 26], [2, 70], [8, 159], [9, 92]]],
            [1288, 2, [[2, 163], [9, 153]]],
            [226, 1, [[7, 86]]],
            [316, 5, [[4, 236], [5, 79], [6, 9], [7, 53], [8, 67]]],
            [365, 5, [[2, 225], [3, 62], [5, 141], [6, 147], [9, 66]]]
        ]
    
    requests = [
        [27, 4, 340],
        [13, 8, 249],
        [1, 1, 449],
        [24, 4, 279],
        [0, 2, 924],
        [8, 4, 862],
        [1, 5, 51],
        [0, 9, 837],
        [30, 9, 927],
        [0, 8, 167],
    ]
    
    solution = [
            [0, [16, 6, 68, 35, 50, 28, 56, 92, 42, 40]],
            [1, [97, 83, 85, 4, 78, 47, 76]],
            [2, [83, 21, 76, 35, 91, 85, 47]],
            [3, [70, 89, 17, 4, 85, 40, 16, 42]],
            [4, [16, 81, 32, 7, 4, 78, 75, 46, 40, 42]],
            [5, [62, 12, 65, 4, 16]],
            [6, [67, 26, 65, 10, 42, 40]],
            [7, [54, 47, 97, 22, 72]],
            [8, [79, 34, 16, 5, 81, 71, 42, 40]],
            [9, [45, 99, 38, 76, 42, 52, 16, 47]]
        ]
    
    print fit(endpoints, requests, solution)
