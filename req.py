import subprocess
import sys
import importlib
import time
import random
import threading

spinner_chars = ["|", "/", "-", "\\", "."]

def spinner(message, stop_event):
    i = 0
    while not stop_event.is_set():
        print(f"\r{spinner_chars[i % len(spinner_chars)]} {message}", end="", flush=True)
        time.sleep(0.1)
        i += 1
    print(f"\r✓ {message} done!        ")

def progress_bar(package, stop_event, bar_length=30):
    start = time.time()
    while not stop_event.is_set():
        elapsed = time.time() - start
        progress = (elapsed % 5.0) / 5.0  
        filled = int(bar_length * progress)
        bar = "[" + "=" * filled + " " * (bar_length - filled) + "]"
        print(f"\r{bar} Installing '{package}'...", end="", flush=True)
        time.sleep(0.1)
    print(f"\r✓ Installed '{package}'{' ' * 30}")

def install_and_import(package_name, import_name=None):
    import_name = import_name or package_name
    try:
        importlib.import_module(import_name)
        print(f"✓ '{package_name}' is already installed.")
    except ImportError:
        mode = random.choice(["spinner", "bar"])
        stop_event = threading.Event()
        
        if mode == "spinner":
            thread = threading.Thread(target=spinner, args=(f"Installing '{package_name}'", stop_event))
        else:
            thread = threading.Thread(target=progress_bar, args=(package_name, stop_event))
        
        thread.start()
        try:
            subprocess.check_output([sys.executable, "-m", "pip", "install", package_name], stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            stop_event.set()
            thread.join()
            print(f"\n❌ Failed to install '{package_name}'.")
            return
        stop_event.set()
        thread.join()

def used():
    required_packages = [
        "sounddevice",
        "lameenc",
        "numpy",
        "torchaudio",
        "resemblyzer",
        "faster-whisper",
        "torchaudio",
        "transformers"
    ]

    for pkg in required_packages:
        install_and_import(pkg)

if __name__ == "__main__":
    used()
