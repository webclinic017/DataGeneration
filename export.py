import pandas as pd
import argparse
import os

# 生成Excel的目录
DIST_FOLDER = 'dist'
# 生成的目标文件
DIST_FILE = 'dataset.xlsx'
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

if __name__ == '__main__':

    pd.set_option('display.max_columns', 20)
    pd.set_option('display.max_colwidth', 2000)

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
    # 机型的数据集
    modelData = 0
    # 国家的数据集
    countryData = 0
    # 队形数据集
    teamTypeData = 0
    # 任务数据集
    taskData = 0
    # 机号数据集
    numberingData = 0
    # 平台编号数据集
    platformData = 0
    # 目标种类数据集
    targetData = 0
    # 环境种类数据集
    environmentData = 0
    # 部别数据集
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
    # 目标标识数据集
    targetRecognitionData = 0
    # 任务企图数据集
    targetAttemptData = 0

    # 命令参数描述
    parser = argparse.ArgumentParser(description='Export DataSet Tool')
    # 获取要分类的标签列表
    parser.add_argument('-c', '--classification', nargs='+', type=str, help='Name of classification', required=True)
    # 获取要忽略的标签列表
    parser.add_argument('-i', '--ignore', nargs='+', help='Ignored labels',
                        default=['位码', '批号', '时间', '经度', '纬度', '长机标识', '横滚', '俯仰', '跳伞标识',
                                 '二次代码', '附加代码', '首点时间', '目标图像', '音频数据', '接收时间'])
    args = parser.parse_args()

    # 获取要分类的标签列表
    classification = args.classification
    # 获取忽略的标签列表
    ignore = args.ignore

    if not os.path.exists(DIST_FOLDER) or not os.path.exists(DIST_FOLDER + '/' + DIST_FILE):
        exit('先运行main.py生成后，再导出数据')

    xlsx = pd.ExcelFile(DIST_FOLDER + '/' + DIST_FILE)
    df = pd.read_excel(xlsx, sheet_name='dataset').loc[0:, '位码':]

    # 获取高度的最大值和最小值
    maxHigh = df.loc[:, datasetColumns[3]].max()
    minHigh = df.loc[:, datasetColumns[3]].min()

    # 获取速度的最大值和最小值
    maxSpeed = df.loc[:, datasetColumns[4]].max()
    minSpeed = df.loc[:, datasetColumns[4]].min()

    # 获取航向的最大值和最小值
    maxCourse = df.loc[:, datasetColumns[5]].max()
    minCourse = df.loc[:, datasetColumns[5]].min()

    # 获取机型数据集
    try:
        modelData = pd.read_json(MODEL_FILE)
    except ValueError as ve:
        exit(MODEL_FILE + "数据格式集错误，请检查！" + format(ve))

    # 获取国家数据集
    try:
        countryData = pd.read_json(COUNTRY_FILE)
    except ValueError as ve:
        exit(COUNTRY_FILE + "数据格式集错误，请检查！" + format(ve))

    # 获取队形数据集
    try:
        teamTypeData = pd.read_json(TEAM_TYPE_FILE)
    except ValueError as ve:
        exit(TEAM_TYPE_FILE + "数据格式集错误，请检查！" + format(ve))

    # 获取架数的最大值和最小值
    maxCount = df.loc[:, datasetColumns[8]].max()
    minCount = df.loc[:, datasetColumns[8]].min()

    # 获取架数的最大值和最小值
    maxMissile = df.loc[:, datasetColumns[13]].max()
    minMissile = df.loc[:, datasetColumns[13]].min()

    # 获取架数的最大值和最小值
    maxOil = df.loc[:, datasetColumns[14]].max()
    minOil = df.loc[:, datasetColumns[14]].min()

    # 获取任务数据集
    try:
        taskData = pd.read_json(TASK_FILE)
    except ValueError as ve:
        exit(TASK_FILE + "数据格式集错误，请检查！" + format(ve))

    # 获取机号数据集
    try:
        numberingData = pd.read_json(NUMBERING_FILE)
    except ValueError as ve:
        exit(NUMBERING_FILE + "数据格式集错误，请检查！" + format(ve))

    # 获取平台编号数据集
    try:
        platformData = pd.read_json(PLATFORM_FILE)
    except ValueError as ve:
        exit(PLATFORM_FILE + "数据格式集错误，请检查！" + format(ve))

    # 获取目标种类数据集
    try:
        targetData = pd.read_json(TARGET_FILE)
    except ValueError as ve:
        exit(TARGET_FILE + "数据格式集错误，请检查！" + format(ve))

    # 获取环境种类数据集
    try:
        environmentData = pd.read_json(ENVIRONMENT_FILE)
    except ValueError as ve:
        exit(ENVIRONMENT_FILE + "数据格式集错误，请检查！" + format(ve))

    # 获取部别数据集
    try:
        armyData = pd.read_json(ARMY_FILE)
    except ValueError as ve:
        exit(ARMY_FILE + "数据格式集错误，请检查！" + format(ve))

    # 获取状态数据集
    try:
        statusData = pd.read_json(STATUS_FILE)
    except ValueError as ve:
        exit(STATUS_FILE + "数据格式集错误，请检查！" + format(ve))

    # 获取起飞机场
    try:
        departureAirportData = pd.read_json(DEPARTURE_AIRPORT_FILE)
    except ValueError as ve:
        exit(DEPARTURE_AIRPORT_FILE + "数据格式集错误，请检查！" + format(ve))

    # 获取降落机场
    try:
        landingAirportData = pd.read_json(LANDING_AIRPORT_FILE)
    except ValueError as ve:
        exit(LANDING_AIRPORT_FILE + "数据格式集错误，请检查！" + format(ve))

    # 获取备降机场
    try:
        alternateAirportData = pd.read_json(ALTERNATE_AIRPORT_FILE)
    except ValueError as ve:
        exit(ALTERNATE_AIRPORT_FILE + "数据格式集错误，请检查！" + format(ve))

    # 获取信号来源
    try:
        signalSourceData = pd.read_json(SIGNAL_SOURCE_FILE)
    except ValueError as ve:
        exit(SIGNAL_SOURCE_FILE + "数据格式集错误，请检查！" + format(ve))

    # 获取目标标识来源
    try:
        targetRecognitionData = pd.read_json(TARGET_RECOGNITION_FILE)
    except ValueError as ve:
        exit(TARGET_RECOGNITION_FILE + "数据格式集错误，请检查！" + format(ve))

    # 获取任务企图来源
    try:
        targetAttemptData = pd.read_json(TARGET_ATTEMPT_FILE)
    except ValueError as ve:
        exit(TARGET_ATTEMPT_FILE + "数据格式集错误，请检查！" + format(ve))

    while i < df.shape[0]:

        # TODO 位码

        # TODO 批号

        # 修改属性值
        if df[datasetColumns[2]][i] == '敌':
            df.loc[i, datasetColumns[2]] = 0
        else:
            df.loc[i, datasetColumns[2]] = 1

        # 修改高度值
        df.loc[i, datasetColumns[3]] = (df.loc[i, datasetColumns[3]] - minHigh) / (maxHigh - minHigh)

        # 修改速度值
        df.loc[i, datasetColumns[4]] = (df.loc[i, datasetColumns[4]] - minSpeed) / (maxSpeed - minSpeed)

        # 修改航向值
        df.loc[i, datasetColumns[5]] = (df.loc[i, datasetColumns[5]] - minCourse) / (maxCourse - minCourse)

        # TODO 时间

        # 修改机型
        df.loc[i, datasetColumns[7]] = modelData.loc[modelData[0] == df.loc[i, datasetColumns[7]]].index

        # 修改架数
        df.loc[i, datasetColumns[8]] = (df.loc[i, datasetColumns[8]] - minCount) / (maxCount - minCount)

        # TODO 经度

        # TODO 纬度

        # 修改国籍
        df.loc[i, datasetColumns[11]] = countryData.loc[countryData[0] == df.loc[i, datasetColumns[11]]].index

        # 修改对型
        df.loc[i, datasetColumns[12]] = teamTypeData.loc[teamTypeData[0] == df.loc[i, datasetColumns[12]]].index

        # 修改挂弹
        df.loc[i, datasetColumns[13]] = (df.loc[i, datasetColumns[13]] - minMissile) / (maxMissile - minMissile)

        # 修改余油
        df.loc[i, datasetColumns[14]] = (df.loc[i, datasetColumns[14]] - minOil) / (maxOil - minOil)

        # 修改名称
        df.loc[i, datasetColumns[15]] = modelData.loc[modelData[0] == df.loc[i, datasetColumns[15]]].index

        # 修改任务
        df.loc[i, datasetColumns[16]] = taskData.loc[taskData[0] == df.loc[i, datasetColumns[16]]].index

        # 修改机号
        df.loc[i, datasetColumns[17]] = numberingData.loc[numberingData[0] == df.loc[i, datasetColumns[17]]].index

        # 修改平台编号
        df.loc[i, datasetColumns[18]] = platformData.loc[platformData[0] == df.loc[i, datasetColumns[18]]].index

        # 修改目标种类编号
        df.loc[i, datasetColumns[19]] = targetData.loc[targetData[0] == df.loc[i, datasetColumns[19]]].index

        # 修改环境种类编号
        df.loc[i, datasetColumns[20]] = environmentData.loc[environmentData[0] == df.loc[i, datasetColumns[20]]].index

        # 修改部别种类编号
        df.loc[i, datasetColumns[21]] = armyData.loc[armyData[0] == df.loc[i, datasetColumns[21]]].index

        # 修改状态种类编号
        df.loc[i, datasetColumns[22]] = statusData.loc[statusData[0] == df.loc[i, datasetColumns[22]]].index

        # TODO 长机标识

        # TODO 横滚

        # TODO 俯仰

        # TODO 跳伞标识

        # 修改起飞机场种类编号
        df.loc[i, datasetColumns[27]] = departureAirportData.loc[departureAirportData[0] == df.loc[i, datasetColumns[27]]].index

        # 修改降落机场种类编号
        df.loc[i, datasetColumns[28]] = landingAirportData.loc[landingAirportData[0] == df.loc[i, datasetColumns[28]]].index

        # 修改备降机场种类编号
        df.loc[i, datasetColumns[29]] = alternateAirportData.loc[alternateAirportData[0] == df.loc[i, datasetColumns[29]]].index

        # 修改信号来源种类编号
        df.loc[i, datasetColumns[30]] = signalSourceData.loc[signalSourceData[0] == df.loc[i, datasetColumns[30]]].index

        # TODO 二次代码

        # TODO 附加代码

        # TODO 首点时间

        # 修改目标标识种类编号
        df.loc[i, datasetColumns[34]] = targetRecognitionData.loc[targetRecognitionData[0] == df.loc[i, datasetColumns[34]]].index

        # 修改任务企图种类编号
        df.loc[i, datasetColumns[35]] = targetAttemptData.loc[targetAttemptData[0] == df.loc[i, datasetColumns[35]]].index

        # TODO 目标图像

        # TODO 音频数据

        # TODO 接收时间

        # 计数器增加
        i += 1

    # 删除要忽略的列
    df.drop(ignore, axis=1, inplace=True)

    # 获取要分类的列表
    classificationList = df.pop(classification[0])
    # 把分类列表插入最后
    df.insert(df.shape[1], 'class', classificationList)

    # 获取训练集
    trainData = df.sample(n=int(df.shape[0] * 0.7))
    # 获取余下的测试集
    testData = df.loc[df.index.difference(trainData.index)]

    # 输出转换好的数据
    df.to_excel("dist/dataset_export.xlsx", sheet_name='dataset')
    # 保存训练数据集
    trainData.to_excel("dist/dataset_train.xlsx", sheet_name='dataset')
    trainData.to_csv("dist/dataset_train.csv", index=False)
    # 保存测试数据集
    testData.to_excel("dist/dataset_test.xlsx", sheet_name='dataset')
    testData.to_csv("dist/dataset_test.csv", index=False)
