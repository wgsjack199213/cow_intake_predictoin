# 泌乳牛自由采食量预测

## 报告

最新版的文字报告（更新于2017.8.9）请见repo根目录下的*采食量稿0809.pdf*文件。

另外，根目录下的*preprocess_data.html*和*model.html*为Jupyter Notebook生成的只读报告，分别包含了数据预处理和模型构建、实验测试的代码和文字说明。

## 程序和源代码

*采食量稿0809.pdf*报告的LaTeX源代码在根目录下，主文件为main.tex，采用XeLaTex编译器对其进行编译即可生成pdf报告文件。

*preprocess_data.html*和*model.html*对应的源代码为Script目录下的*preprocess_data.ipynb*和*model.ipynb*。用Jupyter Notebook打开即可任意编辑、运行。

此外，Script目录下还有其他实验相关的程序代码和数据文件。

## 预测器程序

Script目录下的predictor.py是通过以构建好的模型进行预测的程序，输入文件为*input.csv*。运行方式：

	python predictor.py

结果为：

	牛舍： B1-7N B4-5N B1-3N B1-5N B1-1S B4-3N B4-3S B1-5S B1-3S B4-7N B4-5S B1-7S
	B1-7N: 35.4557
	B4-5N: 35.5256
	B1-3N: 35.0208
	B1-5N: 32.648
	B1-1S: 35.6694
	B4-3N: 32.8765
	B4-3S: 32.5096
	B1-5S: 30.6974
	B1-3S: 34.4773
	B4-7N: 38.4609
	B4-5S: 35.2419
	B1-7S: 34.8519

第二行起，每行输出一个牛舍未来一天的头均采食量预测值，单位为千克。

### 输入文件格式

请参考*input_backup.csv*的格式组织输入文件*input.csv*的格式，包含至少连续4天（含当天）的历史数据，并将需要预测的样本也置于表格中（只需填写date、cowshed，和从天气预报获取到的temp_high、RH字段）。所有未知的量留空，或用NaN填充。

## 实验环境需求
编程语言：Python 2.7。

如希望编辑、运行*preprocess_data.ipynb*和*model.ipynb*，需安装[Jupyter Notebook](https://jupyter.org/)。

需要安装的Python包：numpy，pandas，matplotlib，xgboost，scipy，pywt，sklearn，pickle。




