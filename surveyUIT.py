# -*- coding: utf-8 -*-
import sys
import os
import time
import datetime
import requests
import re
import random
from colored import fg, bg, attr

python_version = 2
if sys.hexversion >= 0x3000000:
    python_version = 3

if python_version == 3:
    raw_input = input

hocluc = ''
tylethoigian = ''
chuandaura = ''
thangdiem = ''
start_thangdiem = ''
end_thangdiem = ''
ykien_hailong = ''
ykien_khonghailong = ''

hl = ["", "Giỏi", "Khá", "Trung bình - Khá", "Trung bình", "Yếu"]
tytg = ["", "<50%", "50-80%", ">80%"]
cdr = ["", "Không biết chuẩn đầu ra là gì", "Dưới 50%", "Từ 50 đến dưới 70%", "Từ 70 đến dưới 90%", "Trên 90%"]


def banner():
    print("%s" % (fg('yellow')))
    print(r"""
                                  _    _ _____ _______ 
            v20.19.01.10         | |  | |_   _|__   __|
 ___ _   _ _ ____   _____ _   _  | |  | | | |    | |   
/ __| | | | '__\ \ / / _ \ | | | | |  | | | |    | |   
\__ \ |_| | |   \ V /  __/ |_| | | |__| |_| |_   | |   
|___/\__,_|_|    \_/ \___|\__, |  \____/|_____|  |_|   
                           __/ |                       
                          |___/    by Truoc Phan

----------------------------------------------------
  Facebook: https://www.facebook.com/TruocPT
  Twitter: https://twitter.com/TruocPhan
  Gmail: truocphan112017@gmail.com
  GitHub: https://github.com/TruocPhan
----------------------------------------------------
""")
    print("%s" % (attr('reset')))


