import requests
from bs4 import BeautifulSoup
import urllib3

is_headers_set = False
fout = open("marks.csv",'w')
for regno in range(314175710088,314175710090):
    print(regno)
    try:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        res = requests.post('https://aucoe.info/RDA/resultsnew/result_grade.php',
                            data={'serialno': 1084,
                                  'course': 'B.E./B.TECH IV/IV FIRST SEMESTER',
                                  'degree': 'B.E./B.TECH',
                                  'table': 'gradestructure3',
                                  'appearing_year': 'NOVEMBER 2017',
                                  'Date_time': '2018-07-17 15:06:23',
                                  'regno': regno,
                                  'revdate': '0000-00-00','revfee': '0'
                                  },verify=False)
        soup = BeautifulSoup(res.text,'html.parser')
        tables = soup.findAll('table')
        name,regno=map(lambda x:x[x.find(':')+1:].strip(),map(lambda x:x.text,tables[3].findAll('td')))
        print(name,regno)
        sub_marks_details = list(map(lambda x:str(x.text).strip(),tables[4].findAll('td')[2:]))
        print(sub_marks_details)
        marks = dict(zip(sub_marks_details[::2],sub_marks_details[1::2]))
        print(marks)
        if(not is_headers_set):
            fout.write("name,regno,"+",".join(marks.keys())+"\n")
            is_headers_set = True
        fout.write(",".join((name,regno)+tuple(marks.values())))
    except Exception as e:
        pass
fout.close()