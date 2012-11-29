@ECHO OFF
FOR %%x IN (*.txt) DO (
    ECHO %%x>>json.log
    CAT %%x | python -m json.tool 1>nul 2>>json.log)