def Setup_data():
    banner()
    print("%sPHẦN 2: THÔNG TIN CÁ NHÂN%s" % (fg('white'), attr('reset')))
    while True:
        global hocluc
        value = raw_input("""%sXếp loại học lực trong học kỳ vừa qua?
[0] Ngẫu nhiên
[1] Giỏi
[2] Khá
[3] Trung bình - Khá
[4] Trung bình
[5] Yếu%s
>>> """ % (fg('yellow'), fg("white")))
        if value == '0':
            hocluc = 'A' + str(random.randint(1,4))
            break
        elif value == '1':
            hocluc = 'A1'
            break
        elif value == '2':
            hocluc = 'A2'
            break
        elif value == '3':
            hocluc = 'A3'
            break
        elif value == '4':
            hocluc = 'A4'
            break
        elif value == '5':
            hocluc = 'A5'
            break

    while True:
        global tylethoigian
        print("\n%sTỷ lệ thời gian Anh/Chị lên lớp đối với môn học này" % (fg('yellow')))
        print("[0] Ngẫu nhiên")
        print("[1] <50%")
        print("[2] 50-80%")
        print("[3] >80%")
        value = raw_input("%s>>> "  % (fg("white")))
        if value == '0':
            tylethoigian = 'A' + str(random.randint(1,3))
            break
        elif value == '1':
            tylethoigian = 'A1'
            break
        elif value == '2':
            tylethoigian = 'A2'
            break
        elif value == '3':
            tylethoigian = 'A3'
            break

    while True:
        global chuandaura
        print("\n%sAnh chị tự đánh giá đạt được bao nhiêu %s chuẩn đầu ra của môn học này:" % (fg('yellow'), "%"))
        print("[0] Ngẫu nhiên")
        print("[1] Không biết chuẩn đầu ra là gì")
        print("[2] Dưới 50%")
        print("[3] Từ 50 đến dưới 70%")
        print("[4] Từ 70 đến dưới 90%")
        print("[5] Trên 90%")
        value = raw_input("%s>>> " % (fg('white')))
        if value == '0':
            chuandaura = 'A' + str(random.randint(1,4))
            break
        elif value == '1':
            chuandaura = 'A1'
            break
        elif value == '2':
            chuandaura = 'A2'
            break
        elif value == '3':
            chuandaura = 'A3'
            break
        elif value == '4':
            chuandaura = 'A4'
            break
        elif value == '5':
            chuandaura = 'A5'
            break

    print("\n%sPHẦN 3: NHẬN XÉT VỀ HOẠT ĐỘNG GIẢNG DẠY CỦA GIẢNG VIÊN%s" % (fg('white'), attr('reset')))
    while True:
        global thangdiem
        global start_thangdiem
        global end_thangdiem
        value = raw_input("""%sNhận xét về hoạt động giảng dạy của giảng viên
[0] Tất cả câu hỏi đều cho thang điểm ngẫu nhiên
[1] Tất cả câu hỏi đều cho thang điểm 1
[2] Tất cả câu hỏi đều cho thang điểm 2
[3] Tất cả câu hỏi đều cho thang điểm 3
[4] Tất cả câu hỏi đều cho thang điểm 4
[5] Thang điểm ngẫu nhiên cho từng câu hỏi (thang điểm ngẫu nhiên trong khoảng từ 1 đến 4)
[6] Thang điểm ngẫu nhiên cho từng câu hỏi (thiết lập khoảng ngẫu nhiên cho thang điểm)%s
>>> """ % (fg('yellow'), fg('white')))
        if value == "0":
            thangdiem = "MH0" + str(random.randint(1,4))
            break
        elif value == "1":
            thangdiem = "MH01"
            break
        elif value == "2":
            thangdiem = "MH02"
            break
        elif value == "3":
            thangdiem = "MH03"
            break
        elif value == "4":
            thangdiem = "MH04"
            break
        elif value == "5":
            thangdiem = "random"
            start_thangdiem = 1
            end_thangdiem = 4
            break
        elif value == "6":
            thangdiem = "random"
            while True:
                start_thangdiem = raw_input("%sTừ (1-4): %s" % (fg('green'), attr('reset')))
                end_thangdiem = raw_input("%sĐến (1-4): %s" % (fg('green'), attr('reset')))
                if start_thangdiem.isdigit() and end_thangdiem.isdigit() and 1 <= int(start_thangdiem) <= 4 and 1 <= int(end_thangdiem) <= 4 and int(start_thangdiem) <= int(end_thangdiem):
                    start_thangdiem = int(start_thangdiem)
                    end_thangdiem = int(end_thangdiem)
                    break
                else:
                    print("%s[-] Khoảng thang điểm ngẫu nhiên không hợp lệ. Vui lòng nhập lại...%s" % (fg('red'), attr('reset')))
            break

    print("\n%sPHẦN 4: Ý KIẾN KHÁC%s" % (fg('white'), attr('reset')))
    global ykien_hailong
    global ykien_khonghailong
    ykien_hailong = raw_input("""%s[+] Điều Anh/ Chị hài lòng nhất về hoạt động giảng dạy của GV (Nhấn Enter nếu không có ý kiến)
%s>>> """ % (fg('yellow'), fg('white')))
    ykien_khonghailong = raw_input("""%s[+] Điều Anh/ Chị không hài lòng nhất về hoạt động giảng dạy của GV (Nhấn Enter nếu không có ý kiến)
%s>>> """ % (fg('yellow'), fg('white')))



