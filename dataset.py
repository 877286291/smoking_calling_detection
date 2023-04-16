import os
from xml.dom.minidom import parse
import xml.dom.minidom


# 获取所有xml文件

def get_xml():
    xml_list = []
    for root, dirs, files in os.walk(r"C:\Users\Administrator.DESKTOP-FK9M9OJ\Downloads\pp_smoke\Annotations"):
        for name in files:
            xml_list.append(os.path.join(root, name))
    return xml_list


def parse_xml(xml_file):
    dom_tree = xml.dom.minidom.parse(xml_file)
    collection = dom_tree.documentElement
    size = collection.getElementsByTagName("size")[0]
    img_w = int(size.getElementsByTagName("width")[0].childNodes[0].data)
    img_h = int(size.getElementsByTagName("height")[0].childNodes[0].data)
    objs = collection.getElementsByTagName("object")
    for obj in objs:
        x1 = int(obj.getElementsByTagName("xmin")[0].childNodes[0].data)
        y1 = int(obj.getElementsByTagName("ymin")[0].childNodes[0].data)
        x2 = int(obj.getElementsByTagName("xmax")[0].childNodes[0].data)
        y2 = int(obj.getElementsByTagName("ymax")[0].childNodes[0].data)
        x_center = round((x1 + x2) / (2.0 * img_w), 6)
        y_center = round((y1 + y2) / (2.0 * img_h), 6)
        width = round((x2 - x1) / (1.0 * img_w), 6)
        height = round((y2 - y1) / (1.0 * img_h), 6)
        with open(f"datasets/smoking/labels/train/{os.path.split(xml_file)[-1].split('.')[0]}.txt", "a+") as f:
            f.write(f"{0} {x_center} {y_center} {width} {height}" + '\n')


if __name__ == '__main__':
    for file in get_xml():
        parse_xml(file)
