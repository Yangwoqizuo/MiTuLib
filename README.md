# 积木机器人编程辅助库
## 关于
这是一个由 **非官方** 的积木爱好者自发创建编程库。  
通过生成积木机器人APP可以识别的编程数据，达到使用电脑简洁编程的目的。帮助开发者快速生成规模大或者逻辑复杂的编程玩法。  
**使用本库生成的数据有不被主控识别导致APP闪退的可能，请在使用前备份好APP数据库。本库为业余爱好者开发，由于使用本库造成的任何故障和损失，开发者不会承担任何责任，请谨慎使用。**
## 使用说明
### 准备工作
* 一部Root了的Android手机，并装有积木机器人APP  
可以使用小米手机开发版，在安全中心打开Root权限即可。但Root之后的手机安全性没有保证，所以不建议使用主力机。
* ADB  
我们需要使用ADB从手机中存取积木机器人APP的数据库文件  
[下载地址](https://developer.android.google.cn/studio/releases/platform-tools.html#downloads)
* SQLite3  
用于读写数据库，上一步下载的platform-tools中有
* SQLite3查看工具（可选）  
用于查看APP已经存储的数据，如果你找到的工具可以编辑数据库，就可以忽略上一步。

### 使用流程
0. 在手机APP中创建一条编程，保存，记住名字
0. 在电脑创建一个文件夹，并在终端cd进去
0. 手机连接电脑，进入ADB ROOT模式  
	`adb root`  
0. 使用ADB把数据库文件取出
	` adb pull /data/data/com.iqi.MiTuBuilder/databases/OneBot.db`  
0. 自行备份一下`OneBot.db`文件
0. 打开数据库文件，查看刚才创建的编程的序号，即`ArchiveID`字段
0. 使用本库编码，并运行获得sql语句
0. 使用SQLite3访问数据库  
	`sqlite3 OneBot.db`
0. 执行本库生成的sql语句
0. 退出SQLite  
	`.quit`
0. 把数据库文件放回手机  
	`adb push OneBot.db /data/data/com.iqi.MiTuBuilder/databases`
	
### DEMO介绍

#### [demo.py](demo.py)
&emsp;简单的if else
#### [demo\_piano\_ringtone.py](demo_piano_ringtone.py)
&emsp;经典小米手机铃声
#### [demo\_piano\_pig.py](demo_piano_pig.py)
&emsp;猪八戒背媳妇

### 编程介绍