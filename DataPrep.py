import xml.etree.ElementTree as et
from path import Path

all_fp = open('output.txt',mode='w+',encoding='utf-8')

fp = open('output-England.txt',mode='w+',encoding='utf-8')
documents_dir = Path('./England')
for file_path in documents_dir.files('*.xml'):
    tree = et.parse(file_path)
    root = tree.getroot()
    textdata = root.findtext("./{http://www.w3.org/2005/Atom}content/page/content")
    fp.write(textdata)
    all_fp.write(textdata)
fp.close()

fp = open('output-NI.txt',mode='w+',encoding='utf-8')
documents_dir = Path('./NI')
for file_path in documents_dir.files('*.xml'):
    tree = et.parse(file_path)
    root = tree.getroot()
    textdata = root.findtext("./{http://www.w3.org/2005/Atom}content/page/content")
    fp.write(textdata)
    all_fp.write(textdata)
fp.close()


fp = open('output-Scotland.txt',mode='w+',encoding='utf-8')
documents_dir = Path('./Scotland')
for file_path in documents_dir.files('*.xml'):
    tree = et.parse(file_path)
    root = tree.getroot()
    textdata = root.findtext("./{http://www.w3.org/2005/Atom}content/page/content")
    fp.write(textdata)
    all_fp.write(textdata)
fp.close()

fp = open('output-Wales.txt',mode='w+',encoding='utf-8')
documents_dir = Path('./Wales')
for file_path in documents_dir.files('*.xml'):
    tree = et.parse(file_path)
    root = tree.getroot()
    textdata = root.findtext("./{http://www.w3.org/2005/Atom}content/page/content")
    fp.write(textdata)
    all_fp.write(textdata)
fp.close()

all_fp.close()