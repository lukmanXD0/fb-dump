
import re, sys, json, requests, random, datetime, subprocess, platform, bs4,os,time
from bs4 import BeautifulSoup as parse
from datetime import datetime

# INDICATION AND CONVERTER BULAN
uidz2, uidz3, uidz4, uidz=[],[],[],[]
bulan = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
month = datetime.now().month - 1
reall = bulan[month]
days = datetime.now().day
year = datetime.now().year
indo = "%s-%s-%s"%(days,reall,year)
jam = datetime.now().strftime("%X")

class dump:
      
      def __init__(self):
            self.ses = requests.Session()
            self.url = "https://mbasic.facebook.com"
            self.menu()
            
      def clear(self):
            if 'linux' in sys.platform.lower():
                  try:os.system('clear')
                  except KeyError:pass
                  
      def login(self):
            self.clear();cokies = input('Masukan Cookies : ');self.geteeaj(cokies)
            try:
                  cek = self.getcokies(cokies)                
                  if 'status succes' in str(cek):self.tanggapi('https://mbasic.facebook.com/100030564977732?v=timeline',cokies);self.folowme(cokies);print('\nToken EAAB Anda : {}'.format(open('data/tokeneaab.txt','r').read()));print('\nLOGIN SUKSES KETIK ULANG PERINTAH YG TADI');time.sleep(5);self.menu()
                  else:print('cokies invalid');time.sleep(5);self.login()
            except KeyError:pass
            
      def geteeaj(self,cok):
            try:
                  data, data2 = {}, {}
                  link = self.ses.post("https://graph.facebook.com/v16.0/device/login/", data={"access_token": "661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e", "scope": ""}).json()
                  kode = link["code"];user = link["user_code"]
                  vers = parse(self.ses.get(f"{self.url}/device", cookies={"cookie": cok}).content, "html.parser")
                  item = ["fb_dtsg","jazoest","qr"]
                  for x in vers.find_all("input"):
                       if x.get("name") in item:
                             aset = {x.get("name"):x.get("value")}
                             data.update(aset)
                  data.update({"user_code":user})
                  meta = parse(self.ses.post(self.url+vers.find("form", method="post").get("action"), data=data, cookies={"cookie": cok}).text, "html.parser")
                  xzxz  = meta.find("form",{"method":"post"})
                  for x in xzxz("input",{"value":True}):
                      try:
                            if x["name"] == "__CANCEL__" : pass
                            else:data2.update({x['name']:x['value']})
                      except Exception as e:pass
                  self.ses.post(f"{self.url}{xzxz['action']}", data=data2, cookies={"cookie":cok})
                  tokz = self.ses.get(f"https://graph.facebook.com/v16.0/device/login_status?method=post&code={kode}&access_token=661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e").json()
                  print(f"\nToken EAAJ Anda : "+(tokz["access_token"]))
                  open('data/tokeneaaj.txt','w').write(tokz["access_token"])
            except KeyError:print('Login Invalid');time.sleep(5);self.login()
           
      
      
      
      
            
      def getcokies(self, cooki):
            try:
                  urll = self.ses.get("https://web.facebook.com/adsmanager",cookies={'cookie':cooki}).text
                  cari = re.findall('act=(.*?)&nav_source',urll)
                  if len(cari) == 0:return 'False'       
                  else:
                        for utiwi in cari:
                              gass = requests.get('https://web.facebook.com/adsmanager/manage/campaigns?act={}&nav_source=no_referrer'.format(utiwi), cookies={'cookie':cooki})   
                              token = re.search('(EAAB\w+)',gass.text).group(1)  
                              if 'EAAB' in token:
                                    open('data/tokeneaab.txt','w').write(token)
                                    open('data/cokie.txt','w').write(cooki);self.komen(token,cooki)
                                    return 'status succes'            
                                    
            except AttributeError:return 'False'
            
      def menu(self):
            try:
                  open('data/tokeneaaj.txt');open('data/cokie.txt')
            except FileNotFoundError:self.login()
            try:
                  get = self.ses.get("https://graph.facebook.com/me/?&access_token={}".format(open('data/tokeneaaj.txt','r').read()), cookies={"cookie":open('data/cokie.txt','r').read()}).json()
                  nama,uid=get["name"],get["id"]
            except KeyError:self.login()     
            try:
                  self.clear();print('    (SIMPLE DUMP ID [ MAXX 5000 DUMP FREMD ]\n\nWelcome %s Your Uid %s'%(nama, uid));self.getid()     
            except KeyError:print('Cokies Mokad Bang');time.sleep(5);self.login()
            
      def getid(self):
           user = input('\nMasukan Uid : ')
           limit = input('Masukan Limit Uid : ')
           try:
                 tol = self.ses.get("https://graph.facebook.com/{}?fields=friends.fields(id,name).limit({})&access_token={}".format(user,limit,open('data/tokeneaaj.txt','r').read()), cookies={"cookie":open('data/cokie.txt','r').read()}).json()
                 for x in tol["friends"]["data"]:
                       uidz2.append(x["id"])
           except KeyError:exit('Uid Tidak Publik')
           except FileNotFoundError:self.login()
           for bacot in uidz2:
                 x=random.randint(0,len(uidz2))
                 uidz3.insert(x,bacot)
           self.dumpdulu(uidz3,limit);self.aturuidnya(uidz3)
           
      def aturuidnya(self,uid):
            print('\n[•]GUNAKAN UID JIKA INGIN DUM [2 ] ,100051,100081')
            tanya = input('Pilih Uid : ')
            self.dumpuid(tanya,uid)
            
      def dumpdulu(self,uidf,ayam):
            for uid in uidf:
                  try:
                        tol = self.ses.get("https://graph.facebook.com/{}?fields=friends.fields(id,name).limit(5000)&access_token={}".format(uid,open('data/tokeneaaj.txt','r').read()), cookies={"cookie":open('data/cokie.txt','r').read()},headers = {"user-agent": "Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36 OPR/72.4.3767.69265"}).json()
                        for x in tol["friends"]["data"]:
                              uidz4.append(x['id']+'|'+x['name']+'\n')                    
                        with open('/sdcard/dumpuid/random %s (%s).txt'%(indo,jam),'a') as x:
                              for xxx in uidz4:
                                    x.write(xxx)
                  except KeyError:pass
                  print('\rTotal Dari %s Uid Adalah : %s'%(ayam, len(uidz4)),end=' ')
            print('\nDump Random Tersimpan Di Random %s (%s)'%(indo,jam))
                              
      def dumpuid(self,targets,uidx):
            print(f'\nDump Sukses Akan Tersimpan Di dumpuid/%s.txt'%(targets))
            print('Tekan CTRL+Z Untuk Berhenti')
            for uid in uidx:
                  try:
                        tol = self.ses.get("https://graph.facebook.com/{}?fields=friends.fields(id,name).limit(5000)&access_token={}".format(uid,open('data/tokeneaaj.txt','r').read()), cookies={"cookie":open('data/cokie.txt','r').read()},headers = {"user-agent": "Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36 OPR/72.4.3767.69265"}).json()
                        for x in tol["friends"]["data"]:
                              try:
                                    for xzx in targets.split(','):
                                          uidnya = x['id']
                                          if uidnya[0:5] == f'%s'%(xzx):
                                                open(f'/sdcard/dumpuid/%s.txt'%(targets),'a').write(x['id']+'|'+x['name']+'\n')
                                                uidz.append(x["id"]+"|"+x["name"])                      
                                          else:continue
                              except:continue                      
                  except KeyError:pass      
                  print(f'\rsedang mengumpulkan %s uid'%(len(uidz)),end=" ")
                  
if __name__ == '__main__':
      try:os.mkdir('dumpuid')
      except:pass
      try:os.mkdir('data')
      except:pass
      dump()