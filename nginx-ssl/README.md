	源码编译nginx支持https
	
基于docker官方centos7镜像构建的nginx镜像

源码编译nginx并加入ssl参数使其支持https，nginx版本为：1.10.2

通过supervisor管理镜像启动服务（nginx/sshd）

nginx和ssh配置文件启动时可定制（默认使用系统自带配置）

ssh远程登录时需设置root密码

构建镜像命令：
docker build -t tag .

tip：以上构建命令需在Dockerfile所在目录下执行

更新日志：
2016-12-30：第一次提交
