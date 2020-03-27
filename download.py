
import requests
from threading import Thread
import os
import time
import queue
from concurrent.futures import ThreadPoolExecutor, as_completed



def fetch_img_func(q,path):
    while True:
        try:
            url = q.get_nowait()
            i = q.qsize()
        except Exception as e:
            print (e)
            break
        print("当前还有{}个任务".format(i))
        try:
            res = requests.get(url, headers=headers,stream=True)
            if res.status_code == 200:
                save_img_path =path+'/{}.jpg'.format(i)
                if os.path.exists(save_img_path):
                    print("已存在，跳过")
                    continue
                with open(save_img_path, 'wb') as f:
                    f.write(res.content)
        except Exception:
            q.put(url)
            print("本次失败，已放回")
            if q.qsize()<10:
                break
                print("已退出")

headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}

path = os.getcwd()
try:
    os.mkdir("image")
except BaseException:
    pass


urlpath=path+'\\url\\'
for file in os.listdir(urlpath):
    with open(os.path.join(urlpath,file),'r') as f:
        lines=f.readlines()
        lines=set(lines)
        q=queue.Queue()
        for line in lines:
            q.put(line)
        imagePath=path+'\\image\\'+file[:-4]
        try:
            os.mkdir(imagePath)
        except BaseException:
            path
        num=10
        threads =[]
        for i  in range(num):
            t = Thread(target=fetch_img_func, args=(q,imagePath))
            threads.append(t)
        for t in threads:
            t.start()
        for t in threads:
            t.join()





# lines=set(lines)
# q=queue.Queue()
# for line in lines:
#     q.put(line)




