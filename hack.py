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
ver='0.01_beta'
btc='https://btc.com/13AM4VW2dhxYgXeQepoHkHSQuy6NgaEb94'
reg=r'class="tx-item-summary-hash">(.*)</a>'
r=requests.get(btc)
print(u'请将在列出的比特币交易ID中选择一串，复制粘贴到勒索软件的Contact us,等待黑客验证后，点击check payment再点击Decypt即可恢复\n' if language else 'Please select one transaction ID，and paste it to the Contact us ,after the hacker confirmed,click Chek payment and then click Decrypt\n')
for txid in re.findall(reg,r.text):
    print(txid)
    th=u'衷心希望这个破解脚本能够帮到你的忙，特别是即将毕业缺丢失毕业论文的大四学长。\n当前版本是0.01beta，效果有待验证,欢迎到我的GitHub反馈：https://github.com/QuantumLiu\n很惭愧，只做了一点微小的工作。\n如果这个脚本有帮到你,欢迎进行小额捐助.\nBTC：19UYnNM1hBduDQq8Z9G3Ld6FD5zjH4TKB7\nzcash:t1ghVzHQRxkCm8vzLRzbfNTTxip3LkZB2sA\n 支付宝alipay：liuyiliang100@sina.com\n'
    th+=u'方法来自：https://www.zhihu.com/pin/846570592869183488#comment-280580859'
print(th)
os.system('pause')
