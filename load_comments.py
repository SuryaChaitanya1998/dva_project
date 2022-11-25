#!/usr/bin/env python3

from zreader import zreader
import ujson as json



# Adjust chunk_size as necessary -- defaults to 16,384 if not specified
reader = zreader.Zreader("./data_in/2020/RC_2020-02.zst")

# Read each line from the reader
print("author","author_flair_text","author_fullname","subreddit","body")
count = 0
for line in reader.readlines():
    if count == 100000:
        break
    obj = json.loads(line)
    if obj["subreddit"]!="mbti":
        continue
    print(obj['author'],obj["author_flair_text"],obj["author_fullname"],obj["subreddit"],obj["body"],sep=",")
    count+=1
print(count)
