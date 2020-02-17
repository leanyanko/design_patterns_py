class Image:
    def __init__(self, filename):
        self.filename = filename

    def load_image_from_disc(self):
        print("loading " + self.filename)

    def display_image(self):
        print("display " + self.filename)


class Proxy:
    def __init__(self, subject):
        self.subject = subject
        self.proxystate = None


class ImageProxy(Proxy):
    def display_image(self):
        if self.proxystate == None:
            self.subject.load_image_from_disc()
            self.proxystate = 1
        print("display " + self.subject.filename)


proxy_image1 = ImageProxy(Image("filename 1"))
proxy_image2 = ImageProxy(Image("another filename"))

proxy_image1.display_image();
proxy_image1.display_image();
proxy_image2.display_image();
proxy_image2.display_image();