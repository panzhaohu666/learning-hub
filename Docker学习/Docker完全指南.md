# Docker 完全指南（零基础到实战部署）

> 适用对象：Docker 完全新手，已掌握 Linux 基础命令与 Git 基础 | 涵盖：容器原理、安装配置、镜像与容器操作、Dockerfile、Compose、数据持久化、网络模型、三大实战（MySQL 全家桶、Dify、GPU 与 vLLM）、镜像瘦身与安全、常用排错、命令速查、章节练习
> 前置知识：建议先通读《Linux 完全操作指南》前八章（命令、权限、进程、网络），本指南中出现的 `curl`、`grep`、`systemctl` 等命令默认你已会用。

---

## 目录

1. [为什么需要 Docker：容器 vs 虚拟机](#一为什么需要-docker容器-vs-虚拟机)
2. [安装 Docker：Ubuntu 与 Docker Desktop](#二安装-dockerubuntu-与-docker-desktop)
3. [核心概念：镜像、容器、仓库与守护进程](#三核心概念镜像容器仓库与守护进程)
4. [镜像操作：拉取、管理、打标签与推送](#四镜像操作拉取管理打标签与推送)
5. [容器操作：run 参数全解析](#五容器操作run-参数全解析)
6. [Dockerfile：构建自己的镜像](#六dockerfile构建自己的镜像)
7. [Docker Compose：多容器编排](#七docker-compose多容器编排)
8. [数据持久化：Volume 与 Bind Mount](#八数据持久化volume-与-bind-mount)
9. [网络：bridge、host、none 与容器互联](#九网络bridgehostnone-与容器互联)
10. [实战一：MySQL + Redis + 后端 API 一键启动](#十实战一mysql--redis--后端-api-一键启动)
11. [实战二：Dify 部署（对接大模型阶段二）](#十一实战二dify-部署对接大模型阶段二)
12. [实战三：GPU 容器与 vLLM 部署（对接大模型阶段五）](#十二实战三gpu-容器与-vllm-部署对接大模型阶段五)
13. [镜像瘦身与安全](#十三镜像瘦身与安全)
14. [常用排错指南](#十四常用排错指南)
15. [命令速查表](#十五命令速查表)
16. [章节练习](#十六章节练习)

---

### 这本指南怎么读

本仓库的理念是"手机阅读概念，电脑动手实操"，全程不依赖视频。本指南遵循同样的结构：

```
📱 概念阅读：通勤、午休时读，理解原理，不急着敲命令
💻 实操：晚上在电脑上照着敲，每章都有可运行的最小示例
```

章节分两类：**概念章**（一、三、八、九、十三）用手机读两遍即可；**实操章**（二、四、五、六、七、十、十一、十二、十四）必须亲手敲一遍。本指南与两条学习主线的对应关系：

| 本仓库路线 | 需要 Docker 的地方 | 对应章节 |
|-----------|-------------------|---------|
| 大模型学习 阶段二（Dify/Coze 实战） | 用 Docker 一键启动 Dify，搭建低代码智能体 | 第十一章 |
| 大模型学习 阶段五（量化与 vLLM 部署） | 用 GPU 容器部署 vLLM 推理服务 + FastAPI 封装 | 第十二章 |
| Python 全栈 DevOps 阶段（博客项目一键部署） | Dockerfile + Compose 编排 API、数据库、Redis、Nginx | 第六、七、十章 |

> ⚡ 学完本指南，你应该能做到三件事：`git clone dify 后用一条 docker compose up -d 把 Dify 跑起来`、`用 GPU 容器对外提供 OpenAI 兼容的大模型 API`、`把自己写的 Django 或 FastAPI 项目打包成镜像并一键部署`。

---

## 一、为什么需要 Docker：容器 vs 虚拟机

> 📱 概念阅读：15 分钟。这一章不敲命令，只建立认知。

### 1.1 一个经典的部署难题

你写了一个 Web 应用，本地跑得好好的，发给同事却起不来。同事的报错五花八门：

```
"Python 版本不对，你用的是 3.11 我这是 3.8"
"MySQL 没装，连接被拒"
"系统库缺一个，pip 装不上"
"Windows 和 Linux 路径不一样，代码直接崩"
```

这就是传说中的"**在我电脑上是好的**"（It works on my machine）问题。根本原因：**代码运行依赖整个环境**，而每个人机器的操作系统、运行库、依赖版本、配置都不一样。

Docker 的思路很直接：**把应用和它需要的整个环境一起打包成"镜像"，镜像在哪跑，环境就在哪。** 打包好的镜像在任何装好 Docker 的机器上，行为完全一致。

```
没有 Docker 时：
  你的电脑 (py3.11 + MySQL8)  → 能跑
  同事电脑 (py3.8 + MySQL5.7) → 崩了
  生产服务器 (没装 MySQL)      → 起不来
  ↓ 环境不一致，处处踩坑

有了 Docker 之后：
  镜像 myapp:v1（代码 + 环境打包）
     ↓ 同一份镜像
  你的电脑 / 同事电脑 / 生产服务器 → 跑出结果一致
```

### 1.2 容器到底是什么

很多人把容器理解成"轻量虚拟机"，这个类比容易，但会误导你。

**虚拟机**：在物理机之上虚拟出一整套计算机。每个虚拟机里有自己的操作系统内核、系统库、应用。隔离靠 Hypervisor，资源占用大，启动要几十秒。

**容器**：不是虚拟计算机，而是一个**被隔离的进程**。所有容器共享宿主机的 Linux 内核，只把文件系统、进程、网络、用户等命名空间隔离开。隔离靠内核的 Namespace（隔离视图）和 Cgroups（限制资源）。

一句话：**虚拟机隔离的是"整台电脑"，容器隔离的是"一个进程的运行环境"。**

```
虚拟机                               容器
┌──────────────┐  ┌──────────────┐   ┌────────┐ ┌────────┐
│  Guest OS    │  │  Guest OS    │   │  应用    │ │  应用    │
│  (完整内核)    │  │  (完整内核)    │   │  依赖    │ │  依赖    │
├──────────────┴──┴──────────────┤   ├────────┴─┴────────┤
│        Hypervisor 层            │   │  共享宿主机内核       │
├───────────────────────────────┤   ├───────────────────┤
│          宿主机硬件               │   │      宿主机硬件       │
└───────────────────────────────┘   └───────────────────┘
每个 VM 一套完整 OS，很重            所有容器共享一个内核，很轻
```

### 1.3 虚拟机 vs 容器对比

| 维度 | 虚拟机 | 容器 |
|------|--------|------|
| 抽象层次 | 虚拟硬件 + 完整操作系统 | 进程级隔离，共享宿主内核 |
| 启动速度 | 几十秒到几分钟 | 毫秒到秒级 |
| 镜像大小 | 数 GB | 几十 MB 到几百 MB |
| 内存占用 | 每台几 GB | 每个几 MB 到几十 MB |
| 隔离强度 | 强（独立内核） | 弱一些（共享内核） |
| 跨平台 | 可跑任意 OS（Windows/Linux/macOS） | Linux 内核，Windows 用 WSL2 模拟 |
| 一台机器的实例数 | 十几个 | 上百个 |
| 典型场景 | 需要完整系统的环境，如测试旧系统 | 微服务、CI/CD、本地开发环境 |

> 💡 一句话总结：**能用容器解决的用容器，必须隔离内核的才用虚拟机。** 本仓库的所有场景（Dify、vLLM、Django 部署）都用容器解决。

### 1.4 Docker 带来的四个核心价值

1. **环境一致**：镜像里已经装好一切，不再有"本地能跑生产崩"。
2. **一条命令部署**：`docker compose up -d` 拉起一整套服务，比手写安装文档强得多。
3. **资源高效**：同一台机器能跑比虚拟机多几倍到几十倍的服务。
4. **版本可回滚**：镜像带标签，`nginx:1.25` 和 `nginx:1.24` 随时切换，出问题秒级回退。

### 1.5 什么时候不该用 Docker

Docker 不是银弹，下面这些场景要慎重：

| 场景 | 原因 |
|------|------|
| 桌面 GUI 应用 | 容器无图形界面（可折腾但代价大） |
| 对内核有强依赖的应用 | 如定制内核、某些数据库性能优化 |
| 极高性能敏感场景 | NAT 网络、文件系统层有少量开销（但通常可忽略） |
| 需要完整 Windows 环境 | 容器跑不了 Windows 内核 |

### 1.6 本仓库为什么处处需要 Docker

- **大模型阶段二**：Dify 依赖 API、Worker、Web、PostgreSQL、Redis、向量数据库六七个组件，手装要半天，`docker compose up -d` 三分钟搞定。
- **大模型阶段五**：vLLM 对 CUDA、驱动、Python 依赖极其挑剔，官方直接把环境做成镜像，GPU 透传进容器即可。
- **全栈 DevOps 阶段**：FastAPI 后端、前端、MySQL、Redis、Nginx 五个组件编排成一套，Docker 就是阶段六"一键部署"的骨架。

> ✅ 进入下一章之前，先确认自己心里能回答：**容器和虚拟机最大的区别是什么？为什么镜像能保证"到处运行一致"？**

---

## 二、安装 Docker：Ubuntu 与 Docker Desktop

> 💻 实操：40 分钟。本章完成后，你的机器上应该能跑 `docker run hello-world`。

### 2.1 安装前先选方案

| 你的系统 | 推荐方案 | 说明 |
|---------|---------|------|
| Ubuntu / Debian 服务器 | 用 apt 装社区版（docker-ce） | 本文 2.2 节 |
| Ubuntu 桌面版 | 同上 | 同上 |
| Windows 10/11 | Docker Desktop | 需先装 WSL2，见 2.6 节 |
| macOS | Docker Desktop | 直接下载安装包 |
| CentOS / RHEL | 用 yum/dnf 装 docker-ce | 命令类似，源不同 |

本仓库主路径是 Linux（AutoDL 云服务器、自己的 Ubuntu 服务器），所以重点讲 Ubuntu。如果开发机是 Windows/macOS，装 Docker Desktop 即可，**容器里的命令完全一样**。

### 2.2 Ubuntu/Debian 用官方源安装（推荐）

用 Docker 官方 apt 源安装，比 `apt install docker.io` 版本新、组件全（含 buildx 和 compose 插件）。

```bash
# 1. 卸载旧版本（如果有）
sudo apt remove docker docker-engine docker.io containerd runc

# 2. 安装依赖
sudo apt update
sudo apt install -y ca-certificates curl

# 3. 添加 Docker 官方 GPG 密钥
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# 4. 添加软件源（Ubuntu）
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Debian 把上面两行里的 ubuntu 换成 debian；$VERSION_CODENAME 报错时（如 24.04 早期源里没有）可临时用 jammy 代替

# 5. 更新索引并安装
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

> 💡 组件说明：`docker-ce` 是守护进程和客户端；`containerd.io` 是容器运行时；`docker-buildx-plugin` 提供新版构建；`docker-compose-plugin` 提供 `docker compose` 命令。这四样装齐，后续章节的命令才都有。

### 2.3 官方脚本一键安装（备选）

不想敲上面那么多条，用官方脚本最省事：

```bash
curl -fsSL https://get.docker.com | sudo sh
```

脚本会自动完成 2.2 节全部步骤。缺点是你不知道它干了什么，出问题不好排查。**服务器上我推荐自己敲 2.2 节的完整流程**，多花五分钟，心里有数。

### 2.4 把当前用户加入 docker 组（免 sudo）

默认情况下 docker 命令需要 root 权限。每次敲 `sudo docker` 很烦，把用户加进 docker 组：

```bash
sudo usermod -aG docker $USER
# 关键：必须重新登录（或执行 newgrp docker）才生效
newgrp docker
```

> ⚠️ **安全提示**：docker 组内的用户等同于 root 权限（因为可以挂载宿主机目录进容器），**只给可信用户加**。学习阶段没问题，生产环境谨慎。

验证一下：

```bash
# 不需要 sudo 就成功，说明组配置生效
docker --version
```

### 2.5 验证安装

```bash
# 查看版本
docker --version
# 查看 compose 插件
docker compose version
# 查看守护进程状态（systemd 管理）
systemctl status docker
# 跑通第一个容器
docker run hello-world
```

`docker run hello-world` 成功的话，会输出一段英文欢迎语，大意是"你的 Docker 安装正确，能拉取镜像并运行容器"。看到它，本章就完成了，顺手 `docker images`、`docker ps` 确认环境干净即可。

### 2.6 Docker Desktop（Windows / macOS）

**Windows**：

1. 确认已启用 WSL2：以管理员打开 PowerShell 执行 `wsl --install`，重启。
2. 下载 Docker Desktop 安装包：`https://www.docker.com/products/docker-desktop/`
3. 安装时勾选"Use WSL 2 instead of Hyper-V"。
4. 打开 Docker Desktop，等状态栏变绿（Engine running）。
5. 在任意终端（PowerShell / WSL）里执行 `docker --version` 验证。

> 💡 Windows 下推荐**在 WSL 里用**，而不是直接在 PowerShell 里用。因为容器是 Linux 的，在 WSL 里操作最顺手，命令和本指南完全一致。

**macOS**：下载安装包拖进 Applications 打开即可，同样等状态栏变绿。

Docker Desktop 有个小坑：它跑在一个轻量虚拟机里，所以容器访问宿主机的 `localhost` 用的是特殊地址 `host.docker.internal`。详见第九章网络章节。

### 2.7 安装常见报错

| 报错 | 原因 | 解决 |
|------|------|------|
| `E: Unable to locate package docker-ce` | 源没更新或 codename 不对 | 重新执行 `sudo apt update`；检查 2.2 步第 4 步 |
| `Got permission denied while trying to connect to the Docker daemon socket` | 用户不在 docker 组 | 执行 2.4 节并重新登录 |
| `Cannot connect to the Docker daemon at unix:///var/run/docker.sock` | 守护进程没启动 | `sudo systemctl enable --now docker` |
| `failed to start daemon: iptables failed` | iptables 权限或内核问题 | 换 Ubuntu 内核，或查 `journalctl -u docker` |

---

## 三、核心概念：镜像、容器、仓库与守护进程

> 📱 概念阅读：20 分钟。这一章的四个名词会贯穿整本指南，务必理解透。

### 3.1 四个核心对象

| 对象 | 一句话理解 | 类比 |
|------|-----------|------|
| **镜像 Image** | 打包好的、只读的"运行环境模板" | 安装光盘 / 类的定义 |
| **容器 Container** | 镜像跑起来的实例，可读写 | 装好并运行的程序 / 类的实例 |
| **仓库 Registry** | 存放和分发镜像的地方 | 应用商店 |
| **守护进程 Daemon** | 常驻后台，替我们拉镜像、跑容器的服务 | 管家 |

### 3.2 整体架构

```
┌───────────────────────────────────────┐
│ 客户端 docker CLI                       │
│ docker pull / run / build ...          │
└───────────────┬───────────────────────┘
                │ 发送请求（unix socket）
                ↓
┌───────────────────────────────────────┐
│ 守护进程 dockerd                        │
│ · 管理镜像/容器/网络/数据卷               │
│ · 与 Registry 通信，拉取/推送镜像          │
└───────────────┬───────────────────────┘
                │ 调用容器运行时
                ↓
┌───────────────────────────────────────┐
│ 容器运行时 (containerd → runc)          │
│ · Namespace 隔离视图                    │
│ · Cgroups 限制 CPU / 内存               │
│ · OverlayFS 分层文件系统                 │
└───────────────┬───────────────────────┘
                ↓
┌───────────────────────────────────────┐
│ 宿主机 Linux 内核（共享，不虚拟）          │
└───────────────────────────────────────┘

镜像来源：docker pull 仓库中的镜像 → dockerd 解包 → 运行时创建容器
```

三条要记住的结论：

1. **你敲的 docker 命令只是"发指令"，真正干活的是 dockerd。** 这也是为什么守护进程没启动时会报"cannot connect to the Docker daemon"。
2. **所有容器共享宿主内核**，所以容器里的进程和宿主进程本质上是同一类东西，只是被隔离了。
3. **镜像来自仓库**，仓库在远端，本地没有就 `pull`。

### 3.3 镜像和容器的关系

```
镜像（只读模板）           docker run          容器（可写实例）
┌───────────────┐      ────────────────→     ┌───────────────┐
│  Ubuntu 22.04 │                            │  一个跑着的 nginx│
│  + Python 3.11│                            │  有自己的可写层  │
│  + 你的代码    │                            │  改它不影响镜像  │
└───────────────┘                            └───────────────┘
      ↑                                            ↑
 docker build 生成                             可以 run 出 N 个
```

关键点：

- 一个镜像可以 `run` 出**任意多个互不干扰的容器**。
- 容器是**可写**的，镜像**永远是只读**的。你在容器里改文件、装软件，改的是容器的可写层，镜像本身不受影响。
- 删容器不删镜像，镜像还在，随时能再 run。
- 把容器里改好的状态保存成新镜像，用 `docker commit`（不推荐，有更好的 Dockerfile 方式）。

### 3.4 镜像的分层结构

镜像不是一个大文件，而是**一层一层叠加**的：

```
┌──────────────────────┐
│  Layer 4: 你的代码      │  ← 顶层，更新最频繁
│  Layer 3: pip install │
│  Layer 2: 系统库        │
│  Layer 1: Ubuntu 基础  │  ← 底层，几乎不变
└──────────────────────┘
         ↓ 只读层叠加
  启动容器时在最上面加一层"可写层"，
  所有写入先发生在可写层，这就是"写时复制"。
```

分层带来两个好处：

1. **省磁盘**：两个镜像如果底层相同（比如都基于 ubuntu:22.04），底层只存一份，共享。
2. **省流量**：拉新镜像时，本地已有的层直接跳过，只下载差的部分。

这也就是第六章 Dockerfile 里"把不常变的东西放前面"这条最佳实践的底层原理。现在不理解没关系，先记住"**镜像 = 多层叠加，底层的缓存可以被上层复用**"。

### 3.5 容器的生命周期

```
  ┌─────────┐  docker run  ┌─────────┐  docker stop  ┌─────────┐
  │  Created │ ──────────→ │ Running  │ ────────────→ │ Stopped  │
  │  (创建)   │             │ (运行中)  │               │ (已停止)  │
  └─────────┘              └────┬────┘               └────┬────┘
                               │ docker kill(强杀)         │ docker start
                               ↓                          ↓
                          docker rm（删除，永别了）←────────┘
```

- **Running**：正在运行，`docker ps` 能看到。
- **Stopped**：进程停了，但容器对象还在，占一点磁盘，`docker ps -a` 能看到。
- **删除**：`docker rm` 后彻底消失，容器内的可写数据（没挂载卷的话）全没了。

> 💡 把容器生命周期和第八章的数据持久化连起来理解：**容器是"一次性"的，会死会删，数据要活下来就必须挂卷。**

---

## 四、镜像操作：拉取、管理、打标签与推送

> 💻 实操：30 分钟。跟着敲，镜像操作就这几板斧。

### 4.1 拉取镜像：docker pull

镜像的完整名字格式是 `仓库地址/命名空间/镜像名:标签`。

```bash
docker pull nginx:1.25                 # 指定版本标签
docker pull nginx:latest               # 最新版（不推荐生产用，见下）
docker pull python:3.11-slim           # -slim 是精简版
docker pull docker.io/library/redis:7  # 从指定仓库拉取
docker pull ghcr.io/owner/image:tag    # GitHub 容器仓库
docker pull --platform linux/amd64 nginx:1.25   # 只拉指定架构（ARM Mac 拉 amd64）
```

> ⚠️ `latest` 标签是"流动"的，今天拉的和三个月后拉的可能不是同一个版本。**生产环境永远指定具体版本号**，比如 `nginx:1.25`、`mysql:8.0`。

### 4.2 查看本地镜像

```bash
docker images                 # 简写 docker image ls
docker images -a              # 显示所有层（含中间层）
docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"
```

输出解读：

```
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
nginx        1.25      6efdb10f1f4e   2 weeks ago   187MB
python       3.11-slim 38179b5d3f0a   3 weeks ago   120MB
```

`IMAGE ID` 是镜像的唯一标识（前 12 位），删除时可以用它代替名字。

### 4.3 打标签：docker tag

标签（Tag）是镜像的别名，同一个镜像可以有好几个名字。打标签最常见的用途：**推送前把它命名为目标仓库要求的格式**。

```bash
# 给本地 nginx:1.25 起一个"我的仓库"格式的别名
docker tag nginx:1.25 docker.io/myname/nginx:prod
docker tag nginx:1.25 myname/nginx:prod      # 默认就是 docker.io

# 查看效果：同一 IMAGE ID 出现两次
docker images
```

### 4.4 删除镜像：docker rmi

```bash
docker rmi nginx:1.25             # 删除指定标签
docker rmi 6efdb10f1f4e           # 按 ID 删
docker rmi myname/nginx:prod      # 删除别名（原标签还在）
docker rmi -f nginx:1.25          # 镜像被容器占用时强制删（先删容器更好）

# 批量清理
docker rmi $(docker images -q)            # 删所有镜像（危险）
docker image prune                        # 删悬空镜像（dangling）
docker image prune -a                     # 删所有没被容器使用的镜像
```

> 💡 `dangling` 镜像：重新 build 之后，旧版本镜像会变成 `<none>:<none>`，占空间但用不上，`docker image prune` 就是清它们的。

### 4.5 搜索镜像

```bash
docker search mysql            # 在 Docker Hub 上按名字搜
docker search --stars 100 nginx  # 只看 star 超过 100 的
```

更靠谱的方式：直接浏览器打开 `https://hub.docker.com` 搜。**搜到后优先选"官方镜像"（名字不带用户名前缀）**，比如 `mysql` 是官方的，`bitnami/mysql` 是第三方的。

### 4.6 登录与推送：docker login / docker push

把镜像推到自己的仓库，或推到 Docker Hub：

```bash
# 登录 Docker Hub
docker login
# 会提示输入用户名和密码（个人令牌）

# 登录其他仓库（比如阿里云容器镜像服务）
docker login registry.cn-hangzhou.aliyuncs.com

# 推送：名字必须符合仓库格式
docker tag myapp:v1 myname/myapp:v1
docker push myname/myapp:v1

# 推送其他仓库
docker push registry.cn-hangzhou.aliyuncs.com/namespace/myapp:v1
```

> ⚠️ **敏感信息警告**：`docker login` 凭证存在 `~/.docker/config.json`，这个文件**绝不能提交进 Git 仓库**。如果误提交，立刻到平台撤销令牌。

### 4.7 仓库 Registry 一览

| 仓库 | 说明 | 典型用途 |
|------|------|---------|
| **Docker Hub** | 官方，公共镜像最多 | 拉公共镜像、发布自己的开源镜像 |
| **GitHub Container Registry (ghcr.io)** | GitHub 托管 | 和代码放一起，配 GitHub Actions 自动发布 |
| **阿里云容器镜像服务 (ACR)** | 国内速度快 | 国内服务器拉镜像快 |
| **Harbor** | 开源私有仓库，自建 | 企业内部镜像管理 |
| **AutoDL/云厂商镜像** | 云端预缓存常用镜像 | 本仓库阶段五在 AutoDL 上直接用 |

> 💡 国内拉 Docker Hub 慢的问题，见第十四章 14.3 节（配置镜像加速器）。

### 4.8 查看镜像详细信息

```bash
docker image inspect nginx:1.25       # 完整 JSON 信息（架构、层、环境变量等）
docker image inspect nginx:1.25 --format '{{.Architecture}}'  # 只看某一项
docker history nginx:1.25             # 查看镜像的分层历史（每层干了什么）
```

`docker history` 很有用，能看出一个镜像怎么构建出来的，也是理解"层"最直观的方式。

---

## 五、容器操作：run 参数全解析

> 💻 实操：40 分钟。这一章是使用频率最高的一章，每个参数都要敲一遍。

### 5.1 第一次真正运行容器

```bash
docker run -d --name web -p 8080:80 nginx:1.25
```

拆开看这条命令：

| 片段 | 含义 |
|------|------|
| `docker run` | 运行一个新容器 |
| `-d` | 后台运行（detach），不占终端 |
| `--name web` | 给容器起名 web，方便后续操作 |
| `-p 8080:80` | 宿主机 8080 端口映射到容器 80 端口 |
| `nginx:1.25` | 用什么镜像 |

现在打开浏览器访问 `http://localhost:8080`，能看到 nginx 默认欢迎页。**你已经成功跑起了一个 Web 服务器，这就是 Docker 的日常。**

```bash
# 查看它
docker ps
# 看日志
docker logs web
# 停止、再启动
docker stop web
docker start web
# 彻底删除
docker rm -f web
```

### 5.2 run 参数速查表

| 参数 | 作用 | 示例 |
|------|------|------|
| `-d` | 后台运行 | `docker run -d nginx` |
| `-it` | 交互式终端（配合 bash 用） | `docker run -it ubuntu bash` |
| `--rm` | 容器退出时自动删除 | `docker run --rm -it ubuntu bash` |
| `-p` | 端口映射 | `-p 8080:80` |
| `-v` | 挂载卷或目录 | `-v ./data:/app/data` |
| `-e` | 设置环境变量 | `-e MYSQL_ROOT_PASSWORD=123456` |
| `--env-file` | 从文件读环境变量 | `--env-file .env` |
| `--name` | 指定容器名 | `--name mynginx` |
| `--restart` | 重启策略 | `--restart=always` |
| `--network` | 指定网络 | `--network my-net` |
| `--cpus` | 限制 CPU 核数 | `--cpus 2` |
| `--memory` | 限制内存 | `--memory 512m` |
| `--gpus` | 透传 GPU（需装 NVIDIA 插件） | `--gpus all` |
| `-u` | 指定容器内用户 | `-u 1000:1000` |
| `-w` | 指定工作目录 | `-w /app` |

### 5.3 前台 vs 后台 vs 交互

```bash
docker run -d --name web nginx                    # 后台运行（服务类，最常用）
docker run -it --rm ubuntu:22.04 bash             # 交互式：进入容器 shell
docker run --rm alpine:3.19 sh -c "echo hi"       # 一次性任务：跑完即删
docker run --rm -p 8080:80 nginx                  # 前台运行：看输出，Ctrl+C 停
```

> 💡 `-it` 的组合含义：`-i` 保持标准输入打开，`-t` 分配一个伪终端。进容器调试必须两个一起用。

### 5.4 端口映射 -p 详解

```bash
docker run -d -p 8080:80 nginx                # 最常用：宿主机端口:容器端口
docker run -d -p 127.0.0.1:8080:80 nginx      # 只绑定本机 IP（安全）
docker run -d -p 80 nginx                     # 随机分配宿主端口（docker ps 看）
docker run -d -p 8080:80 -p 8443:443 nginx    # 同时映射多个端口
docker run -d -p 53:53/udp coredns/coredns    # UDP 端口

docker port web                               # 查看端口映射：80/tcp -> 0.0.0.0:8080
```

> ⚠️ `-p 8080:80` 和 `-p 80:8080` 是**反的**。记忆口诀：**左边宿主机，右边容器**。

### 5.5 环境变量 -e 与 --env-file

很多镜像的行为靠环境变量控制，这是"配置外部化"的核心手段。

```bash
docker run -d --name mysql \
  -e MYSQL_ROOT_PASSWORD=mysecret \
  -e MYSQL_DATABASE=appdb \
  mysql:8.0

# 从文件读取（生产推荐，文件不进 Git）；mysql.env 里每行一个 KEY=VALUE
docker run -d --name mysql --env-file ./mysql.env mysql:8.0
```

`mysql.env` 内容示例：

```
MYSQL_ROOT_PASSWORD=mysecret
MYSQL_DATABASE=appdb
MYSQL_USER=appuser
MYSQL_PASSWORD=apppass
```

> ⚠️ **不要把密码直接写进命令历史**。命令行里敲 `-e MYSQL_ROOT_PASSWORD=xxx`，这个密码会留在 `~/.bash_history` 里。用 `--env-file` 或后面的 `.env` 文件更安全。

```bash
# 查看容器环境变量
docker exec mysql env
docker inspect mysql --format '{{range .Config.Env}}{{println .}}{{end}}'
```

### 5.6 容器名与重启策略

容器名在同一台机器上必须唯一，重复会报 `name already in use`。

```bash
# 四种重启策略
docker run -d --restart=no nginx              # 默认：不自动重启
docker run -d --restart=always nginx          # 挂了/开机都自动重启（服务类最常用）
docker run -d --restart=on-failure:5 nginx    # 非正常退出时重启，最多 5 次
docker run -d --restart=unless-stopped nginx  # 除手动 stop 外都重启
```

> 💡 生产环境的数据库、Web 服务一律用 `--restart=unless-stopped`。服务器重启后服务自动回来，不用人半夜爬起来手动拉起。

### 5.7 查看容器

```bash
docker ps                              # 运行中的容器
docker ps -a                           # 全部容器（含停止的）
docker ps -q                           # 只输出 ID（批量操作神器）
docker ps --filter ancestor=nginx      # 过滤：基于 nginx 镜像的
docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

# 实时资源占用（像 top）：docker stats / docker stats --no-stream
# 容器内进程：docker top web
```

`docker ps -a` 的 Status 列信息量很大，常见状态：

| 状态 | 含义 |
|------|------|
| `Up 2 hours` | 正常运行中 |
| `Up 5 minutes (healthy)` | 健康检查通过 |
| `Exited (0)` | 正常退出（退出码 0） |
| `Exited (1)` | 报错退出（看日志！） |
| `Restarting (1)` | 不断重启（多半配置错了） |

### 5.8 查看日志：docker logs

日志是排错的第一工具，务必熟练。

```bash
docker logs web                  # 全部日志
docker logs -f web               # 实时追踪（等同 tail -f）
docker logs --tail 100 web       # 最近 100 行
docker logs --since 5m web       # 最近 5 分钟的
docker logs -t web               # 带时间戳
docker logs --tail 50 -f web     # 最常用组合：先看 50 行再实时追
```

> 💡 容器打印到标准输出（stdout/stderr）的内容才会进 docker logs。**写应用时请把日志打到 stdout，别写文件**，这是容器世界的约定。

### 5.9 进入容器：docker exec

```bash
docker exec -it web bash                 # 进入容器开 bash（alpine 用 sh）
docker exec web ls /etc/nginx            # 不进入，直接执行一条命令
docker exec mysql mysql -uroot -p
docker exec -u root web whoami           # 以指定用户执行
```

> 💡 对比：`docker run -it ubuntu bash` 是**新建**一个容器进去；`docker exec -it web bash` 是**进入已存在的容器**。调戏运行中的容器用 exec。

### 5.10 停止、启动与删除

```bash
docker stop web                  # 优雅停止（等进程自己退出）
docker kill web                  # 强杀
docker start web                 # 启动已停止的容器
docker restart web               # 重启
docker pause web / unpause web   # 暂停 / 恢复

docker rm web                    # 删除（需先停止）
docker rm -f web                 # 强制删除运行中的
docker rm $(docker ps -aq)       # 删除所有容器（经典批量命令）
```

> ⚠️ `docker rm -f` 不会保留容器内未挂卷的数据。删之前想清楚。

### 5.11 查看详细信息：docker inspect

`docker inspect` 输出容器的完整 JSON：网络 IP、挂载卷、环境变量、退出码、健康状态等。配 `--format` 只取需要的字段：

```bash
docker inspect web
docker inspect web --format '{{.State.Status}}'                            # 运行状态
docker inspect web --format '{{.NetworkSettings.IPAddress}}'               # 容器 IP
docker inspect web --format '{{json .Mounts}}'                             # 挂载情况
```

> 💡 `--format '{{...}}'` 用的是 Go template 语法，查字段用 `--format` 比一页页翻 JSON 高效。

### 5.12 文件复制：docker cp

容器和宿主机之间拷文件，不用进容器。

```bash
# 宿主机 → 容器
docker cp ./config.yml web:/etc/app/config.yml

# 容器 → 宿主机
docker cp web:/var/log/app.log ./app.log

# 目录也可以
docker cp web:/app/logs ./logs/
```

> 💡 `docker cp` 只是拷贝，不解决"持久化"问题。数据要长期存活，用第八章的卷。

### 5.13 资源限制

防止某个容器把整台机器吃垮：

```bash
# 限制最多 1.5 核、512MB 内存
docker run -d --name api \
  --cpus 1.5 \
  --memory 512m \
  --memory-swap 512m \
  myapp:v1

# 验证限制是否生效
docker inspect api --format '{{.HostConfig.CpuShares}} {{.HostConfig.Memory}}'
```

> 💡 `--memory` 设多少，容器用超就会被 OOM 杀掉（退出码 137）。**给数据库类容器预留足够内存**，被 OOM 杀会丢数据。

---

## 六、Dockerfile：构建自己的镜像

> 💻 实操：50 分钟。这是最核心的实操章，写完后你就能把任意 Python 项目变成镜像。

### 6.1 第一个 Dockerfile

新建一个目录，放一个最简单的 Python 脚本：

```
myapp/
├── Dockerfile
└── app.py
```

`app.py`：

```python
print("Hello from Docker!")
```

`Dockerfile`：

```dockerfile
# 用什么基础镜像
FROM python:3.11-slim

# 工作目录（不存在会自动创建）
WORKDIR /app

# 把当前目录的 app.py 复制进镜像
COPY app.py .

# 容器启动时执行的命令
CMD ["python", "app.py"]
```

构建并运行：

```bash
cd myapp
docker build -t hello-app:v1 .
docker run --rm hello-app:v1
# 输出：Hello from Docker!
```

`docker build -t hello-app:v1 .` 末尾的 `.` 是**构建上下文**，指"把当前目录打包发给守护进程"。这个目录里的文件才能被 `COPY`。

### 6.2 指令逐条详解

| 指令 | 作用 | 示例 |
|------|------|------|
| `FROM` | 指定基础镜像（**必须是第一行**） | `FROM python:3.11-slim` |
| `LABEL` | 元信息（作者、版本、描述） | `LABEL version="1.0"` |
| `ENV` | 设置环境变量（构建和运行都生效） | `ENV PYTHONUNBUFFERED=1` |
| `WORKDIR` | 切换工作目录（没有则创建） | `WORKDIR /app` |
| `COPY` | 复制文件进镜像 | `COPY requirements.txt .` |
| `ADD` | 复制+解压 tar+支持 URL（少用） | `ADD app.tar.gz /app/` |
| `RUN` | **构建时**执行命令 | `RUN pip install -r requirements.txt` |
| `EXPOSE` | 声明容器要监听的端口（文档性质） | `EXPOSE 8000` |
| `USER` | 切换运行用户（安全关键） | `USER appuser` |
| `ARG` | 构建参数（仅在构建时存在） | `ARG VERSION=1.0` |
| `VOLUME` | 声明挂载点 | `VOLUME /data` |
| `CMD` | 启动时的默认命令（可被覆盖） | `CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]` |
| `ENTRYPOINT` | 入口命令（不可被轻易覆盖） | `ENTRYPOINT ["python"]` |
| `HEALTHCHECK` | 健康检查 | `HEALTHCHECK CMD curl -f http://localhost:8000/health` |

### 6.3 CMD 与 ENTRYPOINT：最重要的区别

**CMD** 是默认命令，`docker run` 后面跟的东西会**替换**它；**ENTRYPOINT** 是固定入口，`docker run` 的参数会**追加**给它。两者常配合使用：

```dockerfile
FROM ubuntu:22.04
CMD ["echo", "hello"]
# docker run ubuntu         → hello
# docker run ubuntu echo hi → hi（CMD 被替换）
```

```dockerfile
FROM ubuntu:22.04
ENTRYPOINT ["echo", "hello"]
# docker run ubuntu        → hello
# docker run ubuntu world  → hello world（参数追加）
```

```dockerfile
FROM ubuntu:22.04
ENTRYPOINT ["echo", "hello"]     # 固定命令
CMD ["world"]                    # 默认参数
# docker run ubuntu        → hello world
# docker run ubuntu docker → hello docker
```

| 场景 | 用谁 |
|------|------|
| 服务启动命令 | `CMD` |
| 固定不可改的入口（如 `python` 解释器） | `ENTRYPOINT` |
| 镜像像"命令行工具"一样用 | `ENTRYPOINT` + `CMD` 组合 |

### 6.4 exec 形式 vs shell 形式

```dockerfile
# exec 形式（推荐）：JSON 数组，每个元素一个参数，不做 shell 解析
CMD ["python", "app.py"]

# shell 形式：交给 /bin/sh -c 执行，支持管道、变量
CMD python app.py
```

区别：

```dockerfile
# 下面这条 exec 形式会失败：没有 shell 解释 > 符号
CMD ["echo", "a > b.txt"]
# 正确做法：显式用 shell
CMD ["sh", "-c", "echo a > b.txt"]
# 或直接用 shell 形式
CMD echo a > b.txt
```

> 💡 实际工作中 exec 形式能保证信号正确传递（Ctrl+C 能优雅退出），**服务类镜像一律用 exec 形式**。

### 6.5 .dockerignore

构建上下文里不该进镜像的东西，用 `.dockerignore` 排除（类似 `.gitignore`）：

```
# myapp/.dockerignore
__pycache__/
*.pyc
*.pyo
.git/
.vscode/
.idea/
*.log
venv/
.env
```

作用：① 镜像变小；② 构建更快；③ 防止把 `.env`、密钥拷进镜像。

### 6.6 docker build 常用参数

```bash
docker build -t myapp:v1 .                            # 基本构建
docker build -t myapp:v1 -f ./backend/Dockerfile ./backend   # 指定 Dockerfile 和上下文
docker build --build-arg VERSION=2.0 -t myapp:v2 .            # 传构建参数
docker build --no-cache -t myapp:v1 .                         # 不用缓存（排查缓存问题）
docker build --platform linux/amd64 -t myapp:v1 .             # 指定平台（ARM 上构建 x86）
```

### 6.7 最佳实践（必背五条）

1. **不常变的东西放前面，常变的放后面**。依赖层缓存命中，改代码不用重装依赖：

```dockerfile
FROM python:3.11-slim
WORKDIR /app

# 先拷依赖清单（这部分很少变）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 最后拷代码（这部分天天变）
COPY . .
```

2. **每条 RUN 尽量合并，并清理缓存**：

```dockerfile
# 反例：层层留缓存
RUN apt-get update
RUN apt-get install -y curl
RUN rm -rf /var/lib/apt/lists/*

# 正例：一条 RUN 搞定并清理
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*
```

3. **指定基础镜像的精确版本**，不写 `latest`。
4. **不用 root 跑应用**（见 6.9 和第十三章）。
5. **能 `.dockerignore` 的一律忽略**（见 6.5）。

### 6.8 多阶段构建

多阶段构建解决一个经典矛盾：**编译阶段要的依赖多，运行阶段只需要成品**。两个 `FROM`，前一个只是"工坊"，最终镜像只保留后一个阶段的内容。

以 Python 项目为例（编译 C 扩展的场景最能体现）：

```dockerfile
# ===== 第一阶段：构建（builder）=====
FROM python:3.11-slim AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ===== 第二阶段：运行（只留成品）=====
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY app.py .
USER 1000:1000
EXPOSE 8000
CMD ["python", "app.py"]
```

多阶段构建的好处：

| 好处 | 说明 |
|------|------|
| 镜像小 | 编译工具链不会留在最终镜像 |
| 更安全 | 攻击面小（没有 gcc、make 等） |
| 结构清晰 | 一个 Dockerfile 管理"构建"和"运行"两件事 |

### 6.9 一个完整、规范的 Python 服务 Dockerfile

把 6.2 到 6.8 的所有点串起来：

```dockerfile
# myapp/Dockerfile
FROM python:3.11-slim

LABEL maintainer="you@example.com" \
      description="示例 Web 服务"

# 环境变量：不缓冲输出、不写 pyc
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# 先装依赖（利用缓存）
COPY requirements.txt .
RUN pip install -r requirements.txt

# 再拷代码
COPY . .

# 创建非 root 用户并切换
RUN useradd -m -u 1000 appuser
USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

> 💡 上面用 Python 自带 urllib 做健康检查，是因为 slim 镜像里没有 curl。如果需要 curl，在 RUN 里装上并清理，或者 `FROM python:3.11-slim` 换成带 curl 的基础镜像。

---

## 七、Docker Compose：多容器编排

> 💻 实操：45 分钟。一个真实的项目几乎不会只有一个容器，Compose 就是"多个容器的启动脚本"。

### 7.1 为什么需要 Compose

一个典型项目有数据库、缓存、后端、前端四五个服务。没有 Compose 时：

```bash
docker run -d --name db --restart=always -e MYSQL_ROOT_PASSWORD=xxx -v db_data:/var/lib/mysql mysql:8.0
docker run -d --name redis --restart=always redis:7
docker run -d --name api --restart=always -p 8000:8000 -e DB_HOST=db --link db myapp:v1
# ...环境变量一多，一条命令一百多字符，谁记得住
```

有 Compose 时：所有配置写进一个 `docker-compose.yml`，一条 `docker compose up -d` 全部拉起。

> 💡 Compose 的核心价值：**把"怎么启动整套服务"变成代码，放进 Git，别人 clone 下来一条命令就能跑。**

### 7.2 确认 compose 已安装

```bash
docker compose version
# 输出形如：Docker Compose version v2.x.x
```

> ⚠️ 老教程里写的 `docker-compose`（带横线）是独立安装的旧版命令。新版都内置为 `docker compose`（空格）。**本指南统一用 `docker compose`。**

### 7.3 第一个 compose 文件

```
myblog/
├── docker-compose.yml
└── app/
    ├── Dockerfile
    └── main.py
```

`docker-compose.yml`：

```yaml
services:
  web:
    build: ./app                # 用目录里的 Dockerfile 构建
    ports:
      - "8000:8000"
    restart: unless-stopped
```

启动：

```bash
cd myblog
docker compose up -d            # -d 后台，首次会先 build
docker compose ps
docker compose logs -f web
docker compose down
```

### 7.4 核心字段详解

| 字段 | 作用 | 示例 |
|------|------|------|
| `services` | 定义所有服务（顶层必有） | 见下 |
| `build` | 用哪个目录的 Dockerfile 构建 | `build: ./app` |
| `image` | 直接用现成镜像 | `image: mysql:8.0` |
| `container_name` | 指定容器名（不指定则自动生成） | `container_name: mydb` |
| `ports` | 端口映射 | `- "8080:80"` |
| `expose` | 只暴露给同网络容器，不映射宿主机 | `- "8000"` |
| `environment` | 环境变量 | `MYSQL_ROOT_PASSWORD: secret` |
| `env_file` | 从文件读环境变量 | `env_file: .env` |
| `volumes` | 卷或目录挂载 | `- ./data:/var/lib/mysql` |
| `networks` | 加入的网络 | `- mynet` |
| `depends_on` | 依赖关系 | 见 7.6 节 |
| `restart` | 重启策略 | `unless-stopped` |
| `command` | 覆盖镜像默认启动命令 | `command: ["uvicorn", "main:app", "--host", "0.0.0.0"]` |
| `healthcheck` | 健康检查 | 见 7.6 节 |
| `deploy.resources` | 资源限制（GPU/CPU/内存） | 见 12.6 节示例 |

一个包含多种字段的完整示例：

```yaml
services:
  api:
    build: ./backend
    container_name: blog-api
    ports:
      - "8000:8000"
    environment:
      DB_HOST: db
      DB_PORT: "5432"
    env_file:
      - ./backend/.env
    volumes:
      - ./backend:/app          # 开发时热更新
    restart: unless-stopped
```

### 7.5 环境变量与 .env 文件

Compose 有**两级**环境变量，容易混淆：

**第一级：给 compose 文件本身用的变量**，写在项目根目录的 `.env` 里，用 `${变量名}` 引用：

```bash
# myblog/.env
MYSQL_ROOT_PASSWORD=super_secret
TAG=1.2.0
```

```yaml
# docker-compose.yml 里引用
services:
  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
  web:
    image: myapp:${TAG}
```

> 💡 `.env` 文件的规矩：**永远不提交进 Git**（加入 `.gitignore`）。仓库里放一个 `.env.example` 作为模板，让别人复制成 `.env` 再填真实值。这是业界标准做法。

**第二级：传给容器里的应用用的变量**，用 `environment:` 或 `env_file:`：

```yaml
services:
  api:
    image: myapp:v1
    environment:
      DEBUG: "false"               # 直接写
    env_file:
      - ./app.env                  # 从文件读（文件内容也是 KEY=VALUE）
```

### 7.6 depends_on 与健康检查

`depends_on` 控制启动顺序，但普通写法只保证"先启动"，不保证"就绪"。MySQL 可能要 20 秒才真正能连，这时后端的连接就失败了。**正确姿势是配合健康检查**：

```yaml
services:
  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: secret
      MYSQL_DATABASE: appdb
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 5s
      timeout: 3s
      retries: 10
      start_period: 10s

  redis:
    image: redis:7-alpine
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 3s
      retries: 5

  api:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      DB_HOST: db
      REDIS_HOST: redis
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
```

```bash
# 查看健康状态：docker ps 里 Status 列会出现 (healthy) / (unhealthy)
docker ps
docker inspect api --format '{{.State.Health.Status}}'
```

| depends_on 写法 | 含义 |
|----------------|------|
| `depends_on: [db]` | 只保证 db 容器先启动 |
| `depends_on: db: {condition: service_healthy}` | 等 db 健康了才启动（推荐） |

### 7.7 compose 常用命令

```bash
docker compose up -d              # 启动（首次会构建镜像）
docker compose up -d --build      # 改了代码后重新构建再启动（开发常用）
docker compose up -d --force-recreate  # 强制重建容器

docker compose ps                 # 查看服务状态
docker compose logs -f            # 所有服务的日志（-f 实时）
docker compose logs -f api        # 只看 api 服务

docker compose exec api bash      # 进入某个服务的容器
docker compose exec db mysql -uroot -p

docker compose stop               # 停止但保留容器
docker compose start              # 再启动
docker compose restart            # 重启

docker compose down               # 停止并删除容器和网络
docker compose down -v            # 连数据卷一起删（⚠️ 数据没了）
docker compose down --rmi all     # 连镜像一起删

docker compose pull               # 更新所有镜像到最新
docker compose config             # 校验配置并渲染最终结果（调试神器）
```

### 7.8 两个常用调试技巧

**技巧一：渲染最终配置**。变量、默认值都展开给你看，写错一眼可见：

```bash
docker compose config
```

**技巧二：容器名就是网络中的主机名**。compose 里的服务之间用服务名互相访问（第九章会讲原理）：

```bash
# 在 api 容器里连 db，主机名写 "db" 而不是 IP
docker compose exec api python -c "import socket; print(socket.gethostbyname('db'))"
```

---

## 八、数据持久化：Volume 与 Bind Mount

> 📱 概念阅读 + 💻 实操：40 分钟。不持久化的容器数据，一删全没，这是新手最容易踩的坑。

### 8.1 为什么容器里的数据会丢

容器文件系统是**临时的**：容器删了，写在里面的数据跟着没。而且镜像更新、容器重建是家常便饭：

```bash
# 反例：数据写进容器，容器删了就没了
docker run -d --name pg -e POSTGRES_PASSWORD=secret postgres:16
# ...写了很多数据...
docker rm -f pg
# 数据全部消失
```

解决方案是**卷挂载**：把宿主机的一个"存储位置"挂到容器目录，容器写这个目录等于写宿主机。宿主机上的东西，容器删了也还在。

### 8.2 三种数据方案

| 方案 | 挂载位置 | 谁管理 | 典型用途 |
|------|---------|--------|---------|
| **命名卷 (named volume)** | `/var/lib/docker/volumes/<名>` | Docker | 数据库数据、跨容器共享 |
| **绑定挂载 (bind mount)** | 任意宿主机路径 | 你自己 | 开发热更新、挂配置文件 |
| **tmpfs** | 内存 | Docker | 临时数据，重启即失 |

### 8.3 命名卷（named volume）

```bash
# 创建卷
docker volume create mysql_data

# 挂载：卷名:/容器内路径
docker run -d --name mysql \
  -v mysql_data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=secret \
  mysql:8.0

# 删容器，卷还在
docker rm -f mysql
docker volume ls                    # mysql_data 还在

# 用同一个卷再起一个，旧数据全在
docker run -d --name mysql2 \
  -v mysql_data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=secret \
  mysql:8.0
```

卷管理命令：

```bash
docker volume ls
docker volume inspect mysql_data     # 看实际路径和挂载详情
docker volume rm mysql_data
docker volume prune                  # 删除所有没被使用的卷（⚠️ 小心）
```

> 💡 命名卷的好处：不用关心它存在宿主机哪个目录，Docker 管。**数据库类服务一律用命名卷。**

### 8.4 绑定挂载（bind mount）

把宿主机的一个**具体目录**挂进容器：

```bash
# 语法：宿主机绝对路径:容器路径
docker run -d --name web \
  -v /home/me/html:/usr/share/nginx/html \
  -p 8080:80 \
  nginx

# 开发时：改宿主机代码，容器内立即生效
docker run -d --name api \
  -v /home/me/myapp:/app \
  -p 8000:8000 \
  myapp:v1

# 挂单个配置文件（覆盖镜像里的默认配置）
docker run -d --name nginx \
  -v /home/me/my.conf:/etc/nginx/conf.d/my.conf \
  nginx
```

> ⚠️ bind mount 的路径**必须是绝对路径**。相对路径在 `docker run` 里不被支持（Compose 里可以用相对路径）。

### 8.5 命名卷 vs 绑定挂载

| 维度 | 命名卷 | 绑定挂载 |
|------|--------|---------|
| 宿主机路径 | Docker 管理，`/var/lib/docker/volumes/xxx` | 你指定，如 `/home/me/html` |
| 权限 | Docker 处理 | 继承宿主机目录权限（易踩坑） |
| 备份/迁移 | 要额外命令 | 直接拷目录 |
| 适合 | 数据存储（数据库、上传文件） | 开发调试、挂配置、日志目录 |
| Compose 写法 | `- db_data:/var/lib/mysql` | `- ./html:/usr/share/nginx/html` |
| 性能 | 好 | 在 macOS/Windows 上略慢 |

> 💡 记一个简单规则：**数据库和生产数据用命名卷，开发时改代码用 bind mount，临时数据用 tmpfs。**

### 8.6 备份与迁移

**备份卷**（用一个临时容器把卷打包）：

```bash
docker run --rm \
  -v mysql_data:/data \
  -v /home/me/backup:/backup \
  alpine tar czf /backup/mysql_data.tar.gz -C /data .
```

**恢复卷**：命令同上，`tar czf` 换成 `tar xzf`。宿主机与容器互拷也可以用 `docker cp mysql:/var/lib/mysql ./mysql_backup`。

> 💡 生产环境数据库备份，主流做法是数据库自带工具在容器内导出：`docker exec mysql sh -c 'exec mysqldump -uroot -p"$MYSQL_ROOT_PASSWORD" appdb' > appdb.sql`

### 8.7 Compose 中的卷

Compose 里卷的写法分两层：服务里声明"挂哪"，文件底部声明"卷存在"。

```yaml
services:
  db:
    image: mysql:8.0
    volumes:
      - db_data:/var/lib/mysql      # 命名卷
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql   # bind mount
      - ./logs:/var/log/mysql       # bind mount 目录

volumes:
  db_data:                          # 声明命名卷，具体存哪 Docker 管
```

```bash
docker compose down                 # 容器没了
docker compose up -d                # 卷还在，数据还在
docker compose down -v              # ⚠️ 卷也被删，数据没了
```

> ⚠️ **`down -v` 是危险操作**。很多人手滑执行完才发现数据库数据没了。删除卷之前一定确认有没有备份。

---

## 九、网络：bridge、host、none 与容器互联

> 📱 概念阅读 + 💻 实操：40 分钟。本章是《网络协议学习手册》第十三章的容器部分，这里展开成完整一章。

### 9.1 网络驱动总览

| 驱动 | 说明 | 典型场景 |
|------|------|----------|
| **bridge（默认）** | 容器连虚拟网桥 docker0，NAT 上网 | 单机多容器通信 |
| **host** | 容器直接用宿主机网络栈，无隔离 | 高性能、网络性能敏感 |
| **none** | 容器只有 lo，完全无网络 | 纯计算、安全隔离 |
| **custom bridge** | 自定义网桥（推荐！） | 容器名即域名，自动 DNS |
| **overlay** | 跨主机（Swarm 模式） | 多台服务器编排 |
| **macvlan/ipvlan** | 容器直接拿物理网段 IP | 容器要暴露在局域网 |

```bash
# 查看现有网络
docker network ls
```

输出一般有 `bridge`、`host`、`none` 三个内置网络。

### 9.2 bridge 模式详解（默认）

```
宿主机
┌────────────────────────────────────────────┐
│                                            │
│  docker0 (172.17.0.1/16)  ← 虚拟网桥        │
│     │           │                          │
│    veth        veth       ← 虚拟网线         │
│     │           │                          │
│  ┌──────┐   ┌──────┐                       │
│  │ 容器A  │   │ 容器B  │   ← 各自有 IP       │
│  │172.17 │   │172.17 │                     │
│  │ .0.2  │   │ .0.3  │                     │
│  └──────┘   └──────┘                       │
│                                            │
│  eth0 (192.168.1.100) ──── 物理网络         │
│       ↑                                    │
│  宿主机做 SNAT（MASQUERADE）                 │
│  容器出外网：172.17.0.2 → 192.168.1.100    │
└────────────────────────────────────────────┘

三条结论：
1. 同一网桥的容器可以互相通信（容器 A ping 容器 B 的通）
2. 容器访问外网：走 docker0 → eth0 → SNAT → 外网
3. 外网访问容器：必须端口映射 -p（iptables DNAT 规则）
```

```bash
# 看容器在默认 bridge 里的 IP
docker inspect web --format '{{.NetworkSettings.IPAddress}}'
```

**默认 bridge 的三个缺点**：
1. 不支持容器名 DNS 解析，只能靠 IP（而容器 IP 会变）。
2. 容器之间必须手动指定链接。
3. 和宿主机外其他网络隔离得不够干净。

所以实践中几乎总是**创建自定义 bridge 网络**。

### 9.3 自定义网络与容器名 DNS

```bash
# 创建自定义网络
docker network create my-net

# 把容器加进去
docker run -d --name web --network my-net nginx
docker run -d --name app --network my-net myapp:v1

# 在 app 容器里直接 ping web（自定义网络自动 DNS）
# 注意：python:3.11-slim / nginx 等镜像不带 ping 命令，改用 alpine（自带 busybox ping）验证：
docker run --rm --network my-net alpine ping -c2 web
# 输出：PING web (172.19.0.2) ...（自动解析到 IP）

# 连接已有的容器进网络
docker network connect my-net some-container

# 断开
docker network disconnect my-net web

# 网络详情
docker network inspect my-net
```

> 💡 **记住这一条**：同一自定义网络里的容器，**容器名就是主机名**。后端连数据库写 `db`、连缓存写 `redis`，不用管 IP。这正是 Compose 里服务互相访问的基础（第七章 7.8 节）。

### 9.4 端口映射原理

```
外网客户端
    │ 请求 服务器:8080
    ↓
宿主机 eth0 监听 8080
    │ iptables DNAT：8080 → 容器 172.19.0.2:80
    ↓
容器内应用监听 80
```

```bash
# 端口映射三种绑定方式
docker run -p 8080:80 nginx                 # 所有网卡，0.0.0.0:8080
docker run -p 127.0.0.1:8080:80 nginx       # 只本机，外部访问不到（安全）
docker run -p 8080:80/udp coredns/coredns   # UDP

# 查看映射
docker port web
```

> ⚠️ **只有做了端口映射，宿主机才能访问容器。** "我容器里明明监听 80，宿主机怎么访问不到？"十有八九是没加 `-p` 或绑到了 127.0.0.1。

### 9.5 host 和 none 模式

**host 模式**：容器不虚拟网络，直接用宿主机网络栈，性能最好。代价是**端口直接冲突**，宿主机 80 被占用就起不来，且 `-p` 参数失效：

```bash
docker run -d --network host --name myapp myapp:v1
```

**none 模式**：容器只有 lo 回环接口，完全没网。适合纯计算任务、安全隔离的批处理：

```bash
docker run --rm --network none alpine sh -c "ip addr"
```

### 9.6 网络命令汇总

```bash
docker network ls                          # 列表
docker network create my-net               # 创建（可加 --subnet=172.20.0.0/16 指定子网）
docker network connect my-net c1           # 容器加入网络
docker network disconnect my-net c1        # 容器退出网络
docker network inspect my-net              # 详情（看有哪些容器）
docker network rm my-net                   # 删除（先断开容器）
docker network prune                       # 清理无人用的网络
```

### 9.7 网络常见问题速查

| 问题 | 原因 | 解决 |
|------|------|------|
| 容器间 ping 不通 | 不在同一网络 | `docker network connect` 到同一网络 |
| 容器名解析不了 | 用了默认 bridge | 创建自定义网络 |
| 宿主机访问不了容器 | 没做端口映射 | `-p` 或 `docker port` 查看 |
| 容器访问不了宿主机服务 | 服务监听在 127.0.0.1 | 服务监听 `0.0.0.0`，或用 `host.docker.internal`（Docker Desktop） |
| 容器出不了外网 | ip_forward 未开启 | `sysctl net.ipv4.ip_forward` 应为 1 |
| compose 服务间不通 | 跨 compose 文件没共享网络 | 定义 `external` 网络共享 |

---

## 十、实战一：MySQL + Redis + 后端 API 一键启动

> 💻 实操：60 分钟。这是全栈 DevOps 阶段"一键部署"的迷你版，做完你就掌握了 compose 的核心用法。

### 10.1 项目结构

```
fullstack-demo/
├── docker-compose.yml
├── .env
└── backend/
    ├── Dockerfile
    ├── requirements.txt
    └── main.py
```

### 10.2 后端代码

`backend/main.py`：一个能分别探测 MySQL 和 Redis 连接的小 API。

```python
import os

import pymysql
import redis
from fastapi import FastAPI

app = FastAPI(title="Fullstack Demo")

DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "apppass")
DB_NAME = os.getenv("DB_NAME", "appdb")
REDIS_HOST = os.getenv("REDIS_HOST", "redis")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/db")
def check_db():
    conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
    )
    with conn.cursor() as cur:
        cur.execute("SELECT 1")
        result = cur.fetchone()
    conn.close()
    return {"mysql": result[0]}


@app.get("/redis")
def check_redis():
    r = redis.Redis(host=REDIS_HOST, port=6379, db=0, socket_timeout=3)
    return {"redis": r.ping()}
```

`backend/requirements.txt`：

```
fastapi==0.115.0
uvicorn==0.30.6
pymysql==1.1.1
redis==5.0.8
```

### 10.3 后端 Dockerfile

```dockerfile
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .

USER 1000:1000

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 10.4 compose 文件

`.env`（不提交 Git）：

```
MYSQL_ROOT_PASSWORD=root_secret
MYSQL_DATABASE=appdb
MYSQL_USER=appuser
MYSQL_PASSWORD=apppass
```

`docker-compose.yml`：

```yaml
services:
  db:
    image: mysql:8.0
    restart: unless-stopped
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: ${MYSQL_DATABASE}
      MYSQL_USER: ${MYSQL_USER}
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
    volumes:
      - db_data:/var/lib/mysql
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 5s
      timeout: 3s
      retries: 10
      start_period: 10s

  redis:
    image: redis:7-alpine
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 3s
      retries: 5

  api:
    build: ./backend
    restart: unless-stopped
    ports:
      - "8000:8000"
    environment:
      DB_HOST: db
      DB_USER: ${MYSQL_USER}
      DB_PASSWORD: ${MYSQL_PASSWORD}
      DB_NAME: ${MYSQL_DATABASE}
      REDIS_HOST: redis
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy

volumes:
  db_data:
```

### 10.5 启动与验证

```bash
cd fullstack-demo
docker compose up -d --build

# 1. 看状态（三个都应是 Up，db/redis 显示 healthy）
docker compose ps

# 2. 验证 API 和两个依赖（compose 保证 db 健康后才启动 api）
curl http://localhost:8000/health    # {"status":"ok"}
curl http://localhost:8000/db        # {"mysql":1}
curl http://localhost:8000/redis     # {"redis":true}

# 3. 数据持久化验证：容器删了数据还在
docker compose down
docker compose up -d
curl http://localhost:8000/db        # 仍然正常

# 4. 看日志
docker compose logs -f api
```

### 10.6 复盘：这个例子用到了哪些知识

| 知识点 | 用在哪 |
|--------|--------|
| 环境变量 | `.env` + `${VAR}` + `environment:` |
| 健康检查 | db/redis 的 `healthcheck` |
| 启动顺序 | `depends_on` + `condition: service_healthy` |
| 数据持久化 | `db_data` 命名卷 |
| 容器互联 | API 里主机名写 `db`、`redis` |
| 端口映射 | `8000:8000` |
| 镜像构建 | `build: ./backend` |

> 💡 做完这一步，你其实已经掌握了"博客项目一键部署"里 API + DB + Redis 的部分。加一个前端和 Nginx 就是全栈 DevOps 阶段的完整实战，只是多加两个 service 而已。

---

## 十一、实战二：Dify 部署（对接大模型阶段二）

> 💻 实操：40 分钟。阶段二要在 Dify 上搭智能体，官方推荐 Docker 部署，这里把每一步讲透。

### 11.1 Dify 是什么

Dify 是一个开源的大模型应用开发平台：可视化编排工作流、管理知识库、接入各类模型，最后生成带 API 的应用。它自己由多个组件组成，所以用 Docker Compose 部署是最标准的姿势。

### 11.2 前置条件

| 条件 | 要求 | 检查命令 |
|------|------|---------|
| Docker + Compose | 已装好 | `docker compose version` |
| 内存 | 建议 4GB 以上 | `free -h` |
| 磁盘 | 建议 20GB 以上 | `df -h /` |
| 端口 | 80、443 空闲 | `ss -tulnp \| grep -E ':80|:443'` |

> ⚠️ 如果 80 端口被占用（比如 Nginx 已经在跑），可以改 `.env` 里的映射端口，见 11.5 节。

### 11.3 下载与配置

```bash
# 1. 克隆官方仓库
git clone https://github.com/langgenius/dify.git
cd dify/docker

# 2. 创建配置文件（.env.example 是模板）
cp .env.example .env

# 3. 查看关键配置（这一步必做）
grep -E 'SECRET_KEY|POSTGRES_PASSWORD|OPENAI' .env
```

`.env` 里至少要看这几个：

| 配置项 | 说明 |
|--------|------|
| `SECRET_KEY` | 应用加密密钥，**必须改成自己的随机串** |
| `POSTGRES_PASSWORD` | 数据库密码 |
| `EXPOSE_NGINX_PORT` / `EXPOSE_NGINX_SSL_PORT` | 对外端口（默认 80/443） |
| `VECTOR_STORE` | 向量数据库类型（默认 weaviate） |

生成随机密钥：

```bash
openssl rand -base64 42
# 把输出填到 .env 的 SECRET_KEY=
```

### 11.4 启动

```bash
# 后台启动全部组件（首次会拉取镜像，耗时取决于网络）
docker compose up -d

# 等待就绪：docker compose ps 期望看到 api、worker、web、db、redis、
# sandbox、ssrf_proxy、weaviate 等服务都起来
docker compose ps
# 追踪日志，看到 "Application startup complete" 就是起来了
docker compose logs -f api
```

> 💡 镜像拉取很慢就先配置镜像加速（第十四章 14.3 节）再执行上面的命令。

### 11.5 首次访问

```bash
# 浏览器打开（默认端口 80）
# 本机：http://localhost
# 服务器：http://服务器IP

# 如果 80 被占用，改 .env 里的端口后重启：
#   EXPOSE_NGINX_PORT=8080
# 然后访问 http://localhost:8080
docker compose down
docker compose up -d
```

首次打开会进入**初始化页面**：

1. 设置管理员账号密码（邮箱 + 密码）。
2. 进入"设置 → 模型供应商"，配置模型。接入 OpenAI/DeepSeek 等，填入 API Key。
3. 在"工作室"里创建应用（对话型或文本生成型），上传文档建知识库，设计工作流。

阶段二的完整流程（在 Dify 里创建应用、调用 API）见《01-总纲-6个月大模型学习计划.md》阶段二部分，那里有 Dify API 调用示例。

### 11.6 Dify 的常用运维命令

```bash
# 更新 Dify 到新版本
git pull
docker compose down
docker compose pull
docker compose up -d

# 查看所有日志
docker compose logs -f --tail 100

# 只重启 api
docker compose restart api

# 完整停止并保留数据
docker compose down
# 数据在命名卷里，下次 up 还在

# 彻底重置（⚠️ 删所有数据）
docker compose down -v
```

> 💡 **备份 Dify 数据**：关键数据在 Postgres（用户、应用、工作流）和向量库（知识库）的卷里，用第八章 8.6 节的备份方法定期打包卷即可。

---

## 十二、实战三：GPU 容器与 vLLM 部署（对接大模型阶段五）

> 💻 实操：60 分钟（需要一台带 NVIDIA GPU 的机器）。阶段五要把微调好的模型部署成 OpenAI 兼容的 API，本章讲透 GPU 容器。

### 12.1 前置条件

| 条件 | 要求 | 检查命令 |
|------|------|---------|
| NVIDIA 显卡 | 驱动已装好 | `nvidia-smi`（在宿主机能跑） |
| Docker | 已装好 | `docker --version` |
| 磁盘 | 模型 + CUDA 镜像，预留 30GB+ | `df -h /` |
| 内存 | 建议 16GB+ | `free -h` |

> 💡 AutoDL 等 GPU 云主机通常已预装 NVIDIA 驱动和 Docker，直接跳到 12.2 节。**判断标准只有一条：宿主机上 `nvidia-smi` 能输出显卡信息。**

### 12.2 安装 nvidia-container-toolkit

Docker 默认无法让容器访问 GPU，需要装 NVIDIA 的容器运行时插件。

**Ubuntu / Debian**：

```bash
# 1. 添加 NVIDIA 的 apt 源
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | \
  sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg

curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

# 2. 安装
sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit

# 3. 让 Docker 使用 NVIDIA 运行时
sudo nvidia-ctk runtime configure --runtime=docker

# 4. 重启 Docker
sudo systemctl restart docker
```

> 💡 如果上面的源访问不了，也可以直接下载 deb 包安装：去 `https://github.com/NVIDIA/nvidia-container-toolkit/releases` 找 `.deb` 包，`sudo dpkg -i` 装上，再执行步骤 3 和 4。

### 12.3 验证 GPU 容器

```bash
# 用一个带 CUDA 的小镜像测试：容器里能跑 nvidia-smi 就成功
docker run --rm --gpus all nvidia/cuda:12.4.1-base-ubuntu22.04 nvidia-smi

# 看到显卡信息（和宿主机一致）就说明 GPU 透传成功
```

常见错误排查：

| 报错 | 原因 | 解决 |
|------|------|------|
| `could not select device driver "" with capabilities: [[gpu]]` | 插件没装或没配置 | 重做 12.2 的步骤 3 和 4 |
| `nvidia-smi: not found` | 镜像里没有驱动工具 | 正常现象，CUDA base 镜像自带 |

> 💡 **容器里不需要装驱动**，容器用的驱动来自宿主机。驱动版本太旧会导致 CUDA 版本不兼容，规则：**镜像 CUDA 版本 ≤ 驱动支持的 CUDA 版本**。驱动过老就升级驱动。

### 12.4 运行 vLLM 推理服务

vLLM 官方提供现成的 OpenAI 兼容镜像 `vllm/vllm-openai`，把模型路径传进去即可。两种方式选一种：

```bash
# 方式一：让容器自己下载模型（模型自动存到 HuggingFace 缓存目录）
docker run --gpus all -p 8000:8000 --ipc=host --restart=unless-stopped \
  --name vllm \
  -v ~/.cache/huggingface:/root/.cache/huggingface \
  vllm/vllm-openai:latest \
  --model Qwen/Qwen2.5-7B-Instruct --max-model-len 8192 --gpu-memory-utilization 0.9

# 方式二：挂载本地模型目录（阶段五微调好的模型推荐，先本地下载到 ~/models/）
docker run --gpus all -p 8000:8000 --ipc=host \
  --name vllm \
  -v ~/models:/models \
  vllm/vllm-openai:latest \
  --model /models/Qwen2.5-7B-Instruct --host 0.0.0.0 --port 8000
```

> 💡 常用参数含义：`--model` 模型名或路径；`--max-model-len` 最大上下文长度，显存小就调小；`--gpu-memory-utilization` 显存使用上限（0.9 = 90%）；`--ipc=host` 共享内存，vLLM 官方推荐。完整参数见 `docker run --rm vllm/vllm-openai:latest --help`。

### 12.5 测试 OpenAI 兼容接口

vLLM 启动成功后，它在 8000 端口提供 OpenAI 格式的接口：

```bash
# 查看模型列表
curl http://localhost:8000/v1/models

# 发一个对话请求
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "/models/Qwen2.5-7B-Instruct",
    "messages": [{"role": "user", "content": "用一句话介绍 Docker"}],
    "max_tokens": 200
  }'
```

用 Python 调用（阶段五 FastAPI 封装的底座就是它）：

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")

resp = client.chat.completions.create(
    model="/models/Qwen2.5-7B-Instruct",
    messages=[{"role": "user", "content": "你好"}],
)
print(resp.choices[0].message.content)
```

### 12.6 自定义 vLLM 服务：Dockerfile + Compose

阶段五要求"FastAPI 封装 + Docker 打包"。标准做法是：vLLM 做推理引擎，FastAPI 做业务网关。

**Dockerfile**（给自己的微调模型封装一个推理镜像）：

```dockerfile
FROM vllm/vllm-openai:latest

# 把本地模型打进镜像（模型大，也可以运行时挂载）
COPY models/ /models/

EXPOSE 8000

# 默认启动命令；也可以覆盖
CMD ["--model", "/models/Qwen2.5-7B-Instruct", "--host", "0.0.0.0", "--port", "8000"]
```

**docker-compose.yml**（vLLM + FastAPI 网关）：

```yaml
services:
  vllm:
    image: vllm/vllm-openai:latest
    command:
      - --model
      - /models/Qwen2.5-7B-Instruct
      - --host
      - 0.0.0.0
      - --port
      - "8000"
    ports:
      - "8000:8000"
    volumes:
      - ~/models:/models
    ipc: host
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]

  gateway:
    build: ./gateway            # 你的 FastAPI 封装服务
    ports:
      - "9000:9000"
    environment:
      VLLM_URL: http://vllm:8000/v1
    depends_on:
      - vllm
```

`gateway` 的 FastAPI 代码（阶段五总纲里 FastAPI 封装的完整版）：

```python
# gateway/main.py
import os

import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
VLLM_URL = os.getenv("VLLM_URL", "http://vllm:8000/v1")


class GenerateRequest(BaseModel):
    prompt: str
    max_tokens: int = 256
    temperature: float = 0.7


@app.post("/generate")
def generate(req: GenerateRequest):
    resp = requests.post(
        f"{VLLM_URL}/completions",
        json={"model": "/models/Qwen2.5-7B-Instruct", **req.model_dump()},
    )
    return resp.json()
```

### 12.7 GPU 分配与资源限制

```bash
docker run --gpus '"device=0"' ...           # 只用第 0 块 GPU
docker run --gpus '"device=0,1"' ...         # 用 0、1 两块
docker exec vllm nvidia-smi                  # 容器内看可用显存
docker run -d --gpus all --cpus 8 --memory 16g ...   # 同时限制 CPU/内存
```

### 12.8 注意事项汇总

| 事项 | 说明 |
|------|------|
| 显存不够 | 换更小的模型、调低 `--max-model-len` 和 `--gpu-memory-utilization` |
| 模型下载慢 | 提前用 `huggingface-cli download` 下到本地再挂载 |
| 驱动太旧 | 升级 NVIDIA 驱动；镜像 CUDA 版本别超过驱动支持的 |
| 别在容器里装驱动 | 容器用的是宿主驱动，装也没用 |
| 大模型镜像别用 alpine | 需要 glibc 和 CUDA 运行库 |
| 多卡机器 | 用 `--tensor-parallel-size N` 开张量并行 |

> 💡 吞吐量测试（阶段五要求）：vLLM 自带 `benchmark_serving.py`，也可以在宿主机用 `hey`、`ab` 之类工具打并发，对比不同并发下的 tokens/s。

---

## 十三、镜像瘦身与安全

> 📱 概念阅读 + 💻 实操：40 分钟。镜像越小，构建越快、拉取越快、攻击面越小。

### 13.1 镜像为什么越来越大

镜像每层都会保留文件。常见的膨胀来源：

| 来源 | 例子 |
|------|------|
| 无用的包管理器缓存 | apt、pip、npm 的下载缓存 |
| 编译工具链 | gcc、make 在运行时根本不需要 |
| 调试文件 | .pyc、源码里的注释、测试文件 |
| 不必要的系统包 | 跑 Python 不需要 vim、curl（除非健康检查用） |
| 敏感文件 | .env、密钥、日志误拷进镜像 |

### 13.2 选择小基础镜像

| 基础镜像 | 大小 | 说明 |
|---------|------|------|
| `python:3.11` | ~1GB | Debian 全家桶，最大 |
| `python:3.11-slim` | ~120MB | 精简 Debian，最常用 |
| `python:3.11-alpine` | ~50MB | 基于 Alpine，极简（注意 glibc 兼容问题） |
| `nvidia/cuda:12.4.1-base-ubuntu22.04` | ~200MB | GPU 场景的基础 |
| `gcr.io/distroless/...` | 极小 | 无 shell、无包管理器，极致安全 |

> ⚠️ Alpine 的坑：它用 musl 而不是 glibc，有些 Python 库（尤其带 C 扩展的）要额外编译。**遇到奇怪问题就换回 slim**。本仓库项目默认推荐 `-slim` 系列。

### 13.3 层缓存原理（为什么顺序重要）

每一条 `RUN`、`COPY` 指令生成一层。构建时如果某层没变，直接用缓存，后面的层才重新执行。

```dockerfile
# 反例：代码一变，pip install 全部重跑
FROM python:3.11-slim
COPY . /app              # 代码天天变 → 这层缓存天天失效
RUN pip install -r /app/requirements.txt

# 正例：依赖先装，代码后拷
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .  # 依赖清单很少变 → 命中缓存
RUN pip install -r requirements.txt
COPY . .                 # 代码变只重跑这一层
```

```bash
# 想看每一层用了多久、是否命中缓存
docker build --progress=plain -t myapp:v1 . 2>&1 | grep CACHED
```

### 13.4 合并 RUN 并清理

```dockerfile
# 正例：一条 RUN 完成"安装 + 清理"
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# pip 清理
RUN pip install --no-cache-dir -r requirements.txt
```

### 13.5 多阶段构建瘦身（实战）

第六章 6.8 节就是多阶段构建。再给一个 Go 例子：编译阶段带工具链，运行阶段只用 `scratch` 空镜像装一个二进制，最终镜像只有几 MB：

```dockerfile
FROM golang:1.22 AS builder
COPY . /src
RUN cd /src && CGO_ENABLED=0 go build -o /bin/app .

FROM scratch
COPY --from=builder /bin/app /app
ENTRYPOINT ["/app"]
```

> 💡 Python 项目用 slim + 多阶段即可；`scratch` 没有解释器，不适合 Python。

### 13.6 非 root 用户（安全关键）

容器里默认是 root。一旦容器被攻破，攻击者就是 root 权限，而 Docker 的 root 与宿主机权限关系紧密。**生产镜像必须用非 root 运行**：

```dockerfile
FROM python:3.11-slim
WORKDIR /app

# 创建普通用户（-m 建家目录，-u 固定 UID）
RUN useradd -m -u 1000 appuser

COPY --chown=appuser:appuser . .

USER appuser

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

> 💡 注意：非 root 用户对挂载的目录可能没有写权限（bind mount 目录的权限来自宿主机）。遇到 Permission denied 时用 `-v` 挂一个用户可写的目录，或用 `-u 1000:1000` 运行容器。

### 13.7 不要在镜像里放密钥

| 错误做法 | 正确做法 |
|---------|---------|
| 把 API Key 写死在代码里 | 用环境变量传入 |
| `ENV DATABASE_URL=postgres://user:pass@...` | 运行时 `-e` 或 `--env-file` 传入 |
| 把 `.env` COPY 进镜像 | `.dockerignore` 排除 |
| 用 ARG 传密码（会留在镜像历史里） | 用 BuildKit 的 `--mount=type=secret` |

BuildKit 秘密挂载（Docker 23+ 默认开启）：

```dockerfile
# Dockerfile
RUN --mount=type=secret,id=pip_cred \
    pip install -r requirements.txt
```

```bash
docker build --secret id=pip_cred,src=~/.pip-credential.txt -t myapp:v1 .
```

### 13.8 用 .dockerignore 拦住杂鱼

第六章 6.5 节给过模板，再次强调：`.env`、`.git/`、`__pycache__/`、日志、本地数据库文件，全都要 ignore。这既瘦身又防泄密。

### 13.9 镜像扫描

```bash
# Docker Scout（新版内置）
docker scout quickview nginx:1.25

# 或开源工具 Trivy（安装：snap install trivy 或下载二进制）
trivy image nginx:1.25
trivy image --severity HIGH,CRITICAL myapp:v1
```

扫描能列出镜像里的已知漏洞（CVE）。**生产镜像上线前扫一遍**，高危漏洞要处理。

### 13.10 清理磁盘垃圾

```bash
docker system df                      # 看空间都去哪了
docker system prune                   # 清悬空镜像、停止的容器、无用网络
docker system prune -a                # ⚠️ 连未使用的镜像都删（拉回来要花流量）
docker builder prune                  # 清构建缓存
docker volume prune                   # 清无人使用的卷（⚠️ 数据没了）

# 全家桶（慎用）
docker system prune -af
```

> 💡 常用组合：`docker system df` 检查，`docker image prune` 清悬空镜像，`docker builder prune` 清构建缓存。这三步基本够用，别动不动 `-a -f` 全删。

---

## 十四、常用排错指南

> 💻 实操：30 分钟。本章的每一条都是真实生产里天天遇到的。记住**方法论：先看状态，再看日志，最后看配置。**

### 14.1 端口被占用

**报错**：

```
docker: Error response from daemon: driver failed programming external connectivity
on endpoint web: Bind for 0.0.0.0:8080 failed: port is already allocated
```

**排查与解决**：

```bash
ss -tulnp | grep 8080                    # 看是谁占了端口
docker ps | grep 8080                    # 如果是别的容器占了
docker run -d -p 8081:80 --name web nginx   # 换宿主端口（容器内端口不用改）
```

### 14.2 容器启动即退出

**现象**：`docker run` 一执行，容器立刻变 `Exited`。

**第一步永远是看日志**：

```bash
docker ps -a                      # 看到 Exited (退出码) 状态
docker logs <容器名>               # 看退出的原因
```

**常见原因对照**：

| 退出码 | 常见原因 | 处理 |
|--------|---------|------|
| `Exited (0)` | 正常退出：命令执行完 | 服务类进程别用会退出的命令；检查 CMD |
| `Exited (1)` | 应用报错 | 看日志定位 |
| `Exited (127)` | 命令不存在 | CMD 写错了，镜像里没这个命令 |
| `Exited (137)` | 被 OOM 杀掉 | 加内存限制或换大机器 |
| `Exited (2)` | 参数或语法错误 | 看启动参数 |

**典型场景：启动命令被后台化**（`&` 或 nohup 导致主进程秒退）：

```dockerfile
CMD nohup python app.py &     # 反例：主进程退出，容器跟着退出
CMD ["python", "app.py"]      # 正例：服务必须前台运行
```

> 💡 记住：**容器的主进程是前台进程**。主进程退出，容器就退出。用 `&` 后台化是容器新手第一坑。

### 14.3 镜像拉取慢或失败

**现象**：`docker pull` 卡住不动、超时、`dial tcp ... i/o timeout`。

**解决：配置镜像加速器**。

Linux：

```bash
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<'EOF'
{
  "registry-mirrors": [
    "https://docker.m.daocloud.io"
  ]
}
EOF
sudo systemctl restart docker
docker info | grep -A5 "Registry Mirrors"    # 验证生效
```

Docker Desktop：设置 → Docker Engine，改 JSON 后 Apply & Restart。

> ⚠️ 公共加速器的可用性经常变化，上面的地址可能失效。失效就搜"docker 镜像加速"找当前可用的，或直接配置代理。另一个思路：很多云厂商（阿里云/腾讯云）提供免费的专属加速地址，登录控制台看"容器镜像服务"。

```bash
# 拉取失败后重试的姿势
docker pull nginx:1.25            # 直接重试（中断的会续传）
```

### 14.4 权限问题

| 报错 | 原因 | 解决 |
|------|------|------|
| `Got permission denied ... Docker daemon socket` | 用户不在 docker 组 | `sudo usermod -aG docker $USER` 后重新登录 |
| `Mounts denied` | Docker Desktop 未共享该目录 | 设置 → File Sharing 加上该目录 |
| 容器内 `PermissionError: [Errno 13]` | bind mount 目录权限继承宿主机 | 检查宿主机权限，或 `-u 1000:1000` 匹配宿主机用户 |

### 14.5 容器内网络不通

**容器里上不了网**：

```bash
sysctl net.ipv4.ip_forward        # 应为 1，为 0 则 echo 1 > /proc/sys/net/ipv4/ip_forward
docker exec <容器> cat /etc/resolv.conf          # 检查容器内 DNS 配置
docker run --dns 8.8.8.8 --rm alpine ping -c2 baidu.com   # 手动指定 DNS 测试
```

**容器连不上宿主机服务**：宿主机服务必须监听 `0.0.0.0`（不能只监听 127.0.0.1）；Docker Desktop 用 `host.docker.internal` 代替 localhost：

```bash
docker run --rm alpine sh -c "wget -qO- http://host.docker.internal:8080/health"
```

### 14.6 磁盘空间爆了

```bash
# 1. 看空间
df -h /
docker system df

# 2. 定位大头：镜像/容器/卷/构建缓存
docker system df -v

# 3. 清理（从温和到激进）
docker image prune
docker builder prune
docker system prune -a
docker system prune -af
```

> 💡 构建缓存是大户，很多人镜像删光了空间还满，一查是 `builder prune` 没做。

### 14.7 时区问题

容器默认 UTC 时间，日志时间对不上中国时间：

```bash
# 运行容器时指定
docker run -e TZ=Asia/Shanghai ...

# compose 里
environment:
  TZ: Asia/Shanghai
```

### 14.8 排错方法论总结

```
容器出问题 → 三步走
  Step 1: docker ps -a        看状态（Running/Exited/Restarting）
  Step 2: docker logs <名>    看日志（99% 的问题在这里暴露）
  Step 3: docker inspect <名> 看配置（网络/挂载/环境变量对不对）

再不行 → 加 verbosity
  docker run 时去掉 -d 前台跑，直接看报错
  docker logs --tail 100 -f <名> 实时盯
  curl 一下健康检查端点

还是不行 → 还原现场
  换个干净镜像跑一遍（排除应用问题）
  docker compose config 检查 compose 渲染结果
  把报错原文 + docker version 贴到搜索引擎/社区
```

---

## 十五、命令速查表

> 💻 打印出来贴在显示器边上，或存手机里随时翻。

### 镜像

| 场景 | 命令 |
|------|------|
| 拉镜像 | `docker pull nginx:1.25` |
| 看本地镜像 | `docker images` |
| 打标签 | `docker tag nginx:1.25 myname/nginx:prod` |
| 删镜像 | `docker rmi nginx:1.25` |
| 清悬空镜像 | `docker image prune` |
| 看分层历史 | `docker history nginx:1.25` |
| 搜索 | `docker search mysql` |
| 登录仓库 | `docker login` |
| 推镜像 | `docker push myname/nginx:prod` |

### 容器

| 场景 | 命令 |
|------|------|
| 后台运行 | `docker run -d --name web -p 8080:80 nginx` |
| 交互进入 | `docker run -it --rm ubuntu:22.04 bash` |
| 看运行中 | `docker ps` |
| 看全部 | `docker ps -a` |
| 日志 | `docker logs -f --tail 100 web` |
| 进入容器 | `docker exec -it web bash` |
| 执行单命令 | `docker exec web ls /etc` |
| 停止/启动/重启 | `docker stop web` / `docker start web` / `docker restart web` |
| 删除 | `docker rm -f web` |
| 删所有容器 | `docker rm $(docker ps -aq)` |
| 详细信息 | `docker inspect web` |
| 资源占用 | `docker stats` |
| 拷文件 | `docker cp web:/app/x.log ./x.log` |
| 环境变量 | `docker exec web env` |

### 网络

| 场景 | 命令 |
|------|------|
| 列网络 | `docker network ls` |
| 建网络 | `docker network create my-net` |
| 指定网络运行 | `docker run --network my-net ...` |
| 容器入网 | `docker network connect my-net web` |
| 看映射端口 | `docker port web` |
| 容器 IP | `docker inspect web --format '{{.NetworkSettings.IPAddress}}'` |

### 数据卷

| 场景 | 命令 |
|------|------|
| 建卷 | `docker volume create mydata` |
| 挂卷运行 | `docker run -v mydata:/var/lib/mysql ...` |
| 绑定目录 | `docker run -v /host/path:/container/path ...` |
| 列卷 | `docker volume ls` |
| 清无用卷 | `docker volume prune` |

### Compose

| 场景 | 命令 |
|------|------|
| 启动 | `docker compose up -d` |
| 重建启动 | `docker compose up -d --build` |
| 看状态 | `docker compose ps` |
| 看日志 | `docker compose logs -f` |
| 进容器 | `docker compose exec api bash` |
| 停止 | `docker compose stop` |
| 关闭删容器 | `docker compose down` |
| 关闭连数据删 | `docker compose down -v` ⚠️ |
| 校验配置 | `docker compose config` |

### 构建与清理

| 场景 | 命令 |
|------|------|
| 构建 | `docker build -t myapp:v1 .` |
| 无缓存构建 | `docker build --no-cache -t myapp:v1 .` |
| 传构建参数 | `docker build --build-arg VERSION=2.0 -t myapp:v2 .` |
| 空间总览 | `docker system df` |
| 温和清理 | `docker system prune` |
| 彻底清理 | `docker system prune -af` ⚠️ |
| 清构建缓存 | `docker builder prune` |

---

## 十六、章节练习

> 💻 练习：约 3 小时。学完不练等于白学，每道题都对应正文里的一个知识点。做完再对答案思考。

### 基础题（每题 5 分钟）

1. 用自己的话解释：镜像、容器、仓库、守护进程四者的关系。
2. 容器和虚拟机的三个本质区别是什么？为什么容器启动快？
3. `docker run -d -p 8080:80 nginx` 中，`8080` 和 `80` 分别是谁的端口？写反会怎样？
4. 什么是悬空镜像（dangling image）？怎么清理？
5. `docker stop` 和 `docker kill` 有什么区别？各自的退出码是什么？

### 操作题（每题 15 分钟）

6. 用 Docker 运行一个 MySQL 8，要求：数据持久化、root 密码来自环境变量文件、容器名 `mydb`、重启策略 `unless-stopped`、只允许本机访问 3306。写出完整命令。
7. 进入上题的 MySQL 容器，创建一个数据库 `testdb` 和一张表 `users`，然后执行 `docker cp` 把容器内的 SQL 文件拷出来。
8. 写一个 Dockerfile：把任意 Python 脚本打包成镜像（要求：slim 基础镜像、非 root 用户、.dockerignore 至少排除 4 类文件），构建并运行。
9. 用 `docker build --no-cache` 重建一个镜像，然后用 `docker history` 观察每层的大小，说说哪层最大、为什么。

### Compose 题（每题 30 分钟）

10. 从零搭建第十章的 fullstack-demo，验证 `/db` 和 `/redis` 接口正常。然后故意破坏验证排错：把 `.env` 里的数据库密码改错，`docker compose up -d --build` 后观察 api 容器状态和日志。
11. 给 fullstack-demo 加一个 `nginx` 服务：监听 8080，把 `/api` 反向代理到 `api:8000`（提示：nginx 容器里配 upstream，服务名用 `api`），验证 `curl http://localhost:8080/api/health` 能通。
12. 写一个 `docker-compose.yml`，起一个 Redis 并用 `healthcheck` 确保健康，然后演示 `depends_on: {condition: service_healthy}` 的作用（观察 `docker compose ps` 中 Status 的 `(healthy)`）。

### 综合题（每题 40 分钟）

13. 镜像瘦身实验：对一个基于 `python:3.11` 构建的镜像，依次优化为 slim、合并 RUN、加 .dockerignore、多阶段构建，每步用 `docker images` 记录大小变化，写出最终 Dockerfile 和变化表。
14. GPU 排错模拟（有 GPU 的机器）：故意用错误的 CUDA 版本镜像运行 `nvidia-smi`，观察报错；再验证 `--gpus all` 与不加 `--gpus` 时 `nvidia-smi` 输出的差异。
15. 部署 Dify（对接阶段二）：完成 11 章全流程，配置一个模型供应商，创建一个对话应用，用官方 API 调通一次对话，截图留档。

### 参考答案要点

1. 镜像=只读模板，容器=镜像的运行实例，仓库=存放分发镜像，守护进程=执行 docker 命令的服务。
2. 隔离层次（进程 vs 整机）、启动速度、资源占用、镜像大小。容器共享宿主机内核所以秒级启动。
3. 8080 是宿主机端口，80 是容器端口。写反会导致容器内 80 没映射出去，宿主机访问 8080 失败。
4. 没标签、没被容器引用的镜像。`docker image prune`。
5. stop 发 SIGTERM 优雅退出（退出码 0/143），kill 发 SIGKILL 强杀（137）。
6. `docker run -d --name mydb -p 127.0.0.1:3306:3306 --restart=unless-stopped --env-file ./mysql.env -v mysql_data:/var/lib/mysql mysql:8.0`。
7. `docker exec -it mydb mysql -uroot -p`；导出 `docker exec mydb sh -c 'exec mysqldump -uroot -p"$MYSQL_ROOT_PASSWORD" testdb' > testdb.sql`。
8. 见第六章 6.9 完整示例。
9. 通常 requirements 那层最大（依赖体积），代码层小。
10. 密码改错后 api 连接 MySQL 失败，日志里能看到 `Access denied`，容器可能不断重启或接口 500。这正是健康检查 + 正确环境变量的意义。
11. nginx 的 upstream 配置：`upstream api { server api:8000; }`，location `/api` 里 `proxy_pass http://api;`，容器里 nginx 通过 compose 默认网络访问服务名 `api`。
12. 健康检查通过前 Status 显示 `(starting)` 或 `(unhealthy)`，通过后 `(healthy)`；依赖方在 db 健康前不会真正开始工作。
13. 预期变化：`python:3.11` 约 1GB → slim 约 120MB → 清理后更小 → 多阶段构建后接近最小。
14. 旧驱动跑新 CUDA 镜像会报 `CUDA driver version is insufficient`；`--gpus all` 时容器内能看到显卡，不加时 `nvidia-smi` 报 no devices 或命令不存在。
15. 对照第十一章验收：初始化成功、模型配置成功、应用可对话、API 可调用。

---

> **最后的建议**
> 1. **命令记不住很正常**，本指南的速查表（第十五章）就是干这个的，随用随翻。
> 2. **把日常命令写成脚本**：比如"一键启全套"写成 `.sh`，配合 compose 就是你的私有部署工具。
> 3. **每天实际用一次 Docker**，两周后所有概念都会变成肌肉记忆。
> 4. **出了问题先 `docker logs` 再查教程**，90% 的问题日志里写着答案。
> 5. **和本仓库其他手册联动**：容器网络原理见《网络协议学习手册》第十三章，Linux 命令基础见《Linux 完全操作指南》，部署目标见两条学习计划的阶段章节。
