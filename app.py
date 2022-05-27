from flask import Flask, flash, redirect, render_template, request, url_for
from sele_craw import grade_korea_full
from flask_mysqldb import MySQL
# from db import *
import time
import random
import requests
from bs4 import BeautifulSoup
import re
import sys
input = sys.stdin.readline
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument( "--headless" ) 

driver = webdriver.Chrome('chromedriver.exe',chrome_options=chrome_options)
driver.implicitly_wait(3)


app = Flask(__name__)

# app.config['MYSQL_HOST'] = db['mysql_host']
# app.config['MYSQL_USER'] = db['mysql_user']
# app.config['MYSQL_PASSWORD'] = db['mysql_password']
# app.config['MYSQL_DBs'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/Toto")
def Toto():
    return render_template("Toto.html")


# @app.route("/input_data", methods = ['GET','POST'])
# def input_data():
#     data = request.form['input']   
#     print(data,data)
#     data_lst = [int(i) for i in data]
#     print(data_lst)
#     return render_template("input_data.html")

@app.route("/real/<int:int_value>", methods = ['GET','POST'])
def real(int_value):
    return render_template("real.html",int_value = int_value)


@app.route("/download/<int:int_value>", methods = ['GET','POST'])
def download(int_value):
    grad = ["1%2C2%2C3%2C4%2C5","6%2C7%2C8%2C9%2C10","11%2C12%2C13%2C14%2C15","16%2C17%2C18%2C19%2C20","21%2C22%2C23%2C24%2C25","26%2C27%2C28%2C29%2C30"]
    
    titles = []
    numbers = []
    p = re.compile('[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]')
    
    # url_str = ""
    front_url = "https://www.acmicpc.net/problemset?sort=no_asc&solvedac_option=xz%2Cxn&tier="


    url = front_url+grad[int_value]+"&page="

    pages = 1

    for i in range(1,pages+1):
        sum_url = url+str(i)
        driver.get(sum_url)
        print(sum_url)
        request_return = driver.page_source
        soup = BeautifulSoup(request_return, "html.parser")
        time.sleep(random.randint(1,3))
        problems = 5

        for j in range(1,problems+1):
            
            number = soup.select_one("#problemset > tbody > tr:nth-child("+str(j)+") > td.list_problem_id").getText()
            time.sleep(random.randint(1,3))
            title = soup.select_one("#problemset > tbody > tr:nth-child("+str(j)+") > td:nth-child(2) > a").getText()
            time.sleep(random.randint(1,3))
            # if p.match(soup.select_one("#problemset > tbody > tr:nth-child("+str(j)+") > td:nth-child(2) > a").getText()) :
            #     number = soup.select_one("#problemset > tbody > tr:nth-child("+str(j)+") > td.list_problem_id").getText()
            #     title = soup.select_one("#problemset > tbody > tr:nth-child("+str(j)+") > td:nth-child(2) > a").getText()

            titles.append(title)
            numbers.append(number)
            print(title,number,j)
            template_Random_number = random.choice(numbers)
    # if i == 4:
    #     driver.close()        
    
    # print(titles,len(titles), numbers,len(numbers), random.choice(numbers))
    # return render_template("download.html",
    #                        template_number = numbers,
    #                        template_Random_number = template_Random_number,
    #                        Random_url = "https://www.acmicpc.net/problem/"+template_Random_number)



    return redirect("https://www.acmicpc.net/problem/"+template_Random_number)

    # return render_template("download.html")

if __name__ == '__main__':
    app.run(debug=True,port=5001) 
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config["SECRET_KEY"] = "ABCD"
    # debug = True라고 명시하면 해당 파일의 코드를 수정할 때마다 Flask가 변경된 것을 인식하고 다시 시작한다.
 
# @app.route("/input_data", methods = ['GET','POST'])
# def data_input():
    
#return render_template("input_data.html")
