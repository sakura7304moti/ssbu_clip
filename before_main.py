from src import ocr,drive
"""
OCRでスマブラの動画にタイトルをつける
"""
ocr.main()

"""
未クリップをドライブにアップロード
"""
drive.sozai()
drive.named()

"""
その他のファイルをドライブにアップロード
"""
drive.other()
drive.share_db()