import usb.core as core
import usb.backend as backend

SysDVR = {
    "ProductId": 0x4EE0,
    "VendorId": 0x18D1,
}

MAGIC_NS = {
    "ProductId": 0xA710,
    "VendorId": 0x20D6,
}


def find(device: dict):
    idVendor = device["VendorId"]
    idProduct = device["ProductId"]
    return core.find(idVendor=idVendor, idProduct=idProduct)


def main():
    input = find(MAGIC_NS)
    output = find(SysDVR)

    print(input)
    print(output)


if __name__ == "__main__":
    main()
