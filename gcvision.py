import io
import os
import argparse

from google.cloud import vision

parser = argparse.ArgumentParser()
parser.add_argument('--filename', type=str, default='test1')
opts = parser.parse_args()



def save_txt(txt):
    name = opts.filename + '.txt'
    result_dir = os.path.join('result')
    result_file = os.path.abspath(os.path.join(result_dir, name))

    with open(result_file, 'w') as f:
        f.write(txt)
        f.close
    


def main():
    client = vision.ImageAnnotatorClient()

    rel_path = '../data/' + opts.filename + '.png'
    file_name = os.path.abspath(rel_path)

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
    save_txt(output_text)

if __name__ == '__main__':
    main()