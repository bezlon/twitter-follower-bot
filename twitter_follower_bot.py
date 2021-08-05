import tweepy
import time
import random

API_KEY = "YOURS_HERE"
API_KEY_SECRET = "YOURS_HERE"
ACCESS_TOKEN = "YOURS_HERE"
ACCESS_TOKEN_SECRET = "YOURS_HERE"

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
my_id = api.me().id

locked_on_user = api.get_user("elonmusk")
followers_list = locked_on_user.followers()

while True:
	followed = []

	for user in followers_list:
		api.create_friendship(user.id)
		followed.append(user.id)
		time.sleep(random.randint(1, 2))

	time.sleep(4800) # 80 min

	for user in followed:
		is_following = api.exists_friendship(user, my_id)

		if is_following != 1:
			api.destroy_friendship(user)
			time.sleep(random.randint(1, 2))

	time.sleep(random.randint(15, 30)) # Small delay
