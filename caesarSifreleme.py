#caesar sifrelemesi
#Bu program girilen metne ve öteleme değerine göre caesar şifrelemesi yapmaktadır.
def caesar(kelime,iter):
	kelimeListe=list(kelime)
	sifre=""
	for i in range (0,len(kelime)):
		asciiKod=ord(kelimeListe[i])
		if ((asciiKod>=65 and asciiKod<=90) or (asciiKod>=97 and asciiKod<=122)) and (iter>=1 and iter<=26):
			if (asciiKod>=65 and asciiKod<=90) and (ord(kelimeListe[i])+iter>90):
				a=asciiKod+iter-90
				a=64+a
				sifre+=chr(a)	   
			elif (asciiKod>=97 and asciiKod<=122) and (ord(kelimeListe[i])+iter>122):
				a=asciiKod+iter-122
				a=96+a
				sifre+=chr(a)
			else:
				sifre+=chr(ord(kelimeListe[i])+iter)
		elif not((asciiKod>=65 and asciiKod<=90) or (asciiKod>=97 and asciiKod<=122)):
			sifre+=kelimeListe[i]
		else:
			print("İterasyon değeri [1,26] aralığında olmalıdır")
	return sifre


metin=input("Şifrelenecek metin:")
oteleme=input("Öteleme miktarını giriniz[1-26]:")
print(caesar(metin,int(oteleme)))

