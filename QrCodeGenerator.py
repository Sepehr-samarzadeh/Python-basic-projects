# pip install qrcode Image
#install that and follow my codes


import qrcode


def qrcode_generator(text):
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    

    qr.add_data(text)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black",back_color="white")
    img.save("first.png")


#you can use input to take urls from people and turn that into qrcodes
#you need to define a variable and the use input()
#and in the last part you only need to call the function which is (qrcode_generator) and thats it

#url=input("please write down your url and I turn that to qrode: ")
#qrcode_generator(input)

qrcode_generator("https://github.com/")
#enjoy
