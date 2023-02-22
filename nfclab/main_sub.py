import json
import os
from classes import CardReader, Database

def main():
    """メインメソッド"""
    cr = CardReader.CardReader()

    # Felicaを読み取る。
    cr.read_id_stab()
    
    # 読み取ったカードから固有番号を取得する
    idm = cr.idm.upper()
    # 読み取った内容を表示
    print("IDm : " + idm)

    environ_var = os.environ['SPRING_PROFILES_ACTIVE']

    if(environ_var == ""):
        configfile = open("config" + environ_var + ".json","r")
    else:
        configfile = open("config_" + environ_var + ".json","r")

    jsonData = json.load(configfile)

    con = Database.DataBase(jsonData)
    con.test()

if __name__ == '__main__':
    main()
