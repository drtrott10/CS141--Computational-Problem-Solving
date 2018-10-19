import sys
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

class Olympic(QWidget):
  
  def point_is_in_circle(self,origin_x, origin_y, diameter, x, y):
    Xc = origin_x + (diameter/2)
    Yc = origin_y + (diameter/2)
    dist = (((Xc - x)**2 + (Yc - y)**2)**0.5)
    if dist <= (diameter/2):
        return True
    else:
        return False
        
  def __init__(self):
    super().__init__()
    self.coord = [(90,50),(155,105),(220,50),(285,105),(350,50)]
    self.bools = [False, False, False, False, False]
    self.colors = [Qt.blue, Qt.yellow, Qt.black, Qt.green, Qt.red]    
    self._circlesize = 110          
    self.setGeometry(300, 300, 550, 600)
    self.setWindowTitle('Olympic Rings')
    self.show()
  
  def mousePressEvent(self, event):
    for i in range(0,5):
        if self.point_is_in_circle(self.coord[i][0],self.coord[i][1],self._circlesize,event.x(),event.y()):
            self.bools[i] = True
        else:
            self.bools[i] = False
    self.repaint()  

  def paintEvent(self, event):
    qp = QPainter()
    qp.begin(self)
    P=QPen()
    P.setWidth(7)
    P.setColor(Qt.blue)
    qp.setPen(P)
    qp.drawEllipse(90,50,self._circlesize,self._circlesize)
    P.setColor(Qt.black)
    qp.setPen(P)
    qp.drawEllipse(220,50,self._circlesize,self._circlesize)
    P.setColor(Qt.red)
    qp.setPen(P)
    qp.drawEllipse(350,50,self._circlesize,self._circlesize)
    P.setColor(Qt.yellow)
    qp.setPen(P)
    qp.drawEllipse(155,105,self._circlesize,self._circlesize)
    P.setColor(Qt.green)
    qp.setPen(P)
    qp.drawEllipse(285,105,self._circlesize,self._circlesize)
    if self.bools[0]:
        if self.bools[1]:
            qp.fillRect(120,400,150,75,Qt.blue)
            qp.fillRect(270,400,150,75,Qt.yellow)
        else:
            qp.fillRect(120,400,150,75,Qt.blue)
            qp.fillRect(270,400,150,75,Qt.blue)
    elif self.bools[1]:
        if self.bools[2]:
            qp.fillRect(120,400,150,75,Qt.yellow)
            qp.fillRect(270,400,150,75,Qt.black)
        else:
            qp.fillRect(120,400,150,75,Qt.yellow)
            qp.fillRect(270,400,150,75,Qt.yellow)
    elif self.bools[2]:
        if self.bools[3]:
            qp.fillRect(120,400,150,75,Qt.black)
            qp.fillRect(270,400,150,75,Qt.green)
        else:
            qp.fillRect(120,400,150,75,Qt.black)
            qp.fillRect(270,400,150,75,Qt.black)
    elif self.bools[3]:
        if self.bools[4]:
            qp.fillRect(120,400,150,75,Qt.green)
            qp.fillRect(270,400,150,75,Qt.red)
        else:
            qp.fillRect(120,400,150,75,Qt.green)
            qp.fillRect(270,400,150,75,Qt.green)
    elif self.bools[4]:
        qp.fillRect(120,400,150,75,Qt.red)
        qp.fillRect(270,400,150,75,Qt.red)
    qp.end()
    
if __name__ == '__main__':  
  app = QApplication(sys.argv)
  ex = Olympic()
  sys.exit(app.exec_())