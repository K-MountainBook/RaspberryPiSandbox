import socket
import db_access as db
from classes import CardReader, Database, OutputLogs as logs


def main():

    # カードリーダー準備（スタブ）
    cr = CardReader.CardReader()
    log = logs.OutputLogs()
    cr.read_id_stab()

    # idmに紐づく学生番号を検索
    result = db.findidm(cr.idm)

    log.output(className=__name__, message="scanning idm:" + cr.idm)

if __name__ == '__main__':
    main()
