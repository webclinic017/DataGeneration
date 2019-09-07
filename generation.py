import pandas as pd
import os
import argparse
import random
import time
import math

# 生成Excel的目录
DIST_FOLDER = 'dist'
# 机型配置文件
MODEL_FILE = 'config/model.json'
# 国家配置文件
COUNTRY_FILE = 'config/country.json'
# 对型配置文件
TEAM_TYPE_FILE = 'config/team_type.json'
# 名称配置文件
NAME_FILE = 'config/name.json'
# 任务配置文件
TASK_FILE = 'config/task.json'
# 编号配置文件
NUMBERING_FILE = 'config/numbering.json'
# 平台配置文件
PLATFORM_FILE = 'config/platform.json'
# 目标种类配置文件
TARGET_FILE = 'config/target.json'
# 环境类别配置文件
ENVIRONMENT_FILE = 'config/environment.json'
# 部队类别配置文件
ARMY_FILE = 'config/army.json'
# 状态配置文件
STATUS_FILE = 'config/status.json'
# 起飞机场配置文件
DEPARTURE_AIRPORT_FILE = 'config/departure_airport.json'
# 降落机场配置文件
LANDING_AIRPORT_FILE = 'config/landing_airport.json'
# 备降机场配置文件
ALTERNATE_AIRPORT_FILE = 'config/alternate_airport.json'
# 信号来源配置文件
SIGNAL_SOURCE_FILE = 'config/signal_source.json'
# 目标识别配置文件
TARGET_RECOGNITION_FILE = 'config/target_recognition.json'
# 目标企图配置文件
TARGET_ATTEMPT_FILE = 'config/task_attempt.json'

# 创建随机时间
def str_time_prop(start, end, prop, frmt):
    stime = time.mktime(time.strptime(start, frmt))
    etime = time.mktime(time.strptime(end, frmt))
    ptime = stime + prop * (etime - stime)
    return int(ptime)


# 创建随机数时间戳
def random_timestamp(start, end, frmt='%Y/%m/%d %H:%M:%S'):
    return str_time_prop(start, end, random.random(), frmt)


# 创建随机数时间
def random_date(start, end, frmt='%Y/%m/%d %H:%M:%S'):
    return time.strftime(frmt, time.localtime(str_time_prop(start, end, random.random(), frmt)))


# 创建随机数时间戳列表
def random_timestamp_list(start, end, n, frmt='%Y/%m/%d %H:%M:%S'):
    return [random_timestamp(start, end, frmt) for _ in range(n)]


# 创建随机数时间列表
def random_date_list(start, end, n, frmt='%Y/%m/%d %H:%M:%S'):
    return [random_date(start, end, frmt) for _ in range(n)]


# 这里的参数包括一个基准点，和一个距离基准点的距离
def generate_random_gps(base_log=None, base_lat=None, radius=None):
    radius_in_degrees = radius / 111300
    u = float(random.uniform(0.0, 1.0))
    v = float(random.uniform(0.0, 1.0))
    w = radius_in_degrees * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    y = w * math.sin(t)
    longitude = y + base_log
    latitude = x + base_lat
    # 这里是想保留6位小数点
    loga = float('%.6f' % longitude)
    lata = float('%.6f' % latitude)
    return loga, lata


# 把经纬度转化为度分秒
def convert_lon_lat(value):
    degree = int(value)
    min = int((value - degree) * 60)
    sec = int((value - degree) * 3600 - min * 60)

    return str(degree) + '°' + str(min) + "'" + str(sec) + '"'

