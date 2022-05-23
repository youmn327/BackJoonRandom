from urllib.request import Request, urlopen
import time
import random
import requests
from bs4 import BeautifulSoup
import re
import sys
input = sys.stdin.readline

def grade_korea_full():
    pb_group = []
    p = re.compile('[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]')
    front_url = "https://www.acmicpc.net/problemset?sort=no_asc&solvedac_option=xz%2Cxn&tier="
    grad = ["2C1%2C2%2C3%2C4%2C5%","2C6%2C7%2C8%2C9%2C10%","2C11%2C12%2C13%2C14%2C15%","2C16%2C17%2C18%2C19%2C20%2C21%","2C22%2C23%2C24%2C25%2C26%","2C27%2C28%2C29%2C30%2C31%"]
    url_str = ""
    
    T_W = list(map(int,input().split()))
    T_W_temp = T_W[:]
    
    if len(T_W) > len(grad):
        return grade_korea_full()
    else:
        for i in range(len(T_W)-1,0,-1):
            if T_W[i] >= len(grad):
                return grade_korea_full() 
            if T_W[i] in T_W[:i-1]:
                return grade_korea_full()
            else :
                T_W.pop()
    T_W = T_W_temp
    T_W = sorted(T_W)
    
    for i in range(len(T_W)):
        if i == 0 :
            url_str += grad[T_W[i]][2:]
            continue
        url_str += grad[T_W[i]]
    
    url = front_url+url_str+"&page="
    
    for i in range(1,5):
        request_return = requests.get(url+str(i),headers={"User-Agent": "Mozilla/5.0"})

        soup = BeautifulSoup(request_return.content, "html.parser")
        time.sleep(random.randint(1,3))
        
        for j in range(1,100):
            try:
                if p.match(soup.select_one("#problemset > tbody > tr:nth-child("+str(j)+") > td:nth-child(2) > a").getText()) :
                    pb_group.append(soup.select_one("#problemset > tbody > tr:nth-child("+str(j)+") > td.list_problem_id").getText())
            except AttributeError :
                break
    print(pb_group , random.choice(pb_group))
    return len(pb_group) , random.choice(pb_group)

