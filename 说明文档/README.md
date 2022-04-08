# NJU Fundation of Data Science 

## 司法大数据自动化分词与标注

### 成员分工

- 201830115 张月明：前端和后台开发
- 201250061 王昕妍：分词处理（含词典）
- 201250135 魏心怡：数据可视化分析

### 项目功能

- 分词处理：用户可以在前端页面上传本地的文本或者直接输入案件信息，系统对文本内容进行自动化分词，通过文本命名实体、词性分析等方法获取基本信息可能对应的实体，并将其展示为可选项形式   
- 关键词标注：用户可以根据需要的基本信息如当事人等，点击对应的可选项，以此对基本信息进行标注，并可以将案件和基本信息保存到本地  
- 数据可视化：提供一定数量文书样本的性别分布，案由比例，地区作案人数比例及特殊关键词的相关性分析

### 代码结构

- ```bash
  |-- DataScience
      |-- DataScience.iml
      |-- pom.xml
      |-- README.md
      |-- .idea
      |   |-- libraries
      |-- src
      |   |-- main
      |   |   |-- java
      |   |   |   |-- com
      |   |   |       |-- example
      |   |   |           |-- datascience
      |   |   |               |-- DataScienceApplication.java
      |   |   |               |-- Controller
      |   |   |               |   |-- FileUploadController.java
      |   |   |               |   |-- MvcConfigController.java
      |   |   |               |   |-- ToPageController.java
      |   |   |               |   |-- URLConfigController.java
      |   |   |               |-- Service
      |   |   |                   |-- Python.java
      |   |   |                   |-- PythonService.java
      |   |   |                   |-- TextReadService.java
      |   |   |-- resources
      |   |       |-- application.yml
      |   |       |-- Documents
      |   |       |-- static
      |   |       |   |-- ckeditor
      |   |       |   |-- css
      |   |       |   |-- img
      |   |       |   |-- js
      |   |       |   |-- python
      |   |       |       |-- court.txt(词典（相关法院）)
      |   |       |       |-- dict.txt(词典（人物其他信息）)
      |   |       |       |-- stop.txt(词典（停用词）)
      |   |       |       |-- keywordExtraction1.py(提取人物关键词)
      |   |       |       |-- keywordExtraction2.py(划分词性)
      |   |       |-- templates
      |   |       |   |-- keyword.json
      |   |       |   |-- partsofspeech.json
      |   |       |   |-- upload.html(文书上传)
      |   |       |   |-- analyze.html(文书分析)
      |   |       |   |-- sign.html(文书标注)
      |   |       |   |-- index.html(首页)
      |   |       |-- venv
      |   |-- test
      |       |-- java
      |           |-- com
      |               |-- example
      |                   |-- datascience
      |                       |-- DataScienceApplicationTests.java
  ```

### 代码解释

- main
  - java
    - Controller层包含四个类
      - FileUploadController：文书上传类，负责读取上传的文书内容，并调用python程序分词处理
      - MvcConfigController：配置类，负责解决后端向前端返回分词json时的中文乱码问题
      - ToPageController：页面控制类，负责跳转到不同的页面
      - URLConfigController：地址映射类，负责分词json文件的绝对地址与虚拟地址的映射
    - Service层包含一个接口，两个类
      - Python接口：定义了两个方法，分别负责人物关键词和词性的分词处理
      - PythonService：具体实现Python接口的两个方法
      - TextReadService：文书内容读取类，负责读取txt/doc/docx格式的文书内容
    - DataScienceApplication:主程序的入口
  - resources
    - Documents目录：负责存放前端上传的文书文件
    - static目录
      - ckeditor目录：存放富文本编辑器ckeditor4自带文件
      - img目录：存放图片资源
      - css目录：存放添加样式的文件（主要应用bootstrap4）
      - js目录：存放为页面元素绑定特定功能的文件（主要应用bootstrap4）
      - python目录：存放python代码文件和分词词典
    - templates目录：存放html文件和经分词处理后的临时json文件
    - venv目录：存放jieba分词执行自带文件
    - application.yml: springboot项目的配置文件
- test
  - DataScienceApplicationTests：测试类

### 使用工具&实现原理

- 分词处理：
  
  - jieba（python版）： https://github.com/fxsjy/jieba 
  - 根据精确模式分词，添加司法领域的相关词典（法院，罪名等）
  - 关键词提取：基于TF-IDF算法提取后进行停用词过滤
  - 词性标注：采用jieba默认分词模式下的词性分类（paddle模式词性和专名类别 ），并进行停用词过滤
  
- 前端页面设计和后端工程架构：
  - bootstrap4：https://getbootstrap.com/ ：一个基于 HTML、CSS、JAVASCRIPT 的前端框架 
  - layoutit：https://www.layoutit.com/： 能够简单又快速搭建Bootstrap的响应式布局 
  
  - springboot：https://spring.io/projects/spring-boot/ ：基于Spring所有功能的工具框架，快速架构项目
  - 文书上传功能：用户在前端选择对应文书文件并上传后，触发后台FileUploadController类中的upload方法，该方法首先获取到文件的本地路径，之后调用TextReadService类中的txtRead方法（假设文件为txt格式）读取文书内容，接着调用pythonService中的两个分词处理的方法来运行python脚本，生成的临时json分词文件存放在templates目录中。
  - 文书标注功能：在URLConfigController类将json分词文件本地地址映射为前端访问地址后，前端通过show.js找到对应的json分词文件，并分别显示在各个绑定了id标签的选项卡中。用户在前端标注信息，点击保存按钮，触发saveFile.js来完成以json格式保存标注。
  
- 数据可视化：
  
  - pyecharts：https://pyecharts.org/#/zh-cn/intro：可以处理数据，且有良好的交互性和精巧的图表设计 
  - 安装pyecharts模块，依次导入Map、Pie、Bar三个模块
  - 设置各个图的全局配置项和系列配置项，绘制地图并采用顺序多图的方式整合  

### 使用方法

1.安装JDK，添加Maven，并在pom.xml中下载引入一系列依赖文件



![1642518966870](readme.assets\1642518966870.png)



2.在URLConfigController（地址映射类）中修改绝对路径为自己的本地路径



![1642519113046](readme.assets\1642519113046.png)



3.在application.yml（配置文件）中修改servlet/multipart/location中的绝对路径为自己的本地路径



![1642519197455](readme.assets\1642519197455.png)



4.运行DataScienceApplication类中的方法，即可启动程序



![1642519284916](readme.assets\1642519284916.png)



5.打开浏览器（建议谷歌/火狐），输入地址http://localhost:8080/index.html，效果如图，项目启动成功！



![1642519450289](readme.assets\1642519450289.png)



6.进入文书上传页面，可以直接输入纯文本，并保存案件信息；也可以上传本地文件并提交



![1642668559951](readme.assets\1642668559951.png)



7.进入文书标注页面，选择点击对应的可选项，最后可以保存标注信息



![1642668625462](readme.assets\1642668625462.png)



8.进入文书分析页面，可以查看获取到的文书的不同参数的数据分析，并以图表的样式可视化展示



![1642668955119](readme.assets\1642668955119.png)



9.在更多资源的选项卡中有其他权威法律服务网站，它们是我们网站的主要数据来源，特此鸣谢！



![1642672884940](readme.assets\1642672884940.png)