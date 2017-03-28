#coding=utf-8

import re, csv, os, sys
import tkinter.messagebox
from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

#index of limited items
global specItemIndex,final_data_col,col_count, row_count
specItemIndex = []   #记录有spec的item的index
final_data_col = []  #csv文件的内容
col_count = 0        #csv文件的列数
row_count = 0        #csv文件的行数

#显示警告信息
def show_alert_msg(msg):
    tkinter.messagebox.showwarning(title="Warning!", message=msg)
    exit()

#如果目录存在,删除
def rmdir(filedir):
    import shutil

    # remove ' ' at the path beggining
    path = filedir.strip()
    # remove '/' at the path end
    path = path.rstrip("\\")

    # judge the path exsits or not
    # Yes   True
    # No   False
    isExists = os.path.exists(path)
    if not isExists:
        print(path + ' not exist')
    else:
        # if exist,remove it
        print(path + ' removed')
        shutil.rmtree(path)

#删除旧目录,创建新目录
def mkdir(filedir):
    path = filedir.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        # if doesn't exist, creat a new one
        print(path + ' does not exist, creat a new one!')
        os.makedirs(path)
    else:
        # if exist, remove it and creat a new one
        print(path + ' exist, will creat a new one!')
        rmdir(path)
        # creat new dir
        os.makedirs(path)
        print(path + ' is created successfully!')

#检查文件是否存在
def read_file(file):
    if not os.path.isfile(file):
        msg = file + " not exist,please check"
        show_alert_msg(msg)

#csv文件放在用户桌面,名字必须是test.csv,读取其内容
def getDataFromFile():
    summary_log_path = os.path.expanduser(r'~/Desktop')+"/test.csv"
    read_file(summary_log_path)
    summary_log_path = open(summary_log_path)
    summary_log_reader = csv.reader(summary_log_path)
    log_data = list(summary_log_reader)
    print("Data of this summary log =\n",log_data)
    return log_data

#读取有spec的测项,记录他们的序列
def find_data(str, lraw, limit_index):
    # find which item has limit and record its index
    numRegex = re.compile(r'^(\d+\.?\d?)$')
    if str in lraw:
        limit_data = lraw
        #print(len(limit_data))
        if type(limit_data) == list:
            print(str)
            for i in range(0, len(limit_data)):
                #print(limit_data[i])
                if numRegex.search(limit_data[i]) is None:
                    continue
                else:
                    print(limit_data[i], end=" ")
                    limit_index.append(i)
            print("\n")
    return limit_index

#数据初始处理
def initData():
    mkpath = os.path.expanduser(r'~/Desktop/Distribution_Chart/')
    mkdir(mkpath)

    log_data = getDataFromFile()
    upper_index = []
    lower_index = []
    for raw in log_data:
        #print(raw)
        upper_index = find_data('Upper Limit ----->', raw, upper_index)
        lower_index = find_data('Lower Limit ----->', raw, lower_index)

    global specItemIndex
    specItemIndex = list(set(upper_index) | set(lower_index))
    specItemIndex.sort()

    global col_count, row_count
    col_count = len(log_data[0])
    row_count = len(log_data)

    #read data by every column and save in a list
    raw_data_col = []
    for i in range(col_count):
        for raw in log_data:
            raw_data_col.append(raw[i])

    global final_data_col
    for i in range(0, len(raw_data_col)):
        if i%row_count == 0:
            final_data_col.append(raw_data_col[i:i+row_count])
            i += row_count

#打印一些数据
def printData():
    # read some indexs
    print("specItemIndex =", specItemIndex)
    print("col_count =", col_count, ",row_count =", row_count)
    print('final_data_col =',final_data_col)
    print("len(final_data_col) =", len(final_data_col), end='\n\n')

#时间格式转化
def toStampTime(tt):
    import time
    timeArray = time.strptime(tt, "%d/%m/%y %H:%M")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp

#时间格式转化
def toStringTime(tt):
    import time
    timeArray = time.localtime(tt)
    stringTime = time.strftime("%y/%m/%d %H:%M", timeArray)
    return stringTime

#得到最早开始测试时间
def getStartTimeMin():
    timeStampList = []
    print('StartTestTime =',final_data_col[7][7:row_count])
    for tt in final_data_col[7][7:row_count]:
        timeStampList.append(toStampTime(tt))
    startTimeMin = getMinValue(timeStampList)
    startTimeMin = toStringTime(startTimeMin)
    return startTimeMin

