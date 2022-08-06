import qrcode

file_path = r'14_qr_codes.txt'
with open(file_path, 'rt', encoding='UTF8')as f:
    read_lines=f.readlines()

    for line in read_lines:
        line=line.strip()
        print(line)
