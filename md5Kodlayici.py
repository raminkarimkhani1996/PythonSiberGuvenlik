import hashlib
def md5Kodla(metin):
	sifre=hashlib.md5(metin.encode("UTF-8")) 
	#hashlib kütüphanesi içinde hash türlerini barındırır. Bu programda hashlib sınıfının içinden çektiğimiz md5 fonksiyonu aldığı parametreyi md5 olarak şifreler.
#	sifre.update(metin.encode("UTF-8"))
	#içine md5 i attıgımız sifre adlı değişkeni set etmek adına update fonksiyonu kullanılır
	s=sifre.hexdigest()
	#hexdigest fonksiyonu md5 ile hashlenen metni bildiğimiz 32 karakterleri hexadecimal formatta göstermeye yarar.
	return s

m=input("MD5 ile şifrelenecek olan metni giriniz:")
print("MD5(",m,")=",md5Kodla(m))
