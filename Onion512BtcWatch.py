#!/usr/bin/env python
# -*- coding: utf-8 -*-

# athor out0fmemory
# email jiu4majia2@163.com
# just for fun do this to look how much BTC the decryptor author can get>_<
# write this at 17.5.14, middle night with no sleeping

import requests
import re
import string
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

def count_the_decryptor_btc_received():
    btc_list = [add for add in['13AM4VW2dhxYgXeQepoHkHSQuy6NgaEb94', '12t9YDPgwueZ9NyMgw519p7AA8isjr6SMw', '115p7UMMngoj1pMvkpHijcRdfJNXj6LrLn']]
    reg = r'class="tx-item-summary-hash">(.*)</a>'
    #Balance</dt>
    #<dd> 3.4552<span class="text-muted">1512</span> BTC </dd>
    reg_receive_btc = "Balance([\s\S.*]+)<dd> ([0-9]+.[0-9]+)<span class=\"text-muted\">([0-9]+)</span> BTC </dd>"
    reg_receive_btc_main = "<dd> (.*)<span"
    reg_receive_btc_sub = "<span class=\"text-muted\">(.*)</span>"
    # <dt>Tx Count</dt>
    # <dd> 29 </dd>
    reg_receive_cnt_btc = "<dt>Tx Count</dt>([\s\S.*]+)<dd> ([0-9]+) </dd>"
    reg_receive_cnt_btc_main = "<dd> ([0-9]+) </dd>"
    receive_count = 0
    receive_btc_num = 0
    for btc in btc_list:
        url = 'https://btc.com/'+ btc
        r = requests.get(url)
        #count the btc received
        receive = re.search(reg_receive_btc, r.text).group(0)
        main_num = re.search(reg_receive_btc_main, receive).group(1)
        sub_num = re.search(reg_receive_btc_sub, receive).group(1)

        receive_btc = string.atof(main_num) + string.atof(sub_num)/100000000
        receive_btc_num += receive_btc

        #count the btc receive count
        receive_count_str = re.search(reg_receive_cnt_btc, r.text).group(0)
        count = re.search(reg_receive_cnt_btc_main, receive_count_str).group(1)
        receive_count += string.atoi(count)

        print "The Wana Decryptor\'s BTC address:" + btc + " had received:" + str(receive_btc) + " BTC, and received from " +\
            count + "user!"
        print "勒索者病毒作者的BTC地址:" + btc + " 收到:" + str(receive_btc) + " BTC, 有 " + \
              count + "个用户发送BTC到此账户!\n"

    print "The Wana Decryptor\'s " + str(len(btc_list)) + " BTC address had all received:" + str(receive_btc_num) +\
        " BTC, worth about " + str(receive_btc_num * 10000) + " RMB, and received from " + str(receive_count) + " user!" \
                                                          "\nAnd is This Worth to do this hack ??? just funny..." \
                                                          "but of course, much than our program-monkeys\n\n"
    print "勒索者病毒作者的 " + str(len(btc_list)) + " 个BTC 地址一共收到:" + str(receive_btc_num) + \
          " BTC, " "大约值 " + str(receive_btc_num * 10000) + " 人民币，有 " + str(receive_count) + " 个用户发送了比特币!" \
                                                            "\n这么几个比特币值得搞这么大影响么??? 搞笑了..." \
                                                            "当然，肯定比我们程序猿挣得多得多得多咯>_<"

if __name__ == '__main__':
    count_the_decryptor_btc_received()
