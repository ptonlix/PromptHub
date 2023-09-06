# ✒️ Example Prompt

## 一.说明

测试示例，用于测试ssprompt使用

## 二.支持语言环境

英文

## 三.支持LLM模型

* gpt-3.5-turbo

***其他模型待测试***
## 四.支持Prompt类型
* Text
* Python
* Json
* Yaml

## 五.使用参考
ssprompt工具[下载链接](https://github.com/ptonlix/ssprompt)

### 1.使用Python类型的Prompt

```shell
# 进入到项目路径
cd Python项目路径

# 拉取Python库到项目
ssprompt pull -s example -t python

```
####  项目引用Prompt(举例参考)
```python
# __main__.py
from langchain import OpenAI
from langchain.chains import LLMChain

# 使用api2d访问openai
ai = OpenAI()
ai.openai_api_base = "https://oa.api2d.net/v1" 

from example import PROMPT

chain = LLMChain(llm=ai, prompt=PROMPT)

chain.run(conv_rate=0.6, acc_rate=0.8, avg_daily_trips="10km")
```
### 2.使用Json类型的Prompt

```shell
# 进入到项目路径
cd Python项目路径

# 拉取Python库到项目
ssprompt pull -s example -t json
```
####  项目引用Prompt(举例参考)
```python
# __main__.py
from langchain.prompts import load_prompt

prompt = load_prompt("example/example.json")
print(prompt.format(history="funny", input="What does the conversation show?"))

# langchain继续使用
```

### 3.使用Yaml类型的Prompt

```shell
# 进入到项目路径
cd Python项目路径

# 拉取Python库到项目
ssprompt pull -s example -t yaml
```
####  项目引用Prompt(举例参考)
```python
# __main__.py
from langchain.prompts import load_prompt

prompt = load_prompt("example/example.yaml")
print(prompt)

# langchain继续使用
```

### 4.使用Text类型的Prompt

```shell
# 进入到项目路径
cd Python项目路径

# 拉取Python库到项目
ssprompt pull -s example -t text
```
#### 使用

可以通过修改，复制到[openai](http://chat.openai.com)聊天交互页面使用
