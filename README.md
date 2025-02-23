># FFUF Avtomatlaşdırma Skripti

Bu Python skripti, FFUF alətini avtomatik işə salmaq üçün hazırlanıb. 
Skript URL və wordlist qəbul edərək FFUF-u çalışdırır və nəticələri fayla yazır.

# 📌 Tələblər
- *Python 3* (Yoxlamaq üçün: python3 --version)
- *FFUF* (Yoxlamaq üçün: ffuf -V)
- *Wordlist Faylı* (Məsələn: /usr/share/wordlists/dirb/common.txt)

# 🔧 Qurulum
FFUF-un quraşdırılması üçün:
```bash
sudo apt update && sudo apt install ffuf -y


# **İstifadə Qaydaları**

python3 ffuf_tool.py -u URL -w /usr/share/wordlists/dirb/common.txt -o results

# İstənilən URL  seçə bilərsiz
