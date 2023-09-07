# ✒️ Generation Redbook Title Prompt

## 一.说明

学习小红书标题风格，根据输入的主题创造对应小红书标题

## 二.支持语言环境

中文

## 三.支持 LLM 模型

- gpt-3.5-turbo

**_其他模型待测试_**

## 四.支持 Prompt 类型

- Text
- Python

## 五.使用参考

ssprompt 工具[下载链接](https://github.com/ptonlix/ssprompt)

### 1.使用 Python 类型的 Prompt

```shell
# 进入到项目路径
cd Python项目路径

# 拉取Python库到项目
ssprompt pull -s generation_redbook_title -t python

```

#### 项目引用 Prompt(举例参考)

```python
# __main__.py
from langchain import OpenAI
from langchain.chains import LLMChain


# 使用api2d访问openai
OpenAI.openai_api_base = "https://oa.api2d.net"

ai = OpenAI()
ai.openai_api_base = "https://oa.api2d.net/v1"

from generation_redbook_title import PROMPT

chain = LLMChain(llm=ai, prompt=PROMPT)

chain.run(theme="大语言模型Prompt", keywords=["恐龙抗狼, 酱香"])

```

### 4.使用 Text 类型的 Prompt

```shell
# 进入到项目路径
cd Python项目路径

# 拉取Python库到项目
ssprompt pull -s generation_redbook_title -t text
```

#### 使用

可以通过修改，复制到[openai](http://chat.openai.com)聊天交互页面使用
