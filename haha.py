# _*_ encoding:utf-8 _*_
__author__ = 'LYQ'
__data__ = '2018/8/6 12:29'
import requests
import random
from bs4 import BeautifulSoup
import json
proxies_list = ['https://125.122.169.21:6666','https://125.118.145.77:6666','https://125.122.116.179:6666']
proxie = random.choice(proxies_list)
proxies = {'http':proxie}
def crawer(page):
    form_data={
        'first': 'true',
         'pn': page,
         'kd': '爬虫'
    }
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '37',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': '_ga=GA1.2.2127436673.1528115573; user_trace_token=20180604203252-6640389f-67f3-11e8-9199-525400f775ce; LGUID=20180604203252-66403ccd-67f3-11e8-9199-525400f775ce; JSESSIONID=ABAAABAABEEAAJA4CB1D1E1AB77956F4859BA82AF18E7B0; X_HTTP_TOKEN=3b5cc3e8ca1a47cc3fe9029cdefa1645; _gid=GA1.2.1116473640.1533529836; WEBTJ-ID=20180806123128-1650d81174810c-0903bd9e60ebba-47e1039-1049088-1650d81174c16b; PRE_HOST=www.baidu.com; LGSID=20180806123158-a7fc0df0-9931-11e8-b6f5-525400f775ce; PRE_UTM=m_cf_cpc_baidu_pc; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.Ks00000Qw_ga_ChdLyjCAZRGq-tn56TffzGGPADDqyetj3yaXcK1ThbwEKoLB-6FTfvlyhr8omSEczKapjBufbkV4vrouQ7o6zMnPd20tktunZPFjLHR9nfh6J2UNhf1ZzmzVZub3mFUCLJg5HxoPxvTIJH41CMEpS8EiKcpIxxsSo-Kuf.DY_NR2Ar5Od663rj6tJQrGvKD7ZZKNfYYmcgpIQC8xxKfYt_U_DY2yP5Qjo4mTT5QX1BsT8rZoG4XL6mEukmryZZjzsLTJplePXO-8zNqrw5Q9tSMj_qTr1x9tqvZul3xg1sSxW9qx-9LdoDk3eQQQnMugzdtXyG-LQWdQjPakvyyX5mC0.U1Yk0ZDqs2v4VnL30ZKGm1Yk0Zfqs2v4VnL30A-V5HcsP0KM5gN-TZns0ZNG5yF9pywdUAY0TA-b5Hc30APGujYznWm0UgfqnH0kPdtknjD4g1DsnWPxn10kPNt1PW0k0AVG5H00TMfqPWDd0ANGujY0mhbqnW0Y0AdW5HTvn1csrjfdPdtknj0kg17xnH0zg100TgKGujYs0Z7Wpyfqn0KzuLw9u1Ys0A7B5HKxn0K-ThTqn0KsTjYzPWDkPj0YnW0d0A4vTjYsQW0snj0snj0s0AdYTjYs0AwbUL0qn0KzpWYs0Aw-IWdsmsKhIjYs0ZKC5H00ULnqn0KBI1Ykn0K8IjYs0ZPl5fKYIgnqn1D1PjDkP1bLnHmdPHnvrjnLn0Kzug7Y5HDdn1ndnWb4nHcznH60Tv-b5ymsnH-WPjTknj0snj04uHf0mLPV5HRLwjwjrRRknRfsnWDYnRc0mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5H00UyPxuMFEUHYsg1Kxn7tsg100uA78IyF-gLK_my4GuZnqn7tsg1Kxn1D3PWbkg100TA7Ygvu_myTqn0Kbmv-b5Hcvrjf1PHfdP6K-IA-b5iYk0A71TAPW5H00IgKGUhPW5H00Tydh5H00uhPdIjYs0AulpjYs0Au9IjYs0ZGsUZN15H00mywhUA7M5HD0UAuW5H00mLFW5HRvP1m%26ck%3D4341.1.69.255.370.254.361.217%26shh%3Dwww.baidu.com%26sht%3D78000241_13_hao_pg%26us%3D1.0.1.0.2.911.0%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3D78000241_13_hao_pg%26inputT%3D5192%26bc%3D110101; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpc_baidu_pc%26m_kw%3Dbaidu_cpc_cd_e110f9_d2162e_%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1533529836,1533529889,1533529921,1533529928; index_location_city=%E6%88%90%E9%83%BD; TG-TRACK-CODE=search_code; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1533531039; LGRID=20180806125036-4211d970-9934-11e8-b6f7-525400f775ce; SEARCH_ID=80a73d7184d04b198a555f14852cfd56',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?px=default&city=%E5%8C%97%E4%BA%AC',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest'
    }
    response = requests.post('https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false',headers=headers,data=form_data,proxies=proxies)
    soup=BeautifulSoup(response.text,'lxml')
    content=soup.text
    content_json=json.loads(content)
    datas=content_json['content']['positionResult']['result']
    page_ids=[]
    for data in datas:
        page_ids.append(data['positionId'])
        print(data['positionId'])
    return page_ids

page_ids=crawer(1)
for i in page_ids:
    headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie':'_ga=GA1.2.2127436673.1528115573; user_trace_token=20180604203252-6640389f-67f3-11e8-9199-525400f775ce; LGUID=20180604203252-66403ccd-67f3-11e8-9199-525400f775ce; JSESSIONID=ABAAABAABEEAAJA4CB1D1E1AB77956F4859BA82AF18E7B0; X_HTTP_TOKEN=3b5cc3e8ca1a47cc3fe9029cdefa1645; _gid=GA1.2.1116473640.1533529836; WEBTJ-ID=20180806123128-1650d81174810c-0903bd9e60ebba-47e1039-1049088-1650d81174c16b; index_location_city=%E6%88%90%E9%83%BD; TG-TRACK-CODE=search_code; LGSID=20180806165223-09006735-9956-11e8-b714-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1533529921,1533529928,1533545546,1533545551; SEARCH_ID=29ec05c8acd142a984e1de20f0144c93; _gat=1; LGRID=20180806171806-a129c8cd-9959-11e8-a341-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1533547090',
        'Host': 'www.lagou.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    page_response=requests.get('https://www.lagou.com/jobs/{0}.html'.format(i),headers=headers)
    page_soup=BeautifulSoup(page_response.text,'lxml')
    zhiweiyouhuo=page_soup.select('#job_detail > dd.job-advantage')[0]
    print(zhiweiyouhuo.text)
