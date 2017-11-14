from logs import Log
import os

Log = Log(os.getcwd(), '_hello_world_logs')

Log.addToLog('Hello world', 'info')

Log.addToLog('Hello world', 'warning')

Log.addToLog('Hello world', 'debug')