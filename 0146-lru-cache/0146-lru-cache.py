class Node:
    def __init__(self,key=0,val=0):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
       self.cache={}
       self.cap=capacity

       self.right=Node()
       self.left=Node()

       self.right.prev=self.left
       self.left.next=self.right

    def _remove(self, node: Node):
        prev,nxt=node.prev,node.next
        prev.next=nxt
        nxt.prev=prev

    def _insert(self, node):
        prev=self.right.prev
        prev.next=node
        node.prev=prev
        node.next=self.right
        self.right.prev=node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node=self.cache[key]
        self._remove(node)
        self._insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.val=value
            self._remove(node)
            self._insert(node)
            return
        
        node=Node(key,value)
        self.cache[key]=node
        self._insert(node)

        if len(self.cache)>self.cap:
            lru=self.left.next
            self._remove(lru)
            del self.cache[lru.key]

        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)