import math
import Detect.DataClass


# 向量求角度--Z为原点
def FindAngle(X:Detect.DataClass.Point , Y:Detect.DataClass.Point , Z:Detect.DataClass.Point):  # 计算角度

    # 向量a
    a = Detect.DataClass.Vector(X.x-Z.x, X.y-Z.y)
    aMod = a.mod()
    # 向量b
    b = Detect.DataClass.Vector(Y.x-Z.x, Y.y-Z.y)
    bMod = b.mod()
    # 角度计算
    theta = math.acos((a.x*b.x+a.y*b.y)/(aMod*bMod))
    degree = int(180/math.pi)*theta
    return round(degree, 2)
