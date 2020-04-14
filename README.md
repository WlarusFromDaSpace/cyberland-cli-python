A cli client for textboards based on https://github.com/yur3i/cyberland (originally cyberland.club but it is no longer online)

#Requirements

Python 3.x

requests

simplejson //A soft requirement but I prefer it due to it being faster

viu //A soft requirement, viu is used for ansiposting and without viu you can't ansipost

neofetch //Soft requirement, it is used for posting your fethces

#How to use

start the client by opening the client.py in IDLE and running it or by using this command in the folder where the file is located:
```
python3 -i client.py
```

post(board, message, number of the post you're replying to if any, website default is cyberland2.club)

get(board, number of posts, offset, thread if any, website, default is cyberland2.club)

The posts are returned in the following format:
```
+-----------+-------------+----------+---------+ 
|Post number|Responding to|Bump count|Timestamp| 
+-----------+-------------+----------+---------+ 
| 		       Content	               | 
+----------------------------------------------+
```

filter(content to be filtered) //This command adds the content to a .filters file or creates it if it doesn't exist

Filtered posts are shown as follows

```
### (number of posts) filtered ###
```

filter_update() //updates the filter, runs automatically when the client is started or filter()is run.

To see filtered posts just write filters to the CLI

ansipost(path to file) //Converts an imagefile to ANSI and posts it to /i/. Smaller images, like 50x50, are preferred. Size limit is 350000 bytes.

neofetch(board, message) //Allows you to post your neofetch to different boards
