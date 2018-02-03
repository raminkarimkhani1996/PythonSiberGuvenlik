from threading import Thread
import socket
acikPortlar=[]
kapaliPortlar=[]
iplikler=[]
host=input("Host:") #ip adresi
ilkport=input("İlk Port:") #Taranmaya başlanacak ilk port
ilkport=int(ilkport)
sonport=input("Sonuncu Port:") # son port
sonport=int(sonport)
def portTarama(port):
	soket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#socket, host ile bağlantı kurmak amaçlı kullanılır.
	durum = soket.connect_ex((host,port))
	if durum==0:
		acikPortlar.append(port)
		soket.close()
	else:
		kapaliPortlar.append(port)
		soket.close()
	#if bloğuna göre connect_ex ile bağlanılmaya çalışılan port açık ise 
	#port numarasını acikPortlar dizisine, değilse kapaliPortlar dizisine
	#ekle

for i in range (ilkport,sonport):
	#threading sınıfından çekilen Thread fonksiyonu, target adlı fonksiyon
	# ve args adlı port değişkeni parametreleri ile port taraması işleminin
	#girilen baş ve son değerin aralarındaki her bir değer için deneyip
	# gerekli atamaları yapacaktır.
	t=Thread(target=portTarama,args=(i,))
	iplikler.append(t)	
	t.start()
print("Açık Portlar:\n",acikPortlar)


