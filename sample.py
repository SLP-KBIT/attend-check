import time
import nfc

def on_connect(tag):
    SYSTEM_CODE = 0xfe00
    idm, pmm = tag.polling(SYSTEM_CODE)
    tag.idm, tag.pmm, tag.sys = idm, pmm, SYSTEM_CODE

    SERVICE_CODE = 0x1a8b
    sc = nfc.tag.tt3.ServiceCode(SERVICE_CODE >> 6, SERVICE_CODE & 0x3f)
    bc1 = nfc.tag.tt3.BlockCode(0, service=0) # student number
    data = tag.read_without_encryption([sc], [bc1])

    print ("Student Num: " + data[2:8].decode("utf-8"))

def main():
    with nfc.ContactlessFrontend('usb') as clf:
        while clf.connect(rdwr={'on-connect': on_connect}):
            time.sleep(2)

if __name__ == '__main__':
    main()
