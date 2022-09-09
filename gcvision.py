import io
import os
import glob

from google.cloud import vision


def save_txt(txt, name):
    name = name + '.txt'
    result_dir = os.path.join('result')
    result_file = os.path.abspath(os.path.join(result_dir, name))

    with open(result_file, 'w') as f:
        f.write(txt)
        f.close
    


def output(file_name):
    client = vision.ImageAnnotatorClient()

    with open(file_name, 'rb') as f:
        content = f.read()

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
    print(output_text)
    output_name = os.path.splitext(os.path.basename(file_name))[0]
    save_txt(output_text, output_name)
    print('Converted: ', output_name)

def main():
    rel_path = '../data/'
    datapath = os.path.abspath(rel_path)    
    imgs = glob.glob(datapath + '/*.png')
    for img in imgs:
        output(img)

if __name__ == '__main__':
    main()