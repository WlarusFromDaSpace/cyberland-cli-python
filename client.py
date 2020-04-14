import requests as r;
try:
    import simplejson as json
except:
    import json
from subprocess import run, PIPE

filters = []

def filter(cnt):
    file = open('.filters', 'a+')
    file.write(cnt +'\n')
    file.close()
    filter_update()

def filter_update():
    global filters
    try:
        file = open('.filters', 'r')
    except FileNotFoundError:
        file = open('.filters', 'a+')
        file.close()
        file = open('.filters', 'r')
    filters = [line.rstrip() for line in file]
    file.close()


def get(board, num, ofs=None, rsp=None, website='cyberland2.club'):
    rs = r.get('https://' +website +'/' +board, params={'thread':rsp, 'num':num, 'offset':ofs}).content
    rs = json.loads(rs)
    rs = rs[::-1]
    filtered = 0
    for f in rs:
        for i in f:
            if f[i] != str:
                f[i] = str(f[i])
        if website != 'landcyber.herokuapp.com' and f['bumpCount'] == None:
            bmpC = '0'
        elif website == 'landcyber.herokuapp.com':
            bmpC = '#'
        else:
            bmpC = f['bumpCount']
        if f['time'] == None:
            f['time'] = '0'
        if(f['content'] in filters and f['id'] != str(rsp)):
            filtered = filtered + 1
            continue;
        g = '+'
        for i in range(0, len(f['id'])):
            g = g + '-'
        g = g + '+'
        if f['replyTo'] != None and f['replyTo'] != '0':
            z = f['replyTo']
        else:
            z = '0000'
        for i in range(0, len(z) + 2):
            g = g + '-'
        g = g + '+'
        for i in range(0, len(bmpC)):
            g = g + '-'
        g = g + '+'
        for i in range(0, len(f['time'])):
            g = g +'-'
        g = g + '+'
        print(g)
        print('|' +f['id'] +'|' +'>>' +z +'|' +bmpC +'|' +f['time'] +'|')
        if len(f['content']) >= 200:
            print(g)
            print(f['content'])
            continue;
        f['content'] = f['content'].replace('\n', ' ')
        f['content'] = f['content'].replace('\r', '')
        for i in range(0, len(f['content'])):
            g = g + '-'
        g = g + '+'
        print(g)
        while (len(f['content']) < len(g) - 2):
            f['content'] = ' ' +f['content']
            if len(f['content']) < len(g) - 2:
                f['content'] = f['content'] +' '
        print('|' +f['content'] +'|')
        g = '+'
        for i in range(0, len(f['content'])):
            g = g + '-'
        print(g + '+')
    if website == 'landcyber.herokuapp.com':
        print('### landcyber does not return bumpCount and as such they are shown as "#" ###')
    print('### ' +str(filtered) +' posts filtered ###')

def post(board, cnt, rto=None, website='cyberland2.club'):
    r.post('https://' +website +'/' +board +'/', data={'content':cnt, 'replyTo':rto})
    get(board, 2, website=website)

def ansipost(imgfile, msg='', rsp=None, website='cyberland2.club'):
    try:
        img = run(['viu', imgfile], stdout=PIPE, universal_newlines=True)
        if (len(img.stdout.encode('utf-8')) > 350000):
            print('### Image size exceeds the maximum byte size of 350000, it will not be posted ###')
            return;
        post('i', msg +'\n' +img.stdout, rsp, website)
    except FileNotFoundError:
        print('### Viu does not appear to be in your PATH ###')

def neofetch(board='i', msg='', rto=None, website='cyberland2.club'):
    fetch = run('neofetch', stdout=PIPE, universal_newlines=True)
    post(board, msg +'\n' +fetch.stdout, rto, website)

if __name__ == '__main__':
    filter_update()
