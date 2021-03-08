from instapy import InstaPy

from accCred import JSONToUsername, JSONToPassword


bot_username = JSONToUsername(0).translate({ord(i): None for i in "{'username': '"}).translate({ord(i): None for i in "'}"})
bot_password = JSONToPassword(0).translate({ord(i): None for i in "{'password': '"}).translate({ord(i): None for i in "'}"})


session = InstaPy(username=bot_username, password=bot_password)
session.login()

session.set_skip_users(skip_private=False)

#session.like_by_tags(["space", "nasa"], amount=5)
session.follow_by_list(followlist=['Array_in_a_matrix'], times=1, sleep_delay=600, interact=False)
# session.follow_user_followers(['Array_in_a_matrix'], amount=10, randomize=True, sleep_delay=60)

session.end()
