import json
from classes import CardReader, Database, OutputLogs as logs
import db_access as db



def main():
    """メインメソッド"""
    cr = CardReader.CardReader()
    log = logs.OutputLogs()

    # Felicaを読み取る。
    cr.read_id()

    # 読み取ったカードから固有番号を取得する
    idm = str(cr.idm, 'utf-8').upper()

    # idmに紐づく学生番号を検索
    result = db.findidm(idm)

    log.output(className=__name__, message="scanning idm:" + cr.idm)


if __name__ == '__main__':
    main()
