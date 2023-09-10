# ☁️ PromptHub

简体中文 | [English](<(./README-en.md)>)

<p>
	<p align="center">
		<img height=120 src="https://img.gejiba.com/images/e1945208195b199bd244431fd2a6efa0.png">
	</p>
	<p align="center">
		<img src="https://img.gejiba.com/images/605bd1bcc1a14f803f1d8f68b8c1c892.png"><br>
		<b face="雅黑">Change the world, even a little bit.</b>
	<p>
</p>
<p align="center">
<img alt=" Python" src="https://img.shields.io/badge/Python-3.10%2B-blue"/>
<img alt="cleo" src="https://img.shields.io/badge/cleo-2.0.1-yellowgreen"/>
<img alt="license" src="https://img.shields.io/badge/license-Apache-lightgrey"/>
</p>

PromptHub 是[ssprompt](https://github.com/ptonlix/ssprompt) 工具默认使用的 Prompt 仓库

---

## 📃 Metafile 介绍

PromptHub 主要依赖 ssprompt 定义的 Meta 文件定义仓库中各类 Prompt，Meta 文件含义参考如下:

ssprompt 通过定义 prompt 工程的 Meta 文件来约束管理 Prompt 分发规则和内容  
ssprompt 关于 prompt 定义了四种类型的 Prompt

- Text
- Json
- Yaml
- Python

可以按需生成对应的 Prompt 上传到 PromptHub 进行分发  
metafile 以 Prompt 工程名称命名,如 prompt_project.yaml ，是 ssprompt 管理 Prompt 分发的关键

注：上述类型结合参考了 langchain 和 haystack

```yaml
#Prompt工程基础信息
meta:
  name: open #工程名称
  author:
    - ptonlix <baird0917@163.com>
  description: ""
  license: MIT #Prompt工程遵循的协议
  llm: #Prompt支持的LLM模型
    - gpt-3.5-turbo
  readme_format: md #Readme文件格式
  tag: #Prompt工程相关类型领域，如question-generation common为公共领域
    - common
  version: 0.1.0 #版本号

#Text类型的Prompt
text_prompt:
  dirname: text #目录名称, 默认为text

#Json类型的Prompt
json_prompt:
  dirname: json #目录名称，默认为json
  list: #支持多个json类型子工程
    - dependencies:
        langchain: 0.0.266 #json解析依赖的三方库版本号，如langchain等
      name: example #子工程名，对应生成工程目录名

#Yaml类型的prompt
yaml_prompt:
  dirname: yaml #目录名称，默认为yaml
  list: #支持多个yaml类型子工程
    - dependencies:
        langchain: 0.0.266 #yaml解析依赖的三方库版本号，如langchain等
      name: example #子工程名，对应生成工程目录名

#Python类型的Prompt
python_prompt: #目录名称，默认为yaml
  dirname: python #目录名称，默认为yaml
  list: #支持多个yaml类型子工程
    - dependencies:
        langchain: 0.0.266 #Python库引用的三方库版本号，如langchain等
      name: example #子工程名，对应生成工程目录名
```

## 🏷️ Prompt Tag

当前 PromptHub 支持 Prompt 分类如下

| **分类名称** |      **表示**      |                  **备注**                   |
| :----------: | :----------------: | :-----------------------------------------: |
|     总结     |   summarization    |                                             |
|     对话     |   conversational   |                                             |
|   内容生成   | content-generation |                                             |
|   语言检测   | language-detection |                                             |
|     问答     | question-answering |                                             |
|   情感分析   | sentiment-analysis |                                             |
|     分类     |   classification   |                                             |
|     翻译     |    translation     |                                             |
|     代理     |       agent        |                                             |
|     公共     |       common       | ssprompt 默认生成 tag<br>建议更换合适的 tag |

## 💼 Prompt 协议

ssprompt 建议采用流行的开源协议，如

- Apache License
- MIT License
- BSD License
- GNU License

各种协议大全，请参考 [开源协议](https://opensource.org/licenses/)

---

## 🔥 当前 Prompt 工程列表 （持续更新～）

**🎉 欢迎大家提交 Prompt**

### example

1. 项目说明： 示例工程，演示和测试 ssprompt 使用

2. 使用参考：[README](example/README.md)

### summarization

1. 项目说明：一个善于总结文档的 Prompt，可以通过明确要求，让 LLM 总结所需的文档

2. 使用参考：[README](summarization/README.md)

### generation_redbook_title

1. 项目说明：学习小红书标题风格，根据输入的主题创造对应小红书标题

2. 使用参考：[README](generation_redbook_title/README.md)

### generation_redbook_article

1. 项目说明：一键快速生成小红书爆火文章

2. 使用参考：[README](generation_redbook_article/README.md)
