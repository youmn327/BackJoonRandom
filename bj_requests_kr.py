import time
import random
import requests
from bs4 import BeautifulSoup
import re
timeout = 5

def korea_full():
    pb_group = []
    cnt = 0 
    p = re.compile('[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]')
    url = "https://www.acmicpc.net/problemset/"
    for i in range(1,240):
        request_return = requests.get(url+str(i))
        soup = BeautifulSoup(request_return.content, "html.parser")
        time.sleep(random.randint(1,3))
        print("+++"*10)
        print(i,"번째")
        print("+++"*10)
        for j in range(1,100):
            try: 
                if p.match(soup.select_one("#problemset > tbody > tr:nth-child("+str(j)+") > td:nth-child(2) > a").getText()) :
                    # code_num = soup.select_one("#problemset > tbody > tr:nth-child("+str(i)+") > td.list_problem_id").getText()
                    # print(code_num,i)
                    print(cnt)
                    cnt+=1
                    print(soup.select_one("#problemset > tbody > tr:nth-child("+str(j)+") > td:nth-child(2) > a").getText())
            except AttributeError :
                break

def grade_korea_full():
    pb_group = []
    cnt = 0 
    p = re.compile('[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]')
    url = "https://www.acmicpc.net/problemset/"
    for i in range(1,240):
        request_return = requests.get(url+str(i))
        soup = BeautifulSoup(request_return.content, "html.parser")
        time.sleep(random.randint(1,3))
        print("+++"*10)
        print(i,"번째")
        print("+++"*10)
        for j in range(1,100):
            try: 
                if p.match(soup.select_one("#problemset > tbody > tr:nth-child("+str(j)+") > td:nth-child(2) > a").getText()) :
                    # code_num = soup.select_one("#problemset > tbody > tr:nth-child("+str(i)+") > td.list_problem_id").getText()
                    # print(code_num,i)
                    print(cnt)
                    cnt+=1
                    print(soup.select_one("#problemset > tbody > tr:nth-child("+str(j)+") > td:nth-child(2) > a").getText())
            except AttributeError :
                break

print(korea_full())