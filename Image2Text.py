#encoding=utf-8
import argparse
from PIL import Image
'''
这个代码利用PIL处理图片,将一张图片映射到记事本用字符表现出来
'''
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
parse=argparse.ArgumentParser()
parse.add_argument("file")
parse.add_argument("--width",type=int,default=80)
parse.add_argument("--height",type=int,default=80)
args=parse.parse_args()

fileurl=args.file
WIDTH=args.width
HEIGHT=args.height
#将256灰度值映射到70个字符上
def get_char(r,g,b,alpha=256):
	#这个表示透明
	if alpha==0:
		return ' '
	length=len(ascii_char)
	#这里利用传的rgb值来获取对应的灰度值，最大值为256
	gray=int(0.2126*r+0.7152*g+0.0722*b)
	#这里的length值为70，进行下面操作则会保证返回的索引为0-69
	unit=(256.0+1)/length
	return ascii_char[int(gray/unit)]

if __name__=='__main__':
	im=Image.open(fileurl)
	im.resize((WIDTH,HEIGHT))
	txt=""
	width=im.size[0]
	height=im.size[1]
	for i in range(height):
		for j in range(width):
			txt+=get_char(*im.getpixel((j,i)))
		txt+="\n"	

	with open('outfile.txt','w') as f:
		f.write(txt)
