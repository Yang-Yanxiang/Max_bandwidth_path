from heapPriorityQueue import HeapPriorityQueue

class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    
    class Locator(HeapPriorityQueue._Item):
        __slots__ = '_index'

        def __init__(self, k, v, j):
            super().__init__(k, v)
            self._index = j
        
    def _swap(self, i, j):
        super()._swap(i,j)
        self._data[i]._index = i
        self._data[j]._index = j

    def _bubble(self, j):
        if j > 0 and self._data[j] > self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    def add(self, key, value):
        token = self.Locator(key, value, len(self._data))
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token

    def update(self, loc, newkey, newval):
        j = loc._index
        if not (0 <= j< len(self) and self._data[j] is loc):
            raise ValueError('Invalid locator')
        loc._key = newkey
        loc._value = newval
        self._bubble(j)

    def remove(self, loc):
        j = loc._index
        if not (0<=j<len(self) and self._data[j] is loc):
            raise ValueError('Invalid locator')
        if j == len(self)-1:
            self._data.pop()
        else:
            self._swap(j, len(self) -1)
            self._data.pop()
            self._bubble(j)
        return(loc._key, loc._value)

