@Echo off
title INSTALL Running MneEthOn_V3.py Mmdrza.Com
Pushd "%~dp0"
pip install cryptofuzz
pip install rich
pip install mnemonic
pip install requests
pip install psutil
pip install blessed
:loop
python MneEthOn_V3.py
goto loop
