#coding: utf-8
import json

def receivesheng(name): 
    
    if name.find(u"省",1) !=-1:
        name=name.split(u'省')
        namea=name[0]+u"省"
        nameb=name[1]
        
    elif  name[0] in [u"北",u"天",u"重",u"上"]:
        namea=name[:2]
        nameb=name
        
    else:
        namea=name[:2]+u"省"
        nameb=name[2:]
        
    return namea,nameb
        
def receiveshi(name):    
    if name.find(u"市",1) !=-1:
        name=name.split(u'市')
        namea=name[0]+u"市"
        nameb=name[1]
       
    else:
        namea=name[:2]+u"市"
        nameb=name[2:]
        
    return namea,nameb
    
def receivexian(name):    
    if name.find(u"县",1) !=-1:
        name=name.split(u'县')
        namea=name[0]+u'县'
        nameb=name[1]
        
    elif name.find(u"区",1) !=-1:
        name=name.split(u'区')
        namea=name[0]+u"区"
        nameb=name[1]

    elif name.find(u"市",1) !=-1:
        name=name.split(u'市')
        namea=name[0]+u"市"
        nameb=name[1]
    else:
        namea=""
        nameb=name
       
    return namea,nameb
        
def receivezhen(name):    
    if name.find(u"镇",1) !=-1:
        name=name.split(u'镇')
        namea=name[0]+u'镇'
        nameb=name[1]
    elif name.find(u"街",1) !=-1:
        nameb=name.split(u'街')
        if name.find(u"道",1)-name.find(u"街",1)==1:
            namea=nameb[0]+u'街道'
            nameb=nameb[1][1:]
        else:
            namea=nameb[0]+u'街'
            nameb=nameb[1]    
       
    elif name.find(u"乡",1) !=-1:
        name=name.split(u'乡')
        namea=name[0]+u"乡"
        nameb=name[1]
       
    else:
        namea=""
        nameb=name
       
    return namea,nameb

def receivelu(name):    
    if name.find(u"路",1) !=-1:
        name=name.split(u'路')
        namea=name[0]+u'路'
        nameb=name[1]
    else:
        namea=""
        nameb=name
       
    return namea,nameb

def receivehao(name):    
    if name.find(u"号",1) !=-1:
        name=name.split(u'号')
        namea=name[0]+u'号'
        nameb=name[1]
    else:
        namea=""
        nameb=name
    return namea,nameb

def receivenumber(str):
    if str.find('1',1) != -1:
        start=str.find('1')
        newstr=str[start:start+11]
        newstr_=str[:start]+str[start+11:]
        return newstr,newstr_
    else:
        return "",str

def receivename(str):
    str=str.replace('.','')
        
    if str.find(',') !=-1:
        str=str.split(',')
        return str[0],str[1]
    else:
        return "",str
    

def main():
    need={}
    shuju=input()
    if(shuju[0]=='1'):
        a=1
    else:
        a=0
    shuju=shuju[2:]
    name,T=receivename(shuju)
    number,T=receivenumber(T)
    sheng,T=receivesheng(T)
    shi,T=receiveshi(T)
    xian,T=receivexian(T)
    zhen,T=receivezhen(T)
    if a==1:
        dizhi=[sheng,shi,xian,zhen,T]
    else:
        lu,T=receivelu(T)
        hao,T=receivehao(T)
        dizhi=[sheng,shi,xian,zhen,lu,hao,T]
    need[u"姓名"]=name
    need[u"手机"]=number
    need[u"地址"]=dizhi
    json_need=json.dumps(need)
    print(json_need)
    #print(need)
    

main()