def run(url):
    try:
        s = requests.Session()
        print("\n%s[%s] %s%s%s" % (fg('yellow'), str(datetime.datetime.now()).split(".")[0], fg('blue'), url, attr('reset')))
        time.sleep(10)
        req = s.get(url)
        surveyname = re.findall("<p class=\"surveyname\">(.*)</p>", req.text)[0]
        # Giá trị các tham số cần post
        move = re.findall("<input type=\"hidden\" name=\"move\" value=\"(.*)\" id=\"movenext\" />", req.text)[0]
        move2 = re.findall("value='(.*)' name='move2' id='movenextbtn' >", req.text)[0]
        sid = re.findall("<input type='hidden' name='sid' value='(.*)' id='sid' />", req.text)[0]
        token = re.findall("<input type='hidden' name='token' value='(.*)' id='token' />", req.text)[0]
        lastgroupname = re.findall("<input type='hidden' name='lastgroupname' value='(.*)' id='lastgroupname' />", req.text)[0]
        LEMpostKey = re.findall("<input type='hidden' name='LEMpostKey' value='(.*)' id='LEMpostKey' />", req.text)[0]
        thisstep = re.findall("<input type='hidden' name='thisstep' id='thisstep' value='(.*)' />", req.text)[0]
        print("%s--------------------------------------------------%s" % (fg('yellow'), attr('reset')))
        print ("%s%s%s" % (fg('white'), surveyname, attr('reset')))
        cookies = req.cookies

        _REQUEST(s, move, move2, sid, token, lastgroupname, LEMpostKey, thisstep, cookies)

    except:
        print("%s[-] Link khảo sát đã được thực hiện, hoặc là token cung cấp không hợp lệ hoặc là đã được sử dụng. Vui lòng kiểm tra lại link [%s]%s\n" % (fg('red'), url, attr('reset')))



def _REQUEST(s, move, move2, sid, token, lastgroupname, LEMpostKey, thisstep, cookies):
    data = {
        "move": move,
        "move2": move2,
        "sid": sid,
        "token": token,
        "lastgroupname": lastgroupname,
        "LEMpostKey": LEMpostKey,
        "thisstep": thisstep
    }
    try:
        time.sleep(10)
        req = s.post("https://survey.uit.edu.vn/index.php/survey/index", data=data, cookies=cookies)

        if python_version == 2:
            surveyinfo = re.findall("Khảo sát môn: (.*)<br>Mã lớp: (.*)<br>Tên giáo viên: (.*)<br>", req.text.encode('utf8'))
        elif python_version == 3:
            surveyinfo = re.findall("Khảo sát môn: (.*)<br>Mã lớp: (.*)<br>Tên giáo viên: (.*)<br>", req.text)

        print("%sKhảo sát môn: %s%s%s" % (fg('green'), fg('yellow'), surveyinfo[0][0], attr('reset')))
        print("%sMã lớp: %s%s%s" % (fg('green'), fg('yellow'), surveyinfo[0][1], attr('reset')))
        print("%sTên giáo viên: %s%s%s" % (fg('green'), fg('yellow'), surveyinfo[0][2], attr('reset')))

        # Giá trị các tham số cần post
        move = re.findall("<input type=\"hidden\" name=\"move\" value=\"(.*)\" id=\"movenext\" />", req.text)[0]
        move2 = re.findall("value='(.*)' name='move2' id='movenextbtn' >", req.text)[0]
        sid = re.findall("<input type='hidden' name='sid' value='(.*)' id='sid' />", req.text)[0]
        token = re.findall("<input type='hidden' name='token' value='(.*)' id='token' />", req.text)[0]
        lastgroupname = re.findall("<input type='hidden' name='lastgroupname' value='(.*)' id='lastgroupname' />", req.text)[0]
        LEMpostKey = re.findall("<input type='hidden' name='LEMpostKey' value='(.*)' id='LEMpostKey' />", req.text)[0]
        thisstep = re.findall("<input type='hidden' name='thisstep' id='thisstep' value='(.*)' />", req.text)[0]

        PART_2(s, move, move2, sid, token, lastgroupname, LEMpostKey, thisstep, cookies)

    except:
        print("%s[-] Link khảo sát đã được thực hiện, hoặc là token cung cấp không hợp lệ hoặc là đã được sử dụng. Vui lòng kiểm tra lại link [%s]%s\n" % (fg('red'), url, attr('reset')))



