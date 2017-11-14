# PYTHON DAILY LOGGER
[![Build Status](https://travis-ci.org/welir/Python-Logger.svg?branch=master)](https://travis-ci.org/welir/Python-Logger)

Python logging library for realtime daily logging for python version 2.7

# Description
    The library allows you to write your logs into a text file daily. 
    As parameters, you need to specify the path to the logs  and the postfix file name.
    If log directory is not exist it will created. 
    And If logfile <> currendt day file ->>> it will created.

# Initialize
    log = Log('path to log dir', 'postfix log file name')
  
# Usage

    # without log level param
    Log.addToLog('Hello world')
        2017-11-14 12:42:20,413 - INFO - Hello world
        
    # warning log level
    Log.addToLog('Hello world', 'warning')
        2017-11-14 12:42:20,413 - WARNING - Hello world

    # debug log level
    Log.addToLog('Hello world', 'debug')
        2017-11-14 12:42:20,413 - DEBUG - Hello world


