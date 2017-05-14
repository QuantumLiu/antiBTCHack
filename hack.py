# -*- coding: utf-8 -*-
"""
Created on Sat May 13 08:47:08 2017

@author: Quantum Liu
"""

from __future__ import print_function
import re
import sys

ver = '0.31beta'

address = [
    '13AM4VW2dhxYgXeQepoHkHSQuy6NgaEb94',
    '12t9YDPgwueZ9NyMgw519p7AA8isjr6SMw',
    '115p7UMMngoj1pMvkpHijcRdfJNXj6LrLn']

reg = r'class="tx-item-summary-hash">(.*)</a>'

def downloader(url):
    if sys.version[0] == '2':
        import urllib2
        r = urllib2.urlopen(url).read()
        return r
    else:
        import urllib.request
        r = urllib.request.urlopen(url).read().decode('utf-8')
        return r

for add in address:
    btc = 'https://btc.com/'+add 
    resp = downloader(btc)
    txid = re.findall(reg, resp)
    for tx in txid:
        print(tx)

print('\n请将在列出的比特币交易ID中选择一串，复制粘贴到勒索软件的Contact us,等待黑客验证后，点击check payment再点击Decypt即可恢复')
print('Please select one transaction ID，and paste it to the Contact us ,after the hacker confirmed,click Chek payment and then click Decrypt\n')
print('方法来自/form：https://www.zhihu.com/pin/846570592869183488')
