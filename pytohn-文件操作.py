"""
mode模式分类:'r' 只读
            'w' 只写
            'a' 追加
            '增加b':rb,wb,ab  处理二进制文件，例如图片视频等
            '增加+':r+,w+,a+,rb+,wb+,ra+
"""
testfile=open('test.txt','w+')
content=testfile.read()
print(content)
testfile.write("He")
