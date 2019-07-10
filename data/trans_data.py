import re
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

cjk_logic = {
    '<Beijing>': '京', 
    '<Shanghai>': '沪', 
    '<Tianjin>': '津', 
    '<Chongqing>': '渝', 
    '<Hebei>': '冀', 
    '<Shaanxi>': '晋',
    '<Shanxi>': '晋',
    '<InnerMongolia>': '蒙', 
    '<Liaoning>': '辽', 
    '<Jilin>': '吉', 
    '<Heilongjiang>': '黑',
    '<Jiangsu>': '苏', 
    '<Zhejiang>': '浙', 
    '<Anhui>': '皖', 
    '<Fujian>': '闽', 
    '<Jiangxi>': '赣', 
    '<Shandong>': '鲁', 
    '<Henan>': '豫', 
    '<Hubei>': '鄂', 
    '<Hunan>':'湘', 
    '<Guangdong>': '粤',
    '<Guangxi>': '桂', 
    '<Hainan>' :'琼', 
    '<Sichuan>' :'川', 
    '<Guizhou>' :'贵', 
    '<Yunnan>': '云', 
    '<Tibet>': '藏', 
    '<Shaanxi>':'陕', 
    '<Gansu>': '甘', 
    '<Qinghai>':'青', 
    '<Ningxia>':'宁',
    '<Xinjiang>': '新'
}

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    annotation_path = os.path.join(BASE_DIR, sys.argv[2])
    training_path = os.path.join(BASE_DIR, sys.argv[1])
    cjk = re.compile('<[A-Za-z]+>')
    number_english = re.compile('(?<=>)[A-Za-z0-9]+')
    with open(annotation_path, 'r') as annoation_file:
        for line in annoation_file.readlines():
            line = line.split(' ')
            print(line[1])
            print(cjk.search(line[1]).group(0))
            print(number_english.search(line[1]).group(0))
            new_name = cjk_logic[cjk.search(line[1]).group(0)] + number_english.search(line[1]).group(0) + '.png'
            print(new_name)
            os.rename(os.path.join(training_path, line[0]), os.path.join(training_path, new_name)) 
