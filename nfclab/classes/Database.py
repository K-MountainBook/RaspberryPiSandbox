import mysql.connector

class DataBase():
    def __init__(self,config):
        global connector
        connector = mysql.connector.connect(host=config["server"],
                                            port=config["port"],
                                            user=config["user"],
                                            password=config["password"])
        
        
    def test(self):
        print('db is connected:' + str(connector.is_connected()))
    