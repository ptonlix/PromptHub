# ✒️ Generation Redbook Article Prompt

## 一.说明

一键快速生成小红书爆火文章

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
ssprompt pull -s generation_redbook_article -t python

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

from generation_redbook_article import PROMPT

chain = LLMChain(llm=ai, prompt=PROMPT)

chain.run(topic="大语言模型Prompt")

```

### 2.使用 Text 类型的 Prompt

```shell
# 进入到项目路径
cd Python项目路径

# 拉取Python库到项目
ssprompt pull -s generation_redbook_article -t text
```

#### 使用

可以通过修改，复制到[openai](http://chat.openai.com)聊天交互页面使用
