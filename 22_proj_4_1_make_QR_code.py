import qrcode

qr_data = 'www.google.com'
qr_img = qrcode.make(qr_data)

save_path = 'D:\\2022. Sophomore\\Python Study\\220730_project_1_to_4\\'+qr_data+'.png'
qr_img.save(save_path)
