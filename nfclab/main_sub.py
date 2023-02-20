from classes import CardReader, Database


def main():
    cr = CardReader.CardReader()

    cr.read_id_stab()
    print(cr.idm)

    # Detabaseインスタンスの生成
    con = Database.DataBase("testenv")
    con.test()


if __name__ == '__main__':
    main()
