from graph_generator import *
from Dijkstra1 import max_bandwidth_no_heap
from Dijkstra2 import max_bandwidth
from Kruskal import maximum_st_kruskal
import time

print('Brief description: ')
print('graph 1: 5000 vertex, the degree of each node is 6')
print('graph 2: 5000 vertex, the degree of each node is 0.2 * number_of_vertices')
print('algorithm 1: Modified Dijkstra\'s algorithm withour utilizing heap')
print('algorithm 2: Modified Dijkstra\'s algorithm utilizing heap')
print('algorithm 3: Modified Kruskal\'s algorithm utilizing heap')


print('enter \'1\' to randomly generate and test graph 1, including a pair of source and target.')
print('enter \'2\' to randomly generate and test graph 2, including a pair of source and target.')
print('The procedure will automatically apply three algorithm to this graph, and out put  1. Execution time. 2. Verices on the max bandwidth path. 3. Maximum bandwidth')
i=0
while i < 1:
    i += 1
    print('')
    print('please enter your instruction:')
    instruction = input('>>')

    if instruction == '1':
        g1, src1, des1 = graph_generator1()                                     # create graph1
        start_time = time.time()

        path1, max_b1 = max_bandwidth_no_heap(g1, src1, des1)
        print('Modified Dijkstra\'s algorithm without heap data structure takes time: {0} second'.format(time.time()- start_time))
        print('The vertices on the maximum bandwidth path is: ')
        print(path1)
        print('The maximum bandwidth is: ')
        print(max_b1)

        start_time = time.time()
        path2, max_b2 = max_bandwidth(g1, src1, des1)
        print('Modified Dijkstra\'s algorithm with heap data structure takes time: {0} second'.format(time.time() - start_time))
        print('The vertices on the maximum bandwidth path is: ')
        print(path2)
        print('The maximum bandwidth is: ')
        print(max_b2)

        start_time = time.time()
        path3, max_b3 = maximum_st_kruskal(g1, src1, des1)
        print('Modified Kruskal\'s algorithm with heap data structure takes time: {0} second'.format(time.time() - start_time))
        print('The edges in max spanning tree is: ')
        print(path3)
        print('The maximum bandwidth is: ')
        print(max_b3)
    elif instruction == '2':

        g2, src2, des2 = graph_generator2()                                     # create graph1

        start_time = time.time()
        path1, max_b1 = max_bandwidth_no_heap(g2, src2, des2)
        print('Modified Dijkstra\'s algorithm without heap data structure takes time: {0} second'.format(time.time()- start_time))
        print('The vertices on the maximum bandwidth path is: ')
        print(path1)
        print('The maximum bandwidth is: ')
        print(max_b1)

        start_time = time.time()
        path2, max_b2 = max_bandwidth(g2, src2, des2)
        print('Modified Dijkstra\'s algorithm with heap data structure takes time: {0} second'.format(time.time() - start_time))
        print('The vertices on the maximum bandwidth path is: ')
        print(path2)
        print('The maximum bandwidth is: ')
        print(max_b2)

        start_time = time.time()
        path3, max_b3 =maximum_st_kruskal(g2, src2, des2)
        print('Modified Kruskal\'s algorithm with heap data structure takes time: {0} second'.format(time.time() - start_time))
        print('The vertices on the maximum bandwidth path is: ')
        print(path3)
        print('The maximum bandwidth is: ')
        print(max_b3)
    else:
        print('Input error: please enter either 1 or 2')