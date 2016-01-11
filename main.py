from datetime import timedelta
import datetime
import urllib2
import os

url_head = 'http://7xng3o.com2.z0.glb.qiniucdn.com/_log/staticbk/'
date = datetime.date.today()

def download(file, file_name):
    data = file.read()
    if not os.path.isdir('./tmp'):
        os.mkdir('./tmp')
    print "Download\t" + file_name
    with open("tmp/" + file_name, "wb") as code:
        code.write(data)

def set():
    for b in range(1, 500):
        time = date - timedelta(days=b)
        if time > datetime.date(2015, 10, 9):
            for i in range(0, 20):
                file_url = '%s/part%d.gz' % (str(time), i)
                file_name = '%s-part%d.gz' % (str(time), i)
                url = url_head + file_url
                if not os.path.isfile('./tmp/'+file_name):
                    try:
                        file = urllib2.urlopen(url)
                    except urllib2.URLError, e:
                        break
                    download(file, file_name)

if __name__ == '__main__':
    set()