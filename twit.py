#this file to use for the twittwer api
#for overflow treshold
#here because the limit is 100 followers we sleep for 60 IF THE LIMIT IS BIGGER INCREASE THE SLEEP
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(60)

def is_empty(list1):
	return len(list1) == 0

######main functions#######
if __name__ == "__main__":
	import os
	import tweepy
	import time 
	from tweepy import OAuthHandler

	consumer_key = 'aApOB3l2zG8jXkgBFlV5TxazT'
	consumer_secret = 'aSXNh35mMcPiJguXpsog7NAc7NhqHHeGPRspOPJmB46bOcxOMe'
	access_token = '835163872621379584-qxBHRQAFIOuTLqxdEkdd0tneEpKOO5a'
	access_secret =  'vv5eVnziIJy3S1hjERSENOkGcdxlP3sOSrNpbzVmzTuyt'
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	api = tweepy.API(auth)

	#empty list with ids of the followers of the user1
	ids1 = []
	fol1 = []

	#empty list with ids of the followers of the user2
	ids2 = []
	fol2 = []

	#read fron input the names
	name1 = raw_input('Enter first twit user:')
	name2 = raw_input('Enter second twit user:')

	#get the user isntances
	user1 = api.get_user(screen_name = name1)
	user2 = api.get_user(screen_name = name2)

	###########################################
	#get followers for the user1 (ids)
	for item in limit_handled(tweepy.Cursor(api.followers_ids, screen_name = name1).items()):
	    ids1.append(item)

	#get the names for user1
	if len(ids1) !=0:
		fol1 = [user.screen_name for user in api.lookup_users(user_ids = ids1)]

		#print the followers of user1
		print "The FOLLOWERS of User1 with name ",user1.screen_name," are:"
		for name1 in fol1:
			print name1
	else:
		print "The user2 with name",user2.screen_name,"hasnt any followers"
	############################################

	print "\n"

	#############################################
	#get followers for the user2 (ids)
	for item in limit_handled(tweepy.Cursor(api.followers_ids, screen_name = name2).items()):
	    ids2.append(item)

	#get the names for user1
	if len(ids2) != 0:
		fol2 = [user.screen_name for user in api.lookup_users(user_ids = ids2)]

		#print the followers of user1
		print "The FOLLOWERS of User2 with name",user2.screen_name,"are :"
		for name2 in fol2:
			print name2
	else:
		print "The user2 with name",user2.screen_name,"hasnt any followers"
	#############################################
	
	print "\n"

	#now lets check tha same followers
	if len(ids1) == 0 or len(ids2) == 0:
		print "The 2 users havent same followers"
	
	else:
		count = 0
		for name1 in fol1:
			for name2 in fol2:
				if name1 == name2:
					count += 1
					print "The 2 users have the same follower with name,",name1

		if count == 0:
			print "The 2 users havent same followers"
		else:
			print "The total same followers are = ",count
