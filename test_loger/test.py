from logs import Log
import os

Log = Log(os.getcwd(), '_hello_world_logs')

Log.addToLog('Hello world')