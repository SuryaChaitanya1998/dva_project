#!/usr/bin/env python3

from zreader import zreader
import ujson as json
import csv

# Adjust chunk_size as necessary -- defaults to 16,384 if not specified
reader = zreader.Zreader("./data_in/2020/RC_2020-03.zst")
csv_writer = csv.writer(open("mbti_comments_new_03.csv", "w", newline='', encoding='utf8'))
# Read each line from the reader
csv_writer.writerow(["author","author_flair_text","author_fullname","subreddit","body"])
count = 0
for line in reader.readlines():
    if count == 1000000:
        break
    obj = json.loads(line)
    if obj["subreddit"]!="mbti":
        continue
    csv_writer.writerow([obj['author'],obj["author_flair_text"],obj["author_fullname"],obj["subreddit"],obj["body"].replace("\n",'').replace("\r","")])
    
    count+=1
print(count)
