# coding=utf-8

from requests.exceptions import RequestException
import requests
import json
import csv
import re
import os

class Spider(object):

    def __init__(self):
        self.headers = {
            'Accept': 'application / json, text / javascript, * / *; q = 0.01',
            'Accept - Encoding': 'gzip, deflate, br',
            'Accept - Language': 'zh - CN, zh; q = 0.9',
            'Connection': 'keep - alive',
            'Host': 'www.renrendai.com',
            'Referer': 'https: // www.renrendai.com / loan.html',
            'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
            'X - Requested - With': 'XMLHttpRequest',
            'Cookie': 'rrdid=de4b025e-388c-40f2-aa2b-e1d5a15ab8bb; __jsluid_s=90329cc68020c5ce26129949507335e1; gr_user_id=892dec57-971e-4744-86e0-479fba3d77e9; _ga=GA1.2.1044072481.1585795990; _gid=GA1.2.721099571.1585795990; grwng_uid=353925d7-0955-4229-ad7a-113d39a0830a; registerSource=web_top; renrendaiUsername=15736096955; loginMethod=password; __jsluid_h=5c773442c354da5e2f412fca4255b5f5; IS_MOBLIE_IDPASS=true-false; jforumUserInfo=jUtbT%2BGCTMd2p5a7yWYvscQ%2F4ReYAq2jFJN6FcAwPsE%3D%0A; Qs_lvt_181814=1585797181%2C1585797683%2C1585801259%2C1585806560%2C1585814372; Hm_lvt_a00f46563afb7c779eef47b5de48fcde=1585797684,1585801259,1585806560,1585814373; activeTimestamp=18084010; we_token=MVZ3cTlKUmZ5ZUptc1pPSnFwNVI2Ync0b0V3dGhfbGU6MTgwODQwMTA6ZWI1ZTUwZjA1OTMxY2NhOThkY2JjN2NmNzcyZDdmY2U2YzI5OTdmZA%3D%3D; we_sid=s%3AXnfhGJFEGxAcsk3nCIScpgflurgKbxJO.vBQkQiaqmWYW29UnqSeXbKolezZeD0yKyVNVfUsRobc; bf0acacc0a738790_gr_last_sent_sid_with_cs1=41c2d394-9397-493b-9968-ab1830b923aa; bf0acacc0a738790_gr_last_sent_cs1=18084010; bf0acacc0a738790_gr_session_id=41c2d394-9397-493b-9968-ab1830b923aa; bf0acacc0a738790_gr_session_id_41c2d394-9397-493b-9968-ab1830b923aa=true; gr_session_id_bcefa7ae4a57ec9d=cb7db849-3b1e-490a-ab8b-ce7c03262e72; gr_session_id_bcefa7ae4a57ec9d_cb7db849-3b1e-490a-ab8b-ce7c03262e72=true; _gat=1; JSESSIONID=D32AA44C197E784B00CB59EB899D0DDF; bf0acacc0a738790_gr_cs1=18084010; Hm_lpvt_a00f46563afb7c779eef47b5de48fcde=1585816218; Qs_pv_181814=4488195701451093000%2C2645309187173905000%2C2200702580297503000%2C1272394866985211600%2C4590454562721553400'

        }
        self.count = 0 # 记录成功爬取的条数


    # 获取散标信息
    def get_sanbiao(self):
        # 一共1000条，爬10次，每次100条
        for page in range(10):
            url = 'https://www.renrendai.com/loan/list/loanList?startNum={}&limit=100'.format(page)
            try:
                response = requests.get(url, headers=self.headers)
                if response.status_code == 200:
                    self.parse_sanbian(response.text)
            except RequestException as e:
                print(e)


    # 解析散标信息
    def parse_sanbian(self, data):
        data = json.loads(data)
        for item in data['data']['list']:
            url = 'https://www.renrendai.com/loan-{}.html'.format(item['loanId'])
            self.get_detailinfo(url)


    # 获取详细信息
    def get_detailinfo(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                self.count += 1
                print('成功爬取第 {} 条'.format(self.count))
                self.parse_detailinfo(response.text)
            else:
                print('failure: {}'.format(url))
        except RequestException as e:
            print(e)


    # 解析详细信息
    def parse_detailinfo(self, data):
        data = data.replace(u'\xa9', u'').replace('\\u0022', '"').replace('\\u005C', '\\')  # gbk无法对u'\xa9'代表的字符进行编码，在Unicode中u'\xa9'代表的是©。因此直接忽略掉。
        data = re.compile("var info = '({.*?})'", re.S).findall(data)
        data = json.loads(data[0])
       # print(data['borrower'])
        result = {}
        # 顶部信息
        result['loanId'] = data['loan']['loanId'] # Number
        result['borrowType'] = data['loan']['borrowType'] # 贷款类型
        result['amount'] = data['loan']['amount'] #标的总额
        result['interest'] = data['loan']['interest'] # 年利率
        result['months'] = data['loan']['months'] # 还款期限
        result['creditLevel'] = data['borrower']['creditLevel']  # 风险等级
        result['repayType'] = '按季还款' if int(data['loan']['repayType']) else '按月还款' # 还款方式
        result['loanType'] = '等额本息' if data['loan']['loanType'] == 'DEBX' else '付息还本' #借贷方式
        result['repaySource'] = data['repaySource']  # 还款来源
        # 借贷人信息
        result['realName'] = data['borrower']['realName']  # 姓名
        result['gender'] = data['borrower']['gender'] # 性别
        result['age'] = 2019-int(data['borrower']['birthDay'][:4]) # 年龄
        result['marriage'] = '已婚' if data['borrower']['marriage'] else '未婚' # 婚姻
        result['graduation'] = data['borrower']['graduation']  # 学历
        result['salary'] = data['borrower']['salary'] # 收入
        result['houseLoan'] = '有' if data['borrower']['houseLoan'] else '无'  # 房贷
        result['carLoan'] = '有' if  data['borrower']['carLoan'] else '无' # 车贷
        result['officeDomain'] = data['borrower']['officeDomain'] # 公司行业
        result['hasOthDebt'] =data['hasOthDebt'] # 其他负债
        # 信用信息
        result['totalCount'] = data['userLoanRecord']['totalCount'] # 申请借款
        result['successCount'] = data['userLoanRecord']['successCount']  # 成功借款
        result['alreadyPayCount'] = data['userLoanRecord']['alreadyPayCount']   # 还清笔数
        result['availableCredits'] = data['borrower']['availableCredits']  #信用额度
        result['borrowAmount'] = data['userLoanRecord']['borrowAmount']  # 借款总额
        result['notPayTotalAmount'] = data['userLoanRecord']['notPayPrincipal']+data['userLoanRecord']['notPayInterest']  # 待还本息
        result['overdueTotalAmount'] = data['userLoanRecord']['overdueTotalAmount']   # 逾期金额
        result['overdueCount'] = data['userLoanRecord']['overdueCount']  # 逾期次数
        result['failedCount'] = data['userLoanRecord']['failedCount']  # 严重逾期
        self.save_excel(list(result.values()))


    # 存到excel
    def save_excel(self, data):
        out = open('人人贷.csv', 'a', newline='')
        write = csv.writer(out, dialect='excel')
        write.writerow(data)


    def run(self):
        if os.path.exists('./人人贷.csv'):
            os.remove('./人人贷.csv')
        self.save_excel('序号 贷款类型 标的总额 年利率 还款期限 风险等级 还款方式 借贷方式 还款来源'
              ' 姓名 性别 年龄 婚姻 学历 收入 房贷 车贷 公司行业 其他负债'
              ' 申请借款 成功借款 还清笔数 信用额度 借款总额 待还本息 逾期金额 逾期次数 严重逾期'.split(' '))
        self.get_sanbiao()


if __name__ == '__main__':
    spider = Spider()
    spider.run()
