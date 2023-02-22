import nfc
import binascii


class CardReader(object):
    """NFCデータ取得クラス"""

    def __on_connect(self, tag):
        """リーダ読み込み"""

        # IDmのみ取得して表示
        self.idm = binascii.hexlify(tag._nfcid)

    def read_id(self):
        """NFCリーダ接続"""
        clf = nfc.ContactlessFrontend('usb')
        try:
            # おサイフケータイからも取得するため、NFC読み込みの範囲をFelicaに限定する(212bps,424bps)
            # clf.connect(rdwr = {'on-connect':self.on_connect})
            clf.connect(
                rdwr={'targets': ['212F', '424F'], 'on-connect': self.__on_connect})

        finally:
            clf.close

    def getIDm(self):
        result = self.read_id()
        return result

    def read_id_stab(self):
        self.idm = "000000000000"
        return True
