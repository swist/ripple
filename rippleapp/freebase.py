from apiclient.discovery import build
from models import *
import pprint
import pickle


class getFreebaseThing(object):

    DEVELOPER_KEY = "AIzaSyBglmJDi_GL2ZQBO6t-ym9IddElM_6FSo0"
    YOUTUBE_API_SERVICE_NAME = "freebase"
    YOUTUBE_API_VERSION = "v1"
    result_list = []
    result = ''
    freebase = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey = DEVELOPER_KEY)
    query = ''
       
    def __init__(self, q):
        super( getFreebaseThing, self).__init__()
        self.query = q

    def TopicName(self):
        params = {'id' : self.query,
                    'filter': 'suggest'}
        return self.freebase.topic().lookup(**params).execute()['property']['/type/object/name']['values'][0]['value']

    def TopicData(self):
        params = {'id' : self.query,
                'filter': 'suggest'}
        return self.freebase.topic().lookup(**params).execute()










