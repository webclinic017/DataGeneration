## 使用方法（基于Python3.6）

### 第一步：创建虚拟环境

### 第二步：在虚拟环境中执行“pip install -r requirements.txt”指令安装相关依赖

### 第三步：在虚拟环境中执行“python generation.py”后会创建dist目录，数据集就在其中

```bash
python generation.py -h

usage: generation.py [-h] [-c [COUNT]]

Generation DataSet Tool

optional arguments:
  -h, --help            show this help message and exit
  -c [COUNT], --count [COUNT]
                        生成数据集的大小
```

### 第四步：在虚拟环境中执行“python export.py -c ”后会在dist目录生成训练数据和测试数据

```bash
python export.py -h

usage: export.py [-h] -c CLASSIFICATION [CLASSIFICATION ...]
                 [-i IGNORE [IGNORE ...]]

Export DataSet Tool

optional arguments:
  -h, --help            show this help message and exit
  -c CLASSIFICATION [CLASSIFICATION ...], --classification CLASSIFICATION [CLASSIFICATION ...]
                        要进行分类的名称
  -i IGNORE [IGNORE ...], --ignore IGNORE [IGNORE ...]
                        要忽略的标签列表
```

### 第五步：在虚拟环境中执行“python calculation.py”获取训练和测试结果
