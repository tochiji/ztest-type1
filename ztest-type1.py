#########################################################
# 母比率の差の検定／タイプ1
#########################################################

import sys
import math

def error_usage():
    sys.stderr.write("usage: " + sys.argv[0] + "\n")
    sys.stderr.write("\tこのプログラムは、4つの引数が必要です。\n\n")
    sys.stderr.write(
        "\t1.属性1のn数 2.属性1における比率p 3.属性2のn数 4.属性2における比率p\n")
    sys.stderr.write("\t例： 200 0.6 100 0.48\n\n")
    sys.stderr.write("\tただし、それぞれn数は30以上かつ比率pは[0<=p<=1]を満たすこと\n")
    sys.exit(1)

# 引数がちょうど4つあるか？
if len(sys.argv[1:]) != 4:
    error_usage()

n1,p1,n2,p2 = map(float, sys.argv[1:])
p = ((n1*p1) + (n2*p2))/(n1+n2)

# n数が30以上か？
if (n1 < 30) or (n2 < 30):
    error_usage()

# 比率は0から1の間か？
if not (0 <= p1 <= 1) or not (0 <= p2 <= 1):
    error_usage()

T = math.fabs(p1 - p2) / math.sqrt((p * (1-p)) * ((1/n1) + (1/n2)))

if T >= 2.58:
    print("1%有意 (検定統計量:" + str(T) + "）")
elif T >= 1.96:
    print("5%有意 (検定統計量:" + str(T) + "）")
elif T >= 1.65:
    print("10%有意 (検定統計量:" + str(T) + "）")
else:
    print("有意差なし (検定統計量:" + str(T) + "）")

