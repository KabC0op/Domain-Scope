import socket
import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich.text import Text

console = Console()

BANNER = r"""
 ██╗  ██╗ █████╗ ██████╗  ██████╗ ██████╗  ██████╗ ██████╗ 
 ██║ ██╔╝██╔══██╗██╔══██╗██╔════╝██╔═████╗██╔═████╗██╔══██╗
 █████╔╝ ███████║██████╔╝██║     ██║██╔██║██║██╔██║██████╔╝
 ██╔═██╗ ██╔══██║██╔══██╗██║     ████╔╝██║████╔╝██║██╔═══╝ 
 ██║  ██╗██║  ██║██████╔╝╚██████╗╚██████╔╝╚██████╔╝██║     
 ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝     
"""

def welcome():
    console.print(Text(BANNER, style="bold cyan"))
    info = Text.assemble(
        ("  DomainScope", "bold green"),
        ("  -  Domain and IP Lookup Tool\n", "white"),
        ("  Author  : ", "yellow"), ("KabC0op\n", "bold white"),
        ("  Instagram  : ", "yellow"), ("@Blockkop_\n", "bold white"),
        ("  Reddit : ", "yellow"), ("CAPk0pp\n", "bold white"),
        ("\n  Tools sederhana untuk Reconnaissance: lookup IP, lokasi,\n", "white"),
        ("  ISP, dan info geolokasi dari sebuah domain.\n", "white"),
        ("  Bila ada kesalahan,mohon di maafkan because i am beginner :).", "dim"),
    )
    console.print(Panel(Align.left(info), border_style="green", title="[bold magenta]SELAMAT DATANG[/]"))

def lookup(hostname):
    ip_address = socket.gethostbyname(hostname)
    data = requests.get(f"http://ip-api.com/json/{ip_address}").json()

    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column(style="bold yellow", justify="right")
    table.add_column(style="white")
    table.add_row("Domain",   hostname)
    table.add_row("IP",       ip_address)
    table.add_row("Country",  str(data.get("country", "-")))
    table.add_row("Region",   str(data.get("regionName", "-")))
    table.add_row("City",     str(data.get("city", "-")))
    table.add_row("ISP",      str(data.get("isp", "-")))
    table.add_row("Timezone", str(data.get("timezone", "-")))
    table.add_row("Lat/Lon",  f"{data.get('lat', '-')}, {data.get('lon', '-')}")

    console.print(Panel(
        table,
        title="[bold green]HASIL LOOKUP[/]",
        border_style="green",
        subtitle=f"[dim]by KabC0op[/]"
    ))

def main():
    welcome()
    while True:
        try:
            hostname = console.input("[bold cyan][KabC0op][/] Masukan domain: ").strip()
            if not hostname:
                console.print("[red][!] Domain kosong, try again.[/]\n")
                continue
            lookup(hostname)
        except socket.gaierror:
            console.print("[bold red][!] Domain tidak valid atau tidak ditemukan[/]\n")
        except Exception as e:
            console.print(f"[bold red][!] ERROR:[/] {e}\n")

        pilihan = console.input("[cyan]Lanjut? (y/n):[/] ").strip().lower()
        if pilihan in ("n", "no", "tidak"):
            console.print("\n[bold green][✓] Terima kasih telah menggunakan DomainScope by KabC0op[/]\n")
            break

if __name__ == "__main__":
    main()