#得到最后结束测试时间
def getEndTimeMax():
    timeStampList = []
    print('EndTestTime =',final_data_col[8][7:row_count])
    for tt in final_data_col[8][7:row_count]:
        timeStampList.append(toStampTime(tt))
    endTimeMax = getMaxValue(timeStampList)
    endTimeMax = toStringTime(endTimeMax)
    return endTimeMax

#计算每个值的个数
def eachValueCount():
    valueCount = []
    count = 0
    countList = []
    for i in range(10, col_count):
        for n in range(7,row_count):
            k = final_data_col[i][n]
            for j in range(7,row_count):
                if final_data_col[i][j] == k:
                    count += 1
            countList.append(count)
            count = 0
    for i in range(len(countList)):
        if i % (row_count-7) == 0:
            valueCount.append(countList[i:i + (row_count-7)])
            i += (row_count-7)
    return valueCount

#得到最大值
def getMaxValue(testValue):
    maxValue = testValue[0]
    for j in range(1, len(testValue)):
        if maxValue < testValue[j]:
            maxValue = testValue[j]
    return maxValue

#得到最小值
def getMinValue(testValue):
    minValue = testValue[0]
    for j in range(1, len(testValue)):
        if minValue > testValue[j]:
            minValue = testValue[j]
    return minValue

