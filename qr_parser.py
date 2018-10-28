import qrcode


def main():
    img = qrcode.make("https://qiita.com/")
    img.save("qiita.png")


if __name__ == '__main__':
    main()
