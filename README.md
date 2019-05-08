# Voting-application
## 项目描述
`一个投票应用程序`
## 项目来源
&emsp;[官方地址](https://docs.djangoproject.com/zh-hans/2.2/intro/)
- [初识 Django](https://docs.djangoproject.com/zh-hans/2.2/intro/overview/)
- [快速安装指南](https://docs.djangoproject.com/zh-hans/2.2/intro/install/)
- [编写你的第一个 Django 应用，第 1 部分](https://docs.djangoproject.com/zh-hans/2.2/intro/tutorial01/)
- [编写你的第一个 Django 应用，第 2 部分](https://docs.djangoproject.com/zh-hans/2.2/intro/tutorial02/)
- [编写你的第一个 Django 应用，第 3 部分](https://docs.djangoproject.com/zh-hans/2.2/intro/tutorial03/)
- [编写你的第一个 Django 应用，第 4 部分](https://docs.djangoproject.com/zh-hans/2.2/intro/tutorial04/)
- [编写你的第一个 Django 应用，第 5 部分](https://docs.djangoproject.com/zh-hans/2.2/intro/tutorial05/)
- [编写你的第一个 Django 应用，第 6 部分](https://docs.djangoproject.com/zh-hans/2.2/intro/tutorial06/)
- [编写你的第一个 Django 应用，第 7 部分](https://docs.djangoproject.com/zh-hans/2.2/intro/tutorial07/)
- [进阶指南：如何编写可重用程序](https://docs.djangoproject.com/zh-hans/2.2/intro/reusable-apps/)
- [下一步看什么](https://docs.djangoproject.com/zh-hans/2.2/intro/whatsnext/)
- [编写你的第一个 Django 补丁](https://docs.djangoproject.com/zh-hans/2.2/intro/contributing/)
## 项目组成：  
### 它将由两部分组成：
- 一个让人们查看和投票的公共站点。
- 一个让你能添加、修改和删除投票的管理站点。
### 模型：
&emsp;在这个简单的投票应用中，需要创建两个模型：问题 Question 和选项 Choice。
- Question 模型包括问题描述和发布时间。
- Choice 模型有两个字段，选项描述和当前得票数。每个选项属于一个问题。  

<font color=#ff0000 size=4> 一定注意遵循编码规范PEP 8 </font>  


### url对应的页面
url|页面
-|-
127.0.0.1/polls |问题总页面
../polls/1|第一个投票详情页面
../polls/results|投票结果页面

## 第一部分
&emsp;[详细 参考/实现](https://docs.djangoproject.com/zh-hans/2.2/intro/tutorial01/)
- 创建项目
- 启动简易服务器
- 创建投票应用
- 编辑第一个视图
  
## 第二部分
&emsp;[详细 参考/实现](https://docs.djangoproject.com/zh-hans/2.2/intro/tutorial02/)
- 数据库配置
- 创建模型
- 激活模型
- 初试API
- Django管理页面

## 第三部分
&emsp;[详细 参考/实现](https://docs.djangoproject.com/zh-hans/2.2/intro/tutorial03/)
- 编写视图
- 抛出404错误
- 使用模板系统
- 去除模板中的硬编码 URL
- 为 URL 名称添加命名空间

## 第四部分
&emsp;[详细 参考/实现](https://docs.djangoproject.com/zh-hans/2.2/intro/tutorial04/)
- 编写一个简单的表单
- 使用通用视图：代码还是少点好

# 结果展示
1. ***主页面***  

![主页面](https://github.com/Gruffalo123/others/blob/master/mysite_vote/polls.jpg)

2. ***投票详情页面***  

![投票详情展示页面](https://github.com/Gruffalo123/others/blob/master/mysite_vote/1.jpg)

3. ***操作错误页面***  

![不选择任何选项进行投票](https://github.com/Gruffalo123/others/blob/master/mysite_vote/vote_error.jpg)

4. ***成功投票结果展示页面***  

![正确操作结果页面](https://github.com/Gruffalo123/others/blob/master/mysite_vote/correct_vote.jpg)

## 第五部分
&emsp;[详细 参考/实现](https://docs.djangoproject.com/zh-hans/2.2/intro/tutorial05/)
- 自动化测试

## 第六部分
&emsp;[详细 参考/实现](https://docs.djangoproject.com/zh-hans/2.2/intro/tutorial06/)
- 自定义界面和风格
