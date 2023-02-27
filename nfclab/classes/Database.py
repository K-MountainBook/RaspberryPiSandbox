import mysql.connector
import json
from . import OutputLogs, ConstMeta
from .MyConst import Const


class DataBase():

    def __init__(self, env):
        """DB接続インスタンス。

        ホスト名の設定が存在しない場合defaultの設定を読み込む。
        """
        logs = OutputLogs.OutputLogs()

        configfile = open(Const.CONFIG_FILE, "r")
        jsonData = json.load(configfile)

        if env not in jsonData:
            env = "default"

        logs.output(self.__class__.__name__, "environment:" + env)

        self.con = mysql.connector.connect(host=jsonData[env]["server"],
                                           port=jsonData[env]["port"],
                                           user=jsonData[env]["user"],
                                           password=jsonData[env]["password"],
                                           db=jsonData[env]["database"])

    def connectedCheck(self):
        """このインスタンスでDBに接続できるかのチェック。

        標準出力に出力される。
        """
        log = OutputLogs.OutputLogs()
        log.output(self.__class__.__name__, "db is connected:" +
                   str(self.con.is_connected()))

        # print('[{}] [{}] db is connected:{}'.format(datetime.datetime.now(),
        #       str(self.con.is_connected())))

    def execute(self, query, param):
        """引数で渡されたクエリを実行する
         dictionary引数を指定して、dict型で値を受け取る"""
        csr = self.con.cursor(dictionary=True)
        csr.execute(query,param)

        fetched = csr.fetchall()
        csr.close()

        return fetched
