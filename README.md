# PYTHON DAILY LOGGER
https://travis-ci.org/welir/Python-Logger.svg?branch=master
Python logging library for realtime daily logging for python version 2.7

# Description
    The library allows you to write your logs into a text file every day. 
    As parameters, you need to specify the path to the logs with logs and the postfix file name.
    If log directory is not exist it will created. 
    And If logfile <> currendt day file ->>> it will created.

# Hello world example
  You may see it in repository

# Initialize
    log = Log('path to log dir', 'postfix log file name')
  
# Usage
    log.addToLog('Hello world')


