from src import folder,char,drive,clip,db
"""
切り抜きをフォルダ別にコピーする
"""
folder.drive_cp('ウルトラC')
folder.drive_cp('未来')
folder.drive_cp('焼き直し')
folder.drive_cp('ウルツラC')
folder.drive_cp('思い出')
folder.drive_cp('大江戸温泉物語')
folder.drive_cp('素材')

"""
nameListの更新
"""
db.insert_nameList(r'Z:\git\sharemotiApi2\main\share.db')

"""
切り抜きをAPIのフォルダにコピーする
"""
clip.copy_clip(r'D:\python\git\sharemotiApi\data\ssbu')
clip.copy_clip(r'Z:\Python\sharemotiApi\data\ssbu')
clip.copy_clip(r'Z:\git\sharemotiApi2\file\data\ssbu')
clip.copy_clip(r'X:\server\git\sharemotiApi2\file\data\ssbu')

"""
キャラ別に分ける
"""
char.main()

"""
ドライブにアップロード
"""
drive.base_update('ウルトラC','ウルトラC')
drive.base_update('未来','未来から来た男達')
drive.base_update('焼き直し','焼き直し')
drive.base_update('ウルツラC','ウルツラC')
drive.base_update('思い出','思い出')
drive.base_update('大江戸温泉物語','大江戸温泉物語')
drive.base_update('素材','素材')
drive.char_update()

drive.clip()
drive.other()
drive.share_db()