def PART_2(s, move, move2, sid, token, lastgroupname, LEMpostKey, thisstep, cookies):
    headers = {
        "Referer": "https://survey.uit.edu.vn/index.php/survey/index"
    }
    data = {
        "move": move,
        "move2": move2,
        "sid": sid,
        "token": token,
        "lastgroupname": lastgroupname,
        "LEMpostKey": LEMpostKey,
        "thisstep": thisstep
    }

    try:
        print("\n%sPHẦN 2: THÔNG TIN CÁ NHÂN%s" % (fg('white'), attr('reset')))
        time.sleep(10)
        req = s.post("https://survey.uit.edu.vn/index.php/survey/index", data=data, cookies=cookies)
        questions = re.findall("<span class=\"asterisk\">\*</span><span class=\"qnumcode\">  </span>(.*)<br /><span class=\"questionhelp\"></span>", req.text)

        for i in range(len(questions)):
            if python_version == 2:
                if questions[i].encode('utf8') == "Xếp loại học lực trong học kỳ vừa qua?":
                    print("%s[+] %s %s%s[ %s ]%s\n" % (fg('green'), questions[i], fg('black'), bg('white'), hl[int(hocluc[1])].decode('UTF-8'), attr('reset')))
                elif questions[i].encode('utf8') == "Tỷ lệ thời gian Anh/Chị lên lớp đối với môn học này":
                    print("%s[+] %s %s%s[ %s ]%s\n" % (fg('green'), questions[i], fg('black'), bg('white'), tytg[int(tylethoigian[1])].decode('UTF-8'), attr('reset')))
                elif questions[i].encode('utf8') == "Anh chị tự đánh giá đạt được bao nhiêu % chuẩn đầu ra của môn học này:":
                    print("%s[+] %s %s%s[ %s ]%s\n" % (fg('green'), questions[i], fg('black'), bg('white'), cdr[int(chuandaura[1])].decode('UTF-8'), attr('reset')))

            elif python_version == 3:
                if questions[i] == "Xếp loại học lực trong học kỳ vừa qua?":
                    print("%s[+] %s %s%s[ %s ]%s\n" % (fg('green'), questions[i], fg('black'), bg('white'), hl[int(hocluc[1])], attr('reset')))
                elif questions[i] == "Tỷ lệ thời gian Anh/Chị lên lớp đối với môn học này":
                    print("%s[+] %s %s%s[ %s ]%s\n" % (fg('green'), questions[i], fg('black'), bg('white'), tytg[int(tylethoigian[1])], attr('reset')))
                elif questions[i] == "Anh chị tự đánh giá đạt được bao nhiêu % chuẩn đầu ra của môn học này:":
                    print("%s[+] %s %s%s[ %s ]%s\n" % (fg('green'), questions[i], fg('black'), bg('white'), cdr[int(chuandaura[1])], attr('reset')))


        # Giá trị các tham số cần post
        fieldnames = re.findall("<input type='hidden' name='fieldnames' value='(.*)' id='fieldnames' />", req.text)[0]
        lastgroup = re.findall("<input type='hidden' name='lastgroup' value='(.*)' id='lastgroup' />", req.text)[0]
        relevance = re.findall("<input type='hidden' id='relevance(.*)' name='relevance(.*)' value='(.*)'/>", req.text)
        move = re.findall("<input type=\"hidden\" name=\"move\" value=\"(.*)\" id=\"movenext\" />", req.text)[0]
        thisstep = re.findall("<input type='hidden' name='thisstep' value='(.*)' id='thisstep' />", req.text)[0]
        sid = re.findall("<input type='hidden' name='sid' value='(.*)' id='sid' />", req.text)[0]
        start_time = re.findall("<input type='hidden' name='start_time' value='(.*)' id='start_time' />", req.text)[0]
        LEMpostKey = re.findall("<input type='hidden' name='LEMpostKey' value='(.*)' id='LEMpostKey' />", req.text)[0]
        token = re.findall("<input type='hidden' name='token' value='(.*)' id='token' />", req.text)[0]

        PART_3(s, fieldnames, lastgroup, relevance, move, thisstep, sid, start_time, LEMpostKey, token, cookies)

    except:
        print("%s[-] Link khảo sát đã được thực hiện, hoặc là token cung cấp không hợp lệ hoặc là đã được sử dụng. Vui lòng kiểm tra lại link [%s]%s\n" % (fg('red'), url, attr('reset')))


