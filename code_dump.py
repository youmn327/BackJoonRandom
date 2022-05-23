@app.route("/download", methods = ['GET','POST'])
def download():
    print("enter download page")
    global DATA_aarange
    if request.method == "POST":
        input_DATA = request.form
        DATA_aarange = input_DATA['IN_DATA']
        print(DATA_aarange)
        print("check")
    # print(BJ_numbers , R_number)
    # BJ_numbers , R_number = 1,2
    # ,
    #         template_numbers =BJ_numbers,
    #         template_Random_number = R_number
    return render_template("download.html")


@app.route("/Toto")
def grade_korea_full():
    titles = []
    numbers = []
    # send_inte = []
    # print(DATA_aarange)
    # for i in DATA_aarange:
    #     print(i)
    print()
    
    p = re.compile('[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]')
    front_url = "https://www.acmicpc.net/problemset?sort=no_asc&solvedac_option=xz%2Cxn&tier="
    
    url = front_url+filter_group()+"&page="
    
    for i in range(1,5):
        sum_url = url+str(i)
        driver.get(sum_url)
        print(sum_url)
        request_return = driver.page_source
        soup = BeautifulSoup(request_return, "html.parser")
        time.sleep(random.randint(1,3))

        for j in range(1,10):
            try:
                if p.match(soup.select_one("#problemset > tbody > tr:nth-child("+str(j)+") > td:nth-child(2) > a").getText()) :
                    number = soup.select_one("#problemset > tbody > tr:nth-child("+str(j)+") > td.list_problem_id").getText()
                    title = soup.select_one("#problemset > tbody > tr:nth-child("+str(j)+") > td:nth-child(2) > a").getText()

                    titles.append(title)
                    numbers.append(number)

            except AttributeError :
                break
    
    # df = pd.DataFrame([titles,numbers],index=["제목","번호"])
    # df = df.transpose()
    # df.to_excel(excel_writer='backjoonT1.xlsx')    
    driver.close()
    return titles, numbers, random.choice(numbers)
    

@app.route("/Toto")
def filter_group():
    url_str = ""
    print("checkpoint")
    grad = ["2C1%2C2%2C3%2C4%2C5%2C6%","2C7%2C8%2C9%2C10%2C11%","2C12%2C13%2C14%2C15%2C16%","2C17%2C18%2C19%2C20%2C21%","2C22%2C23%2C24%2C25%2C26%","2C27%2C28%2C29%2C30%2C31%"]
    T_W = []
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

if __name__ == '__main__':
    app.run(debug=True,port=5001) 
    # debug = True라고 명시하면 해당 파일의 코드를 수정할 때마다 Flask가 변경된 것을 인식하고 다시 시작한다.

# @app.route("/input_data", methods = ['GET','POST'])
# def data_input():
    
#return render_template("input_data.html")


# # # # # # # # # # # # # # # # 

