import hashlib
import http.client
import json
import os
import random
import re
import shutil
import time
import urllib.parse

####################
"""


缺陷：
    目前只支持百度
    翻译时，有时翻译会把[1]标记吞掉，导致部分 不翻译字符串 {}|[] 丢失
    目前还未匹配 %abc 类标记

"""

#####################
# 你的appid
appid = input('请输入你的百度appid：')
# 你的密钥
secretKey = input('请输入你的百度secretKey：')
fromLang = input('请输入源语言(如en)：')  # 源语言
toLang = input('请输入目标语言(如zh)')


def baidu_translation(content):
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = content

    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign + "&action=1"

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()  # response是HTTPResponse对象
        jsonResponse = response.read().decode("utf-8")  # 获得返回的结果，结果为json格式
        js = json.loads(jsonResponse)  # 将json格式的结果转换字典结构
        text = ""
        dict1 = {}
        for i in js["trans_result"]:
            dict1[i["src"]] = i["dst"]
        return (dict1)  # 打印结果
    except Exception as e:
        print(e)


def appendtxt(path1):
    dict1 = {}
    with open(path1, "r", encoding="utf8") as f:
        txtlist = f.readlines()
    for i in range(len(txtlist) - 1):
        if re.findall('""', txtlist[i + 1]):  # 查找第二行是否有 ""
            list1 = re.findall('#.*"(.*?)".*\n|old.*"(.*?)".*\n', txtlist[i])  # 有，则提取出""中文本
            if list1 != []:
                dict1[i] = (list1[0][0] + list1[0][1]).strip(" ") + "\n\n"  # 放入字典

    with open(os.path.dirname(__file__) + "\翻译.json", "w", encoding="utf8") as f:
        f.write(json.dumps(dict1, ensure_ascii=False, indent=4))  # 写入json


def tran(path1):
    try:
        os.mkdir(os.path.split(path1)[0] + "\\new\\")  # 在翻译文本目录创建new文件夹
    except:
        pass
    path2 = os.path.split(path1)[0] + "\\new\\" + os.path.split(path1)[1]
    print(path2)

    if not os.path.isfile(path2):
        shutil.copyfile(path1, path2)  # 复制文件到new文件夹

    appendtxt(path2)
    with open(os.path.dirname(__file__) + "\翻译.json", "r", encoding="utf8") as f:
        data = json.loads(f.read())  # 读取json字典

    key = list(data.keys())
    value = list(data.values())
    text = ""
    keylist = []
    i = 0
    num = 0
    dict1 = {}

    for i in range(len(data)):

        keylist.append(key[i])  # 添加当前翻译字符串列表
        text = text + value[i]  # 字符串拼接
        # print(i)
        if len(text) > 3000:  # 字符串长度大于3000

            time.sleep(1)
            text = text.replace(value[i], "", 1)  # 去除最后一个字符串
            del keylist[-1]  # 当前翻译字符串列表去除最后一个字符串
            while True:

                notran1 = re.findall("\[.*?]|{.*?}", text)  # 查找[] | {}不翻译字符串
                for itx in notran1:
                    text = text.replace(itx, "[" + str(num) + "]", 1)  # 如[name]替换为[1]
                    dict1["[" + str(num) + "]"] = itx  # 写入字典"[1]":"[name]"
                    num = num + 1  # 编号加1

                trandict = baidu_translation(text)  # 调用百度api翻译，返回dict,键值对为oldtxt:trantxt，或者自己写接口

                trandictkey = list(trandict.keys())  # 获取oldtxt
                for k in trandictkey:

                    if "[" in k:  # 判断是否有[]
                        for ixxxx in re.findall("\[.*?]", k):  # 查找[]
                            trandict[k] = trandict[k].replace(ixxxx, dict1[ixxxx],
                                                              1)  # 通过[num]在字典中找到对应的不翻译字符串，替换的是value
                        k0 = k
                        for ixxxx in re.findall("\[.*?]", k):
                            k = k.replace(ixxxx, dict1[ixxxx], 1)  # 通过[num]在字典中找到对应的不翻译字符串，替换的是key

                        trandict[k] = trandict.pop(k0)  # 替换key,并删除就键值对

                if trandict:  # 如果百度api返回结果，为真，结束翻译；为假，再次翻译
                    time.sleep(1)
                    break

            with open(path2, "r", encoding="utf8") as f:
                txtlists = f.readlines()  # new文件夹下文件，行读取

            for ix in range(len(keylist)):
                print((keylist[ix]))
                print(data[str(keylist[ix])])
                print(trandict[data[str(keylist[ix])].split("\n\n")[0].strip(" ")])
                # 把翻译的到文本填入“”中
                txtlists[int(keylist[ix]) + 1] = txtlists[int(keylist[ix]) + 1].replace('""', '"' + trandict[
                    data[str(keylist[ix])].split("\n\n")[0].strip(" ")] + '"')

            with open(path2, "w", encoding="utf8") as f:
                f.writelines(txtlists)  # 写入文件

            keylist = []  # 清空列表

            text = value[i]  # 添加上次未翻译文本
            keylist.append(int(key[i]))  # 添加上次未翻译文本

        #######################
    if text:  # 总文本小于3000，即收尾，原理相同
        while True:

            notran1 = re.findall("\[.*?]|{.*?}", text)
            for itx in notran1:
                text = text.replace(itx, "[" + str(num) + "]", 1)
                dict1["[" + str(num) + "]"] = itx
                num = num + 1

            trandict = baidu_translation(text)
            trandictkey = list(trandict.keys())
            for k in trandictkey:

                if "[" in k:

                    for ixxxx in re.findall("\[.*?]", k):
                        trandict[k] = trandict[k].replace(ixxxx, dict1[ixxxx], 1)
                    k0 = k
                    for ixxxx in re.findall("\[.*?]", k):
                        k = k.replace(ixxxx, dict1[ixxxx], 1)

                    trandict[k] = trandict.pop(k0)

            if trandict:
                time.sleep(1)
                break

        with open(path2, "r", encoding="utf8") as f:
            txtlists = f.readlines()

        for ix in range(len(keylist)):
            print("############################")  #####之间可以x掉
            print((keylist[ix]))
            print(data[str(keylist[ix])])
            print(trandict[data[str(keylist[ix])].split("\n\n")[0].strip(" ")])
            print("############################")  ####之间可以x掉

            txtlists[int(keylist[ix]) + 1] = txtlists[int(keylist[ix]) + 1].replace('""', '"' + trandict[
                data[str(keylist[ix])].split("\n\n")[0].strip(" ")] + '"')

        with open(path2, "w", encoding="utf8") as f:
            f.writelines(txtlists)


def get_rpypath(txtpath):
    rpy_pathlist = []
    for parent, dirnames, filenames in os.walk(txtpath):
        for filename in filenames:

            if '.rpy' == os.path.splitext(filename)[1]:
                # print(os.path.join(parent, filename)
                if "new" in parent:
                    continue
                rpy_pathlist.append(os.path.join(parent, filename))
    return rpy_pathlist


if __name__ == "__main__":
    path0 = input("请输入文件路径：(如D:\game\tl\chinese目录下)")
    pathlist = get_rpypath(path0)
    for i in pathlist:
        tran(i)
