import os
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import GetDialogsRequest
from tqdm import tqdm

# ====== User: Fill these in ======
API_ID = 123456 # <-- Replace with your API ID
API_HASH = 'your_api_hash' # <-- Replace with your API Hash
CHANNEL_NAME = 'My Channel Name' # <-- The channel's name (exactly as shown in Telegram)
SAVE_FOLDER = 'Downloads' # (Optional) Folder to save files, default is 'Downloads'
# ================================

def find_channel(client, name):
    dialogs = client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=100,
        hash=0
    ))
    for chat in dialogs.chats:
        if chat.title == name:
            return chat
    return None

def media_type_selected(msg, selection):
    # 1 = photo, 2 = video, 3 = document (excluding video docs)
    if 1 in selection and msg.photo:
        return True
    if 2 in selection and (msg.video or (msg.document and any(attr.mime_type and attr.mime_type.startswith('video') for attr in [msg.document]))):
        # If msg.video present, Telethon sets it; else, for some video docs, check mime type
        return True
    if 3 in selection:
        # Document but not video (by extension)
        if msg.document:
            mime = getattr(msg.document, 'mime_type', '')
            if not (mime and mime.startswith('video')):
                return True
    return False

def get_user_selection():
    print("\nSelect media types to download (you can choose multiple, separated by commas):")
    print("   1. Photos")
    print("   2. Videos")
    print("   3. Documents")
    choices = input("Enter your choice(s) (e.g., 1 or 1,2 or 2,3): ").strip()
    sel = set()
    for c in choices.replace(' ', '').split(','):
        if c in {'1', '2', '3'}:
            sel.add(int(c))
    if not sel:
        print("No valid selection made. Defaulting to all types (1, 2, 3).")
        return {1, 2, 3}
    return sel

def download_selected_media(client, channel, output_folder, selection):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    count = 0
    for message in tqdm(client.iter_messages(channel), desc="Downloading Media"):
        try:
            if message.media and media_type_selected(message, selection):
                message.download_media(file=output_folder)
                count += 1
        except Exception as e:
            print(f"[!] Failed on message {message.id}: {e}")
    print(f"\n✔️ Done! {count} media files downloaded to: {output_folder}")

def main():
    print("\n=== Telegram Channel Archiver (Selective Download) ===\n")
    # Check placeholder values
    if API_ID == 123456 or API_HASH == 'your_api_hash' or not CHANNEL_NAME:
        print("Please edit this script and set your API_ID, API_HASH, and CHANNEL_NAME near the top of the file.")
        return

    selection = get_user_selection()
    with TelegramClient('archiver_session', API_ID, API_HASH) as client:
        channel = find_channel(client, CHANNEL_NAME)
        if not channel:
            print(f"❌ Channel '{CHANNEL_NAME}' not found. Make sure you're a member.")
            return

        print(f"🔍 Channel found: {channel.title}\nStarting download of selected media type(s)...\n")
        download_selected_media(client, channel, SAVE_FOLDER, selection)

if __name__ == '__main__':
    main()
