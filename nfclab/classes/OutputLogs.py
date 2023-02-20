import datetime


class OutputLogs():
    def __init__(self):
        pass

    def output(self, className, message):
        print('[{}] [{}] db is connected: {}'.format(datetime.datetime.now(), className,
              message))
