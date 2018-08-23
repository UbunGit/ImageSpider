#!/usr/bin/env python
# encoding: utf-8

import re
import requests

class tbimage():
    def __init__(self,key,pageNum,savepath):

        self.url = 'https://s.taobao.com/search'
        self.payload = {'q':key, 's':'1', 'ie':'utf8'}  #字典传递url参数
        self.pageNum =  int(pageNum)
        self.savepath =  savepath
        imgelist = self.getImgeurlList()
        self.downImge(imgelist)


    def getImgeurlList(self):

        imagelist = []

        for i in range(0,self.pageNum):        #10次，就是10页的商品数据

            self.payload['s'] = 44 * i + 1   #此处改变的url参数为s，s为1时第一页，s为45是第二页，89时第三页以此类推
            resp = requests.get(self.url, params=self.payload)
            resp.encoding = 'utf-8'  #设置编码
            imagelist = imagelist+re.findall(r'pic_url":"//(.*?)"', resp.text, re.I)
        return imagelist;

    def downImge(self,imagelist):

        for i in range(0,len(imagelist)):
            imageurl = "http://"+ str(imagelist[i]).encode("utf-8") ;
            print(imageurl)
            file = savepath+"/"+str(i)+".jpg"
            ir = requests.get(imageurl)
            sz = open(file, 'wb').write(ir.content)
        print("done:共计："+str(len(imagelist)))


if __name__ == '__main__':


    #url = "https://www.processon.com/i/570f38cbe4b0a2221694a2f5";
    print("\n")
    print("===根据关键字获取淘宝商品列表图片===")
    print("根据提示：")
    print("1：输入你的关键字 ")
    print("2：输入你所需页数（每页44个）")
    print("3：输入保存路径 ")
    print("===================================")
    print("  输入你的关键字:")
    key = raw_input()
    print("  输入你所需页数（每页44个）:")
    pagenum = raw_input()
    print("  输入保存路径:")
    savepath = raw_input()
    try:
        print("开始获取关键字为："+key+"的商品图片")
        runlop = tbimage(key,pagenum,savepath)
    except Exception as e:
        print("error"+str(e))
        print("================end================")



