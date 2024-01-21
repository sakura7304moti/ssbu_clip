#指定したフォルダーにスマブラの切り抜き/2022,2023...をコピーする
import glob
import os
import shutil
from tqdm import tqdm

#コピー先への2023前期,20230201,ファイル名の3つを取得
def get_dir(path):
    directory = os.path.dirname(path)
    yyyymmdd = os.path.basename(directory)
    
    up_directory = os.path.dirname(directory)
    year = os.path.basename(up_directory)
    return year,yyyymmdd,os.path.basename(path)


def copy_clip(dir_name:str):
    years = [2022,2023]
    clip_dir = r'D:\素材\スマブラ\切り抜き'
    copy_from = []
    for year in years:
        ls = glob.glob(os.path.join(clip_dir,str(year),'*','*','*.mp4'))
        for path in ls:
            copy_from.append(path)
    print(f'files -> {len(copy_from)}')
    
    for path in tqdm(copy_from):
        #保存先を取得
        year,yyyymmdd,file_name = get_dir(path)
        copy_to_dir = os.path.join(dir_name,year,yyyymmdd)

        #フォルダ作成
        if not os.path.exists(copy_to_dir):
            os.makedirs(copy_to_dir)

        #ファイルコピー
        copy_to = os.path.join(copy_to_dir,file_name)
        if not os.path.exists(copy_to):
            shutil.copyfile(path,copy_to)