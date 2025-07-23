# Telegram Channel Downloader

Download photos, videos, and documents from any Telegram channel you are a member of, directly to your computer.  
Built with [Telethon](https://github.com/LonamiWebs/Telethon) for reliability and privacy.

---

## 📌 Features

- Choose to download **photos**, **videos**, **documents**, or any combination
- Works with both public and private channels (where you are a member)
- Saves all downloaded files to a folder of your choice
- Uses your own Telegram API credentials for secure authentication
- Easy command-line interface

---

## 📦 Installation

1. **Clone this repository:**
git clone https://github.com/Nizamkhzn/Telegram-Channel-Downloader.git

cd Telegram-Channel-Downloader



2. **Install dependencies:**

pip install -r requirements.txt



> Requires Python 3.8 or higher

---

## 🔑 Telegram API Setup

To use this tool, you’ll need your own Telegram API credentials:

1. Go to [my.telegram.org](https://my.telegram.org)
2. Log in with your Telegram account
3. Select **API Development Tools** and create a new application
4. Copy your **API ID** and **API Hash** from this page

**Keep these credentials confidential**.

---

## ⚙️ Setup: Configure the Script

Before running the script, open `downloader.py` in a text editor and fill in the section at the top:

API_ID = 123456 # <-- Replace with your API ID
API_HASH = 'your_api_hash' # <-- Replace with your API Hash
CHANNEL_NAME = 'My Channel Name' # <-- The channel's name (exactly as shown in Telegram)
SAVE_FOLDER = 'Downloads' # (Optional) Folder to save files, default is 'Downloads'



*You must be a member of the target channel.*

---

## ▶️ Usage

Run the script with:

python downloader.py



You will be prompted to select which types of media to download:

Select media types to download (you can choose multiple, separated by commas):

Photos

Videos

Documents
Enter your choice(s) (e.g., 1 or 1,2 or 2,3):



Choose one or several options (for example, `1` for photos, `1,2` for photos and videos, `1,2,3` for all).

All chosen media files will be downloaded into the folder you specified.

---

### Example

Suppose your top configuration in `downloader.py` is:

API_ID = 1234567
API_HASH = 'a1b2c3d4e5f6g7'
CHANNEL_NAME = 'example'
SAVE_FOLDER = 'Archive'



You run:

python downloader.py



You select: `1,2`

- **All photos and videos** are downloaded to the `Archive` folder.

---

## 📂 Output

- Downloaded files are saved to your specified folder (`SAVE_FOLDER`).
- Files keep their original names when possible.
- A `.session` file is created for secure authentication (do not delete if you want to stay logged in).

---

## ⚠️ Limitations

- Only works for Telegram channels which you are a member of (public or private).
- Telegram bots, private chats, groups, or expired messages are **not** supported.
- Download speeds may be slow due to Telegram API limitations.
- Media deleted from the channel cannot be recovered.

---

## 🔒 Security Notice

- Your API credentials are stored only locally and **not** uploaded anywhere.
- The `.session` authentication file is saved locally in the project directory.
- This script never asks for or stores your Telegram password.

---

## 🤝 Contributing

Contributions are welcome! If you have ideas, bug reports, or enhancements:
- Fork this repository
- Make your changes in a separate branch
- Open a pull request with a summary of your modifications

For issues or feature requests, use the [GitHub Issues page](https://github.com/Nizamkhzn/Telegram-Channel-Downloader/issues).

---

## 📜 License

This project is licensed under the MIT License.

---

## 👍 Acknowledgements

- Built using the excellent [Telethon](https://github.com/LonamiWebs/Telethon) library.
- Thanks to everyone contributing open-source tools for Telegram.

---

_Last updated: July 24, 2025_