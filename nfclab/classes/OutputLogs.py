import datetime


class OutputLogs():
    def __init__(self):
        pass

    def output(self, className, message):
        print('[{}] [{}] {}'.format(datetime.datetime.now(), className,
              message))
