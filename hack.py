# -*- coding: utf-8 -*-
"""
Created on Sat May 13 08:47:08 2017

@author: Quantum Liu
"""

import requests
import re
import win32api
import os
if win32api.GetSystemDefaultLangID()==2052:
    language=1#chinese
else:
    language=0#english
ver='0.2.0beta'
btc_list=['https://btc.com/'+add for add in['13AM4VW2dhxYgXeQepoHkHSQuy6NgaEb94','12t9YDPgwueZ9NyMgw519p7AA8isjr6SMw']]
reg=r'class="tx-item-summary-hash">(.*)</a>'
r_list=[requests.get(btc) for btc in btc_list]
print(u'请将在列出的比特币交易ID中选择一串，复制粘贴到勒索软件的Contact us,等待黑客验证后，点击check payment再点击Decypt即可恢复\n' if language else 'Please select one transaction ID，and paste it to the Contact us ,after the hacker confirmed,click Chek payment and then click Decrypt\n')
for r in r_list:
    for txid in re.findall(reg,r.text):
        print(txid)
        th=u'方法来自：https://www.zhihu.com/pin/846570592869183488#comment-280580859'
print(th)
os.system('pause')
