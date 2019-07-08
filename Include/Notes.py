#!F:PythonWorkSpace
# encoding: utf-8
'''
@author: wangshicheng
@license: Copyright 2018-2010, Facebook.
@contact: icandicefly@163.com
@software: never ,never,never.... give up
@file: Notes.py
@time: 2019/7/4 15:45
@desc:
'''

'''
基本
- `node_size`: 指定节点的尺寸大小(默认是300，单位未知，就是上图中那么大的点)
- `node_color`: 指定节点的颜色 (默认是红色，可以用字符串简单标识颜色，例如'r'为红色，'b'为绿色等，具体可查看手册)
- `node_shape`: 节点的形状（默认是圆形，用字符串'o'标识，具体可查看手册）
- `alpha`: 透明度 (默认是1.0，不透明，0为完全透明) 
- `width`: 边的宽度 (默认为1.0)
- `edge_color`: 边的颜色(默认为黑色)
- `style`: 边的样式(默认为实现，可选： solid|dashed|dotted,dashdot)
- `with_labels`: 节点是否带标签（默认为True）
- `font_size`: 节点标签字体大小 (默认为12)
- `font_color`: 节点标签字体颜色（默认为黑色）
布局
circular_layout：节点在一个圆环上均匀分布
random_layout：节点随机分布
shell_layout：节点在同心圆上分布
spring_layout： 用Fruchterman-Reingold算法排列节点
spectral_layout：根据图的拉普拉斯特征向量排列节点


'''