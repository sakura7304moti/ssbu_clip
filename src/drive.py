#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime
import glob
import os
import shutil
from tqdm import tqdm
import sqlite3
import pandas as pd

def base_update(fromName:str,toName:str):
    copy_from_list = glob.glob(f'D:/素材/スマブラ/切り抜き/{fromName}/*')

    copy_to_base = f'G:/マイドライブ/クラウドデータまとめ/スマブラの動画/{toName}'
    
    if not os.path.exists(copy_to_base):
        os.makedirs(copy_to_base)
    
    copy_to_list = [os.path.basename(path) for path in glob.glob(f'G:/マイドライブ/クラウドデータまとめ/スマブラの動画/{toName}/*')]

    copy_list = [path for path in copy_from_list if os.path.basename(path) not in copy_to_list]

    #ファイルコピーを実行
    for copy_from in tqdm(copy_list):
        copy_to = os.path.join(copy_to_base,os.path.basename(copy_from))
        print('-----')
        print('FROM ',copy_from)
        print('TO ',copy_to)
        shutil.copyfile(copy_from,copy_to)


# ## キャラ別

# In[2]:


#キャラ別でアップロードしていない動画をアップロードする
def char_update():
    #キャラクターごとのループ
    for char_name_path in tqdm(glob.glob(r'D:/素材/スマブラ/切り抜き/キャラクター別/*')):
        #キャラ単位で動画のパスのリストを取得
        copy_from_list = glob.glob(os.path.join(char_name_path,'*.mp4'))
        #キャラ名だけを変数にセット
        char_name = os.path.basename(char_name_path)
        
        #ドライブに保存されている動画のパスを取得
        copy_to_base = os.path.join(r'G:/マイドライブ/クラウドデータまとめ/スマブラの動画/キャラクター別',char_name)
        copy_to_list = [os.path.basename(path) for path in glob.glob(os.path.join(copy_to_base,'*'))]
        
        #ローカルにあってドライブにない動画のパスを取得
        copy_list = [path for path in copy_from_list if os.path.basename(path) not in copy_to_list]
        
        print('char : ',char_name)
        print('copy_list')
        for path in copy_list:
            print(path)
        print('-----------')
        print('')
        #ファイルコピーを実行
        for path in copy_list:
            if not os.path.exists(copy_to_base):
                os.makedirs(copy_to_base)
            shutil.copyfile(path,os.path.join(copy_to_base,os.path.basename(path)))

def clip():
    local_list = glob.glob(r'D:/素材/スマブラ/切り抜き/*/*/*/*.mp4')
    
    drive_list = glob.glob(r'G:/マイドライブ/クラウドデータまとめ/スマブラの動画/*/*/*/*.mp4')
    drive_list = [os.path.basename(path) for path in drive_list if '切り抜き' in path]
    
    copy_list = [path for path in local_list if os.path.basename(path) not in drive_list]
    
    drive_base = r'G:/マイドライブ/クラウドデータまとめ/スマブラの動画'
    for path in tqdm(copy_list):
        to_base = path.replace('D:/素材/スマブラ/切り抜き\\','')
        copy_to = os.path.join(drive_base,to_base)
        copy_to_dir = os.path.dirname(copy_to)
        print('FROM:',path)
        print('TO:',copy_to)

        if not os.path.exists(copy_to_dir):
            os.makedirs(copy_to_dir)

        shutil.copyfile(path,copy_to)
        

def other():
    copy_from = r'D:/素材/スマブラ/データベース/ssbu_dict.csv'
    copy_to = r'G:/マイドライブ/クラウドデータまとめ/スマブラの動画/プログラム用/ssbu_dict.csv'
    shutil.copyfile(copy_from,copy_to)

def _copy_file(source_path, destination_folder):
    # 今日の年、月、日を取得
    today = datetime.date.today()
    year = str(today.year)
    month = today.strftime("%m")
    day = today.strftime("%Y%m%d")

    # 保存先のフォルダパスを作成
    destination_folder = os.path.join(destination_folder, year, day)

    # 保存先のフォルダが存在しない場合、作成する
    os.makedirs(destination_folder, exist_ok=True)

    # コピー先のファイルパスを作成
    destination_path = os.path.join(destination_folder, os.path.basename(source_path))

    # ファイルをコピーする
    shutil.copy2(source_path, destination_path)

def share_db():
    """
    ドライブにアップロードする
    """
    # コピー元のファイルパス
    source_file = r"Z:/Python/sharemotiApi/share.db"

    # コピー先のフォルダパス
    destination_folder = r"G:/マイドライブ/クラウドデータまとめ/データベースバックアップ"

    # ファイルをコピーする
    print('google drive copy...')
    _copy_file(source_file, destination_folder)


    """
    ローカルのssbu_dict.csvを更新する
    """
    dbname = r'Z:/Python/sharemotiApi/share.db'
    print('database connect...')
    conn = sqlite3.connect(dbname)
    query = "select * from nameList"
    print('query wait')
    results = pd.read_sql_query(query,conn)
    results = results.sort_values(by='val')
    results.to_csv(r'D:/素材/スマブラ/データベース/ssbu_dict.csv', index=False)
    shutil.copyfile(r'D:/素材/スマブラ/データベース/ssbu_dict.csv',r'G:/マイドライブ/クラウドデータまとめ/スマブラの動画/プログラム用/ssbu_dict.csv')


"""
未クリップ
"""
def sozai():
    local_list = glob.glob(r'D:/素材/スマブラ/素材/*/*/*/*.mp4')
    local_list = [path for path in local_list if '切り抜き' not in path]
    
    drive_list = glob.glob(r'G:/マイドライブ/クラウドデータまとめ/スマブラの動画/*/*/*/*.mp4')
    drive_list = [os.path.basename(path) for path in drive_list if '切り抜き' not in path]
    
    copy_list = [path for path in local_list if os.path.basename(path) not in drive_list]
    
    drive_base = r'G:/マイドライブ/クラウドデータまとめ/スマブラの動画'
    for path in tqdm(copy_list):
        copy_to = os.path.join(drive_base,*path.split('\\')[1:])
        print('FROM:',path)
        print('TO:',copy_to)
        copy_to_dir = os.path.dirname(copy_to)

        if not os.path.exists(copy_to_dir):
            os.makedirs(copy_to_dir)

        shutil.copyfile(path,copy_to)
        
def named():
    local_list = glob.glob(r'D:/素材/スマブラ/素材キャラ名つき/*/*/*/*.mp4')
    drive_list = [os.path.basename(path) for path in glob.glob(r'G:/マイドライブ/クラウドデータまとめ/スマブラの動画/未クリップのキャラ名つき/*/*/*/*.mp4')]
    copy_list = [path for path in local_list if os.path.basename(path) not in drive_list]
    drive_base = r'G:/マイドライブ/クラウドデータまとめ/スマブラの動画'
    for path in tqdm(copy_list):
        copy_to = os.path.join(drive_base,'未クリップのキャラ名つき',*path.split('\\')[1:])
        copy_to_dir = os.path.dirname(copy_to)

        if not os.path.exists(copy_to_dir):
            os.makedirs(copy_to_dir)

        shutil.copyfile(path,copy_to)