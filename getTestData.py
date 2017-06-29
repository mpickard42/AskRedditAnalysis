import praw
from datetime import datetime
from datetime import timedelta
import pandas as pd
from collections import namedtuple


Submission = namedtuple('Submission', ['score', 'hour', 'weekday', 'title', 'text', 'ofReddit', 'serious'])
data = []
count = 0
reddit = praw.Reddit(client_id='J_n1ci2ZW2Q7AQ', client_secret='ZbzPckEGgWugfD0JtAOFGeV7jLs',
                     user_agent='testscript by /u/SilentButtDeadlies')
subreddit = reddit.subreddit('AskReddit')
for submission in subreddit.submissions(1496275200, 1497916800):  # 1496275200 June 1, 1497916800 June 20
    count += 1
    print count
    hour = datetime.utcfromtimestamp(submission.created_utc).hour
    weekday = datetime.utcfromtimestamp(submission.created_utc).weekday()
    score = submission.score
    title = len(submission.title)
    text = len(submission.selftext)
    if 'of reddit' in submission.title.lower():
        ofReddit = 1
    else:
        ofReddit = 0
    if '[serious]' in submission.title.lower():
        serious = 1
    else:
        serious = 0
    data.append(Submission(score, hour, weekday, title, text, ofReddit, serious))
df = pd.DataFrame(data)
filename = 'AskRedditData' + str(datetime.now()) + '.csv'
df.to_csv(filename, index=False, encoding='utf-8')
# for obj in data:
#     print obj.time
#     print obj.score
#     print obj.title
#     print obj.text
#     print obj.ofReddit
#     print obj.serious