def PART_3(s, fieldnames, lastgroup, relevance, move, thisstep, sid, start_time, LEMpostKey, token, cookies):
    headers = {
        "Referer": "https://survey.uit.edu.vn/index.php/survey/index"
    }
    data = {
        "fieldnames": fieldnames,
        "lastgroup": lastgroup,
        "move": move,
        "thisstep": thisstep,
        "sid": sid,
        "start_time": start_time,
        "LEMpostKey": LEMpostKey,
        "token": token
    }

    try:
        for i in range(len(fieldnames.split("|"))):
            if i == 0:
                data[fieldnames.split("|")[i]] = hocluc
                data["java" + fieldnames.split("|")[i]] = hocluc
            elif i == 1:
                data[fieldnames.split("|")[i]] = tylethoigian
                data["java" + fieldnames.split("|")[i]] = tylethoigian
            elif i == 2:
                data[fieldnames.split("|")[i]] = chuandaura
                data["java" + fieldnames.split("|")[i]] = chuandaura
        for i in relevance:
            data["relevance" + i[0]] = "1"

        time.sleep(10)
        req = s.post("https://survey.uit.edu.vn/index.php/survey/index", data=data, cookies=cookies)
        # Giá trị các tham số cần post
        fieldnames = re.findall("<input type='hidden' name='fieldnames' value='(.*)' id='fieldnames' />", req.text)[0]
        lastgroup = re.findall("<input type='hidden' name='lastgroup' value='(.*)' id='lastgroup' />", req.text)[0]
        relevance = re.findall("<input type='hidden' id='relevance(.*)' name='relevance(.*)' value='(.*)'/>", req.text)
        move  = re.findall("<input type=\"hidden\" name=\"move\" value=\"(.*)\" id=\"movenext\" />", req.text)[0]
        thisstep = re.findall("<input type='hidden' name='thisstep' value='(.*)' id='thisstep' />", req.text)[0]
        sid = re.findall("<input type='hidden' name='sid' value='(.*)' id='sid' />", req.text)[0]
        start_time = re.findall("<input type='hidden' name='start_time' value='(.*)' id='start_time' />", req.text)[0]
        LEMpostKey = re.findall("<input type='hidden' name='LEMpostKey' value='(.*)' id='LEMpostKey' />", req.text)[0]
        token = re.findall("<input type='hidden' name='token' value='(.*)' id='token' />", req.text)[0]
        print("\n%sPHẦN 3: NHẬN XÉT VỀ HOẠT ĐỘNG GIẢNG DẠY CỦA GIẢNG VIÊN%s" % (fg('white'), attr('reset')))
        points = {}

        for i in range(int(len(fieldnames.split("|"))/2)):
            if thangdiem == "random":
                p = str(random.randint(start_thangdiem, end_thangdiem))
                points[fieldnames.split("|")[i]] = "MH0" + p
                question = re.findall("(.*)<input type=\"hidden\" name=\"java"+fieldnames.split("|")[i]+"\" id=\"java"+fieldnames.split("|")[i]+"\" value=\"\" />", req.text)[0]

                if python_version == 2:
                    print("%s[+] %s %s%s[ %s ]%s\n" % (fg('green'), question, fg('black'), bg('white'), "Thang điểm: ".decode('UTF-8') + p, attr('reset')))
                elif python_version == 3:
                    print("%s[+] %s %s%s[ %s ]%s\n" % (fg('green'), question, fg('black'), bg('white'), "Thang điểm: " + p, attr('reset')))

            else:
                points[fieldnames.split("|")[i]] = thangdiem
                question = re.findall("(.*)<input type=\"hidden\" name=\"java"+fieldnames.split("|")[i]+"\" id=\"java"+fieldnames.split("|")[i]+"\" value=\"\" />", req.text)[0]

                if python_version == 2:
                    print("%s[+] %s %s%s[ %s ]%s\n" % (fg('green'), question, fg('black'), bg('white'), "Thang điểm: ".decode('UTF-8') + thangdiem[-1:], attr('reset')))
                elif python_version == 3:
                    print("%s[+] %s %s%s[ %s ]%s\n" % (fg('green'), question, fg('black'), bg('white'), "Thang điểm: " + thangdiem[-1:], attr('reset')))

        PART_4(s, fieldnames, points, lastgroup, relevance, move, thisstep, sid, start_time, LEMpostKey, token, cookies)

    except:
        print("%s[-] Link khảo sát đã được thực hiện, hoặc là token cung cấp không hợp lệ hoặc là đã được sử dụng. Vui lòng kiểm tra lại link [%s]%s\n" % (fg('red'), url, attr('reset')))


