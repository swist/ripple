import facebook
import time
import pprint
import re

	
def getFriends(token):
	pp = pprint.PrettyPrinter(indent = 4)
	oauth_access_token  = token


	user_graph = facebook.GraphAPI(oauth_access_token)
	music_likes = tuple(int(item['id']) for item in user_graph.get_connections('me', 'music')['data'])

	music_plays = tuple(int(item['id']) for item in user_graph.get_connections('me', 'music.listens', limit = 250)['data'])

	query = {'friends': 'SELECT page_id, uid FROM page_fan WHERE page_id IN'+str(music_likes)+'AND uid IN (SELECT uid1 FROM friend WHERE uid2=me())',
			 'friends_data': 'SELECT uid, name, pic_big, username FROM user WHERE uid IN (SELECT uid FROM'+'#friends)',
			 'pages_data': 'SELECT name, page_id, pic_big, username FROM page WHERE page_id IN'+str(music_likes) }

	query_results = user_graph.fql(query)

	results = {}

	friends_data = (result for result in query_results if result['name'] == 'friends_data').next()['fql_result_set']
	friends = (result for result in query_results if result['name'] == 'friends').next()['fql_result_set']
	pages_data = (result for result in query_results if result['name'] == 'pages_data').next()['fql_result_set']

	for friend in friends_data:
		likes = [like['page_id'] for like in friends if like['uid'] == friend['uid']]
		friend['likes'] = []
		for like in likes:
			entry = (result for result in pages_data if result['page_id'] == like).next()
			friend['likes'].append(entry)

	return friends_data