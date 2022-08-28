# Google Cloud Vision APIを用いたAI OCRの利用方法について
参考にしたサイトは[こちら](https://dev.classmethod.jp/articles/google-cloud_vision-api/)
1. Cloud Vision APIの[クイックスタート](https://cloud.google.com/vision/docs/setup)を参考に，まずはキーを取得する．
1. 使うためには，`pip install --upgrade google-cloud-vision`でパッケージをダウンロード
1. キーと紐づけるために，`export GOOGLE_APPLICATION_CREDENTIALS="jsonキーのフルパス"`を実行
1. コード内で関数を実装
    1. `from google.cloud import vision`で，visionをimport
    1. `client = vision.ImageAnnotatorClient()`
    1. PIL形式の画像を`f.read`で読み込み
    1. ```python:gcvision.py
    image = vision.Image(content=content)

    response = client.document_text_detection(
        image=image,
        image_context={'language_hints': ['ja']}
    )

    output_text = ''
    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    output_text += ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                output_text += '\n'
    ```
