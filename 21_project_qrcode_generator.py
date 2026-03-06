import qrcode

link = input("Enter link: ")
filename = input("Enter file name: ")

img = qrcode.make(link)

img.save(filename)