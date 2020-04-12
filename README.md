A cli client for textboards based on this https://github.com/yur3i/cyberland (originally cyberland.club but it is no longer online)

#Requirements

Python 3.x

requests

simplejson //A soft requirement but I prefer it due to it being faster

#How to use

start the client by opening the client.py in IDLE and running it or by using this command in the folder where the file is located:
```
python3 -i client.py
```

post(board, message, number of the post you're replying to if any, website default is cyberland2.club)

get(board, number of posts, thread if any, website default is cyberland2.club)

The posts are returned in the following format:
```
+-----------+-------------+----------+---------+ 
|Post number|Responding to|Bump count|Timestamp| 
+-----------+-------------+----------+---------+ 
| 		       Content	               | 
+----------------------------------------------+
```

filter(content to be filtered) //This command adds the content to a .filters file or creates it if it doesn't exist

filter_update() //updates the filter, runs automatically when the client is started or filter()is run.
