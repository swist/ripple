import requests

class lastAPI(object):
	result = {}
	query = ''


	def __init__(self, q):
        super( lastAPi, self).__init__()
        self.query = q

    def getLastFM(method, query):

	baseURL = "http://ws.audioscrobbler.com/2.0/?method="
	api_key = "&api_key=8717be831cfce83e52144bf79ff1c942&format=json"
	api_secret = '37f4a5667d5b106784a1f0e37a628249'
	r = requests.get(baseURL+method+query+api_key)
	if r.status_code != 200:
		return None
	return r.json

    def searchArtist(self):

    	return selfgetLastFM('artist.search', '&artist='+self.query)