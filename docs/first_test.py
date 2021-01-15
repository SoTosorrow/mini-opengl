# coding:utf-8
# first test of py-opengl

# 核心库GL用于常规的核心的图像处理
from OpenGL.GL import *
#工具库GLUT
from OpenGL.GLUT import *

def draw():
    # begin to draw lines
    glBegin(GL_LINES)
    
    # set current color is red not-alpha
    glColor4f(1.0, 0.0, 0.0, 1.0)

    # 设置x轴顶点（x轴负向）
    glVertex3f(-0.8,0.0,0.0)
    # 正向
    glVertex3f(0.8,0.0,0.0)
    
    glColor4f(0.0, 1.0, 0.0, 1.0)
    glVertex3f(0.0,-0.8,0.0)
    glVertex3f(0.0,0.8,0.0)
    glColor4f(0.0, 0.0, 1.0, 1.0)
    glVertex3f(0.0,0.0,-0.8)
    glVertex3f(0.0,0.0,0.8)


    # end
    glEnd()


    # begin to draw triangle
    glFlush()


    glBegin(GL_TRIANGLES)                # 开始绘制三角形（z轴负半区）

    glColor4f(1.0, 0.0, 0.0, 1.0)        # 设置当前颜色为红色不透明
    glVertex3f(-0.5, -0.366, -0.5)       # 设置三角形顶点
    glColor4f(0.0, 1.0, 0.0, 1.0)        # 设置当前颜色为绿色不透明
    glVertex3f(0.5, -0.366, -0.5)        # 设置三角形顶点
    glColor4f(0.0, 0.0, 1.0, 1.0)        # 设置当前颜色为蓝色不透明
    glVertex3f(0.0, 0.5, -0.5)           # 设置三角形顶点

    glEnd()                              # 结束绘制三角形


if __name__ == '__main__':
    glutInit()  # 初始化glut库
    glutCreateWindow('first test')  # 创建glut窗口
    glutDisplayFunc(draw)  # 注册回调函数draw
    glutMainLoop()

