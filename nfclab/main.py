import json
from classes import CardReader, Database


def main():
    """メインメソッド"""
    cr = CardReader.CardReader()

    # Felicaを読み取る。
    cr.read_id()

    # 読み取ったカードから固有番号を取得する
    idm = str(cr.idm, 'utf-8').upper()
    # 読み取った内容を表示
    print("IDm : " + idm)

    # Detabaseインスタンスの生成
    con = Database.DataBase("testenv")
    con.connectedCheck()

    return con


if __name__ == '__main__':
    main()
