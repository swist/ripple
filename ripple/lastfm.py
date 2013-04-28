import requests

class lastAPI(object):
	result = {}
	query = ''


	def __init__(self, q):
        super( lastAPI, self).__init__()
        self.query = q



    def searchArtist(self):

    	result =  selfgetLastFM('artist.search', '&artist='+self.query)
    	self.mbid = result['results']['artistmatches']['artist'][0]['mbid']



