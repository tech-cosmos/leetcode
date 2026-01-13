import heapq
from collections import defaultdict 
class Twitter:

    def __init__(self):
        self.tweets=defaultdict(list)
        self.time=0
        self.follows=defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        heapq.heappush(self.tweets[userId],(self.time,tweetId))
        # if len(self.tweets[userId])>10:
            # heapq.heappop(self.tweets[userId])

    def getNewsFeed(self, userId: int) -> List[int]:
        heap=[]
        users=set(self.follows[userId])
        users.add(userId)
        
        def push_latest(u):
            arr = self.tweets[u]
            if arr:
                idx=len(arr)-1
                t,tid=arr[idx]
                heapq.heappush(heap, (-t, tid, u, idx))
        def push_prev(u, i):
            idx=i-1
            if idx>=0:
                t,tid=self.tweets[u][idx]
                heapq.heappush(heap, (-t, tid, u, idx))
        
        for u in users:
            push_latest(u)
        
        res=[]
        while heap and len(res)<10:
            _,tid,u,idx=heapq.heappop(heap)
            res.append(tid)
            push_prev(u, idx)

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)