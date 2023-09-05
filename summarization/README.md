# ✒️ Summarization Prompt

## 一.说明

一个善于总结文档的Prompt，可以通过明确要求，让LLM总结所需的文档

## 二.支持语言环境

中文

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
ssprompt pull -s summarization -t python

```
####  项目引用Prompt(举例参考)
```python
# __main__.py
from langchain import OpenAI
from langchain.chains import LLMChain

# 使用api2d访问openai
ai = OpenAI()
ai.openai_api_base = "https://oa.api2d.net/v1" 

from summarization import PROMPT

chain = LLMChain(llm=ai, prompt=PROMPT)

doc="""
Feature stores are a concept from traditional machine learning that make sure data fed into models is up-to-date and relevant. For more on this, see here.

This concept is extremely relevant when considering putting LLM applications in production. In order to personalize LLM applications, you may want to combine LLMs with up-to-date information about particular users. Feature stores can be a great way to keep that data fresh, and LangChain provides an easy way to combine that data with LLMs.

In this notebook we will show how to connect prompt templates to feature stores. The basic idea is to call a feature store from inside a prompt template to retrieve values that are then formatted into the prompt.
"""
chain.run(documents=doc, require=["字数限定在30个字左右"])
```
### 2.使用Json类型的Prompt

```shell
# 进入到项目路径
cd Python项目路径

# 拉取Python库到项目
ssprompt pull -s summarization -t json
```
####  项目引用Prompt(举例参考)
```python
# __main__.py
from langchain.prompts import load_prompt

prompt = load_prompt("summarization/summarization.json")
print(prompt.format(documents="funny", require="chickens"))

# langchain继续使用
```

### 3.使用Yaml类型的Prompt

```shell
# 进入到项目路径
cd Python项目路径

# 拉取Python库到项目
ssprompt pull -s summarization -t yaml
```
####  项目引用Prompt(举例参考)
```python
# __main__.py
from langchain.prompts import load_prompt

prompt = load_prompt("summarization/summarization.yaml")
print(prompt.format(documents="funny", require="chickens"))

# langchain继续使用
```

### 4.使用Text类型的Prompt

```shell
# 进入到项目路径
cd Python项目路径

# 拉取Python库到项目
ssprompt pull -s summarization -t text
```
#### 使用

可以通过修改，复制到[openai](http://chat.openai.com)聊天交互页面使用

