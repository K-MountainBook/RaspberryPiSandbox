import datetime
import sys


class OutputLogs():
    def __init__(self):
        pass

    def output(self, className, message):
        print('[{}] [{}] {}'.format(datetime.datetime.now(), className,
              message))

    def outputError(self, className, message):
        print('[{}] [{}] {}'.format(datetime.datetime.now(), className,
                                    message), file=sys.stderr)
