import os, json
import hashlib
import urllib.request, urllib.parse
root_path = './@Сайт'
d = os.listdir(root_path)

teachers = {}

for f in d:
    print(root_path+'/'+f)
    if os.path.isdir(root_path+'/'+f):
        if not os.path.exists(root_path+'/'+f+'/descr.txt'):
            continue
        teachers[f] = {'Name':'','Photo':{'FileName':'','MD5':''},'Descr':''}
        fDescr = open(root_path+'/'+f+'/descr.txt','r')
        fio = fDescr.readline()
        descr = fDescr.readline()
        teachers[f]['Name'] = fio
        teachers[f]['Descr'] = descr
        teachers[f]['Photo']['FileName'] = root_path+'/'+f+'/фото.jpg'
        teachers[f]['Photo']['MD5'] = hashlib.md5(open(teachers[f]['Photo']['FileName'],'rb').read()).hexdigest()


values = {'Data':json.dumps(teachers),'Command':'UpdateTeachers'}
data = urllib.parse.urlencode(values).encode('utf-8')
print(data)
url='http://127.0.0.1:5000/test'
req = urllib.request.Request(url,data)
f = urllib.request.urlopen(req)
print(f.read())
