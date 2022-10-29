#!/usr/bin/env python3

from zreader import zreader
import ujson as json



# Adjust chunk_size as necessary -- defaults to 16,384 if not specified
reader = zreader.Zreader("./data_in/RS_2019-04.zst")

# Read each line from the reader
print("author","author_flair_text","author_fullname","num_comments","subreddit","selftext",",")
count = 0
for line in reader.readlines():
    if count == 100000:
        break
    obj = json.loads(line)
    print(obj['author'],obj["author_flair_text"],obj["author_fullname"],obj["num_comments"],obj["subreddit"],obj["selftext"],sep=",")
    count+=1
