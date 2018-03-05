#Yazmış olduğum bu program kullanıcı tarafından girilen ağ ve IP adreslerine göre makinaların aktif olup olmadığını göstermektedir. Bu işlem ping ile gerçekleşmektedir. Eğer ping ile iletişim kurulursa makina aktiftir, kurulamazsa pasiftir.
import os #Linux komutu kullanmak için 'os' kütüphanesini import ettik.
aktifIPler=[] #Tarama sonucu aktif makinaların IP adreslerinin kayıt edileceği bir liste tanımladık.
try:
	ipAraligi=input("IP Aralığını Giriniz:(Örn:192.168.10):") # Kullanıcıdan ağ adresini istedik.
	ilkIP=int(input("Taranmaya başlanacak ilk IP(0-255):")) #Kullanıcıdan alınan ağ adresinin hangi IP'sinden başlanarak tarama yapılacağını belirtmek için ilk IP'yi istedik.
	sonIP=int(input("Taranacak son IP(ilkIP-255):")) #Taramanın biteceği son IP adresini istedik.
	if (ilkIP<sonIP) and (ilkIP>=0 and ilkIP<=255) and (sonIP>=0 and sonIP<=255): #Kullanıcının girdiği ilk IP'nin son IP'den küçük olduğunu onaylamak ve IP'lerin 0-255 aralığında olduğunu onaylamak için bu koşulu belirttik
		for a in range(ilkIP,sonIP+1):
			ip=ipAraligi+"."+str(a) #Kullanıcıdan alınan ağ adresi ve IP adresilerini birleştirerek adresi 32 bit formatına tamamladık.
			sonuc=os.system("ping -c 1 "+ip+" > a.txt") #Makina ile başarılı bir şekilde iletişime geçilebildiğini anlamak için 1 defa ping atıyoruz. Eğer ping atmanın sonucu başarılı olursa 0 değeri dönecektir. '> a.txt' yazmamızın amacı ise ping işleminin çıktısının ekranda görünmemesini sağlayarak daha düzgün bir çıktı görüntüsü sağlamaktır.
			if sonuc==0: #Eğer sonuc değişkeni 0 ise yani ping başarılı ise ekrana 'IP [+]' yazılacak ve bu IP aktifIPler listesine eklenecektir.
				print("\n"+ip+" [+]"+"\n")
				aktifIPler.append(ip)	
			else:
				print(ip+" [-]") #Eğer ping başarısız ise 'IP [-]' çıktısı alınacaktır.
	else:
		print("İlk IP değeri son IP değerinden büyük olmalıdır veya ilk ve son IP değerleri 0-255 aralığında olmalıdır.")
except ValueError: #Tarama için girişleri düzgün yapmak hassas bir konudur. Bu nedenle oluşabilecek bir değer hatası sonucu kullanıcıya düzgün bir çıktı vermek için 'except ValueError:' bloğunu kullandık.
	print("Hatalı giriş yaptınız")
print("Aktif IP'ler")
print(aktifIPler)
os.system("rm a.txt") #Aracı olarak kullandığımız a.txt dosyası işimize yaramayacağı için siliyoruz.
