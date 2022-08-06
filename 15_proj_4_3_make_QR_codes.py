import qrcode

file_path = r'14_qr_codes.txt'
with open(file_path, 'rt', encoding='UTF8')as f:
    read_lines=f.readlines()

    for line in read_lines:
        line=line.strip()
        print(line)

        qr_data = line
        qr_img = qrcode.make(qr_data)

        save_path = 'D:\\2022. Sophomore\\Python Study\\220730_project_1_to_4\\'+qr_data+'.png'
        qr_img.save(save_path)
