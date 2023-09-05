# ☁️ PromptHub
简体中文 | [English]((./README-en.md))
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


PromptHub是[ssprompt](https://github.com/ptonlix/ssprompt) 工具默认使用的Prompt仓库

---
## 📃 Metafile介绍
PromptHub主要依赖ssprompt定义的Meta文件定义仓库中各类Prompt，Meta文件含义参考如下:

ssprompt通过定义prompt工程的Meta文件来约束管理Prompt分发规则和内容  
ssprompt关于prompt定义了四种类型的Prompt
- Text
- Json
- Yaml
- Python

可以按需生成对应的Prompt上传到PromptHub进行分发  
metafile以Prompt工程名称命名,如prompt_project.yaml ，是ssprompt管理Prompt分发的关键

注：上述类型结合参考了langchain和haystack
```yaml
#Prompt工程基础信息
meta:
  name: open #工程名称
  author: 
  - ptonlix <baird0917@163.com>
  description: ''
  license: MIT #Prompt工程遵循的协议
  llm:    #Prompt支持的LLM模型
  - gpt-3.5-turbo 
  readme_format: md #Readme文件格式
  tag:  #Prompt工程相关类型领域，如question-generation common为公共领域
  - common
  version: 0.1.0 #版本号

#Text类型的Prompt
text_prompt:
  dirname: text #目录名称, 默认为text

#Json类型的Prompt
json_prompt:
  dirname: json #目录名称，默认为json
  list:                  #支持多个json类型子工程
  - dependencies:   
      langchain: 0.0.266 #json解析依赖的三方库版本号，如langchain等
    name: example        #子工程名，对应生成工程目录名

#Yaml类型的prompt
yaml_prompt: 
  dirname: yaml #目录名称，默认为yaml
  list:					 #支持多个yaml类型子工程
  - dependencies:		
      langchain: 0.0.266 #yaml解析依赖的三方库版本号，如langchain等
    name: example		 #子工程名，对应生成工程目录名

#Python类型的Prompt
python_prompt:	#目录名称，默认为yaml
  dirname: python		 #目录名称，默认为yaml
  list: 				 #支持多个yaml类型子工程
  - dependencies:
        langchain: 0.0.266 #Python库引用的三方库版本号，如langchain等
    name: example		 #子工程名，对应生成工程目录名
```

## 🏷️ Prompt Tag

当前PromptHub支持Prompt分类如下

| **分类名称** | **表示** | **备注**|  
|:----:|:----:|:----:|
|总结 |summarization||
|对话|conversational||
|问题生成|question-generation||
|语言检测|language-detection||
|问答|question-answering||
|情感分析|sentiment-analysis||
|分类|classification||
|翻译|translation||
|代理|agent||
|公共|common|ssprompt默认生成tag<br>建议更换合适的tag|

## 💼 Prompt协议

ssprompt建议采用流行的开源协议，如

* Apache License
* MIT License
* BSD License
* GNU License


各种协议大全，请参考 [开源协议](https://opensource.org/licenses/)

---

## 🔥当前Prompt工程列表 （持续更新～）

**🎉 欢迎大家提交Prompt**

### example 

1. 项目说明： 示例工程，演示和测试ssprompt使用

2. 使用参考：[README](example/README.md)


### summarization

1. 项目说明：一个善于总结文档的Prompt，可以通过明确要求，让LLM总结所需的文档

2. 使用参考：[README](summarization/README.md)