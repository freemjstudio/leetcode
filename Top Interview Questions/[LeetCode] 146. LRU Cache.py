# https://leetcode.com/problems/lru-cache/?envType=study-plan-v2&envId=top-interview-150


class Node:
    def __init__(self, key=0, value=0):
        self.key, self.value = key, value
        self.prev = self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.__capacity = capacity # minimum capacity
        self.__cache = {} # Dictionary Type for O(1)
        self.left, self.right = Node(), Node()
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        last = self.right.prev
        last.next = node
        node.next = self.right
        node.prev = last
        self.right.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.__cache: # check the key in the cache
            # Delete the exist Node
            self.remove(self.__cache[key])
            # Insert the new Node
            self.insert(self.__cache[key])
            return self.__cache[key].value

        return -1  # If the key doesn't exist

    def put(self, key: int, value: int) -> None:
        # check the key
        if key in self.__cache:
            self.remove(self.__cache[key]) # remove if already exists
        self.__cache[key] = Node(key, value) # Node 생성하기
        self.insert(self.__cache[key])

        # capacity check
        if len(self.__cache) > self.__capacity:
            # 삭제하기
            LRU = self.left.next # ?
            self.remove(LRU)
            del self.__cache[LRU.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)