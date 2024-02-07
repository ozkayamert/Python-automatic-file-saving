import os
import datetime
import shutil
import schedule
import time

source_dir = "C:\\Users\\Lenovo\\Pictures\\Screenshots"
destination_dir = "C:\\Backups"
# Çift ters tırnak kısımlarını kendimiz yaptık.

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")

# def l():
#    copy_folder_to_directory(source_dir, destination_dir)

schedule.every().day.at("18:55").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

# copy_folder_to_directory(source_dir, destination_dir)

while True:
    schedule.run_pending()
    time.sleep(60)