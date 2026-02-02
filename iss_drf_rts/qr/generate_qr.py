import qrcode

def generate_qr(url: str):
    img = qrcode.make(url)
    img.save("researcher_verify_qr.png")
