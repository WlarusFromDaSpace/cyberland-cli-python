import requests as r;
try:
    import simplejson as json
except:
    import json

def get(board, num, rsp=None, website='cyberland2.club/'):
    rs = r.get('https://' +website +board, params={'thread':rsp, 'num':num}).content
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
        for i in range(0, len(f['bumpCount'])):
            g = g + '-'
        g = g + '+'
        for i in range(0, len(f['time'])):
            g = g +'-'
        g = g + '+'
        print(g)
        print('|' +f['id'] +'|' +'>>' +z +'|' +f['bumpCount'] +'|' +f['time'] +'|')
        if len(f['content']) >= 300:
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

def post(board, cnt, rto=None, website='cyberland2.club'):
    if rto!=None:
        dat = {'content':cnt, 'replyTo':rto}
    else:
        dat = {'content':cnt, 'replyTo':None}
    r.post('https://' +website +'/' +board +'/', data=dat)
