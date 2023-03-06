from classes import Database
import socket


def findStuNoByIdm(idm):
    """読み込んだIDM情報から学生番号を抽出する。"""

    # Databaseインスタンスの生成
    con = Database.DataBase(socket.gethostname())
    con.connectedCheck()
    sql = "select IDM, StudentId from idm_bind_number where IDM = %s"
    return con.execute(sql, (idm,))
