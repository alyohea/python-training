from datetime import datetime
import tzlocal


class InfoLogger:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'a+')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

    def log(self, log):
        t = datetime.now(tzlocal.get_localzone()).strftime('[%d.%m.%y - %X %z]')
        self.file.write(f'{t}: {log}\n')


if __name__ == '__main__':
    with InfoLogger('log.txt') as logger:
        logger.log('LOG')
