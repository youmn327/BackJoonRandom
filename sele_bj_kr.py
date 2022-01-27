import time
import random
import requests
from bs4 import BeautifulSoup
import re
import sys
input = sys.stdin.readline
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(3)

grad = ["2C1%2C2%2C3%2C4%2C5%","2C6%2C7%2C8%2C9%2C10%","2C11%2C12%2C13%2C14%2C15%","2C16%2C17%2C18%2C19%2C20%2C21%","2C22%2C23%2C24%2C25%2C26%","2C27%2C28%2C29%2C30%2C31%"]
    
def filter_group():
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
    return url_str

def grade_korea_full():
    cnt = 0 
    p = re.compile('[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]')
    front_url = "https://www.acmicpc.net/problemset?sort=no_asc&solvedac_option=xz%2Cxn&tier="
    
    url = front_url+filter_group()+"&page="
    
    for i in range(1,240):
        driver.get(url+str(i))
        request_return = driver.page_source
        soup = BeautifulSoup(request_return, "html.parser")
        # print(soup)
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
    driver.close()


print(grade_korea_full())


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