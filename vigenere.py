#VIGENERE ŞİFRELEMESİ
#Bu program kullanıcıdan gelen metin ve anahtar kelime ile vigenere şifrelemesi ve çözümlemesi yapmaktadır
def vigenereKodlama(metin,anahtar):
	harf=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	metinListe=list(metin.lower())
	anahtarListe=list(anahtar.lower())
	sifre=""
	for i in range(0,len(metin)):
		asciiKodMetin=ord(metinListe[i])
		a=i%len(anahtar)
		asciiKodKey=ord(anahtarListe[a])
		if (asciiKodMetin>=97 and asciiKodMetin<=122) and (asciiKodKey>=97 and asciiKodKey<=122):
			
			indis=harf.index(metinListe[i])+harf.index(anahtarListe[a])
			indis=indis%26
			sifre+=harf[indis]
		elif not(asciiKodMetin>=97 and asciiKodMetin<=122) and (asciiKodKey>=97 and asciiKodKey<=122):
			sifre+=metinListe[i]
		else:
			print("Girdiğiniz anahtar kelime harflerden oluşmalıdır.")
			break
	return sifre
def vigenereKodCozme(sifre,anahtar):
	harf=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	sifreListe=list(sifre.lower())
	anahtarListe=list(anahtar.lower())
	metin=""
	for i in range(0,len(sifre)):
		asciiKodSifre=ord(sifreListe[i])
		a=i%len(anahtar)
		asciiKodKey=ord(anahtarListe[a])
		if (asciiKodSifre>=97 and asciiKodSifre<=122) and (asciiKodSifre>=97 and asciiKodSifre<=122):
			indis=harf.index(sifreListe[i])-harf.index(anahtarListe[a])
			if indis<0:
				indis=26+indis
				metin+=harf[indis]
			elif indis>=0:
				metin+=harf[indis]
		elif not(asciiKodSifre>=97 and asciiKodSifre<=122) and (asciiKodKey>=97 and asciiKodKey<=122):
			metin+=sifreListe[i]
		else:
			print("Girdiğiniz anahtar kelime harflerden oluşmalıdır.")
			break
	return metin
print("Yapmak istediğiniz işlemi seçiniz:")
print("1-Vigenere Kodlama")
print("2-Vigenere Kod Çözme")
secim=input("Yapmak istediğiniz işlemi seçiniz(1|2):")

if secim=="1":
	metin=input("Kodlanacak olan metni giriniz:")
	key=input("Kodlamak için kullanılacak anahtarı giriniz:")
	print("Metin:",metin,"\nAnahtar:",key,"\n",vigenereKodlama(metin,key))

elif secim=="2":
	sifre=input("Kodu çözülecek olan metni giriniz:")
	key=input("Kod çözmek için kullanılacak anahtarı giriniz:")
	print("Şifreli Metin:",sifre,"\nAnahtar:",key,"\n",vigenereKodCozme(sifre,key))
else:
	print("Düzgün bir seçim yapınız:")


