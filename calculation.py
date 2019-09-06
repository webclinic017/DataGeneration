from atm import ATM
from atm import Model
import pandas as pd

if __name__ == '__main__':
    # 创建ATM对象
    atm = ATM()

    # 运行训练数据
    results = atm.run(train_path='dist/dataset_train.csv')

    # 获取运行后的节后
    results.describe()

    # 获取最佳模型
    print(results.get_best_classifier())

    #
    print(results.get_scores())

    # 导出模型
    results.export_best_classifier('models/model.pkl')

    # 载入模型
    model = Model.load('models/model.pkl')

    # 载入测试数据
    data = pd.read_csv('dist/dataset_test.csv')

    # 预测数据
    predictions = model.predict(data)

    print(predictions)