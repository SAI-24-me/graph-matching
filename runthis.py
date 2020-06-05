# -*- coding: UTF-8 -*-
import matplotlib
from matplotlib import pyplot as plt

from ga_method import ga_mehod
from greedyMapping import gm
from makeGraphMaching import makeM
from sm_method import sm_mehod

'''
97行 on_key_press 开始实现图匹配
'''


class dian:
    def __init__(self, line):
        self.line = line
        self.index_02 = None
        self.press = None
        self.pick = None
        self.motion = None
        self.xs = list()
        self.ys = list()
        self.cidpress = line.figure.canvas.mpl_connect('button_press_event', self.on_press)
        self.cidrelease = line.figure.canvas.mpl_connect('button_release_event', self.on_release)
        self.cidmotion = line.figure.canvas.mpl_connect('motion_notify_event', self.on_motion)
        self.cidpick = line.figure.canvas.mpl_connect('pick_event', self.on_picker)

    def on_press(self, event):
        if event.inaxes != self.line.axes: return
        self.press = 1

    def on_motion(self, event):
        if event.inaxes != self.line.axes: return
        if self.press is None: return
        if self.pick is None: return
        if self.motion is None:
            self.motion = 1
            x = self.xs
            xdata = event.xdata
            ydata = event.ydata
            index_01 = 0
            for i in x:
                if abs(i - xdata) < 0.019:
                    if abs(self.ys[index_01] - ydata) < 0.019: break
                index_01 = index_01 + 1
            self.index_02 = index_01
        if self.index_02 is None: return
        self.xs[self.index_02] = event.xdata
        self.ys[self.index_02] = event.ydata
        self.draw_01()

    def on_release(self, event):
        if event.inaxes != self.line.axes: return
        if self.pick == None:
            self.xs.append(event.xdata)
            self.ys.append(event.ydata)
        if self.pick == 1 and self.motion != 1:
            x = self.xs
            xdata = event.xdata
            ydata = event.ydata
            index_01 = 0
            for i in x:
                if abs(i - xdata) < 0.02:
                    if abs(self.ys[index_01] - ydata) < 0.02: break
                index_01 = index_01 + 1
            self.xs.pop(index_01)
            self.ys.pop(index_01)
        self.draw_01()
        self.pick = None
        self.motion = None
        self.press = None
        self.index_02 = None

    def on_picker(self, event):
        self.pick = 1

    def draw_01(self):
        self.line.clear()
        self.line.axis([0, 1, 0, 1])
        self.line.scatter(self.xs, self.ys, color='b', s=200, marker="o", picker=5)
        # self.line.plot(self.xs, self.ys, color='r')
        self.line.figure.canvas.draw()


class lian:
    def __init__(self, fig, ax1, ax2):
        self.fig = fig
        self.keybordpress = self.fig.canvas.mpl_connect('key_press_event', self.on_key_press)
        self.ax2 = ax2.line
        self.ax1 = ax1.line
        self.x1 = ax1.xs
        self.x2 = ax2.xs
        self.y2 = ax2.ys
        self.y1 = ax1.ys

    def on_key_press(self, event):  # x1,y1为图一坐标 ,x2,y2为图二坐标
        self.fig.lines.clear()
        n = len(self.x1)
        m = len(self.x2)
        if n > m:
            M = makeM(self.x1, self.y1, self.x2, self.y2)  # 创造相似度矩阵nm*nm
            ans_sm = sm_mehod(n, m, M)  # sm方法
            xy = gm(ans_sm)  # 结果贪心算法获取匹配点下标
            for i, j in xy:
                x1 = self.x1[i]
                y1 = self.y1[i]
                x2 = self.x2[j]
                y2 = self.y2[j]
                transFigure = fig.transFigure.inverted()
                coord1 = transFigure.transform(ax1.transData.transform([x1, y1]))
                coord2 = transFigure.transform(ax2.transData.transform([x2, y2]))
                line = matplotlib.lines.Line2D((coord1[0], coord2[0]), (coord1[1], coord2[1]), color='r', linewidth=2.0,
                                               transform=fig.transFigure)
                self.fig.lines.append(line)

            ans_ga = ga_mehod(n, m, M)
            xy = gm(ans_ga)
            for i, j in xy:
                x1 = self.x1[i]
                y1 = self.y1[i]
                x2 = self.x2[j]
                y2 = self.y2[j]
                transFigure = fig.transFigure.inverted()
                coord1 = transFigure.transform(ax1.transData.transform([x1, y1]))
                coord2 = transFigure.transform(ax2.transData.transform([x2, y2]))
                line = matplotlib.lines.Line2D((coord1[0], coord2[0]), (coord1[1], coord2[1]), color='g', linewidth=1.0,
                                               transform=fig.transFigure)
                self.fig.lines.append(line)
            self.fig.canvas.draw()

        else:
            M = makeM(self.x2, self.y2, self.x1, self.y1)
            ans_sm = sm_mehod(m, n, M)
            xy = gm(ans_sm)
            for i, j in xy:
                x1 = self.x1[j]
                y1 = self.y1[j]
                x2 = self.x2[i]
                y2 = self.y2[i]
                transFigure = fig.transFigure.inverted()
                coord1 = transFigure.transform(ax1.transData.transform([x1, y1]))
                coord2 = transFigure.transform(ax2.transData.transform([x2, y2]))
                line = matplotlib.lines.Line2D((coord1[0], coord2[0]), (coord1[1], coord2[1]), color='r', linewidth=2.0,
                                               transform=fig.transFigure)
                self.fig.lines.append(line)

            ans_ga = sm_mehod(m, n, M)
            xy = gm(ans_ga)
            for i, j in xy:
                x1 = self.x1[j]
                y1 = self.y1[j]
                x2 = self.x2[i]
                y2 = self.y2[i]
                transFigure = fig.transFigure.inverted()
                coord1 = transFigure.transform(ax1.transData.transform([x1, y1]))
                coord2 = transFigure.transform(ax2.transData.transform([x2, y2]))
                line = matplotlib.lines.Line2D((coord1[0], coord2[0]), (coord1[1], coord2[1]), color='g', linewidth=1.0,
                                               transform=fig.transFigure)
                self.fig.lines.append(line)
            self.fig.canvas.draw()


if __name__ == '__main__':
    fig = plt.figure("redlines-sm,greenlines-ga,press any key to makegraphmaching", figsize=(12, 6))  #
    fig.canvas.mpl_disconnect(fig.canvas.manager.key_press_handler_id)
    ax2 = fig.add_subplot(122)
    ax1 = fig.add_subplot(121)
    g1 = dian(ax1)
    g2 = dian(ax2)
    mylian = lian(fig, g1, g2)
    plt.show()
