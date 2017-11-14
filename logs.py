# coding=utf-8

import logging
import os
import sys
from time import strftime, gmtime
from time import asctime
from sys import platform

plfm = 'windows'

if platform == "linux" or platform == "linux2":
    plfm = 'linux'
elif platform == "darwin":
    plfm = 'OS X'
elif platform == "win32":
    plfm = 'windows'



class Log:
    file_path = os.getcwd()
    file_name = 'file_log'
    logger = logging.getLogger()

    def __init__(self, file_path, file_name):

        if file_path == "":
            self.file_path = "D:\\"
        else:
            self.file_path = file_path

        if file_name == "":
            self.file_name = 'file_log.txt'
        else:
            self.file_name = file_name

        self.logger = self.init_logging()

    def setFilePath(self, filePath):
        self.file_path = filePath
        self.init_logging()

    def setFileName(self, fileName):
        self.file_name = fileName
        self.init_logging()

    def getFilePath(self):
        return self.file_path

    def getFileName(self):
        return self.file_name

    def getFullPath(self):
        return self.file_path + self.file_name

    def getLogger(self):
        return self.logger

    def addToLog(self, s, type_output='info'):
        if plfm == 'windows':
            file_ = self.file_path + "\\logs\\" + self.file_name + "_" + strftime('%d_%m_%Y', gmtime()) + ".txt"
        else:
            file_ = self.file_path + "/logs/" + self.file_name + "_" + strftime('%d_%m_%Y', gmtime()) + ".txt"

        if not os.path.isfile(file_):
            self.init_logging()

        output_level = {'info':    0, 'warning':   1, 'debug':  2}

        if output_level[type_output] == 0:
            self.getLogger().info(s)
        elif output_level[type_output] == 1:
            self.getLogger().warning(s)
        else:
            self.getLogger().debug(s)

    def initLogFolder(self):
        try:
            if (plfm == 'windows'):
                if not os.path.exists(self.file_path + "\\logs\\"):
                    os.makedirs("logs")
            else:
                if not os.path.exists(self.file_path + "/logs/"):
                    os.makedirs("logs")

        except Exception as e:
            print 'error makedir in log lib {}'.format(str(e))
        except IOError:
            print "Ошибка создания каталога logs" \
                  ""

    def init_logging(self):
        try:
            logger = logging.getLogger()
            logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            self.initLogFolder()

            if plfm == 'windows':
                file_ = self.file_path + "\\logs\\" + self.file_name + "_" + strftime('%d_%m_%Y', gmtime()) + ".txt"
            else:
                file_ = self.file_path + "/logs/" + self.file_name + "_" + strftime('%d_%m_%Y', gmtime()) + ".txt"

            file_.upper()
            fh = logging.FileHandler(file_)
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(formatter)
            logger.handlers = []
            logger.addHandler(fh)
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)
            ch.setFormatter(formatter)
            logger.addHandler(ch)
        except IOError as e:
            print "Ошибка при инициализации файла логов {}".format(str(e))
            sys.exit(0)

        return logger
