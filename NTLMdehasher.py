#Programın amacı parola listesine bağlı olarak NTLM kodlanmış ifadeleri çözmektir.
import hashlib
try:
	cozulecekNTLM=input("Kodu çözülecek NTLM Hash:")
	#Girilen hash büyük harflerden oluşursa anlaşılamıyor. Bu nedenle her ihtimale karşı lower fonksiyonu çalıştırmak işimize yarayabilir
	cozulecekNTLM=cozulecekNTLM.lower()
	parolaDosyasi=input('Parola Dosyasının Adı:')
	parolalar=[]
	file=open(parolaDosyasi,'r')
	for parola in file:
		NTLM=hashlib.new('md4',parola.rstrip('\n').encode('utf-16le')).hexdigest()
		if(NTLM==cozulecekNTLM):
			print('PAROLA:'+parola)
			exit()
		else:
			continue
except FileNotFoundError:
	print("Lütfen dosya adını doğru giriniz.Eğer dosya farklı bir konumdaysa, konum yolu ile beraber giriniz.")
except UnicodeDecodeError:
	print("Aranan parola bulunamadı")
except IsADirectoryError:
	print("Lütfen klasör adını doğru giriniz")
