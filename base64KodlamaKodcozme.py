import base64
def base64KodCozme(sifre):
	try:
		s=list(sifre)
		if(s[len(sifre)-1]!='='): # eğer base64 ün sonunda = olmazsa cözülmez. Online decoder sitelerinde = olmadan girilen base64 ifadelerinin sonuna = ifadesi otomatik konulur
			sifre+='='
		cozum=base64.b64decode(sifre) #base64 kütüphanesinden b64decode fonksiyonun çağırarak, verdiğimiz şifreyi çözüp cozum değişkenine atadık
		cozum=str(cozum) #Çözülen şifre, bytes formatında ve b'' formatında çıktı vereceği için cozum değişkenini string ifadeye çevirip, yazdırma sırasında b'' ifadelerinden kurtulmak için cozum[2:len(cozum)] ifadesini kullanıyoruz.
		print(cozum[2:len(cozum)-1])
	except (ValueError):
		print("Girmiş olduğunuz kod çözülemedi!!!")
def base64Kodlama(metin):
		sifre=base64.b64encode(metin.encode()) # b64encode fonksiyonunun kodlama yapabilmesi için byte tipinde değişken gerekmektedir. Bu nedenle metin stringini metin.encode() olarak parametre yaptık
		sifre=str(sifre)
		print(sifre[2:len(sifre)-1]) # Kod çözmede olduğu gibi elde ettiğimiz kod b'' şeklinde yazılacağı için bu ifadeyi [2:len(sifre)-1] ile temizlemiş olduk

print("Yapılacak işlemi seçiniz:")
print("1-BASE64 KODLAMA")
print("2-BASE64 KOD ÇÖZME")
sec=input("Seçiminizi yapınız(1|2):")
if sec=="1":
	metin=input("Base64 olarak kodlanacak metni giriniz:")
	base64Kodlama(metin)
elif sec=="2":
	sifre=input("Çözülecek olan base64 kodunu giriniz:")
	base64KodCozme(sifre)
else:
	print("Yanlış seçim!!!")
