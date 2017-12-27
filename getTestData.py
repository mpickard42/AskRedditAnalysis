import praw
from datetime import datetime
from datetime import timedelta
import pandas as pd
from collections import namedtuple

def addSubmission(submission):
    hour = datetime.utcfromtimestamp(submission.created_utc).hour
    weekday = datetime.utcfromtimestamp(submission.created_utc).weekday()  # 0 = Monday
    score = submission.score
    if score < 20:
        score = 0
    elif score < 100:
        score = 1
    else:
        score = 2
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
    
    
Submission = namedtuple('Submission', ['score', 'hour', 'weekday', 'title', 'text', 'ofReddit', 'serious'])
data = []
count = 0
reddit = praw.Reddit(client_id='J_n1ci2ZW2Q7AQ', client_secret='ZbzPckEGgWugfD0JtAOFGeV7jLs',
                     user_agent='testscript by /u/USERNAME')
subreddit = reddit.subreddit('AskReddit')
# for submission in subreddit.submissions(1496075200, 1496575200):  # 1496075200 May 29, 1496575200 June 4
#     count += 1
#     print count
#     addSubmission(submission)
for submission in subreddit.submissions(1485907200, 1496575200):  # 1485907200 Feb 1, 1486512000 Feb 8
    count += 1
    print count
    addSubmission(submission)
for submission in subreddit.top('month', limit=900): 
    count += 1
    print count
    addSubmission(submission)
for submission in subreddit.top('all', limit=900): 
    count += 1
    print count
    addSubmission(submission)
df = pd.DataFrame(data)
filename = 'AskRedditData.csv'
df.to_csv(filename, index=False, encoding='utf-8')
# for obj in data:
#     print obj.time
#     print obj.score
#     print obj.title
#     print obj.text
#     print obj.ofReddit
#     print obj.serious
