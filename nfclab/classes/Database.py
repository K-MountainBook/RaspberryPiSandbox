import mysql.connector
import json
from . import OutputLogs


class DataBase():
    def __init__(self, env):

        configfile = open("config.json", "r")
        jsonData = json.load(configfile)

        self.con = mysql.connector.connect(host=jsonData[env]["server"],
                                           port=jsonData[env]["port"],
                                           user=jsonData[env]["user"],
                                           password=jsonData[env]["password"])

    def test(self):
        log = OutputLogs.OutputLogs()
        log.output(self.__class__.__name__, str(self.con.is_connected()))

        # print('[{}] [{}] db is connected:{}'.format(datetime.datetime.now(),
        #       str(self.con.is_connected())))
