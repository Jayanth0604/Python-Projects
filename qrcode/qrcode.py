import pyqrcode
data="https://twitter.com/login"
twitter=pyqrcode.create(data)
twitter.svg('appqr.svg',scale=10)