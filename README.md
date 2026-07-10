# DomainScope

Tools sederhana untuk *reconnaissance*: lookup IP, lokasi, ISP, dan info geolokasi dari sebuah domain.

## Fitur
- Lookup IP address dari domain
- Info negara, region, kota
- Info ISP
- Timezone
- Latitude / Longitude

## Instalasi
JANGAN LUPA INSTALL LIBRARY DAN WAJIB PAKAI PYTHON3 ATAU VERSI YANG TERBARU
```bash
pip3 install -r requirements.txt <----- library
```

```bash
git clone https://github.com/KabC0op/Domain-Scope.git
cd Domain-Scope
```

## Troubleshooting

### `error: externally-managed-environment` saat `pip3 install`
Beberapa distro Linux terbaru (contoh: Kali Linux, Debian, Ubuntu 23.04+) mengunci Python sistem sehingga `pip install` langsung akan gagal dengan error ini. Ini bukan bug dari DomainScope, melainkan proteksi bawaan OS (PEP 668).

**Solusi (disarankan) — pakai virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 domainscope.py
```
Setiap kali mau menjalankan tools ini lagi, aktifkan dulu venv-nya dengan `source venv/bin/activate`.

**Solusi alternatif — override paksa (berisiko, gunakan dengan hati-hati):**
```bash
pip3 install -r requirements.txt --break-system-packages
```

## Cara Pakai

```bash
python3 domainscope.py
```

Setelah dijalankan, masukkan nama domain (contoh: `google.com`), lalu hasil lookup akan terlihat sesuai Scanning yang berjalan.

## Author
- **KabC0op**
- Instagram: [@Blockkop_](https://instagram.com/Blockkop_)
- Reddit: CAPk0pp

## Disclaimer
Tools ini dibuat untuk tujuan edukasi dan reconnaissance yang sah (misalnya cek server sendiri). Gunakan dengan bertanggung jawab.

## Lisensi
Proyek ini menggunakan lisensi MIT — lihat file [LICENSE](LICENSE) untuk detail.
