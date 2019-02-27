from requests import get
from bs4 import BeautifulSoup as bs
from threading import Thread

print('K O N T O O O O L'.center(40))
print('*'*50)
link = ['https://ailisgarcia.com/wp-content/uploads/2018/09/',
	  'https://ailisgarcia.com/wp-content/uploads/2018/10/',
	  'https://ailisgarcia.com/wp-content/uploads/2018/11/',
	  'https://ailisgarcia.com/wp-content/uploads/2018/12/']

o = open('hasil.txt','a')
bc = open('hasil.txt','r').read()
def gett():
  #for l1 in link:
	print('oke')
	r1 = get(z)
	b1 = bs(r1.text,'html.parser')
	a1 = b1.find_all('a')
	for li in a1:
		if '.txt' in li.get('href'):
			txt = get(z+li.get('href'))
			tt = txt.text
			if 'PW' in tt:#'EMAIL' in tt or 'PW' in tt or 'email' in tt or 'password' in tt:
				if tt in bc:
					pass
				print(tt)
				o.write(tt)
				
def trd():
  global z
  t =[]
  for z in link:
  	tx = Thread(name='heh',target=gett)
  	tx.start()
  	t.append(tx)
  for xxx in t:
  	xxx.join()
trd()
o.close()
