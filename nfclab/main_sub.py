import socket
import db_access as db
from classes import CardReader, Database, OutputLogs as logs


def main():

    # カードリーダー準備（スタブ）
    cr = CardReader.CardReader()
    log = logs.OutputLogs()
    cr.read_id_stab()

    # idmに紐づく学生番号を検索
    result = db.findStuNoByIdm(cr.idm)
    # print(result[0]['IDM'])
    # print(result[0]['StudentId'])
    if(len(result) == 1):
        log.output(className=__name__, message="scanning idm:" +
                   result[0]['IDM'] + ' ' + "StudentNumber:" + result[0]['StudentId'])
    else:
        log.outputError(className=__name__,
                        message="student Number is duplicate or not exist")


if __name__ == '__main__':
    main()
