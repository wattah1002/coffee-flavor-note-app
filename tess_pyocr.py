import sys
import os
import datetime
from PIL import Image

import pyocr
import pyocr.builders as bd

import config as conf
import binarization as bin



root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



'''二値化なしでのpyocr適用'''
def pyocr_auto(args):
    filename = '{}.png'.format(args.filename)
    file_path = os.path.join(root_dir, 'data', filename)
    print('convert file: ', filename)

    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print('No OCR tools')
        sys.exit(1)

    tool = tools[0]
    print('tool: {} used!'.format(tool.get_name()))

    layout = args.layout
    txt = tool.image_to_string(
                        Image.open(file_path),
                        lang='jpn',
                        builder=bd.TextBuilder(tesseract_layout=layout)
                    )
    return txt



'''二値化ありのpyocr'''
def pyocr_bin(args):
    filename = '{}.png'.format(args.filename)
    file_path = os.path.join(root_dir, 'data', filename)
    print('convert file: ', filename)
    image = bin.binarize(file_path)

    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print('No OCR tools')
        sys.exit(1)

    tool = tools[0]
    print('tool: {} used!'.format(tool.get_name()))

    layout = args.layout
    txt = tool.image_to_string(
                        image,
                        lang='jpn',
                        builder=bd.TextBuilder(tesseract_layout=layout)
                    )
    return txt, image



'''条件のテキストファイル，結果のテキストファイル，二値化画像を保存'''
def save_txt(txt, args, img=0):
    dt = datetime.datetime.now()
    name = args.filename
    if args.binarization:
        flag = 'True'
    else:
        flag = 'False'
    result_name = '{}_{}_{}-{}-{}-{}-{}'.format(name, flag, dt.year, dt.month, dt.day, dt.hour, dt.minute)
    result_dir = os.path.join(root_dir, 'pyocr', 'result', result_name)

    
    os.mkdir(result_dir)
    result_file = os.path.join(result_dir, 'result.txt')
    condition_file = os.path.join(result_dir, 'condition.txt')
    binarize_img = os.path.join(result_dir, 'binarize.png')

    with open(result_file, 'w') as f:
        f.write(txt)
        f.close
    with open(condition_file, 'w') as f_:
        f_.write('Layout: {}\n'.format(args.layout))
        f_.write('Binarization: {}'.format(flag))
        f_.close
    
    if img == 0:
        print('No binarization: Done!\n')
    else:
        img.save(binarize_img)
        print('With binarization: Done!\n')

    


def main(args):
    if args.binarization:
        text, img = pyocr_bin(args)
        save_txt(text, args, img)
    else:
        text = pyocr_auto(args)
        save_txt(text, args)



if __name__ == '__main__':
    opts = conf.get_args()
    main(opts)