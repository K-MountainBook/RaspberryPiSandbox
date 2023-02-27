import socket
from classes import CardReader, Database


def main():

    # カードリーダー準備（スタブ）
    cr = CardReader.CardReader()
    cr.read_id_stab()
    print(cr.idm)

    # Detabaseインスタンスの生成
    con = Database.DataBase(socket.gethostname())
    con.connectedCheck()
    result = con.execute('select IDM, StudentId from idm_bind_number')

    print(result)


if __name__ == '__main__':
    main()