def PART_4(s, fieldnames, points, lastgroup, relevance, move, thisstep, sid, start_time, LEMpostKey, token, cookies):
    headers = {
        "Referer": "https://survey.uit.edu.vn/index.php/survey/index"
    }
    data = {
        "fieldnames": fieldnames,
        "lastgroup": lastgroup,
        "move": move,
        "thisstep": thisstep,
        "sid": sid,
        "start_time": start_time,
        "LEMpostKey": LEMpostKey,
        "token": token
    }

    try:
        for i in points:
            data[i] = points[i]
            data["java" + i] = points[i]
        for i in range(int(len(fieldnames.split("|"))/2), len(fieldnames.split("|"))):
            data[fieldnames.split("|")[i]] = ""
        for i in relevance:
            data["relevance" + i[0]] = "1"

        time.sleep(10)
        req = s.post("https://survey.uit.edu.vn/index.php/survey/index", data=data, cookies=cookies)
        # Giá trị các tham số cần post
        fieldnames = re.findall("<input type='hidden' name='fieldnames' value='(.*)' id='fieldnames' />", req.text)[0]
        lastgroup = re.findall("<input type='hidden' name='lastgroup' value='(.*)' id='lastgroup' />", req.text)[0]
        relevance = re.findall("<input type='hidden' id='relevance(.*)' name='relevance(.*)' value='(.*)'/>", req.text)
        move = re.findall("<input type=\"hidden\" name=\"move\" value=\"(.*)\" id=\"movesubmit\" />", req.text)[0]
        thisstep = re.findall("<input type='hidden' name='thisstep' value='(.*)' id='thisstep' />", req.text)[0]
        sid = re.findall("<input type='hidden' name='sid' value='(.*)' id='sid' />", req.text)[0]
        start_time = re.findall("<input type='hidden' name='start_time' value='(.*)' id='start_time' />", req.text)[0]
        LEMpostKey = re.findall("<input type='hidden' name='LEMpostKey' value='(.*)' id='LEMpostKey' />", req.text)[0]
        token = re.findall("<input type='hidden' name='token' value='(.*)' id='token' />", req.text)[0]

        print("\n%sPHẦN 4: Ý KIẾN KHÁC%s" % (fg('white'), attr('reset')))
        print("%s[+] Điều Anh/ Chị hài lòng nhất về hoạt động giảng dạy của GV%s" % (fg('green'), attr('reset')))
        print("%s==> Ý kiến của bạn: %s%s\"%s\"%s" % (fg('white'), fg('black'), bg('white'), ykien_hailong, attr('reset')))
        print("\n%s[+] Điều Anh/ Chị không hài lòng nhất về hoạt động giảng dạy của GV%s" % (fg('green'), attr('reset')))
        print("%s==> Ý kiến của bạn: %s%s\"%s\"%s" % (fg('white'), fg('black'), bg('white'), ykien_khonghailong, attr('reset')))

        submit_form(s, fieldnames, lastgroup, relevance, move, thisstep, sid, start_time, LEMpostKey, token, cookies)

    except:
        print("%s[-] Link khảo sát đã được thực hiện, hoặc là token cung cấp không hợp lệ hoặc là đã được sử dụng. Vui lòng kiểm tra lại link [%s]%s\n" % (fg('red'), url, attr('reset')))


