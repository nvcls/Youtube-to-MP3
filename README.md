# YouTube to MP3 Desktop Downloader

A fast, modern, and minimal Windows desktop application for downloading high‑quality MP3 audio from YouTube links. Built with **CustomTkinter**, powered by **yt-dlp**, and enhanced with **Windows Acrylic** for a sleek, native look.

---

## ✨ Features
* **One‑click MP3 downloads** using yt-dlp
* **Smooth Windows 11 Acrylic backdrop** (DWM) for a professional UI
* **Real‑time status updates** (progress, speed, ETA)
* **Automatic MP3 conversion** via FFmpeg
* **Clean, compact, and modern UI** made with CustomTkinter
* **Threaded downloads** — GUI never freezes
* **Safe and sandboxed**: downloads are stored automatically in `/downloads`

---

## 📦 Requirements

Before running, ensure you have the following installed:

### **Python 3.9+**
Download from: [https://www.python.org](https://www.python.org)

### **FFmpeg (for MP3 conversion)**
You *must* have FFmpeg installed and added to your system PATH.

* Windows Build: [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
* After installing, ensure running this works:

```powershell
ffmpeg -version
```

### Python Libraries

Install the required packages:

```bash
pip install customtkinter yt-dlp
```

---

## 🚀 Usage
1. Run the script:

```bash
python nvricals.py
```

2. Paste any YouTube link into the input box.
3. Click **Download MP3**.
4. The app will:

   * Fetch best audio
   * Convert it to MP3 (192kbps)
   * Save it in: `./downloads/<title>.mp3`

---

## 🧩 How It Works

### **1. Windows Acrylic Integration**
The script uses `DwmSetWindowAttribute` on Windows to apply a modern acrylic blurred background to the app window.
### **2. Threaded Downloading**
All yt-dlp operations run in a separate thread so the GUI remains smooth.
### **3. yt-dlp + FFmpeg**
Downloads best audio, then a postprocessor converts it into a high‑quality MP3.
### **4. Safe UI Updates**
Tkinter isn’t thread-safe, so `.after()` is used to update labels from any thread.

---

## 📁 Folder Structure

```
project/
│   musicly.py
│   README.md
└── downloads/
        <mp3 files will appear here>
```

---

## 🔧 Customizing

You can easily modify:

* Output folder
* Default quality
* Appearance mode / theme
* Window size, title, and components

All key settings are clearly labeled inside the script.

---

## 🛠 Troubleshooting

### **"Download failed"**

Check your console — FFmpeg or yt-dlp may not be installed correctly.

### **MP3 not converting**

Ensure `ffmpeg.exe` is accessible via PATH.

### **Acrylic not appearing**

Requires Windows 10 1903+ or Win11.

---

## 📄 License
This project is open-source. Modify and use freely.

---


