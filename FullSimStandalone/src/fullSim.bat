@ECHO off
IF %1 == 4 GOTO TRACE
start /B /affinity 1 memsim.exe spm_memory.txt %1> ..\Results\tempSpmLog.txt 2>..\Results\spmError.txt
start /B /affinity 4 memsim.exe cache_memory.txt %1> ..\Results\tempCacheLog.txt 2>..\Results\cacheError.txt
GOTO DONE
:TRACE
start /B /affinity 1 memsim.exe spm_memory.txt trace file="trace.txt"> ..\Results\tempSpmLog.txt 2>..\Results\spmError.txt
start /B /affinity 4 memsim.exe cache_memory.txt trace file="trace.txt"> ..\Results\tempCacheLog.txt 2>..\Results\cacheError.txt
GOTO DONE
:DONE
::