import usb.core as core
import usb.backend as backend

SysDVR = {
    "ProductId": "0x4ee0",
    "VendorId": "0x18d1",
}

MAGIC_NS = {
    "ProductId": "0xa710",
    "VendorId": "0x20d6",
}


def find(device: dict):
    idVendor = device["VendorId"]
    idProduct = device["ProductId"]
    return core.find(idVendor=idVendor, idProduct=idProduct)


def main():
    print(find(SysDVR))
    print(find(MAGIC_NS))


if __name__ == "__main__":
    main()