def submit_form(s, fieldnames, lastgroup, relevance, move, thisstep, sid, start_time, LEMpostKey, token, cookies):
    headers = {
        "Referer": "https://survey.uit.edu.vn/index.php/survey/index"
    }
    data = {
        "fieldnames": fieldnames,
        "lastgroup": lastgroup,
        "move": move,
        "thisstep": thisstep,
        "sid": sid,
        "start_time": start_time,
        "LEMpostKey": LEMpostKey,
        "token": token
    }
    
    try:
        data[fieldnames.split("|")[0]] = ykien_hailong
        data[fieldnames.split("|")[1]] = ykien_khonghailong
        for i in relevance:
            data["relevance" + i[0]] = "1"

        time.sleep(10)
        req = s.post("https://survey.uit.edu.vn/index.php/survey/index", data=data, cookies=cookies)

        if python_version == 2:
            if re.findall("<td class=\"site-name\"><p>(.*)</p></td>", req.text)[0].encode('utf8') == "HOÀN THÀNH KHẢO SÁT":
                print("\n%s%s>>> HOÀN THÀNH KHẢO SÁT <<<%s" % (fg('white'), bg('yellow'), attr('reset')))
            else:
                print("\n%s>>> Quá trình khảo sát gặp lỗi. Vui lòng thử lại <<<%s" % (fg('red'), attr('reset')))

        elif python_version == 3:
            if re.findall("<td class=\"site-name\"><p>(.*)</p></td>", req.text)[0] == "HOÀN THÀNH KHẢO SÁT":
                print("\n%s%s>>> HOÀN THÀNH KHẢO SÁT <<<%s" % (fg('white'), bg('yellow'), attr('reset')))
            else:
                print("\n%s>>> Quá trình khảo sát gặp lỗi. Vui lòng thử lại <<<%s" % (fg('red'), attr('reset')))

        print("%s--------------------------------------------------%s\n\n" % (fg('yellow'), attr('reset')))

    except:
        print("%s[-] Link khảo sát đã được thực hiện, hoặc là token cung cấp không hợp lệ hoặc là đã được sử dụng. Vui lòng kiểm tra lại link [%s]%s\n\n" % (fg('red'), url, attr('reset')))


def main():
    if len(sys.argv) != 2:
        banner()
        exit("%sUsage: %spython %s [survey_file]%s\n\t[survey_file]: file chứa danh sách các link cần khảo sát\n" % (fg('white'), fg('yellow'), sys.argv[0], attr('reset')))
    # Kiểm tra file danh sách link khảo sát có tồn tại không
    if os.path.isfile(sys.argv[1]) == False:
        banner()
        exit("%sUsage: %spython %s [survey_file]%s\n\t[survey_file]: file chứa danh sách các link cần khảo sát\n" % (fg('white'), fg('yellow'), sys.argv[0], attr('reset')))

    Setup_data()
    os.system("clear")
    banner()
    survey_file = sys.argv[1]
    f = open(survey_file, "r")
    for url in f:
        run(url.split("\n")[0])


if __name__ == "__main__":
    main()