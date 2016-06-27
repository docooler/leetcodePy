class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweetId2UserId = {}
        self.followList     = {}
        self.tweetList      = []
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweetList.insert(0, tweetId)
        self.tweetId2UserId[tweetId] = userId
        self.follow(userId,userId)
        
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        Cnt = 0
        result = []
        if self.followList.has_key(userId):
            fList = self.followList[userId]
        else:
            return []
            
       
        for tweetId in self.tweetList:
            userId = self.tweetId2UserId[tweetId]
            if Cnt >= 10:
                return result
            if userId in fList:
                result.append(tweetId)
                Cnt += 1
                
        return result
                
            
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        fList = []
        if self.followList.has_key(followerId):
            fList =  self.followList[followerId]
        else:
            fList = []
        if followeeId not in fList:
            fList.append(followeeId)
        self.followList[followerId] = fList

        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        #self always follow self
        if followerId == followeeId:
            return 
        fList = []
        if self.followList.has_key(followerId):
            fList =  self.followList[followerId]
        else:
            return
        if followeeId in fList:
            fList.remove(followeeId)
        self.followList[followerId] = fList
        
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
