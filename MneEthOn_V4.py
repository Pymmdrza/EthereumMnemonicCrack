import random
import time
import concurrent.futures as cf
import requests
from blessed import Terminal
import psutil
from rich.panel import Panel
from rich.console import Console
from rich.style import Style
from cryptofuzz import Convertor, Ethereum
from mnemonic import Mnemonic
import os
import sys

conv = Convertor()
eth = Ethereum()
console = Console()


def OnClear():
    if "win" in sys.platform.lower():
        os.system("cls")
    else:
        os.system("clear")


def balance(addr):
    url_n = f"https://ethereum.atomicwallet.io/api/v2/address/{addr}"
    req = requests.get(url_n)
    if req.status_code == 200:
        return dict(req.json())["balance"]
    else:
        return "0"


def transaction(addr):
    req = requests.get(f"https://ethereum.atomicwallet.io/api/v2/address/{addr}")
    if req.status_code == 200:
        return int(dict(req.json())["txs"])
    else:
        return 0


def draw_system_status(term):
    cpu_percent = psutil.cpu_percent()
    ram_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent
    termWidth = term.width
    system_status = (
        f'\n{draw_graph("CPU", cpu_percent, termWidth)}\n'
        f'\n{draw_graph("RAM", ram_percent, termWidth)}\n'
        f'\n{draw_graph("HDD", disk_percent, termWidth)}\n'
    )
    return system_status


def draw_ethereum_info(z, w, addr, priv, mixWord, txs):
    MmdrzaPanel = (
        f'\n[gold1]Total Checked: [orange_red1]{z}[/][gold1]  Win: [white]{w}[/]'
        f'[gold1]  Transaction: [/][aquamarine1]{txs}\n\n[/][gold1]ADDR: [white] {addr}[/white]\n\n'
        f'PRIVATE: [grey54]{priv}[/grey54]\n\nMNEMONIC: [white]{mixWord}[/white]\n'
    )
    return MmdrzaPanel


def draw_graph(title, percent, width):
    bar_length = int(width - 17)
    num_blocks = int(percent * bar_length / 100)
    dash = "[grey54]–[/]"
    barFill = "[green]▬[/]"
    bar = barFill * num_blocks + dash * (bar_length - num_blocks)
    return f"[white]{title}[/]: |{bar}| {percent}%"


def main():
    term = Terminal()
    with term.fullscreen():
        with term.cbreak(), term.hidden_cursor():
            OnClear()
            while True:
                z = 0
                w = 0
                while True:
                    system_status = draw_system_status(term)
                    draw_system_status_panel = Panel(system_status, border_style="grey66")
                    mne = Mnemonic("english")
                    NumberList = [128, 256]
                    randomSize = random.choice(NumberList)
                    words = mne.generate(strength=randomSize)
                    priv = conv.mne_to_hex(words)
                    addr = eth.hex_addr(priv)
                    mixWord = words[:64]
                    txs = transaction(addr)
                    if txs > 0:
                        w += 1
                        with open("Found.txt", "a") as fr:
                            fr.write(f"{addr} TXS: {txs} BAL: {balance(addr)}\n")
                            fr.write(f"{priv}\n")
                            fr.write(f"{words}\n")
                            fr.write(f"{'-' * 50}\n")
                    MmdrzaPanel = draw_ethereum_info(z, w, addr, priv, mixWord, txs)
                    with term.location(0, 1):
                        console.print(draw_system_status_panel, justify="full", soft_wrap=True)
                        console.print(Panel(MmdrzaPanel, title="[white]Ethereum Mnemonic Checker V4[/]",
                                            subtitle="[green_yellow blink] Mmdrza.Com [/]", style="green"),
                                      justify="full", soft_wrap=True)
                    z += 1


if __name__ == "__main__":
    with cf.ProcessPoolExecutor(max_workers=8) as executor:
        for _ in range(8):
            executor.submit(main).result()

