import time
import random
import requests
from bs4 import BeautifulSoup
import re
timeout = 5

# url = "https://opendic.korean.go.kr/search/searchResult?query=%EB%B6%81%ED%95%9C%EC%96%B4&dicType=3&wordMatch=N&searchType=&currentPage=1&cateCode=&fieldCode=&spCode=&divSearch=search&infoType=confirm&rowsperPage=10"


# front_url = "https://www.acmicpc.net/problemset?sort=no_asc&solvedac_option="

# page_url = "&page="

# max_pagenumber = 2314 # 2313+1
# full_url = "https://www.acmicpc.net/problemset?sort=no_asc&solvedac_option=xz%2Cxn&tier=6%2C7%2C8%2C9%2C10&page=1"
# request_return = requests.get(full_url)

# soup = BeautifulSoup(request_return.content, "html.parser")
# pages = soup.select_one("ul.pagination").getText()
# pages_group = [pages[-1:],pages[-2:],pages[-3:]]
# # for i in range(len(pages_group)-1,-1,-1):
# #     if pages_group[i] in pages:
# #         print(pages_group[i])
# #     else:
# #         print("x")
# print(soup.select_one("ul.pagination"))


# def test():
#     cnt = 0 
#     p = re.compile('[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]')
#     url = "https://www.acmicpc.net/problemset"
#     for i in range(1,):
#         request_return = requests.get(url+str(i))
#         soup = BeautifulSoup(request_return.content, "html.parser")
#         for i in range(1,100):
#             if p.match(soup.select_one("#problemset > tbody > tr:nth-child("+str(i)+") > td:nth-child(2) > a").getText()) :
#                 # code_num = soup.select_one("#problemset > tbody > tr:nth-child("+str(i)+") > td.list_problem_id").getText()
#                 # print(code_num,i)
#                 print(cnt)
#                 cnt+=1
#                 print(soup.select_one("#problemset > tbody > tr:nth-child("+str(i)+") > td:nth-child(2) > a").getText())

# print(test())

def test():
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
            
print(test())