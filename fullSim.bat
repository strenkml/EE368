@ECHO off
IF %1 == 5 GOTO TRACE
start /B /affinity 1 .\memsim-master\memsim-master\memsim.exe .\memsim-master\memsim-master\spm_memory.txt %1> spmLog.txt 2>nul
start /B /affinity 4 .\memsim-master\memsim-master\memsim.exe .\memsim-master\memsim-master\memory.txt %1> cacheLog.txt 2>nul
GOTO DONE
:TRACE
start /B /affinity 1 .\memsim-master\memsim-master\memsim.exe .\memsim-master\memsim-master\spm_memory.txt trace file="memsim-master\memsim-master\trace.txt"> spmLog.txt 2>nul
start /B /affinity 4 .\memsim-master\memsim-master\memsim.exe .\memsim-master\memsim-master\memory.txt trace file="memsim-master\memsim-master\trace.txt"> cacheLog.txt 2>nul
GOTO DONE
:DONE
::