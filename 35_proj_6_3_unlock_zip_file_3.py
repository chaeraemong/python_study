import itertools
import zipfile

def un_zip(passwd_string, min_len, max_len, zFile):
    for len in range(min_len,max_len+1):
        to_attempt=itertools.product(passwd_string, repeat=len)
        for attempt in to_attempt:
            passwd=''.join(attempt)
            print(passwd)
            try:
                zFile.extractall(pwd=passwd.encode())
                print(f"Password : {passwd}")
                return 1
            except:
                pass

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

zfile=zipfile.ZipFile(r'D:\2022. Sophomore\Python Study\220806_project_5_to_8\05_text.zip')


min_len=1
max_len=5

unzip_result=un_xip(passwd_string,min_len,max_len,zFile)

if unzip_result==1:
    print("Success")
else:
    print("Failure")
