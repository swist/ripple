
from apiclient.discovery import build
from models import *
from freebase import *
import pprint
import pickle


class getYouTubeThing(object):

    DEVELOPER_KEY = "AIzaSyBglmJDi_GL2ZQBO6t-ym9IddElM_6FSo0"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    result_list = []
    result = ''
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey = DEVELOPER_KEY)
    query = ''
       
    def __init__(self, q):
        super(getYouTubeThing, self).__init__()
        self.query = q

    def Creator(self):
        ids = ''
        params = {'part':'id,snippet',
                      'type': 'channel'}                      
        params['q'] = self.query
        print params

        for res in self.youtube.search().list(**params).execute()['items']:
            if self.query in res['snippet']['channelTitle']:
                ids+=','+res['snippet']['channelId']

        pp = pprint.PrettyPrinter(indent = 4)
        params = {'part':'id,snippet,contentDetails,statistics,topicDetails',
                  'id': ids}  

        res = self.youtube.channels().list(**params).execute()

        channel = res['items'][0]

        params = {'part':'id,snippet,contentDetails',
                  'id': ids}  

        creator, created = Creator.objects.get_or_create(
            name = self.query, 
            title = channel['snippet']['title'],
            refs = channel)
        print created
        creator.save()


        self.Playlist(channel['contentDetails']['relatedPlaylists']['uploads'])


        for topic in channel['topicDetails']['topicIds']:
            top, created  = Topic.objects.get_or_create(freebase_id = topic, hits = 0, title = getFreebaseThing(topic).TopicName())
            print created
            if created:
                try:
                    top.save()    
                except:
                    pass
            creator.topics.add(top)

        print topics

        for vid in self.result_list:
            creator.videos.add(vid)


        try:
            creator.save()
        except:
            pass

        pp.pprint(channel)

    def Video(self, video_ids):

        params = {
            'part': 'id,snippet,player,topicDetails',
            'id' : video_ids}
        results = self.youtube.videos().list(**params).execute()['items']
        for res in results:
            video, created = Video.objects.get_or_create(
                description = res['snippet']['description'],
                title = res['snippet']['title'],
                refs = res)
            print created, 'video'
        if 'topicDetails' in res:
            for topic in res['topicDetails']['topicIds']:
                print topic
                res_top, created = Topic.objects.get_or_create(freebase_id = topic)

                if created:
                    res_top.title = getFreebaseThing(topic).TopicName()
                    res_top.save()
                video.topics.add(res_top)
                print 'added a topic'



            video.save()
            print 'saved changes to the video'
            self.result_list.append(video)
            print len(self.result_list)


    def Playlist(self, playlist_id):
        next_page_token = ""
        ids = ''
        while next_page_token is not None:
            playlistitems_response = self.youtube.playlistItems().list(
              playlistId=playlist_id,
              part="snippet",
              maxResults=50,
              pageToken=next_page_token
            ).execute()

            for playlist_item in playlistitems_response["items"]:
                self.Video(playlist_item["snippet"]["resourceId"]["videoId"])
                
            print len(self.result_list)

            try:
                next_page_token = playlistitems_response['nextPageToken']
            except:
                next_page_token = None
        return ids











