# import heapq
# import sys

# input = sys.stdin.readline

# def dijkstra_heap(s,edge):
#     #始点sから各頂点への最短距離
#     d = [10**20] * n
#     used = [True] * n #True:未確定
#     d[s] = 0
#     used[s] = False
#     edgelist = []
#     for a,b in edge[s]:
#         heapq.heappush(edgelist,a*(10**6)+b)
#     while len(edgelist):
#         minedge = heapq.heappop(edgelist)
#         #まだ使われてない頂点の中から最小の距離のものを探す
#         if not used[minedge%(10**6)]:
#             continue
#         v = minedge%(10**6)
#         d[v] = minedge//(10**6)
#         used[v] = False
#         for e in edge[v]:
#             if used[e[1]]:
#                 heapq.heappush(edgelist,(e[0]+d[v])*(10**6)+e[1])
#     return d
# #########################
# n,w = map(int,input().split())

# edge = [[] for i in range(n)]
# #隣接リスト edge[i]:[コスト,行先]
# for i in range(w):
#     x,y,z = map(int,input().split())
#     edge[x].append([z,y])
#     edge[y].append([z,x])
# print(prim_heap())