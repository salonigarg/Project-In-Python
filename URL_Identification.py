import urllib
import nltk
import urllib2
from bs4 import BeautifulSoup
import re
list=['cricket','tennis','badminton','hockey','basketball','football','archery','fifa','hoopshype']

def read_file():
    user_input=raw_input("ente the file name:")#input_file.txt
    f =open(user_input,"r")
    for line in f:
        main_line=line.rstrip()
        if main_line:
            main(main_line)
    f.close()

    
def list_checker(tokens):
    flag=0
    for t in tokens:
        if t.lower() in list:
            flag=1
            if t.lower()=='fifa':
                print "football"
                break
            elif t.lower()=='hoopshype':
                print "basketball"
                break
            else:
                print t 
                break
    return flag
    
def check(url):
    try:
        urllib2.urlopen(url)
        return "True"
    except urllib2.URLError:
        return "False"

def main(url):
    token=[]
    url=url.lstrip()
    print  url
    if url[0:8]=='https://' or url[0:7]=='http://':
        value=check(url)
        print value
        if value.lower()=="true":
            connection=urllib.urlopen(url)
            html1=connection.read()
            regex_title="<title>(.+?)</title>"
            pattern=re.compile(regex_title)
            title_result=re.findall(pattern,html1)
            title_res_string=''.join(title_result) #for converting back entire list to string
            title_list=title_res_string.split()
                # for splitting string into token in list
                #print title_list
            flag=list_checker(title_list)
                #print flag
            k=0
            if flag!=1:
                for t in title_list:
                    if t.lower()=='yahoo' or t.lower()=='youtube':
                        k=1
                        print 'N/A'
                        break
           
            if flag!=1 and k!=1:
                soup=BeautifulSoup(html1,'html.parser')
                raw1=soup.get_text()
                token=nltk.word_tokenize(raw1)
                f=list_checker(token)
                if f==0:
                    print  'N/A'
            print "________________________________________________"
            connection.close()
        else:
            print "website does not exist"
            print "________________________________________________"
    else:
        print "website does not exist"
        print "________________________________________________"
        
read_file()
