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
import requests
from lxml import html

console = Console()


def mmdrza() :
    z = 1
    w = 0
    while True :
        z += 1

        langrnd = ['english' , 'french']
        sellan = random.choice(langrnd)
        mne = Mnemonic(str(sellan))
        listno = ["128" , "256"]
        rnd = random.choice(listno)
        words = mne.generate(strength = int(rnd))
        STRENGTH = int(rnd)
        LANGUAGE: str = (sellan)
        MNEMONIC = words
        PASSPHRASE: str = "meherett"
        assert is_mnemonic(mnemonic = words , language = sellan)

        bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency = Cryptocurrency , account = 0 , change = False ,
                                                      address = 0)
        bip44_hdwallet.from_mnemonic(mnemonic = MNEMONIC , passphrase = PASSPHRASE , language = LANGUAGE)
        mixword = words[:32]
        addr = bip44_hdwallet.p2pkh_address()
        priv = bip44_hdwallet.private_key()
        # =======================================
        urlblock = f"https://ethereum.atomicwallet.io/api/v2/address/{addr}"
        respone_block = requests.get(urlblock)
        res = respone_block.json()
        xVol = dict(res)['balance']
        timer = respone_block.elapsed
        bal = xVol

        # =======================================
        MmdrzaPanel = str(
            '[gold1 on grey15]Total Checked: '+'[orange_red1]'+str(z)+'[/][gold1 on grey15] '+' Win:'+'[white]'+str(w)+'[/]'+ '[grey74]  ReqSpeed: ' + str(timer)[5:] + '[/][gold1]                  Balance: ' + '[/][aquamarine1]' + str(bal) + '\n[/][gold1 on grey15]Addr: '+'[white] '+str(addr)+'[/]\nPRIVATEKEY: [grey54]'+str(priv)+'[/]')
        style = "gold1 on grey11"
        console.print(Panel(str(MmdrzaPanel) , title = "[white]Ethereum Mnemonic Checker V3[/]" , subtitle = "[green_yellow blink] Mmdrza.Com [/]" , style = "green") , style = style , justify = "full")

        z += 1
        if float(bal) > 0:
            w += 1
            f1 = open('Winner___ETH___WalletWinner.txt' , 'a')
            f1.write('\nAddress     === '+str(addr))
            f1.write('\nPrivateKey  === '+str(priv))
            f1.write('\nMnemonic    === '+str(words))
            f1.write('\nTransaction === '+str(bal))
            f1.write('\n            -------[ M M D R Z A . C o M ]------                   \n')
            f1.close()

    # ============================


mmdrza()

if __name__ == '__main__' :
    for i in range(len(add)) :
        p = multiprocessing.Process(target = mmdrza)
        p.start()
        p.join()
