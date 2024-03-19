@Echo off
title INSTALL Running MneEthOn_V4.py Mmdrza.Com
Pushd "%~dp0"
pip install cryptofuzz
pip install rich
pip install mnemonic
pip install requests
pip install psutil
pip install blessed
:loop
python MneEthOn_V4.py
goto loop
