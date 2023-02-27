import mysql.connector
import json
from . import OutputLogs


class DataBase():
    def __init__(self, env):
        """DB接続インスタンス。

        ホスト名の設定が存在しない場合defaultの設定を読み込む。
        """
        logs = OutputLogs.OutputLogs()

        configfile = open("config.json", "r")
        jsonData = json.load(configfile)

        logs.output(self.__class__.__name__, "environment:" + env)

        if env not in jsonData:
            env = "default"

        self.con = mysql.connector.connect(host=jsonData[env]["server"],
                                           port=jsonData[env]["port"],
                                           user=jsonData[env]["user"],
                                           password=jsonData[env]["password"])

    def connectedCheck(self):
        """このインスタンスでDBに接続できるかのチェック。

        標準出力に出力される。
        """
        log = OutputLogs.OutputLogs()
        log.output(self.__class__.__name__, "db is connected:" + str(self.con.is_connected()))

        # print('[{}] [{}] db is connected:{}'.format(datetime.datetime.now(),
        #       str(self.con.is_connected())))
