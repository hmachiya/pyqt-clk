import PyQt5.QtWidgets
import PyQt5.QtCore
import PyQt5.QtGui
import sys
import math
import datetime

class AnalogClock(PyQt5.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(self.windowFlags()
                            | PyQt5.QtCore.Qt.FramelessWindowHint
                            | PyQt5.QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(PyQt5.QtCore.Qt.WA_TranslucentBackground,True)
        n=datetime.datetime.now()
        self.h=n.hour
        self.m=n.minute
        self.s=n.second
        self.year=n.year
        self.month=n.month
        self.day=n.day
        self.r=16
        self.p=4
        self._is_drag=False
        self._startx=0
        self._starty=0
        self.timer=PyQt5.QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.clock_handler)
        self.timer.start()
        r=self.r
        self.setMinimumHeight((r+self.p)*2)
        self.setMinimumWidth((r+self.p)*2)
        
    def clock_handler(self):
        n=datetime.datetime.now()
        self.h=n.hour
        self.m=n.minute
        self.s=n.second
        self.year=n.year
        self.month=n.month
        self.day=n.day
        self.update()

    def draw(self):
        r=self.r
        qp=PyQt5.QtGui.QPainter()
        theta_h=-((self.h+(self.m+self.s/60)/60)/12)*2*math.pi+0.5*math.pi
        theta_m=-(self.m+self.s/60)/60*2*math.pi+0.5*math.pi
        theta_s=-self.s/60*2*math.pi
        #w=self.frameGeometry().width()
        #h=self.frameGeometry().height()
        x0=r+self.p
        y0=r+self.p
        xh=r*math.cos(theta_h)*0.5+x0
        yh=-r*math.sin(theta_h)*0.5+y0
        xm=r*math.cos(theta_m)*0.8+x0
        ym=-r*math.sin(theta_m)*0.8+y0
        xs=r*math.cos(theta_s)*0.9+x0
        ys=-r*math.sin(theta_s)*0.9+y0
        qp.begin(self)
        qp.setRenderHint(PyQt5.QtGui.QPainter.Antialiasing)
        qp.setPen(PyQt5.QtGui.QPen(PyQt5.QtCore.Qt.black, 1, PyQt5.QtCore.Qt.SolidLine))
        g=PyQt5.QtGui.QLinearGradient(0,0,0,r*2+self.p*2)
        g.setColorAt(0,PyQt5.QtGui.QColor("#666"))
        g.setColorAt(1.0,PyQt5.QtGui.QColor("#222"))
        qp.setBrush(PyQt5.QtGui.QBrush(g))
        qp.drawRoundedRect(PyQt5.QtCore.QRect(0,0,100+2*r+self.p,2*r+2*self.p),4,4)
        qp.setPen(PyQt5.QtGui.QPen(PyQt5.QtGui.QColor("#888"), 2, PyQt5.QtCore.Qt.SolidLine))
        g2=PyQt5.QtGui.QLinearGradient(0,0,0,r*2+self.p*2)
        g2.setColorAt(0,PyQt5.QtGui.QColor("#555"))
        g2.setColorAt(1.0,PyQt5.QtGui.QColor("#111"))
        qp.setBrush(PyQt5.QtGui.QBrush(g2))
        qp.drawEllipse(PyQt5.QtCore.QPointF(x0,y0),r*1,r*1)
        qp.setPen(PyQt5.QtGui.QPen(PyQt5.QtGui.QColor("#0ff"), 2, PyQt5.QtCore.Qt.SolidLine))
        qp.drawLine(PyQt5.QtCore.QPointF(x0,y0),PyQt5.QtCore.QPointF(xh,yh))
        qp.setPen(PyQt5.QtGui.QPen(PyQt5.QtGui.QColor("#0ff"), 2, PyQt5.QtCore.Qt.SolidLine))
        qp.drawLine(PyQt5.QtCore.QPointF(x0,y0),PyQt5.QtCore.QPointF(xm,ym))
        qp.setPen(PyQt5.QtGui.QPen(PyQt5.QtGui.QColor("#f0f"), 1, PyQt5.QtCore.Qt.SolidLine))
        qp.drawLine(PyQt5.QtCore.QPointF(x0,y0),PyQt5.QtCore.QPointF(xs,ys))
        qp.setPen(PyQt5.QtGui.QPen(PyQt5.QtGui.QColor("#0ff"), 2, PyQt5.QtCore.Qt.SolidLine))
        qp.setFont(PyQt5.QtGui.QFont("Segoe UI Black",16))
        qp.drawText(PyQt5.QtCore.QRect(2*r+self.p,12,100,25),PyQt5.QtCore.Qt.AlignCenter,"{:02}:{:02}:{:02}".format(self.h,self.m,self.s))
        qp.setPen(PyQt5.QtGui.QPen(PyQt5.QtGui.QColor("#ddd"), 2, PyQt5.QtCore.Qt.SolidLine))
        qp.setFont(PyQt5.QtGui.QFont("Segoe UI",10))
        qp.drawText(PyQt5.QtCore.QRect(2*r+2*self.p,1,100,25),PyQt5.QtCore.Qt.AlignLeft,"{:04}/{:02}/{:02}".format(self.year,self.month,self.day))
        qp.end()

    def paintEvent(self,ev):
        self.draw()

    def mouseMoveEvent(self,ev):
        if self._is_drag:
            x=ev.globalX()
            y=ev.globalY()
            dx=x-self._startx
            dy=y-self._starty
            self.move(self.x()+dx,self.y()+dy)
            self._startx=x
            self._starty=y
        #print("Mouse move")

    def mousePressEvent(self,ev):
        self._is_drag=True
        self._startx=ev.globalX()
        self._starty=ev.globalY()
        #print("Mouse press x={}, y={}".format(self._startx,self._starty))
    
    def mouseReleaseEvent(self,ev):
        self._is_drag=False
        #print("Mouse release")

    def mouseDoubleClickEvent(self,ev):
        self.close()

def main():
    app=PyQt5.QtWidgets.QApplication(sys.argv)
    #clk=Clock()
    aclk=AnalogClock()
    aclk.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()