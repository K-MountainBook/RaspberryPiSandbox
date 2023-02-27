from classes import Database
import socket

def findidm(idm):
    
    # Detabaseインスタンスの生成
    con = Database.DataBase(socket.gethostname())
    con.connectedCheck()
    sql = "select IDM, StudentId from idm_bind_number where IDM = %s"
    return con.execute(sql,(idm,))
    