from bs4 import BeautifulSoup
import requests
import xlrd
from xlutils.copy import copy
import re
import json
import time,random
from multiprocessing import Pool
from functools import partial
def crawer(id,company_name):
    try:
        print('*'*50+'开始爬取第'+str(id)+'页'+'*'*50)
        rule=re.compile('^[0-9]+[A-Za-z0-9]+$',re.X)
        datas=[]
        USER_AGENTS = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
            "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12",
            "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",

        ]
        headers={
            'User-Agent':random.choice(USER_AGENTS),
        }
        data=requests.get('http://chinaports.com/chuanqibiao/{0}/null/null/{1}/query/'.format(id,company_name),headers=headers)
        soup=BeautifulSoup(data.text,'lxml')
        route_name=soup.select('body > section > div > div.shipscheduleSpread > div.shiplist > table > tbody > tr')
        ship_names=soup.select('body > section > div > div.shipscheduleSpread > div.shiplist > table > tbody > tr > td > a')
        for (a,b) in zip(route_name,ship_names):
            ship_weights = []
            ship_link=b.attrs['href']
            ship_data=requests.get(ship_link)
            ship_soup=BeautifulSoup(ship_data.text,'lxml')
            names=ship_soup.select('body > div > div > div > div')
            for name in names[:-1]:
                # print(names[names.index(name)].text)
                if rule.match(names[names.index(name)+1].text):
                    useragent1=random.choice(USER_AGENTS)
                    number = getship_id(name.text,useragent1)
                    if number:
                       useragent2=random.choice(USER_AGENTS)
                       wei=weight(number,useragent2)
                       if wei:
                           ship_weight={
                               's_name':name.text,
                               'weight':wei
                           }
                       else:
                           ship_weight = {
                               's_name': name.text,
                               'weight': 0
                           }
                    else:
                        ship_weight = {
                            's_name': name.text,
                            'weight': 0
                         }
                    ship_weights.append(ship_weight)
            data={
                'ship_weights':ship_weights,
                'route_datas':a.text.split('\n')[1:-2],
                 }
            # print(data)
            datas.append(data)
        print('*' * 50 + '第' + str(id) + '页爬取成功' + '*' * 50)
        if id%50==0:
            print('页数为50的倍数，随机休息几秒钟')
            time.sleep(random.randint(1,3))
        return datas
    except:
        print('$'*100+'参数不正确'+str(id)+'$'*100)
        time.sleep(random.randint(5,10))
        print('$' * 100 + '从新爬取' + str(id) + '$' * 100)
        crawer(id,company_name)
        return None
def write2(datas):
    col = 0
    rb = xlrd.open_workbook('航船.xls')
    # 通过sheet_by_index()获取的sheet没有write()方法
    rs = rb.sheet_by_index(0)
    row=rs.nrows
    wb = copy(rb)
    # 通过get_sheet()获取的sheet有write()方法
    ws = wb.get_sheet(0)
    for da_s in datas:
      if da_s:
       for data in da_s:
        if data['ship_weights']:
                i=5
                ws.write(row, col, data['route_datas'][0])
                ws.write(row, col + 1, data['route_datas'][1])
                ws.write(row, col + 2, data['route_datas'][2])
                ws.write(row, col + 3, data['route_datas'][3])
                ws.write(row, col + 4, data['route_datas'][4])
                for s_w in data['ship_weights']:
                      ws.write(row, i,s_w['s_name'])
                      ws.write(row,i+1,s_w['weight'])
                      i=i+2
                row += 1
        else:
            ws.write(row, col, data['route_datas'][0])
            ws.write(row, col + 1, data['route_datas'][1])
            ws.write(row, col + 2, data['route_datas'][2])
            ws.write(row, col + 3, data['route_datas'][3])
            ws.write(row, col + 4, data['route_datas'][4])
            ws.write(row, col + 5, '无')
            ws.write(row,col+6,'0')
            row+=1
      else:
          continue
    wb.save('航船.xls')
def weight(id,user_agent):
    try:
        headers={
            'User-Agent':user_agent,
        }
        form_datas={
            'method': 'pospoint',
            'type': '1',
            'shipid':id

        }
        # data=requests.get('http://www.chinaports.com/shiptracker/shipinit.do?method=forIndex&shipall=CMA%20CGM%20CHOPIN')
        data=requests.post('http://www.chinaports.com/shiptracker/shipinit.do',headers=headers,data=form_datas)
        soup=BeautifulSoup(data.text,'lxml')
        if soup.text:
            wt=json.loads(soup.text[10:-2])[17]
            if wt:
                # print('船对应的id为'+str(id)+'载重量:'+str(wt))
                return wt
            else:
                # print(str(id)+':'+'无')
                return None
        else:
             return None
    except:
        print(id+'未搜索到')
def getship_id(name,user_agent):
    try:
        headers = {
            'User-Agent': user_agent,
        }
        form_data={
            'method':'search',
            'queryParam': name.replace(' ','').lower(),
        }
        data=requests.post('http://www.chinaports.com/shiptracker/newshipquery.do',headers=headers,data=form_data)
        soup=BeautifulSoup(data.text,'lxml')
        number=json.loads(soup.text)[0][1]
        if number:
            # print('搜索成功----'+name+'_id:'+number)
            return number
        else:
            # print(name+'无相关信息')
            return None
    except:
        pass
        # print(name+':'+'未查询到相关内容')
if __name__=='__main__':
    pool=Pool()
    datas=pool.map(partial(crawer,company_name='MSK(马士基)'),[i for i in range(1,298)])
    write2(datas)
    pool.close()
    pool.join()


