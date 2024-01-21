import os
import shutil
import glob
import time
from tqdm import tqdm
import datetime

"""
----------------------------------------------------------------------------------------------
外から呼び出さないやつ
"""
#ローカルのパスのファイル名取得
def get_copy_path(path:str,word:str):
    copy_to_dir=os.path.join(r'D:\素材\スマブラ\切り抜き',word)
    return os.path.join(copy_to_dir,os.path.basename(path))

#ドライブにアップロード用の保存先
def get_drive_path(path:str,word:str):
    today = datetime.date.today()
    date = today.strftime('%Y%m%d')
    drive_copy_dir = os.path.join(r'D:\素材\スマブラ\移動用',date,word)
    if not os.path.exists(drive_copy_dir):
        os.makedirs(drive_copy_dir)
    return os.path.join(drive_copy_dir,os.path.basename(path))

"""
----------------------------------------------------------------------------------------------
外から呼び出すやつ
"""
#ドライブのコピー
def drive_cp(word:str):
    copy_to_dir=os.path.join(r'D:\素材\スマブラ\切り抜き',word)
    os.makedirs(copy_to_dir, exist_ok=True)
    
    C_list=glob.glob(os.path.join(r'D:\素材\スマブラ\切り抜き\*\*\*',f'*{word}*.mp4'))
    C_list = [path for path in C_list if not os.path.exists(get_copy_path(path,word))]
    print(f'copy files : {len(C_list)}')
    for path in tqdm(C_list):
        #ローカルへコピー
        copy_to = get_copy_path(path,word)
        shutil.copyfile(path,copy_to)

        #ドライブ用に別フォルダへコピー
        drive_path = get_drive_path(path,word)
        shutil.copyfile(path,drive_path)
