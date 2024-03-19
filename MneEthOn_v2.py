import random
import time
from rich import print
from rich.panel import Panel
from rich.console import Console
from cryptofuzz import Convertor, Ethereum
from mnemonic import Mnemonic
import concurrent.futures as cf
import requests

conv = Convertor()
eth = Ethereum()
console = Console()


def getBal(addr: str):
    req = requests.get(f"https://ethereum.atomicwallet.io/api/v2/address/{addr}")
    if req.status_code == 200:
        return dict(req.json())["balance"]
    else:
        return "0"


def mmdrza():
    z = 1
    w = 0
    while True:
        z += 1
        start_time = time.time()
        mne = Mnemonic("english")
        words = mne.generate(strength=random.choice([128, 256]))
        priv = conv.mne_to_hex(words)
        addr = eth.hex_addr(priv)
        mixWord = words[:64]
        # //-----------------------------------------------------
        bal = int(getBal(addr)) / 1000000000000000000
        end_time = time.time()
        timer = end_time - start_time
        # //-----------------------------------------------------
        MmdrzaPanel = str(
            '[gold1 on grey15]Total Checked: ' + '[orange_red1]' + str(
                z) + '[/][gold1 on grey15] ' + ' Win:' + '[white]' + str(w) + '[/]' + '[grey74]  ReqSpeed: ' + str(
                timer)[5:] + '[/][gold1]                  Balance: ' + '[/][aquamarine1]' + str(
                bal) + '\n[/][gold1 on grey15]Addr: ' + '[white] ' + str(addr) + '[/]\nPRIVATEKEY: [grey54]' + str(
                priv) + '[/]')
        style = "gold1 on grey11"
        console.print(Panel(str(MmdrzaPanel), title="[white]Ethereum Mnemonic Checker V2[/]",
                            subtitle="[green_yellow blink] Mmdrza.Com [/]", style="green"), style=style, justify="full")

        z += 1
        if int(bal) > 0:
            w += 1
            f1 = open('Winner___ETH___WalletWinner.txt', 'a')
            f1.write('\nAddress     === ' + str(addr))
            f1.write('\nPrivateKey  === ' + str(priv))
            f1.write('\nMnemonic    === ' + str(words))
            f1.write('\nTransaction === ' + str(bal))
            f1.write('\n            -------[ M M D R Z A . C o M ]------                   \n')
            f1.close()
        # //------------------------------------------------------
mmdrza()


if __name__ == '__main__':
    with cf.ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(mmdrza)