def drawDistributionChart():
    import matplotlib.pyplot as plt

    #加载csv数据,做特殊处理,备画图
    initData()
    printData()

    #坐标title设置
    numRegex = re.compile(r'Version(.*?)$')
    overlayVer = numRegex.match(final_data_col[1][0]).group(1)
    print('overlayVer =',overlayVer)
    station = final_data_col[0][0]
    print('station =',station)
    path = os.path.expanduser(r'~/Desktop/Distribution_Chart/')
    startTimeMin = getStartTimeMin()
    print("startTimeMin =", startTimeMin)
    endTimeMax = getEndTimeMax()
    print("endTimeMax =", endTimeMax)

    for i in range(10,col_count):
        testValue = []  #存放测试值
        limitType = []  #存放limit形式
        itemName = final_data_col[i][1]  #存放测项名

        #确定整个图的大小和左,右,上,下宽度
        plt.subplots(figsize=(6.6, 3.4))
        plt.subplots_adjust(left=0.4, right=0.95, top=0.92, bottom=0.3)

        #子图设置
        ax = plt.subplot()
        ax.set_ylabel('Count',fontsize='small',color='b')
        ax.set_xlabel('Value'+'\n\n'+station+overlayVer+'\n'+startTimeMin+' -- '+endTimeMax,fontsize='small',color='b')
        ax.set_title(itemName,fontsize='small',color='b')

        #如果测项名中有'.',用下划线代替
        if itemName.find('.'):
            itemName = itemName.replace('.', '-')
        print('\nitemName =', itemName)

        #读测试值,计算各个值得个数
        for j in range(7,row_count):
            print('final_data_col[',i,'][',j,'] =',final_data_col[i][j])
            if final_data_col[i][j] != '':
                testValue.append(float(final_data_col[i][j]))
            else:
                testValue.append(float(final_data_col[i][j-1]))
        testValue = tuple(testValue)
        print('testValue =',testValue,'valueCount =',len(testValue))
        maxTestValue = getMaxValue(testValue)
        print('maxTestValue =', maxTestValue)
        minTestValue = getMinValue(testValue)
        print('minTestValue =', minTestValue)
        valueCount = eachValueCount()
        countOfValue = tuple(valueCount[i-10])
        print('countOfValue =', countOfValue)
        maxCount = getMaxValue(countOfValue)
        print('maxCount =', maxCount)
        minCount = getMinValue(countOfValue)
        print('minCount =', minCount)

        #确定横纵坐标显示的最大最小刻度
        deltaX = (maxTestValue - minTestValue) / 2
        print('pre_deltaX =',deltaX)
        if deltaX == 0 and minTestValue > 2:
            deltaX = int(minTestValue / 2)
        elif deltaX == 0 and minTestValue == 0:
            deltaX = 1
        elif deltaX == 0 and minTestValue < 2:
            deltaX = int((minTestValue + maxTestValue) / 2)
        elif deltaX < 1 and minTestValue < 0:
            deltaX = int(-(minTestValue+maxTestValue)/2)
        elif deltaX < 1:
            deltaX = 1
        else:
            deltaX = int(deltaX)
        deltaY = 1
        if maxCount == 1:
            deltaY = 0.1
        print('post_deltaX =',deltaX)

        #画spec的红线
        maxSpec = final_data_col[i][4]
        minSpec = final_data_col[i][5]
        if i in specItemIndex:
            if minSpec != 'NA':
                limitType.append('Lower')
                minSpec = float(final_data_col[i][5])
                minTestValue = minSpec
                vlines(x=minSpec, ymin=0, ymax=maxCount + deltaY, color='r')
            if maxSpec != 'NA':
                limitType.append('Upper')
                maxSpec = float(final_data_col[i][4])
                maxTestValue = maxSpec
                vlines(x=maxSpec, ymin=0, ymax=maxCount + deltaY, color='r')
            print(i, ':', final_data_col[i][1], ': uplimit=', maxSpec, 'lowlimit=', minSpec)
        else:
            limitType.append('NA')

        #设置横纵坐标范围
        ax.axis([minTestValue-deltaX,maxTestValue+deltaX, 0,maxCount+deltaY],fontsize='small')
        #得到横纵坐标的坐标值
        x = ax.get_xticks()
        y = ax.get_yticks()
        print('x =',x)
        print('y =',y)
        #得到坐标间距
        insX = x[1] - x[0]
        insY = y[1] - y[0]
        xmajorLocator = MultipleLocator(insX)  # 将x主刻度标签设置为insXX的倍数
        xmajorFormatter = FormatStrFormatter('%.1f')  # 设置x轴标签文本的格式
        xminorLocator = MultipleLocator(insX/5.)  # 将x轴次刻度标签设置为insXX/5.的倍数

        ymajorLocator = MultipleLocator(insY)  # 将y轴主刻度标签设置为insXY的倍数
        ymajorFormatter = FormatStrFormatter('%.1f')  # 设置y轴标签文本的格式
        yminorLocator = MultipleLocator(insY/5.)  # 将此y轴次刻度标签设置为insXY/5.的倍数

        # 设置主刻度标签的位置,标签文本的格式
        ax.xaxis.set_major_locator(xmajorLocator)
        ax.xaxis.set_major_formatter(xmajorFormatter)

        ax.yaxis.set_major_locator(ymajorLocator)
        ax.yaxis.set_major_formatter(ymajorFormatter)

        # 显示次刻度标签的位置,没有标签文本
        ax.xaxis.set_minor_locator(xminorLocator)
        ax.yaxis.set_minor_locator(yminorLocator)

        ax.xaxis.grid(False, which='major')  # x坐标轴的网格使用主刻度
        ax.yaxis.grid(True, which='minor',alpha=0.25)  # y坐标轴的网格使用次刻度

        #确定text显示的位置
        textX = x[0] - 2.5*insX
        textY = maxCount + deltaY
        if insX < 0.5:
            textX = x[0] -  4.5* insX
        elif insX >= 0.5 and insX < 1:
            textX = x[0] - 2.3 * insX
        elif insX == 1:
            textX = x[0] - 3.2 * insX

        #确定text内容
        strString = []
        strString.append('File Row Count : '+' '+str(row_count))
        strString.append('File Col Count : ' + ' ' + str(col_count))
        if len(limitType) == 2:
            strString.append('Limit Type : '+limitType[0]+' '+limitType[1])
        else: strString.append('Limit Type : '+limitType[0])
        strString.append('Limit High : '+str(maxSpec))
        strString.append('Limit Low : ' +str(minSpec))
        strString.append('Max Value : ' +str(maxTestValue))
        strString.append('Min Value : ' + str(minTestValue))
        strString.append('Max Count : ' + str(maxCount))
        strString.append('Min Count : ' + str(minCount))

        #写text到图片
        for i in range(len(strString)):
            ax.text(textX,textY- i/2*insY,
                strString[i],
                style='italic',horizontalalignment='left',
                verticalalignment='center',bbox = {'facecolor':'lightgrey','alpha': 0.009, 'pad': 400})        #bbox = {'facecolor': 'lightgrey', 'alpha': 0.75, 'pad': 400}
        #画图
        plt.bar(left=testValue, height=countOfValue,align='center',color='purple',width=insX/5.)

        #保存: ~/Desktop/Distribution_Chart/测项名.png
        plt.savefig(path+itemName)
        #plt.show()

drawDistributionChart()
