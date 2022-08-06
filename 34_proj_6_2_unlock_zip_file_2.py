import itertools
import zipfile

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

zfile=zipfile.ZipFile(r'D:\2022. Sophomore\Python Study\220806_project_5_to_8\05_text.zip')

for len in range(1,6):
    to_attempt=itertools.product(passwd_string, repeat=len)
    for attempt in to_attempt:
        passwd=''.join(attempt)
        print(passwd)

        try:
            zFile.extractall(pwd=passwd.encode())
            print(f"Password : {passwd}")
            break
        except:
            pass
