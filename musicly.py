import customtkinter as ctk
import yt_dlp
import threading
import os
import ctypes
from ctypes import wintypes

# ------------------- ENABLE WINDOWS ACRYLIC ------------------- #

def enable_acrylic(hwnd):
    DWMWA_SYSTEMBACKDROP_TYPE = 38
    backdrop_type = wintypes.DWORD(2)  # Acrylic
    try:
        ctypes.windll.dwmapi.DwmSetWindowAttribute(
            hwnd,
            DWMWA_SYSTEMBACKDROP_TYPE,
            ctypes.byref(backdrop_type),
            ctypes.sizeof(backdrop_type)
        )
    except Exception:
        pass


# ------------------- DOWNLOAD LOGIC --------------------------- #

def download_audio():
    url = url_entry.get().strip()
    if not url:
        status_update("Please paste a URL.", "red")
        return

    status_update("Starting download...", "white")

    def run_thread():
        output_folder = "downloads"
        os.makedirs(output_folder, exist_ok=True)

        # progress hook to update UI from yt_dlp
        def progress_hook(d):
            status = d.get("status")
            if status == "downloading":
                # percent string comes like ' 12.3%'
                percent = d.get("_percent_str") or d.get("percent") or ""
                speed = d.get("_speed_str") or ""
                eta = d.get("_eta_str") or ""
                status_update(f"Downloading... {percent} {speed} ETA {eta}", "white")
            elif status == "finished":
                status_update("Converting to mp3...", "white")

        # NOTE: outtmpl should keep the original extension so postprocessor can find it
        ydl_opts = {
            "format": "bestaudio/best",
            # don't hard-code ffmpeg_location unless you know where ffmpeg.exe lives;
            # rely on ffmpeg being in PATH (recommended) to avoid path issues
            # "ffmpeg_location": os.path.abspath("."),
            "outtmpl": f"{output_folder}/%(title)s.%(ext)s",
            "quiet": True,
            "noplaylist": True,
            "progress_hooks": [progress_hook],
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            status_update("✔ Download complete! Saved to /downloads", "#00ff99")

        except Exception as e:
            # show the exception text so you can paste it back if something goes wrong
            status_update(f"Download failed", "#ff5555")

    threading.Thread(target=run_thread, daemon=True).start()


# Helper to safely update UI from any thread
def status_update(text, color="white"):
    # Tkinter is not thread-safe; use app.after to call configure on the main thread
    def _update():
        status_label.configure(text=text, text_color=color)
    try:
        app.after(0, _update)
    except Exception:
        # if app isn't created yet, ignore
        pass


# ------------------- GUI --------------------------- #

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("nvricals")
app.geometry("520x240")
app.resizable(False, False)

app.after(50, lambda: enable_acrylic(ctypes.windll.user32.GetForegroundWindow()))

panel = ctk.CTkFrame(app, corner_radius=20)
panel.pack(fill="both", expand=True, padx=20, pady=20)

title_label = ctk.CTkLabel(panel, text="nvricals", font=("Segoe UI", 24, "bold"))
title_label.pack(pady=(20, 10))

url_entry = ctk.CTkEntry(panel, width=440, height=42, corner_radius=12, placeholder_text="Paste link here...")
url_entry.pack(pady=10)

download_button = ctk.CTkButton(panel, text="Download MP3", width=440, height=42, corner_radius=12, command=download_audio)
download_button.pack(pady=10)

status_label = ctk.CTkLabel(panel, text="", font=("Segoe UI", 14))
status_label.pack(pady=8)

# small hint line
# hint_label = ctk.CTkLabel(panel, text="Tip: install ffmpeg and add it to PATH for conversions to work.", font=("Segoe UI", 10))
# hint_label.pack(side="bottom", pady=(1, 2))

app.mainloop()