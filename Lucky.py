import sys,requests,webbrowser,bs4,re
doc =  ''' 
"{}" Command not Found
For using : python lucky.py [OPTION] [VALUE] 
                    exampel : - python lucky.py -s  "HamzaOPLEX"
                    or >>     - python lucky.py --search "HamzaOPLEX" 
                    output >> HamzaOPLEX'''                               
def lucky(keywords) :
    for i in keywords :
        print("Googling...")
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.0.2990 Safari/537.36'
        req = requests.get("https://www.google.com/search?q="+i,headers={"User-Agent":user_agent})
        print("Your URL is :",req.url)
        page = req.text
        bs4_url = bs4.BeautifulSoup(page,features="lxml")
        links =  bs4_url.select(".r a")
        for G in links :
            good_url = G.get('href')
        pages = input("How many pages you want :")
        if pages.isalpha() or pages=="" :
            for j in links :
                a = j.get("href")
                if a == "#" or a == "" :
                    a= ""
                else :
                    sub_url = re.sub("https://(webcache|translate).*","", a)
                    print(sub_url.strip())
                    webbrowser.open(sub_url)
        if pages.isdigit() :
            k = 1
            for k in range(int(pages)) :
                    a = links[k].get("href")
                    if a == "#" or a == "" :
                        a = ''
                    else :
                        sub_url = re.sub("https://(webcache|translate).*","", a.strip())
                        print(sub_url.strip())
                        webbrowser.open(sub_url)
if len(sys.argv) > 1 :       # -s / --search
    if sys.argv[1] == "-s" or sys.argv[1] == "--search" :
        lucky(sys.argv[2::])
    elif sys.argv[1] != "-s" or sys.argv[1] != "--search" : 
        print(doc.format(sys.argv[1]))
else :
    print("No argument")
