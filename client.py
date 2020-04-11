import requests as r;
import simplejson as json


def get(board, num, rsp=None):
    if rsp != None:
        rs = r.get('https://cyberland.club/' +board +'/?' +'thread=' +str(rsp) +'&num=' +str(num)).content
    else:
        rs = r.get('https://cyberland.club/' +board +'/?' +'num=' +str(num)).content
    rs = json.loads(rs)
    for f in rs:
        g = '+'
        for i in range(0, len(f['id'])):
            g = g + '-'
        g = g + '+'
        if f['replyTo'] != None and f['replyTo'] != '0':
            z = f['replyTo']
            rlen = len(f['replyTo'])
        else:
            z = '0000'
            rlen = 0
        for i in range(0, len(z) + 2):
            g = g + '-'
        g = g + '+'
        print(g)
        print('|' +f['id'] +'|' +'>>' +z +'|')
        if len(f['content']) >= 200:
            print(g)
            print(f['content'])
            continue;
        for i in range(0, len(f['content']) - len(f['id']) - rlen - 4):
            g = g +'-'
        g = g + '+'
        print(g)
        f['content'] = f['content'].replace('\n', ' ')
        while (len(f['content']) + 2 < len(g)):
            f['content'] = ' ' +f['content']
            if len(f['content']) + 2 < len(g):
                f['content'] = f['content'] +' '
        print('|' +f['content'] +'|')
        g = '+'
        for i in range(0, len(f['content'])):
            g = g + '-'
        print(g + '+')

def post(board, cnt, rto=None):
    if rto!=None:
        dat = {'content':cnt, 'replyTo':rto}
    else:
        dat = {'content':cnt, 'replyTo':None}
    r.post('https://cyberland.club/' +board +'/', data=dat)