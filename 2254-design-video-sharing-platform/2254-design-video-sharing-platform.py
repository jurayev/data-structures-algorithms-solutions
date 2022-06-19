class VideoMeta:
    def __init__(self, id, content):
        self.id = id
        self.content = content
        self.views = 0
        self.likes = 0
        self.dislikes = 0


class VideoSharingPlatform:

    def __init__(self):
        self.videos = {}
        self.next_id = 0
        self.used_ids = []

    def upload(self, video: str) -> int:
        video_id = self.get_id()
        self.videos[video_id] = VideoMeta(video_id, video)
        return video_id

    def remove(self, videoId: int) -> None:
        if self.exist(videoId):
            del self.videos[videoId]
            heappush(self.used_ids, videoId)

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if self.exist(videoId):
            video = self.videos[videoId]
            video.views += 1
            endMinute = min(endMinute, len(video.content) - 1)
            return video.content[startMinute:endMinute+1]
        return "-1"
    
    def like(self, videoId: int) -> None:
        if self.exist(videoId):
            self.videos[videoId].likes += 1

    def dislike(self, videoId: int) -> None:
        if self.exist(videoId):
            self.videos[videoId].dislikes += 1

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        if self.exist(videoId):
            video = self.videos[videoId]
            return [video.likes, video.dislikes]
        return [-1]

    def getViews(self, videoId: int) -> int:
        if self.exist(videoId):
            video = self.videos[videoId]
            return video.views
        return -1
    
    def exist(self, videoId: int) -> bool:
        return videoId in self.videos
    
    def get_id(self):
        if self.used_ids:
            min_id = heappop(self.used_ids)
            return min_id
        self.next_id += 1
        return self.next_id - 1
        


# Your VideoSharingPlatform object will be instantiated and called as such:
# obj = VideoSharingPlatform()
# param_1 = obj.upload(video)
# obj.remove(videoId)
# param_3 = obj.watch(videoId,startMinute,endMinute)
# obj.like(videoId)
# obj.dislike(videoId)
# param_6 = obj.getLikesAndDislikes(videoId)
# param_7 = obj.getViews(videoId)