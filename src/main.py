import qrcode
import argparse


def main(data: str | None, filename: str | None):
    qr: qrcode.QRCode = qrcode.QRCode()
    qr.add_data(data)
    qr.make(fit=True)

    if filename:
        img = qr.make_image(fill="black", back_color="white")
        img.save(filename)
    else:
        qr.print_ascii()


if __name__ == '__main__':
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description='Generate a QR code')
    parser.add_argument('-d', '--data', type=str, help='Data to encode in QR code')
    parser.add_argument('-f', '--filename', type=str, help='Filename to save QR code')
    args: argparse.Namespace = parser.parse_args()

    filename: str | None = None

    if args.filename:
        filename = args.filename

    if filename is not None and not filename.endswith('.png'):
        filename += '.png'

    data: str | None = None

    if args.data:
        data = args.data

    main(data, filename)