if __name__ == '__main__':
    # 循环生成计数器
    i = 0
    # 数据集表格的表头
    datasetColumns = ['位码', '批号', '属性', '高度',
                      '速度', '航向', '时间', '机型',
                      '架数', '经度', '纬度', '国籍',
                      '队型', '挂弹', '余油', '名称',
                      '任务', '机号', '平台编号', '目标种类',
                      '环境类别', '部别', '状态', '长机标识',
                      '横滚', '俯仰', '跳伞标识', '起飞机场',
                      '降落机场', '备降机场', '信号来源', '二次代码',
                      '附加代码', '首点时间', '目标标识', '任务企图',
                      '目标图像', '音频数据', '接收时间']
    # 生成空的数据表
    dataset = pd.DataFrame(columns=datasetColumns)
    # 机型的数据集
    modelData = 0
    # 国家的数据集
    countryData = 0
    # 对型数据集
    teamTypeData = 0
    # 名称数据集
    nameData = 0
    # 任务数据集
    taskData = 0
    # 编号数据集
    numberingData = 0
    # 平台数据集
    platformData = 0
    # 目标种类数据集
    targetData = 0
    # 环境类别数据集
    environmentData = 0
    # 部队类别数据集
    armyData = 0
    # 状态数据集
    statusData = 0
    # 起飞机场数据集
    departureAirportData = 0
    # 降落机场数据集
    landingAirportData = 0
    # 备降机场数据集
    alternateAirportData = 0
    # 信号来源数据集
    signalSourceData = 0
    # 目标识别数据集
    targetRecognitionData = 0
    # 目标企图数据集
    targetAttemptData = 0

    # 命令参数描述
    parser = argparse.ArgumentParser(description='Generation DataSet Tool')
    # 设置数据集的默认大小为50
    parser.add_argument('-c', '--count', type=int, default=100, nargs='?', help='Generate the size of the dataset')
    args = parser.parse_args()
    # 获取生成的数据集大小
    DATASET_COUNT = args.count

    if not os.path.exists(DIST_FOLDER):
        os.mkdir(DIST_FOLDER)
    else:
        file_list = os.listdir(DIST_FOLDER)
        for file in file_list:
            os.remove(DIST_FOLDER + '/' + file)

    # 判断机型文件是否存在
    if not os.path.exists(MODEL_FILE):
        exit(MODEL_FILE + "文件不存在，请检查！")
    if not os.path.exists(COUNTRY_FILE):
        exit(COUNTRY_FILE + "文件不存在，请检查！")
    if not os.path.exists(TEAM_TYPE_FILE):
        exit(TEAM_TYPE_FILE + "文件不存在，请检查！")
    if not os.path.exists(NAME_FILE):
        exit(NAME_FILE + "文件不存在，请检查！")
    if not os.path.exists(TASK_FILE):
        exit(TASK_FILE + "文件不存在，请检查！")
    if not os.path.exists(NUMBERING_FILE):
        exit(NUMBERING_FILE + "文件不存在，请检查！")
    if not os.path.exists(PLATFORM_FILE):
        exit(PLATFORM_FILE + "文件不存在，请检查！")
    if not os.path.exists(TARGET_FILE):
        exit(TARGET_FILE + "文件不存在，请检查！")
    if not os.path.exists(ENVIRONMENT_FILE):
        exit(ENVIRONMENT_FILE + "文件不存在，请检查！")
    if not os.path.exists(ARMY_FILE):
        exit(ARMY_FILE + "文件不存在，请检查！")
    if not os.path.exists(STATUS_FILE):
        exit(STATUS_FILE + "文件不存在，请检查！")
    if not os.path.exists(DEPARTURE_AIRPORT_FILE):
        exit(DEPARTURE_AIRPORT_FILE + "文件不存在，请检查！")
    if not os.path.exists(LANDING_AIRPORT_FILE):
        exit(LANDING_AIRPORT_FILE + "文件不存在，请检查！")
    if not os.path.exists(ALTERNATE_AIRPORT_FILE):
        exit(ALTERNATE_AIRPORT_FILE + "文件不存在，请检查！")
    if not os.path.exists(SIGNAL_SOURCE_FILE):
        exit(SIGNAL_SOURCE_FILE + "文件不存在，请检查！")
    if not os.path.exists(TARGET_RECOGNITION_FILE):
        exit(TARGET_RECOGNITION_FILE + "文件不存在，请检查！")
    if not os.path.exists(TARGET_ATTEMPT_FILE):
        exit(TARGET_ATTEMPT_FILE + "文件不存在，请检查！")

    # 获取各类数据集
    try:
        modelData = pd.read_json(MODEL_FILE)
    except ValueError as ve:
        exit(MODEL_FILE + "数据格式集错误，请检查！" + format(ve))
    try:
        countryData = pd.read_json(COUNTRY_FILE)
    except ValueError as ve:
        exit(COUNTRY_FILE + "数据格式集错误，请检查！" + format(ve))
    try:
        teamTypeData = pd.read_json(TEAM_TYPE_FILE)
    except ValueError as ve:
        exit(TEAM_TYPE_FILE + "数据格式集错误，请检查！" + format(ve))
    try:
        nameData = pd.read_json(NAME_FILE)
    except ValueError as ve:
        exit(NAME_FILE + "数据格式集错误，请检查！" + format(ve))
    try:
        taskData = pd.read_json(TASK_FILE)
    except ValueError as ve:
        exit(TASK_FILE + "数据格式集错误，请检查！" + format(ve))
    try:
        numberingData = pd.read_json(NUMBERING_FILE)
    except ValueError as ve:
        exit(NUMBERING_FILE + "数据格式集错误，请检查！" + format(ve))
    try:
        platformData = pd.read_json(PLATFORM_FILE)
    except ValueError as ve:
        exit(PLATFORM_FILE + "数据格式集错误，请检查！" + format(ve))
    try:
        targetData = pd.read_json(TARGET_FILE)
    except ValueError as ve:
        exit(TARGET_FILE + "数据格式集错误，请检查！" + format(ve))
    try:
        environmentData = pd.read_json(ENVIRONMENT_FILE)
    except ValueError as ve:
        exit(ENVIRONMENT_FILE + "数据格式集错误，请检查！" + format(ve))
    try:
        armyData = pd.read_json(ARMY_FILE)
    except ValueError as ve:
        exit(ARMY_FILE + "数据格式集错误，请检查！" + format(ve))
    try:
        statusData = pd.read_json(STATUS_FILE)
    except ValueError as ve:
        exit(STATUS_FILE + "数据格式集错误，请检查！" + format(ve))
    try:
        departureAirportData = pd.read_json(DEPARTURE_AIRPORT_FILE)
    except ValueError as ve:
        exit(DEPARTURE_AIRPORT_FILE + "数据格式集错误，请检查！" + format(ve))
    try:
        landingAirportData = pd.read_json(LANDING_AIRPORT_FILE)
    except ValueError as ve:
        exit(LANDING_AIRPORT_FILE + "数据格式集错误，请检查！" + format(ve))
    try:
        alternateAirportData = pd.read_json(ALTERNATE_AIRPORT_FILE)
    except ValueError as ve:
        exit(ALTERNATE_AIRPORT_FILE + "数据格式集错误，请检查！" + format(ve))
    try:
        signalSourceData = pd.read_json(SIGNAL_SOURCE_FILE)
    except ValueError as ve:
        exit(SIGNAL_SOURCE_FILE + "数据格式集错误，请检查！" + format(ve))
    try:
        targetRecognitionData = pd.read_json(TARGET_RECOGNITION_FILE)
    except ValueError as ve:
        exit(TARGET_RECOGNITION_FILE + "数据格式集错误，请检查！" + format(ve))
    try:
        targetAttemptData = pd.read_json(TARGET_ATTEMPT_FILE)
    except ValueError as ve:
        exit(TARGET_ATTEMPT_FILE + "数据格式集错误，请检查！" + format(ve))

    # 循环创建数据
    while i < DATASET_COUNT:
        # 生成一对经纬度
        longitude, latitude = generate_random_gps(base_log=120.7, base_lat=30, radius=1000000)
        # 生成每一行数据
        dataset = dataset.append(
            {
                '位码': i + 1,
                '批号': str(random.randint(1, 2000)).zfill(4),
                '属性': '敌' if random.randint(0, 1) == 1 else '我',
                '高度': random.randint(0, 20000),
                '速度': random.randint(200, 1000),
                '航向': random.randint(0, 180),
                '时间': random_date('2019/04/22 12:12:12', '2019/12/06 12:12:12'),
                '机型': modelData[0].values[random.randint(0, modelData.shape[0] - 1)],
                '架数': random.randint(0, 200),
                '经度': convert_lon_lat(longitude),
                '纬度': convert_lon_lat(latitude),
                '国籍': countryData[0].values[random.randint(0, countryData.shape[0] - 1)],
                '队型': teamTypeData[0].values[random.randint(0, teamTypeData.shape[0] - 1)],
                '挂弹': random.randint(0, 20),
                '余油': random.randint(20000, 60000),
                '名称': nameData[0].values[random.randint(0, nameData.shape[0] - 1)],
                '任务': taskData[0].values[random.randint(0, taskData.shape[0] - 1)],
                '机号': numberingData[0].values[random.randint(0, numberingData.shape[0] - 1)],
                '平台编号': platformData[0].values[random.randint(0, platformData.shape[0] - 1)],
                '目标种类': targetData[0].values[random.randint(0, targetData.shape[0] - 1)],
                '环境类别': environmentData[0].values[random.randint(0, environmentData.shape[0] - 1)],
                '部别': armyData[0].values[random.randint(0, armyData.shape[0] - 1)],
                '状态': statusData[0].values[random.randint(0, statusData.shape[0] - 1)],
                '横滚': str(random.randint(-180, 180)) + '°',
                '俯仰': str(random.randint(-180, 180)) + '°',
                '起飞机场': departureAirportData[0].values[random.randint(0, departureAirportData.shape[0] - 1)],
                '降落机场': landingAirportData[0].values[random.randint(0, landingAirportData.shape[0] - 1)],
                '备降机场': alternateAirportData[0].values[random.randint(0, alternateAirportData.shape[0] - 1)],
                '信号来源': signalSourceData[0].values[random.randint(0, signalSourceData.shape[0] - 1)],
                '二次代码': str(random.randint(1, 2000)).zfill(4),
                '附加代码': str(random.randint(1, 2000)).zfill(4),
                '首点时间': time.strftime('%H:%M:%S', time.localtime(random_timestamp('2019/04/22 12:12:12', '2019/12/06 12:12:12'))),
                '目标标识': targetRecognitionData[0].values[random.randint(0, targetRecognitionData.shape[0] - 1)],
                '任务企图': targetAttemptData[0].values[random.randint(0, targetAttemptData.shape[0] - 1)],
                '接收时间': random_date('2019/04/22 12:12:12', '2019/12/06 12:12:12'),
            },
            ignore_index=True)
        # 计数器增加
        i += 1

    # 输出Excel表格
    dataset.to_excel("dist/dataset.xlsx", sheet_name='dataset')
