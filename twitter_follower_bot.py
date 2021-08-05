import tweepy
import time
import random

API_KEY = "XhRXKZ4N6i3Nhv1jopb5HepWy"
API_KEY_SECRET = "cHhbvBuHfPII6AD9wxB6gooof7tMpi1VJH1ibBLPhzfn7R7xeG"
ACCESS_TOKEN = "1396598884751712256-9jNSNI52IJ42XQty31TCA5gTMhQ4KC"
ACCESS_TOKEN_SECRET = "RrH8ObUS9Ret1TIl0AJ29NiCM1RpYpkVrKmD7jxxC4KZ5"

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

	time.sleep(4800) # 80 min

	for user in followed:
		is_following = api.exists_friendship(user, my_id)

		if is_following != 1:
			api.destroy_friendship(user)

	time.sleep(random.randint(15, 30)) # Small delay