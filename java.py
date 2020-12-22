import re
import requests
num=input("input number:")
num=str(num)
headers={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66',
'referer': 'https://www.lanqiao.cn/courses/2977/learning/',
'cookie': '_ga=GA1.2.1320862616.1606727101; comet=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiIxMTk1NjQ2IiwiaXNfYWRtaW4iOmZhbHNlLCJleHAiOjE2MTA4ODkxNDAsImlzcyI6InNoaXlhbmxvdS5jb20iLCJpYXQiOjE2MDgyMTA3NDB9.JjqKu0HM0D9olTULevTdX1QwTjQ-C78-_Y6948SI3XI; session=603ac627-bf6a-4953-b013-ab67702f4dae.s5Lmi82nRhxsfM6KRmvoyQTspq8; Hm_lvt_56f68d0377761a87e16266ec3560ae56=1607659565,1607661557,1608210732,1608622922; _gid=GA1.2.126650501.1608622923; Hm_lpvt_56f68d0377761a87e16266ec3560ae56=1608623803'}
url='https://www.lanqiao.cn/api/v2/labs/'+num+'/document/'
r=requests.get(url=url,headers=headers)
# print(r.text)
text=str(r.text)
text=re.findall(r"[a-zA-z0-9]*\.java",text)
java=[]
for t in text:
    t=t.replace("`","")
    java.append(t)
java=list(set(java))
print(java)
print(len(java))
for j in java:
    f=open("/home/project/"+j,"w")
    f.write(r.text)
    f.close()
