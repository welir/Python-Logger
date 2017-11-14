from logs import Log
import os

Log = Log(os.getcwd(), '_hello_world_logs')

# without log level param
Log.addToLog('Hello world')

# warning log level
Log.addToLog('Hello world', 'warning')

# debug log level
Log.addToLog('Hello world', 'debug')