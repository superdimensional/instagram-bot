from instapy import InstaPy

session = InstaPy(username="tt6965914", password="QeeDzfHMPmZf2g4")
session.login()

session.set_skip_users(skip_private=False)

#session.like_by_tags(["space", "nasa"], amount=5)
session.follow_by_list(followlist=['Array_in_a_matrix'], times=1, sleep_delay=600, interact=False)
session.follow_user_followers(['Array_in_a_matrix'], amount=10, randomize=True, sleep_delay=60)
session.end()
