# Python ve FFUF quraşdırın
sudo apt update && sudo apt install ffuf python3 -y

# Skript yükləyin və icazələr verin
git clone https://github.com/adilov4337757/ffuf.git
cd ffuf
chmod +x ffuf_tool.py

# Skripti işə salın
python3 ffuf_tool.py -u https://target.com -w /usr/share/wordlists/dirb/common.txt -o results

# Nəticələrə baxın 
cat results_YYYY-MM-DD_HH-MM-SS.txt

# Əgər problem yaranarsa köməkçi  menyuya baxa bilərsiz
ffuf -h 
