from socket import *

print("--IP Bulucu--")
print("-------------")

siteAdi=input("Sitenin adı:")
ip=gethostbyname(siteAdi)

print("IP=",ip)
