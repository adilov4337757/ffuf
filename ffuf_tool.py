import subprocess
import argparse
import datetime

def run_ffuf(url, wordlist, output_file):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"{output_file}_{timestamp}.txt"

    command = [
        "ffuf",
        "-u", f"{url}/FUZZ",
        "-w", wordlist,
        "-o", output_file,
        "-of", "json"
    ]

    print("[+] FFUF işə salınır...")
    subprocess.run(command)

    print(f"[+] Nəticələr: {output_file} faylına yazıldı.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FFUF avtomatlaşdırma skripti")
    parser.add_argument("-u", "--url", required=True, help="Hədəf URL (https://example.com)")
    parser.add_argument("-w", "--wordlist", required=True, help="Wordlist faylı (/usr/share/wordlists/dirb/common.txt)")
    parser.add_argument("-o", "--output", default="ffuf_results", help="Çıxış faylının adı (default: ffuf_results)")
    
    args = parser.parse_args()
    
    run_ffuf(args.url, args.wordlist, args.output)
