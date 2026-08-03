# Linux 完全操作指南（零基础到实战）

> 适用对象：Linux 完全新手 | 涵盖：基础认知、命令大全、正则、脚本、系统管理、安全、Git、Docker、数据库、网络排错、Vim/Nano、效率工具、实战 + 练习题

---

## 目录

1. [Linux 基础认知](#一linux-基础认知)
2. [文件系统](#二文件系统)
3. [终端命令大全](#三终端命令大全)
   - [文件与目录操作](#31-文件与目录操作)
   - [文本处理](#32-文本处理)
   - [权限管理](#33-权限管理)
   - [进程管理](#34-进程管理)
   - [网络操作](#35-网络操作)
   - [包管理](#36-包管理)
   - [磁盘与存储](#37-磁盘与存储)
   - [用户与组管理](#38-用户与组管理)
   - [压缩与归档](#39-压缩与归档)
   - [正则表达式速成](#310-正则表达式速成)
4. [Shell 脚本基础](#四shell-脚本基础)
5. [系统管理](#五系统管理)
6. [安全基础](#六安全基础)
7. [实战场景](#七实战场景)
8. [Git 版本控制基础](#八git-版本控制基础)
9. [Docker 基础入门](#九docker-基础入门)
10. [数据库基础](#十数据库基础)
11. [网络排错深入](#十一网络排错深入)
12. [Vim/Nano 编辑器详解](#十二vimnano-编辑器详解)
13. [Shell 美化与效率工具](#十三shell-美化与效率工具)
14. [常用快捷键](#十四常用快捷键)
15. [章节练习题汇总](#十五章节练习题汇总)

---

## 一、Linux 基础认知

### 1.1 什么是 Linux

Linux 是一个**开源的操作系统内核**，由 Linus Torvalds 于 1991 年创建。"Linux" 通常指基于 Linux 内核的完整操作系统（GNU/Linux）。

### 1.2 主流发行版

| 发行版家族 | 代表版本 | 包管理器 | 适用场景 |
|-----------|---------|---------|---------|
| **Debian 系** | Ubuntu, Debian, Kali Linux | `apt` | 桌面、服务器、安全测试 |
| **RHEL 系** | CentOS, Rocky Linux, Fedora | `yum` / `dnf` | 企业服务器 |
| **Arch 系** | Arch Linux, Manjaro | `pacman` | 极客、滚动更新 |
| **openSUSE** | openSUSE Leap, Tumbleweed | `zypper` | 企业、桌面 |
| **Alpine** | Alpine Linux | `apk` | Docker 容器、轻量 |

> **新手推荐**：Ubuntu（社区最大，资料最多）或 Linux Mint（类 Windows 体验）。

### 1.3 内核 vs 用户空间

```
┌──────────────────────────┐
│      用户空间 (User Space)    │  ← 你运行的程序、Shell、GUI
│  ┌──────┐ ┌──────┐ ┌────┐  │
│  │ bash │ │ vim  │ │app │  │
│  └──────┘ └──────┘ └────┘  │
├──────────────────────────┤
│        系统调用 (Syscall)     │  ← 用户空间与内核的桥梁
├──────────────────────────┤
│     内核空间 (Kernel Space)   │  ← 管理硬件、进程、内存、文件
│  进程调度 │ 内存管理 │ 驱动 │  │
├──────────────────────────┤
│        硬件 (Hardware)       │  ← CPU、内存、硬盘、网卡
└──────────────────────────┘
```

### 1.4 什么是 Shell

**Shell** 是用户与 Linux 内核之间的命令解释器。你把命令输入 Shell，Shell 翻译给内核执行。

| Shell | 特点 |
|-------|------|
| **bash** | 最常用，几乎所有 Linux 默认 |
| **zsh** | 功能更强大，macOS 默认，支持更好补全 |
| **fish** | 开箱即用，智能提示，语法不同 |
| **sh** | 最原始的 Bourne Shell，兼容性最好 |

> 查看当前 Shell：`echo $SHELL`

---

## 二、文件系统

### 2.1 文件系统层次结构标准（FHS）

Linux 一切皆文件，没有 Windows 的 C 盘 D 盘概念，只有一个根目录 `/`。

```
/                         # 根目录，一切从这里开始
├── /bin                  # 基本命令（ls, cp, mv 等）
├── /boot                 # 启动相关文件（内核、grub）
├── /dev                  # 设备文件（硬盘、USB、终端）
├── /etc                  # 系统配置文件
│   ├── /etc/passwd       # 用户账户信息
│   ├── /etc/shadow       # 密码信息（加密）
│   ├── /etc/group        # 用户组信息
│   └── /etc/fstab        # 磁盘挂载配置
├── /home                 # 用户主目录（/home/username）
├── /lib, /lib64          # 系统库文件
├── /media                # 自动挂载点（U盘、光驱）
├── /mnt                  # 手动挂载点
├── /opt                  # 第三方软件（手动安装的程序）
├── /proc                 # 虚拟文件系统（进程、内存信息）
│   ├── /proc/cpuinfo     # CPU 信息
│   └── /proc/meminfo     # 内存信息
├── /root                 # root 用户的主目录
├── /run                  # 运行时临时文件
├── /sbin                 # 系统管理命令（需要 root 权限）
├── /srv                  # 服务数据（Web 服务器文件等）
├── /sys                  # 内核与设备信息
├── /tmp                  # 临时文件（重启后清理）
├── /usr                  # 用户程序和数据
│   ├── /usr/bin          # 用户命令
│   ├── /usr/lib          # 库文件
│   └── /usr/local        # 本地编译安装的软件
└── /var                  # 可变数据（日志、缓存、数据库）
    ├── /var/log          # 日志文件
    └── /var/cache        # 缓存
```

### 2.2 文件类型

Linux 中一切皆文件，包括硬件设备。使用 `ls -l` 第一个字符标识类型：

| 标识 | 类型 | 说明 |
|-----|------|------|
| `-` | 普通文件 | 文本、二进制、图片等 |
| `d` | 目录 | 文件夹 |
| `l` | 符号链接 | 快捷方式 |
| `b` | 块设备 | 硬盘、USB |
| `c` | 字符设备 | 键盘、鼠标、终端 |
| `s` | 套接字 | 网络通信 |
| `p` | 管道 | 进程间通信 |

### 2.3 路径概念

```bash
# 绝对路径：从根目录 / 开始
/home/user/documents/report.txt

# 相对路径：从当前目录开始
./report.txt         # 当前目录下的文件
../report.txt        # 上级目录的文件
../../data/file.txt  # 上两级目录

# 特殊路径
~                    # 当前用户的主目录（/home/username）
~/documents          # 主目录下的 documents 文件夹
-                    # 上一次所在的目录
.                    # 当前目录
..                   # 上级目录
```

---

## 三、终端命令大全

> **阅读约定**：
> - `[]` 表示可选参数
> - `<>` 表示必填参数
> - `...` 表示可以有多个
> - 每条命令都附有新手最常用的示例

### 3.1 文件与目录操作

#### `pwd` — 显示当前目录（Print Working Directory）

```bash
pwd                     # /home/user/documents
pwd -P                  # 显示物理路径（不跟随符号链接）
```

#### `ls` — 列出目录内容（List）

```bash
ls                      # 列出当前目录
ls /home                # 列出指定目录
ls -l                   # 长格式（详细信息：权限、大小、时间）
ls -a                   # 显示隐藏文件（以 . 开头）
ls -la                  # 长格式 + 隐藏文件（最常用组合）
ls -lh                  # 人性化显示文件大小（1K, 234M, 2G）
ls -lt                  # 按修改时间排序（最新的在前）
ls -ltr                 # 按修改时间倒序（最旧的在最前）
ls -R                   # 递归列出子目录
ls *.txt                # 通配符：列出所有 .txt 文件
```

**ls -l 输出解读**：
```
-rw-r--r-- 1 john dev 4096 Jan 15 14:30 report.txt
│├─┤├─┤├─┤ │  │    │    │     │          │
││ │ ││ │ │  │  │    │    │     │          └─ 文件名
││ │ ││ │ │  │  │    │    │     └─ 修改时间
││ │ ││ │ │  │  │    │    └─ 文件大小(字节)
││ │ ││ │ │  │  │    └─ 所属组
││ │ ││ │ │  │  └─ 所有者
││ │ ││ │ │  └─ 硬链接数
│└─┘└┘└─┘└┘└── 权限 (详见权限管理章节)
├── 所有者权限(rwx)
│   ├── 所属组权限(r-x)
│       └── 其他人权限(r--)
```

#### `cd` — 切换目录（Change Directory）

```bash
cd /home/user           # 切换到绝对路径
cd documents            # 切换到当前目录下的 documents
cd ..                   # 返回上级目录
cd ../..                # 返回上两级
cd ~                    # 回到主目录
cd -                    # 回到上一次所在的目录
cd                      # 不加参数 = cd ~，回到主目录
```

#### `mkdir` — 创建目录（Make Directory）

```bash
mkdir newfolder         # 创建单个目录
mkdir -p a/b/c/d        # 递归创建多层目录（最常用）
mkdir -m 755 mydir      # 创建并指定权限
mkdir dir1 dir2 dir3    # 同时创建多个目录
```

#### `rmdir` — 删除空目录

```bash
rmdir emptyfolder       # 只能删除空目录
rmdir -p a/b/c          # 递归删除空目录链
```

#### `rm` — 删除文件或目录（Remove）

```bash
# ⚠️ Linux 没有回收站，删除后无法恢复！操作前请确认！

rm file.txt             # 删除文件
rm -i file.txt          # 删除前逐个确认
rm -f file.txt          # 强制删除，不提示（危险！）
rm -rf folder/          # 递归强制删除目录（非常危险！）
rm *.log                # 删除所有 .log 文件
rm -rf /                # 🚨 绝对不要执行！会删除整个系统！
```

#### `cp` — 复制文件或目录（Copy）

```bash
cp source.txt dest.txt          # 复制文件
cp file.txt /home/user/         # 复制到指定目录
cp -r folder1/ folder2/         # 递归复制整个目录
cp -i file1.txt file2.txt       # 覆盖前确认
cp -p file1.txt file2.txt       # 保留权限、时间戳
cp -a source/ dest/             # 归档模式（保留所有属性、递归）
cp file1.txt file2.txt dest/    # 复制多个文件到目录
```

#### `mv` — 移动/重命名（Move）

```bash
mv oldname.txt newname.txt      # 重命名文件
mv file.txt /home/user/         # 移动到指定目录
mv file1.txt file2.txt dest/    # 移动多个文件
mv -i source.txt dest.txt       # 覆盖前确认
mv folder/ newfolder/           # 重命名目录
```

#### `touch` — 创建空文件或更新文件时间

```bash
touch newfile.txt               # 创建空文件
touch file1.txt file2.txt       # 同时创建多个
touch -t 202512312359 file.txt  # 指定时间戳
```

#### `find` — 搜索文件（功能极其强大）

```bash
# 按名称搜索
find . -name "*.txt"                    # 当前目录及子目录所有 .txt
find /home -name "report*"              # /home 下以 report 开头的文件
find . -iname "README*"                 # 不区分大小写搜索

# 按类型搜索
find . -type f                          # 所有普通文件
find . -type d                          # 所有目录
find . -type l                          # 所有符号链接

# 按大小搜索
find . -size +10M                       # 大于 10MB 的文件
find . -size -1k                        # 小于 1KB 的文件
find . -size +100M -size -500M          # 100M 到 500M 之间

# 按时间搜索（天：time | 分钟：min）
find . -mtime -7                        # 7 天内修改过的文件
find . -mtime +30                       # 30 天前修改的
find . -atime -1                        # 1 天内访问过的
find . -mmin -60                        # 60 分钟内修改过的

# 按权限搜索
find . -perm 777                        # 权限为 777 的文件

# 对搜索结果执行操作
find . -name "*.log" -delete            # 删除所有 .log 文件
find . -name "*.tmp" -exec rm {} \;     # 对每个结果执行 rm
find . -name "*.txt" -exec cp {} /backup/ \;  # 复制到备份目录
find . -type f -empty                   # 查找空文件
```

#### `locate` — 快速文件搜索（基于数据库）

```bash
locate report.txt           # 快速查找（需要先 updatedb）
updatedb                    # 更新文件数据库（需要 sudo）
locate -i readme            # 不区分大小写
locate -c "*.pdf"           # 统计匹配数量
```

#### `ln` — 创建链接

```bash
# 硬链接（同一个文件多个名字，共享 inode，不能跨分区，不能链接目录）
ln target.txt linkname.txt

# 符号链接（软链接，类似 Windows 快捷方式，最常用）
ln -s /path/to/target linkname
ln -s /usr/bin/python3 /usr/bin/python   # 创建 Python 快捷方式
ln -sf /new/target linkname              # 强制覆盖已有链接
```

#### `stat` — 查看文件详细信息

```bash
stat file.txt
# 输出：大小、块、Inode、权限、时间戳（访问/修改/状态变更）
```

#### `file` — 判断文件类型

```bash
file unknown.bin            # 显示文件真实类型（不依赖扩展名）
file *.txt                  # 批量查看
```

---

### 3.2 文本处理

#### `cat` — 查看/拼接文件内容（Concatenate）

```bash
cat file.txt                # 显示全部内容
cat file1.txt file2.txt     # 拼接显示多个文件
cat -n file.txt             # 显示行号
cat > newfile.txt           # 从键盘输入内容到文件（Ctrl+D 结束）
cat file1.txt > file2.txt   # 将 file1 内容写入 file2（覆盖）
cat file1.txt >> file2.txt  # 追加到末尾
```

#### `tac` — 反向显示（从最后一行开始）

```bash
tac file.txt                # 反向输出（常用于查看日志最新内容）
```

#### `head` — 查看文件开头

```bash
head file.txt               # 默认显示前 10 行
head -n 20 file.txt         # 显示前 20 行
head -c 100 file.txt        # 显示前 100 个字节
```

#### `tail` — 查看文件末尾

```bash
tail file.txt               # 默认显示最后 10 行
tail -n 50 file.txt         # 显示最后 50 行
tail -f log.txt             # ⭐ 实时追踪文件更新（最常用于看日志）
tail -f -n 100 log.txt      # 显示最后 100 行并实时追踪
```

#### `less` — 分页查看文件（推荐代替 cat 查看大文件）

```bash
less file.txt               # 打开文件
# less 内快捷键：
#   空格 = 下一页    b = 上一页
#   /keyword = 向下搜索    ?keyword = 向上搜索
#   n = 下一个匹配    N = 上一个匹配
#   g = 跳到开头    G = 跳到末尾
#   q = 退出
less -N file.txt            # 显示行号
less +100 file.txt          # 从第 100 行开始
```

#### `more` — 基础分页查看（功能比 less 少）

```bash
more file.txt               # 空格翻页，q 退出
```

#### `grep` — 文本搜索（Global Regular Expression Print）⭐

```bash
# 基础搜索
grep "keyword" file.txt             # 在文件中搜索关键词
grep "error" *.log                  # 在所有 .log 文件中搜索
grep -i "error" file.txt            # 不区分大小写
grep -v "debug" file.txt            # 反向搜索（排除匹配行）
grep -n "error" file.txt            # 显示行号
grep -c "error" file.txt            # 只显示匹配行数
grep -r "keyword" /path/to/dir/     # 递归搜索整个目录
grep -rl "keyword" .                # 只列出包含关键词的文件名
grep -w "word" file.txt             # 匹配整个单词（不匹配部分）

# 上下文显示
grep -A 3 "error" file.txt          # 显示匹配行及之后 3 行 (After)
grep -B 3 "error" file.txt          # 显示匹配行及之前 3 行 (Before)
grep -C 3 "error" file.txt          # 显示匹配行及前后各 3 行 (Context)

# 正则表达式
grep "^start" file.txt              # 以 start 开头的行
grep "end$" file.txt                # 以 end 结尾的行
grep "^$" file.txt                  # 空行
grep -E "error|warning" file.txt    # 匹配 error 或 warning（扩展正则）
grep -E "[0-9]{3}-[0-9]{4}" file.txt  # 匹配电话号码格式

# 管道配合（最常用的组合）
ps aux | grep nginx                 # 查找 nginx 进程
history | grep git                  # 搜索历史命令中的 git
cat log.txt | grep -i "error"       # 查看日志中的错误
```

#### `sed` — 流编辑器（Stream Editor）⭐

```bash
# 替换（最常用）
sed 's/old/new/' file.txt           # 每行替换第一个匹配
sed 's/old/new/g' file.txt          # 全局替换
sed 's/old/new/2' file.txt          # 每行替换第二个匹配
sed -i 's/old/new/g' file.txt       # ⚠️ 直接修改文件（危险！建议先不加 -i 测试）
sed -i.bak 's/old/new/g' file.txt   # 修改前备份为 file.txt.bak

# 删除
sed '3d' file.txt                   # 删除第 3 行
sed '3,10d' file.txt                # 删除第 3-10 行
sed '/pattern/d' file.txt           # 删除匹配 pattern 的行
sed '/^$/d' file.txt                # 删除空行

# 打印
sed -n '5p' file.txt                # 打印第 5 行
sed -n '5,10p' file.txt             # 打印第 5-10 行
sed -n '/error/p' file.txt          # 打印包含 error 的行

# 插入
sed '3i\new line' file.txt          # 在第 3 行前插入
sed '3a\new line' file.txt          # 在第 3 行后追加
```

#### `awk` — 文本处理语言 ⭐

```bash
# awk 处理流程：按行读取 → 按列分割 → 执行操作
# $0 = 整行, $1 = 第一列, $2 = 第二列 ... NF = 列数, NR = 行号

# 打印指定列
awk '{print $1}' file.txt                           # 打印第 1 列
awk '{print $1, $3}' file.txt                       # 打印第 1 和第 3 列
awk '{print $NF}' file.txt                          # 打印最后一列
awk '{print NR, $0}' file.txt                       # 打印行号和内容

# 条件过滤
awk '$3 > 100' file.txt                             # 第 3 列大于 100 的行
awk '$2 == "error"' file.txt                        # 第 2 列等于 "error"
awk '$1 ~ /pattern/' file.txt                       # 第 1 列匹配正则

# 分隔符
awk -F':' '{print $1}' /etc/passwd                  # 用冒号作为分隔符
awk -F',' '{print $2}' data.csv                     # 处理 CSV 文件

# 统计
awk '{sum+=$3} END {print sum}' file.txt            # 求第 3 列总和
awk '{sum+=$3} END {print sum/NR}' file.txt         # 求第 3 列平均值
awk '{count[$1]++} END {for(i in count) print i, count[i]}'  # 分组计数

# 实用示例
df -h | awk '$5+0 > 80 {print $1, $5}'              # 找出磁盘使用率 > 80% 的分区
netstat -an | awk '/^tcp/ {++S[$NF]} END {for(a in S) print a, S[a]}'  # TCP 连接状态统计
```

#### `cut` — 按列提取

```bash
cut -d':' -f1 /etc/passwd            # 用冒号分隔，取第 1 列
cut -d',' -f1,3 data.csv             # 取第 1 和第 3 列
cut -c1-5 file.txt                   # 取每行的第 1-5 个字符
cut -c5- file.txt                    # 从第 5 个字符到行尾
```

#### `sort` — 排序

```bash
sort file.txt                       # 按字母/数字排序
sort -n file.txt                    # 按数值排序
sort -r file.txt                    # 逆序
sort -u file.txt                    # 去重排序
sort -t',' -k2 data.csv             # CSV 按第 2 列排序
sort -t':' -k3 -n /etc/passwd       # 按 UID 数值排序
```

#### `uniq` — 去重（通常配合 sort）

```bash
uniq file.txt                       # 去除连续重复行
sort file.txt | uniq                # 先排序再去重（标准用法）
sort file.txt | uniq -c             # 去重并统计出现次数
sort file.txt | uniq -d             # 只显示重复的行
sort file.txt | uniq -u             # 只显示不重复的行
```

#### `wc` — 统计（Word Count）

```bash
wc file.txt                         # 行数 单词数 字节数 文件名
wc -l file.txt                      # 只统计行数
wc -w file.txt                      # 只统计单词数
wc -c file.txt                      # 只统计字节数
wc -m file.txt                      # 只统计字符数
find . -name "*.js" | xargs wc -l   # 统计所有 .js 文件的总行数
```

#### `diff` — 比较文件差异

```bash
diff file1.txt file2.txt            # 比较两个文件
diff -u file1.txt file2.txt         # 统一格式（类似 git diff）
diff -r dir1/ dir2/                 # 比较两个目录
```

#### `tee` — 同时输出到屏幕和文件

```bash
ls -l | tee output.txt              # 输出到屏幕的同时保存到文件
ls -l | tee -a output.txt           # 追加模式
command 2>&1 | tee log.txt          # 同时保存标准输出和错误输出
```

#### `tr` — 字符转换或删除

```bash
echo "hello" | tr 'a-z' 'A-Z'       # 小写转大写
echo "hello" | tr -d 'aeiou'        # 删除所有元音字母
cat file.txt | tr -s '\n'           # 压缩连续空行
```

---

### 3.3 权限管理

#### 权限基础

Linux 权限分为三组，每组有读（r=4）、写（w=2）、执行（x=1）三种：

```
  所有者   所属组   其他人
  r w x   r - x   r - -
  4 2 1   4 0 1   4 0 0  ← 数字表示法
  └─7──┘  └─5──┘  └─4──┘

  rwxr-xr-- = 754
```

| 权限 | 文件 | 目录 |
|-----|------|------|
| **r** (读) | 可以查看文件内容 | 可以列出目录内容 (ls) |
| **w** (写) | 可以修改文件 | 可以在目录中创建/删除文件 |
| **x** (执行) | 可以执行文件 | 可以进入目录 (cd) |

#### `chmod` — 修改权限（Change Mode）⭐

```bash
# 符号模式（直观）
chmod u+x script.sh             # 所有者(u) 添加(+) 执行(x) 权限
chmod g-w file.txt              # 所属组(g) 移除(-) 写(w) 权限
chmod o=r file.txt              # 其他人(o) 设置(=) 只读(r)
chmod a+x script.sh             # 所有人(a=all) 添加执行权限
chmod u+rwx,g+rx,o+r file.txt   # 组合设置

# 数字模式（最常用）
chmod 755 script.sh             # rwxr-xr-x (所有者全权限，其他人读+执行)
chmod 644 file.txt              # rw-r--r-- (所有者读写，其他人只读)
chmod 777 file.txt              # rwxrwxrwx (所有人全权限，不推荐！)
chmod 600 secret.key            # rw------- (只有所有者能读写)

# 常用权限速查
# 777 = 所有人都能读写执行  (危险！一般不使用)
# 755 = 所有者全权限，其他读+执行 (目录，脚本)
# 700 = 只有所有者有全权限 (私人目录/脚本)
# 644 = 所有者读写，其他只读 (普通文件)
# 600 = 只有所有者读写 (配置文件，私钥)

# 递归修改
chmod -R 755 folder/            # 递归修改整个目录
chmod -R u+rwX folder/          # 对目录加执行权限，文件不加(大写X)
```

#### `chown` — 修改所有者（Change Owner）

```bash
chown user file.txt             # 修改文件所有者
chown user:group file.txt       # 同时修改所有者和所属组
chown :group file.txt           # 只修改所属组
chown -R user:group folder/     # 递归修改整个目录（用 -R）
```

#### `chgrp` — 修改所属组

```bash
chgrp developers file.txt       # 修改文件所属组
chgrp -R developers folder/     # 递归修改
```

#### `umask` — 默认权限掩码

```bash
umask                           # 查看当前掩码
umask 022                       # 设置掩码（新文件默认 644，新目录默认 755）
# 计算公式：新文件权限 = 666 - umask  新目录权限 = 777 - umask
```

#### `sudo` — 以超级用户身份执行命令

```bash
sudo command                    # 以 root 身份执行一条命令
sudo -i                         # 切换到 root shell
sudo -u username command        # 以指定用户身份执行
sudo !!                         # 以 sudo 重新执行上一条命令
sudo -l                         # 查看当前用户 sudo 权限

# 配置 sudo (/etc/sudoers, 用 visudo 编辑)
# username ALL=(ALL:ALL) ALL    # 允许用户执行所有命令
```

#### `su` — 切换用户

```bash
su username                     # 切换到指定用户
su - username                   # 切换并加载该用户的环境变量
su                              # 默认切换到 root
```

---

### 3.4 进程管理

#### `ps` — 查看进程状态（Process Status）

```bash
ps                              # 当前终端的进程
ps aux                          # ⭐ 显示所有用户的所有进程（BSD 风格）
ps -ef                          # 显示所有进程（Linux 风格）
ps aux | grep nginx             # 查找 nginx 进程
ps -u username                  # 查看指定用户的进程
ps -p 1234 -o pid,ppid,cmd,%cpu,%mem  # 按 PID 查看特定进程详情

# ps aux 列说明：
# USER  PID  %CPU %MEM    VSZ   RSS TTY  STAT  START   TIME COMMAND
# 用户  进程ID CPU  内存  虚拟内存 物理内存 终端  状态  启动时间 运行时间 命令
```

#### `top` — 实时进程监控

```bash
top                             # 实时显示进程（q 退出）
# top 快捷键：
#   1        = 显示每个 CPU 核心
#   M        = 按内存使用排序
#   P        = 按 CPU 使用排序
#   k        = 杀掉进程（输入 PID）
#   q        = 退出
#   c        = 切换显示完整命令

top -u username                 # 只看指定用户的进程
top -p 1234                     # 只看指定 PID
```

#### `htop` — 增强版 top（需安装）

```bash
htop                            # 彩色、交互式、鼠标支持
# sudo apt install htop         # Ubuntu/Debian 安装
# sudo yum install htop         # CentOS/RHEL 安装
```

#### `kill` — 终止进程

```bash
kill 1234                       # 发送 TERM 信号（优雅终止）
kill -9 1234                    # 发送 KILL 信号（强制终止）
kill -15 1234                   # 同 kill（默认 TERM）
kill -l                         # 列出所有信号

# 常用信号：
# 1  (HUP)   重新加载配置
# 2  (INT)   中断（相当于 Ctrl+C）
# 9  (KILL)  强制终止（进程无法忽略）
# 15 (TERM)  终止（默认，进程可以清理后退出）
# 19 (STOP)  暂停进程
# 18 (CONT)  继续暂停的进程

kill -HUP 1234                  # 重新加载进程配置（常用于 nginx）
```

#### `pkill` / `killall` — 按名称终止进程

```bash
pkill nginx                     # 终止所有名为 nginx 的进程
pkill -f "python app.py"        # 匹配完整命令行
killall nginx                   # 同上（部分系统）
```

#### `bg` / `fg` / `jobs` — 前后台任务管理

```bash
# 在命令后加 & 直接放到后台运行
sleep 100 &                     # 后台运行

jobs                            # 查看当前终端的后台任务
fg %1                           # 将 1 号任务调到前台
bg %1                           # 继续在后台运行 1 号任务

Ctrl+Z                          # 暂停当前前台任务
Ctrl+C                          # 终止当前前台任务
```

#### `nohup` — 后台运行且不受终端关闭影响

```bash
nohup command &                 # 后台运行，输出到 nohup.out
nohup command > log.txt 2>&1 &  # 后台运行，指定日志文件
```

#### `screen` / `tmux` — 终端复用器（保持会话不中断）

```bash
# screen
screen                          # 创建新会话
screen -S mysession             # 创建命名会话
Ctrl+A, D                       # 脱离会话（detach）
screen -r                       # 重新连接
screen -r mysession             # 重新连接到指定会话
screen -ls                      # 列出所有会话

# tmux（更现代，推荐）
tmux                            # 创建新会话
tmux new -s mysession           # 创建命名会话
Ctrl+B, D                       # 脱离会话
tmux attach -t mysession        # 重新连接
tmux ls                         # 列出所有会话
```

#### `nice` / `renice` — 调整进程优先级

```bash
nice -n 10 command              # 以较低优先级启动（-20 最高，19 最低）
renice -n 5 -p 1234             # 修改运行中进程的优先级
```

#### `pgrep` — 查找进程 PID

```bash
pgrep nginx                     # 查找 nginx 的 PID
pgrep -u username               # 指定用户的所有进程
pgrep -f "python app.py"        # 完整命令行匹配
```

---

### 3.5 网络操作

#### `ping` — 测试网络连通性

```bash
ping google.com                 # 持续 ping（Ctrl+C 停止）
ping -c 4 google.com            # 发送 4 个包后停止
ping -i 2 google.com            # 每 2 秒发送一次
```

#### `curl` — 发送 HTTP 请求（最强大的网络工具之一）⭐

```bash
# GET 请求
curl https://api.example.com                    # 发送 GET 请求
curl -I https://example.com                     # 只获取响应头
curl -o file.html https://example.com           # 下载并保存
curl -O https://example.com/file.zip            # 下载并保持原文件名
curl -L https://short.link                      # 跟随重定向

# POST 请求
curl -X POST https://api.example.com/data       # POST 请求
curl -d "name=john&age=25" https://api.com      # POST 表单数据
curl -H "Content-Type: application/json" \      # POST JSON
     -d '{"name":"john"}' https://api.com
curl -F "file=@localfile.txt" https://api.com   # 上传文件

# 调试
curl -v https://example.com                     # 详细输出（看请求/响应头）
curl -k https://self-signed.example.com         # 忽略 SSL 证书验证
```

#### `wget` — 下载文件

```bash
wget https://example.com/file.zip               # 下载文件
wget -O customname.zip https://example.com/f    # 指定文件名
wget -c https://example.com/large.zip           # 断点续传
wget -r https://example.com/                    # 递归下载整站
wget -i urls.txt                                # 批量下载（文件中每行一个 URL）
```

#### `ip` — 网络配置（现代，替代 ifconfig）

```bash
ip addr                         # 查看 IP 地址（同 ip a）
ip link                         # 查看网络接口状态
ip route                        # 查看路由表
ip neigh                        # 查看 ARP 表
ip -s link                      # 查看网络统计
```

#### `ifconfig` — 传统网络配置（部分新系统需安装 net-tools）

```bash
ifconfig                        # 查看所有网络接口
ifconfig eth0                   # 查看指定接口
ifconfig eth0 192.168.1.100     # 设置 IP 地址
```

#### `ss` — 查看网络连接（现代，替代 netstat）

```bash
ss -tuln                        # 查看所有监听的 TCP/UDP 端口
ss -tulnp                       # 加上进程名
ss -s                           # 显示摘要统计
ss -t state established         # 查看已建立的 TCP 连接
ss -t state time-wait           # 查看 TIME-WAIT 状态连接
```

#### `netstat` — 传统网络查看

```bash
netstat -tuln                   # 监听端口
netstat -an | grep 80           # 查看 80 端口连接
netstat -tulnp | grep nginx     # 查看 nginx 监听的端口
netstat -s                      # 网络统计
```

#### `nslookup` / `dig` — DNS 查询

```bash
nslookup google.com             # 查询域名 IP
nslookup google.com 8.8.8.8     # 指定 DNS 服务器查询

dig google.com                  # 详细 DNS 查询
dig google.com +short           # 简短输出（只显示 IP）
dig -x 8.8.8.8                  # 反向查询（IP → 域名）
dig google.com MX               # 查询邮件服务器记录
dig google.com ANY              # 查询所有记录
```

#### `nc` (netcat) — 网络瑞士军刀

```bash
nc -zv 192.168.1.1 80           # 测试端口是否开放
nc -l 8080                      # 监听 8080 端口
echo "test" | nc host 8080      # 发送数据到指定端口
```

#### `ssh` — 远程登录 ⭐

```bash
ssh user@192.168.1.100          # 远程登录
ssh -p 2222 user@host           # 指定端口
ssh -i ~/.ssh/private_key user@host  # 使用密钥登录
ssh -L 8080:localhost:80 user@host   # 本地端口转发

# SSH 配置 (~/.ssh/config)
Host myserver
    HostName 192.168.1.100
    User john
    Port 2222
    IdentityFile ~/.ssh/mykey
# 配置后只需: ssh myserver
```

#### `scp` — 远程文件复制（基于 SSH）

```bash
scp file.txt user@host:/remote/path/     # 本地上传到远程
scp user@host:/remote/file.txt ./        # 远程下载到本地
scp -r folder/ user@host:/remote/        # 递归复制目录
scp -P 2222 file.txt user@host:/path/    # 指定端口
```

#### `rsync` — 高效文件同步（增量传输）

```bash
rsync -av source/ dest/                         # 本地同步（保留属性）
rsync -av source/ user@host:/remote/path/       # 同步到远程
rsync -av --delete source/ dest/                # 同步并删除目标多余文件
rsync -avz --progress source/ user@host:/path/  # 压缩传输 + 进度条
```

#### `tcpdump` — 抓包分析（需 root）

```bash
tcpdump -i eth0                                 # 监听 eth0 所有流量
tcpdump -i any port 80                          # 监听所有接口的 80 端口
tcpdump -i eth0 host 192.168.1.100              # 监听指定主机
tcpdump -i eth0 -w capture.pcap                 # 保存到文件
tcpdump -r capture.pcap                         # 读取文件
```

---

### 3.6 包管理

#### Debian/Ubuntu — `apt`（Advanced Package Tool）⭐

```bash
# 基础操作
sudo apt update                     # 更新软件包列表（必须！）
sudo apt upgrade                    # 升级所有已安装的包
sudo apt full-upgrade               # 更彻底的升级（可能删除冲突包）
sudo apt install package-name       # 安装软件包
sudo apt install pkg1 pkg2 pkg3     # 一次安装多个
sudo apt remove package-name        # 删除包（保留配置）
sudo apt purge package-name         # 完全删除（包括配置）
sudo apt autoremove                 # 删除不再需要的依赖

# 搜索与信息
apt search keyword                  # 搜索软件包
apt show package-name               # 显示软件包详情
apt list --installed                # 列出已安装的包
apt list --upgradable               # 列出可升级的包

# 管理
sudo apt-mark hold package-name     # 阻止包升级
sudo apt-mark unhold package-name   # 取消阻止
```

#### Debian/Ubuntu — `dpkg`（底层包管理）

```bash
sudo dpkg -i package.deb            # 安装 .deb 文件
sudo dpkg -r package-name           # 删除包
dpkg -l                             # 列出所有包
dpkg -l | grep keyword              # 搜索已安装的包
dpkg -L package-name                # 列出包安装的所有文件
dpkg -S /path/to/file               # 查找文件属于哪个包
```

#### CentOS/RHEL/Fedora — `dnf`（现代）/ `yum`（传统）

```bash
# dnf（Fedora 22+, RHEL 8+, CentOS 8+）
sudo dnf install package-name       # 安装
sudo dnf remove package-name        # 删除
sudo dnf update                     # 更新所有包
sudo dnf search keyword             # 搜索
sudo dnf info package-name          # 详情
sudo dnf autoremove                 # 删除无用依赖

# yum（CentOS 7, RHEL 7 及更早）
sudo yum install package-name       # 安装
sudo yum update                     # 更新
sudo yum remove package-name        # 删除
sudo yum search keyword             # 搜索
```

#### Arch — `pacman`

```bash
sudo pacman -S package-name         # 安装
sudo pacman -R package-name         # 删除
sudo pacman -Syu                    # 全面系统更新
sudo pacman -Ss keyword             # 搜索
sudo pacman -Qi package-name        # 信息
```

#### 通用包格式

```bash
# Snap（Ubuntu 默认支持）
sudo snap install package-name
sudo snap remove package-name

# Flatpak（跨发行版）
flatpak install flathub app.id
flatpak run app.id

# AppImage（免安装直接运行）
chmod +x application.AppImage
./application.AppImage
```

---

### 3.7 磁盘与存储

#### `df` — 查看磁盘空间使用（Disk Free）

```bash
df -h                           # ⭐ 人性化显示所有挂载点空间
df -h /home                     # 查看特定分区的空间
df -i                           # 查看 inode 使用情况
df -T                           # 显示文件系统类型
```

#### `du` — 查看目录/文件占用空间（Disk Usage）⭐

```bash
du -sh *                        # ⭐ 当前目录下每个文件/目录的大小汇总
du -sh folder/                  # 查看某个目录的总大小
du -h --max-depth=1             # 显示一层深度的目录大小
du -ah | sort -rh | head -10    # 找出最大的 10 个文件/目录
```

#### `mount` / `umount` — 挂载与卸载

```bash
mount                           # 查看所有挂载点
mount /dev/sdb1 /mnt/usb        # 挂载设备到指定目录
mount -t ext4 /dev/sdb1 /mnt    # 指定文件系统类型
umount /mnt/usb                 # 卸载
umount -l /mnt/usb              # 强制卸载（繁忙时）

# fstab 自动挂载 (/etc/fstab)
# /dev/sdb1  /data  ext4  defaults  0  2
```

#### `lsblk` — 列出块设备

```bash
lsblk                           # 树形显示所有块设备
lsblk -f                        # 显示文件系统类型和 UUID
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT  # 自定义输出列
```

#### `fdisk` / `parted` — 磁盘分区

```bash
sudo fdisk -l                   # 列出所有磁盘和分区
sudo fdisk /dev/sdb             # 交互式分区工具

# 常用 fdisk 交互命令：
# m = 帮助, p = 打印分区表, n = 新建分区
# d = 删除分区, w = 写入并退出, q = 不保存退出
```

#### `dd` — 磁盘读写（危险但强大）

```bash
# ⚠️ dd 非常危险，操作前务必确认 of= 目标正确！

dd if=/dev/sda of=/backup/disk.img bs=4M     # 备份整个磁盘
dd if=/path/to/image.iso of=/dev/sdb bs=4M   # 写入 ISO 到 USB
dd if=/dev/zero of=/swapfile bs=1M count=2048 # 创建 2GB 空文件
```

#### `blkid` — 查看块设备 UUID 和类型

```bash
blkid                           # 列出所有块设备
blkid /dev/sda1                 # 查看特定分区
```

---

### 3.8 用户与组管理

#### `useradd` / `adduser` — 创建用户

```bash
sudo useradd -m username                # 创建用户并创建主目录
sudo useradd -m -s /bin/bash username   # 指定 Shell
sudo useradd -m -g developers username  # 指定初始组
sudo adduser username                   # Debian 系交互式创建（更友好，推荐）
```

#### `usermod` — 修改用户

```bash
sudo usermod -aG sudo username          # 将用户加入 sudo 组 ⭐
sudo usermod -aG docker username        # 加入 docker 组
sudo usermod -s /bin/zsh username       # 修改 Shell
sudo usermod -L username                # 锁定用户
sudo usermod -U username                # 解锁用户
```

#### `userdel` — 删除用户

```bash
sudo userdel username                   # 删除用户（不删除主目录）
sudo userdel -r username                # 删除用户及主目录
```

#### `passwd` — 密码管理

```bash
passwd                          # 修改自己的密码
sudo passwd username            # 修改用户密码（管理员）
sudo passwd -l username         # 锁定用户密码
sudo passwd -u username         # 解锁
```

#### `groupadd` / `groupdel` — 组管理

```bash
sudo groupadd developers        # 创建组
sudo groupdel developers        # 删除组
```

#### `id` / `who` / `whoami` / `w` / `last` — 用户信息

```bash
id                              # 查看自己的 UID、GID、组
id username                     # 查看指定用户
whoami                          # 当前用户名
who                             # 当前登录的用户列表
w                               # 详细信息（登录用户及正在做什么）
last                            # 最近登录记录
last -n 10                      # 最近 10 条登录记录
```

---

### 3.9 压缩与归档

#### `tar` — 归档工具（Tape Archive）⭐

```bash
# 创建
tar -cvf archive.tar file1 file2/       # 创建 .tar（v = 显示过程, f = 文件名）
tar -czvf archive.tar.gz folder/        # ⭐ 创建 .tar.gz（gzip 压缩，最常用）
tar -cjvf archive.tar.bz2 folder/       # 创建 .tar.bz2（bzip2 压缩，更小）
tar -cJvf archive.tar.xz folder/        # 创建 .tar.xz（xz 压缩，最小）

# 解压
tar -xvf archive.tar                    # 解压 .tar
tar -xzvf archive.tar.gz                # ⭐ 解压 .tar.gz
tar -xjvf archive.tar.bz2               # 解压 .tar.bz2
tar -xJvf archive.tar.xz                # 解压 .tar.xz
tar -xzvf archive.tar.gz -C /target/    # 解压到指定目录

# 查看内容（不解压）
tar -tvf archive.tar.gz                 # 列出压缩包内容

# 记忆技巧：c=Create 创建, x=eXtract 解压, t=lisT 查看
#          z=gzip, j=bzip2, J=xz
#          v=Verbose 显示过程, f=File 文件名
```

#### `gzip` / `gunzip`

```bash
gzip file.txt                   # 压缩为 file.txt.gz（原文件会被删除）
gzip -k file.txt                # 压缩并保留原文件
gunzip file.txt.gz              # 解压
gzip -d file.txt.gz             # 同 gunzip
```

#### `bzip2` / `bunzip2`

```bash
bzip2 file.txt                  # 压缩率比 gzip 高，但更慢
bunzip2 file.txt.bz2            # 解压
```

#### `zip` / `unzip`

```bash
zip archive.zip file1.txt file2.txt     # 压缩
zip -r archive.zip folder/              # 压缩整个目录
zip -e archive.zip file.txt             # 加密压缩（需要输入密码）
unzip archive.zip                        # 解压
unzip archive.zip -d /target/            # 解压到指定目录
unzip -l archive.zip                     # 查看内容不解压
```

---

### 3.10 正则表达式速成

正则表达式（regex）是一种模式匹配语言，是 `grep`、`sed`、`awk` 的灵魂。掌握正则，文本处理功力提升 10 倍。

#### 基础元字符

| 元字符 | 含义 | 示例 | 匹配 |
|--------|------|------|------|
| `.` | 任意单个字符 | `h.t` | hat, hot, h3t |
| `*` | 前一个字符重复 0 次或多次 | `ab*c` | ac, abc, abbc |
| `+` | 前一个字符重复 1 次或多次 | `ab+c` | abc, abbc（不含 ac） |
| `?` | 前一个字符出现 0 或 1 次 | `colou?r` | color, colour |
| `^` | 行首 | `^Hello` | 以 Hello 开头的行 |
| `$` | 行尾 | `end$` | 以 end 结尾的行 |
| `[]` | 字符集（任一匹配） | `[aeiou]` | 任一元音字母 |
| `[^]` | 排除字符集 | `[^0-9]` | 任意非数字字符 |
| `|` | 或（需 `-E` 或转义） | `cat|dog` | cat 或 dog |
| `()` | 分组 | `(ab)+` | ab, abab, ababab |
| `\` | 转义 | `\.` | 字面意义的点 |
| `{n}` | 恰好 n 次 | `a{3}` | aaa |
| `{n,}` | 至少 n 次 | `a{2,}` | aa, aaa, aaaa... |
| `{n,m}` | n 到 m 次 | `a{2,4}` | aa, aaa, aaaa |

#### 预定义字符类（POSIX 和 PCRE）

```bash
# BRE（基本正则，grep 默认）/ ERE（扩展正则，grep -E / sed -r）
\d  = 数字 [0-9]          （仅 PCRE，grep -P）
\D  = 非数字              （仅 PCRE）
\w  = 单词字符 [a-zA-Z0-9_]（仅 PCRE）
\W  = 非单词字符          （仅 PCRE）
\s  = 空白字符            （仅 PCRE）
\S  = 非空白字符          （仅 PCRE）
\b  = 单词边界            （仅 PCRE）

# POSIX 字符类（所有工具通用）
[[:digit:]]   = 数字
[[:alpha:]]   = 字母
[[:alnum:]]   = 字母+数字
[[:lower:]]   = 小写字母
[[:upper:]]   = 大写字母
[[:space:]]   = 空白字符
[[:punct:]]   = 标点符号
```

#### grep 正则实战

```bash
# 匹配 IP 地址
grep -E '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' file.txt

# 匹配邮箱
grep -E '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' file.txt

# 匹配手机号（中国）
grep -E '1[3-9][0-9]{9}' file.txt

# 匹配日期 YYYY-MM-DD
grep -E '[0-9]{4}-[0-9]{2}-[0-9]{2}' file.txt

# 反向引用（匹配重复单词）
grep -E '\b([a-zA-Z]+) \1\b' file.txt    # 匹配 "the the", "is is" 等

# 删除空行和注释行
grep -vE '^$|^#' config.conf

# 查找不以 # 开头的非空行（有效配置）
grep -E '^[^#]' config.conf
```

#### sed 正则实战

```bash
# 删除行首空格
sed 's/^[[:space:]]*//' file.txt

# 删除行尾空格
sed 's/[[:space:]]*$//' file.txt

# 删除 HTML 标签
sed 's/<[^>]*>//g' file.html

# 给每行加引号
sed 's/.*/"&"/' file.txt

# 交换两列（逗号分隔）
sed -E 's/([^,]*),(.*)/\2,\1/' file.csv

# 提取括号内内容
sed -E 's/.*\((.*)\).*/\1/' file.txt
```

#### awk 正则实战

```bash
# 打印以 error 开头的行
awk '/^error/' log.txt

# 第二列匹配数字
awk '$2 ~ /^[0-9]+$/' file.txt

# 不匹配注释或空行
awk '!/^#|^$/' config.conf

# 根据正则提取（match 函数）
awk 'match($0, /[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/) {print substr($0, RSTART, RLENGTH)}'
```

#### 正则模式速查

```bash
# 常用场景的正则模式

# 正整数:        ^[1-9][0-9]*$
# 整数:          ^-?[0-9]+$
# 浮点数:        ^-?[0-9]+\.[0-9]+$
# 中文字符:      [\x{4e00}-\x{9fa5}]（grep -P）
# URL:           https?://[^\s]+
# 文件路径:      ^(/[^/ ]*)+/?$
# MAC 地址:      ^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$
# 强密码(8位+大小写数字): ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$
```

#### 工具正则模式对照

| 工具 | 默认模式 | 启用扩展 | PCRE |
|------|---------|---------|------|
| grep | BRE 基本正则 | `grep -E` | `grep -P` |
| sed | BRE 基本正则 | `sed -E` / `sed -r` | — |
| awk | ERE 扩展正则 | 默认就是 | — |
| vim | 魔数模式 | `\v` 前缀 | — |
| find | Emacs 正则 | `-regex` | `-regextype posix-extended` |

---

## 四、Shell 脚本基础

### 4.1 第一个脚本

```bash
#!/bin/bash
# 这是我的第一个脚本

echo "Hello, Linux!"
echo "当前用户: $(whoami)"
echo "当前目录: $(pwd)"
echo "当前时间: $(date)"
```

保存为 `hello.sh`，然后：
```bash
chmod +x hello.sh       # 添加执行权限
./hello.sh              # 运行脚本
```

### 4.2 变量

```bash
#!/bin/bash
# 变量定义（等号两边不能有空格！）
name="John"
age=25

# 使用变量
echo "Name: $name"
echo "Age: $age"
echo "Hello, ${name}"       # 花括号用于明确变量边界

# 只读变量
readonly PI=3.14159

# 命令结果赋给变量
current_date=$(date +%Y-%m-%d)
file_count=$(ls | wc -l)
echo "Today is $current_date, $file_count files here"

# 环境变量
echo "HOME: $HOME"
echo "PATH: $PATH"
echo "USER: $USER"
```

### 4.3 输入与输出

```bash
#!/bin/bash
# 读取用户输入
echo -n "Enter your name: "
read username
echo "Hello, $username!"

# 带提示的读取
read -p "Enter your age: " age
echo "You are $age years old"

# 静默输入（密码）
read -sp "Enter password: " password
echo       # 换行
echo "Password received"

# printf 格式化输出
printf "Name: %-10s Age: %3d\n" "$username" "$age"
```

### 4.4 条件判断

```bash
#!/bin/bash
# if 语句
if [ $age -ge 18 ]; then
    echo "Adult"
elif [ $age -ge 13 ]; then
    echo "Teenager"
else
    echo "Child"
fi

# 数值比较
# -eq  等于      -ne  不等于
# -gt  大于      -lt  小于
# -ge  大于等于  -le  小于等于

# 字符串比较
# =    等于      !=   不等于
# -z   为空      -n   不为空

# 文件测试
# -f   是普通文件  -d   是目录
# -e   存在       -r   可读
# -w   可写       -x   可执行
# -s   非空文件

# 条件组合
# &&   与         ||   或        !    非

# [[ ]] 增强版（推荐，支持正则和模式匹配）
if [[ $name == J* ]]; then
    echo "Name starts with J"
fi

# case 语句
case $1 in
    start)
        echo "Starting..."
        ;;
    stop)
        echo "Stopping..."
        ;;
    restart)
        echo "Restarting..."
        ;;
    *)
        echo "Usage: $0 {start|stop|restart}"
        ;;
esac
```

### 4.5 循环

```bash
#!/bin/bash
# for 循环
for i in 1 2 3 4 5; do
    echo "Number: $i"
done

for i in {1..10}; do
    echo "$i"
done

for file in *.txt; do
    echo "Processing $file"
done

# while 循环
counter=1
while [ $counter -le 5 ]; do
    echo "Counter: $counter"
    ((counter++))
done

# until 循环
counter=1
until [ $counter -gt 5 ]; do
    echo "$counter"
    ((counter++))
done

# break 和 continue
for i in {1..10}; do
    if [ $i -eq 5 ]; then
        break       # 退出循环
    fi
    echo $i
done
```

### 4.6 函数

```bash
#!/bin/bash
# 定义函数
greet() {
    local name=$1           # local = 局部变量
    echo "Hello, $name!"
}

# 调用函数
greet "John"
greet "Jane"

# 带返回值的函数
add() {
    local result=$(($1 + $2))
    echo $result            # 通过 echo 返回
    return 0                # return 只能返回 0-255 的状态码
}

sum=$(add 5 3)
echo "Sum: $sum"

# 带参数
myfunc() {
    echo "参数个数: $#"
    echo "所有参数: $@"
    echo "第1个参数: $1"
    echo "第2个参数: $2"
}
myfunc a b c d
```

### 4.7 数组

```bash
#!/bin/bash
# 定义数组
fruits=("apple" "banana" "orange" "grape")

# 访问
echo ${fruits[0]}           # 第一个
echo ${fruits[1]}           # 第二个
echo ${fruits[@]}           # 所有元素
echo ${#fruits[@]}          # 数组长度

# 遍历
for fruit in "${fruits[@]}"; do
    echo "$fruit"
done

# 添加元素
fruits+=("mango")

# 关联数组（类似字典）
declare -A scores
scores[math]=90
scores[english]=85
echo ${scores[math]}
echo ${!scores[@]}          # 所有 key
```

### 4.8 重定向与管道

```bash
# 输出重定向
command > file.txt          # 覆盖写入（标准输出）
command >> file.txt         # 追加写入
command 2> error.txt        # 错误输出到文件
command 2>&1                # 错误输出合并到标准输出
command &> all.txt          # 标准输出和错误都输出到文件
command > /dev/null 2>&1    # 丢弃所有输出

# 输入重定向
command < input.txt
wc -l < file.txt

# 管道 |
command1 | command2         # command1 的输出作为 command2 的输入
ps aux | grep nginx | awk '{print $2}'

# xargs — 将标准输入转为命令参数
find . -name "*.log" | xargs rm          # 删除所有 .log
echo "file1 file2 file3" | xargs touch   # 批量创建文件
find . -name "*.txt" | xargs -I {} cp {} /backup/  # 复制每个文件
```

### 4.9 特殊变量

```bash
#!/bin/bash
echo "脚本名: $0"
echo "第1个参数: $1"
echo "第2个参数: $2"
echo "参数个数: $#"
echo "所有参数: $@"
echo "所有参数(单字符串): $*"
echo "上一条命令退出码: $?"
echo "当前进程 PID: $$"
echo "最后一个后台进程 PID: $!"
```

### 4.10 错误处理

```bash
#!/bin/bash
# 遇到错误立即退出（推荐）
set -e
# 使用未定义变量时报错
set -u
# 管道中任何命令失败都视为失败
set -o pipefail

# 综合使用
set -euo pipefail

# 自定义错误处理
trap 'echo "Error on line $LINENO"' ERR
```

---

## 五、系统管理

### 5.1 systemd — 服务管理

```bash
# 服务管理
sudo systemctl start nginx               # 启动服务
sudo systemctl stop nginx                # 停止服务
sudo systemctl restart nginx             # 重启服务
sudo systemctl reload nginx              # 重新加载配置（不中断服务）
sudo systemctl status nginx              # 查看服务状态
sudo systemctl enable nginx              # 开机自启
sudo systemctl disable nginx             # 取消开机自启
sudo systemctl is-enabled nginx          # 检查是否开机自启
sudo systemctl is-active nginx           # 检查是否正在运行

# 列出服务
systemctl list-units --type=service      # 所有活跃的服务
systemctl list-units --type=service --all # 包括未激活的
systemctl list-unit-files --type=service # 所有服务的启用状态

# 系统控制
sudo systemctl reboot                    # 重启系统
sudo systemctl poweroff                  # 关机
sudo systemctl suspend                   # 挂起
```

### 5.2 查看日志 — `journalctl`

```bash
journalctl                              # 查看所有日志
journalctl -xe                          # 查看最近的日志（含详细解释）
journalctl -u nginx                     # 查看 nginx 服务日志
journalctl -u nginx -f                  # 实时追踪 nginx 日志
journalctl -u nginx --since "2025-01-01" # 指定日期之后的日志
journalctl -u nginx --since "1 hour ago" # 1 小时内的日志
journalctl -u nginx -n 100              # 最近 100 条
journalctl -p err                       # 只看错误级别日志
journalctl --disk-usage                 # 查看日志占用空间
sudo journalctl --vacuum-size=500M      # 清理日志至 500MB 以内
```

### 5.3 传统日志文件 — `/var/log/`

```bash
tail -f /var/log/syslog         # Debian/Ubuntu 系统日志
tail -f /var/log/messages       # RHEL/CentOS 系统日志
tail -f /var/log/auth.log       # 认证日志（登录记录）
tail -f /var/log/nginx/access.log  # nginx 访问日志
tail -f /var/log/nginx/error.log   # nginx 错误日志
```

### 5.4 定时任务 — `crontab` ⭐

```bash
crontab -e                      # 编辑当前用户的定时任务
crontab -l                      # 查看当前用户的定时任务
crontab -r                      # 删除所有定时任务

# 格式：分 时 日 月 周 命令
# * * * * * command
# | | | | |
# | | | | └─ 星期 (0-7, 0和7都表示周日)
# | | | └─── 月份 (1-12)
# | | └───── 日期 (1-31)
# | └─────── 小时 (0-23)
# └───────── 分钟 (0-59)

# 常用示例
0 2 * * * /backup/script.sh             # 每天凌晨 2 点执行备份
*/5 * * * * /check.sh                   # 每 5 分钟执行一次
0 9 * * 1-5 /work/task.sh               # 工作日早上 9 点
0 0 1 * * /monthly/report.sh            # 每月 1 号凌晨执行
@reboot /startup/script.sh              # 系统启动时执行
@daily /daily/cleanup.sh                # 每天一次

# 查看 cron 日志
grep CRON /var/log/syslog
```

### 5.5 环境变量

```bash
# 查看
env                             # 查看所有环境变量
printenv                        # 同上
echo $PATH                      # 查看 PATH
echo $HOME                      # 查看 HOME

# 临时设置（仅当前会话）
export MY_VAR="hello"
export PATH=$PATH:/new/path

# 永久设置
# 1. 用户级别：编辑 ~/.bashrc 或 ~/.profile
echo 'export PATH=$PATH:/my/custom/path' >> ~/.bashrc
source ~/.bashrc                # 立即生效

# 2. 系统级别：编辑 /etc/environment 或 /etc/profile
```

### 5.6 内核与模块

```bash
uname -a                        # 查看系统信息（内核版本等）
uname -r                        # 只看内核版本
cat /proc/version               # 内核版本详细信息

lsmod                           # 列出当前加载的内核模块
sudo modprobe module_name       # 加载模块
sudo modprobe -r module_name    # 移除模块
modinfo module_name             # 查看模块信息
```

### 5.7 性能监控

```bash
# 内存
free -h                         # 内存使用情况
cat /proc/meminfo               # 详细内存信息

# CPU
lscpu                           # CPU 信息
cat /proc/cpuinfo               # 详细 CPU 信息
uptime                          # 系统运行时间 + 平均负载

# 磁盘 I/O
iostat -x 1                     # 磁盘 I/O 统计（每秒刷新）
iotop                           # 类似 top 的磁盘 I/O 监控

# 综合
vmstat 1                        # 虚拟内存统计（每秒刷新）
sar -u 1 5                      # CPU 使用率（5 次，每秒 1 次）
sar -r                          # 内存使用率

# 实时进程
htop                            # 最推荐
top -c                          # 显示完整命令
```

### 5.8 时间与日期

```bash
date                            # 显示当前时间
date "+%Y-%m-%d %H:%M:%S"      # 格式化：2025-01-15 14:30:00
date -d "7 days ago" "+%Y-%m-%d"  # 7 天前的日期
date -d "next Friday"             # 下周五
sudo date -s "2025-01-15 14:30"   # 设置系统时间

timedatectl                     # 查看时间、时区信息
timedatectl list-timezones      # 列出所有时区
sudo timedatectl set-timezone Asia/Shanghai  # 设置时区

cal                             # 显示日历
cal 2025                        # 显示全年日历
```

### 5.9 系统信息

```bash
hostname                        # 主机名
hostnamectl                     # 详细主机信息
sudo hostnamectl set-hostname new-name  # 修改主机名

cat /etc/os-release             # 操作系统版本信息
lsb_release -a                  # 发行版信息

lscpu                           # CPU 信息
lsmem                           # 内存信息
lspci                           # PCI 设备
lsusb                           # USB 设备
lshw -short                     # 硬件概览
```

---

## 六、安全基础

### 6.1 SSH 安全

```bash
# 生成 SSH 密钥对
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
ssh-keygen -t ed25519 -C "your_email@example.com"  # 更现代推荐

# 复制公钥到远程服务器（免密码登录）
ssh-copy-id user@host
# 或手动：cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

# SSH 配置文件安全加固 (/etc/ssh/sshd_config)
# Port 2222                    # 修改默认端口
# PermitRootLogin no           # 禁止 root 直接登录
# PasswordAuthentication no    # 只允许密钥登录
# MaxAuthTries 3               # 限制尝试次数

sudo systemctl restart sshd    # 修改后重启 SSH 服务
```

### 6.2 防火墙

```bash
# UFW（Ubuntu/Debian，推荐新手使用）
sudo ufw enable                         # 启用防火墙
sudo ufw disable                        # 禁用
sudo ufw status                         # 查看状态
sudo ufw status verbose                 # 详细状态
sudo ufw allow 22                       # 允许 22 端口
sudo ufw allow 80/tcp                   # 允许 TCP 80
sudo ufw allow 443                      # 允许 443
sudo ufw allow from 192.168.1.0/24      # 允许整个子网
sudo ufw deny 23                        # 拒绝 23 端口
sudo ufw delete allow 80                # 删除规则
sudo ufw default deny incoming          # 默认拒绝入站
sudo ufw default allow outgoing         # 默认允许出站

# firewalld（RHEL/CentOS/Fedora）
sudo systemctl start firewalld
sudo firewall-cmd --state
sudo firewall-cmd --list-all
sudo firewall-cmd --add-port=80/tcp --permanent
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --reload

# iptables（底层，功能最强但也最复杂）
sudo iptables -L                    # 查看规则
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT  # 允许 80 端口
sudo iptables-save > /etc/iptables/rules.v4         # 保存规则
```

### 6.3 用户安全

```bash
# 检查登录失败记录
sudo lastb                       # 查看失败的登录尝试
sudo cat /var/log/auth.log | grep "Failed password"

# 查看当前登录用户
who
w

# 查看谁有 sudo 权限
grep 'sudo' /etc/group

# 检查无密码用户
sudo awk -F: '($2 == "") {print $1}' /etc/shadow

# 检查可登录的非系统用户
awk -F: '$3 >= 1000 && $7 != "/usr/sbin/nologin" && $7 != "/bin/false" {print $1}' /etc/passwd
```

### 6.4 Fail2Ban — 防暴力破解

```bash
# 安装
sudo apt install fail2ban           # Debian/Ubuntu
sudo yum install fail2ban           # CentOS/RHEL

# 基本配置
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
sudo systemctl enable fail2ban
sudo systemctl start fail2ban

# 查看状态
sudo fail2ban-client status
sudo fail2ban-client status sshd    # 查看 SSH 监狱状态

# 查看被封禁的 IP
sudo fail2ban-client status sshd | grep "Banned IP"
```

### 6.5 文件完整性

```bash
# 查找 SUID / SGID 文件（可能有安全风险）
find / -perm -4000 -type f 2>/dev/null     # SUID
find / -perm -2000 -type f 2>/dev/null     # SGID

# 查找全局可写文件
find / -perm -2 ! -type l -ls 2>/dev/null

# 查找无主文件
find / -nouser -o -nogroup 2>/dev/null
```

---

## 七、实战场景

### 7.1 创建新用户并授予 sudo 权限

```bash
# 1. 创建用户
sudo useradd -m -s /bin/bash newuser
sudo passwd newuser                    # 设置密码

# 2. 授予 sudo 权限
sudo usermod -aG sudo newuser          # Debian/Ubuntu
sudo usermod -aG wheel newuser         # CentOS/RHEL

# 3. 验证
su - newuser
sudo whoami                            # 应输出 root
```

### 7.2 安装 Nginx 并设置开机自启

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install nginx
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl status nginx

# 防火墙放行
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
```

### 7.3 挂载新硬盘

```bash
# 1. 查看新硬盘
lsblk                                  # 假设新硬盘为 /dev/sdb

# 2. 分区
sudo fdisk /dev/sdb
# n → p → 默认 → 默认 → w（创建一个主分区使用全部空间）

# 3. 格式化
sudo mkfs.ext4 /dev/sdb1

# 4. 创建挂载点并挂载
sudo mkdir /data
sudo mount /dev/sdb1 /data

# 5. 设置开机自动挂载
# 获取 UUID
sudo blkid /dev/sdb1
# 编辑 /etc/fstab，添加：
# UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx  /data  ext4  defaults  0  2

# 6. 验证
sudo mount -a                           # 测试 fstab
df -h /data
```

### 7.4 排查常见问题

```bash
# 端口被占用
sudo ss -tulnp | grep :80               # 查看谁在用 80 端口
sudo lsof -i :80                        # 同上
sudo kill -9 $(sudo lsof -t -i:80)      # 杀掉占用 80 端口的进程

# 磁盘空间不足
df -h                                   # 查看哪个分区满了
du -sh /* 2>/dev/null | sort -rh | head -10  # 找出根目录下大文件夹
sudo journalctl --vacuum-size=200M      # 清理日志
sudo apt autoremove --purge             # 清理无用包

# 内存不足（OOM）
dmesg | grep -i "out of memory"         # 查看 OOM 日志
free -h                                 # 查看内存
ps aux --sort=-%mem | head -10          # 找出内存占用最高的进程

# 进程僵死
ps aux | grep Z                         # 查找僵尸进程（状态为 Z）

# 网络不通
ping 8.8.8.8                            # 测试外网
ping google.com                         # 测试 DNS
ip route                                # 查看路由
cat /etc/resolv.conf                    # 查看 DNS 配置
```

### 7.5 源码编译安装软件

```bash
# 典型流程
wget https://example.com/software.tar.gz
tar -xzvf software.tar.gz
cd software/

# 检查依赖并配置
./configure --prefix=/usr/local/software

# 编译（-j 指定并行编译线程数，通常用 CPU 核数）
make -j$(nproc)

# 安装
sudo make install

# 添加到 PATH（~/.bashrc）
echo 'export PATH=/usr/local/software/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

### 7.6 创建 Swap 交换空间

```bash
# 创建 4GB 的 Swap 文件
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# 永久生效
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

# 验证
swapon --show
free -h
```

---

## 八、Git 版本控制基础

Git 是目前最流行的分布式版本控制系统，无论是个人项目还是团队协作都离不开它。

### 8.1 Git 核心概念

```
工作区 (Working Directory)    ← 你正在编辑的文件
    ↓ git add
暂存区 (Staging Area / Index) ← 准备提交的更改
    ↓ git commit
本地仓库 (Local Repository)   ← 提交历史记录
    ↓ git push
远程仓库 (Remote Repository)  ← GitHub / GitLab 等
```

### 8.2 安装与初始配置

```bash
# 安装 Git
sudo apt install git                  # Debian/Ubuntu
sudo yum install git                  # CentOS/RHEL

# 初始配置（必须设置！）
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
git config --global init.defaultBranch main  # 默认分支名设为 main
git config --list                     # 查看所有配置

# 配置别名（推荐）
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.st status
git config --global alias.lg "log --oneline --graph --all"
```

### 8.3 创建仓库与基本工作流

```bash
# 初始化新仓库
git init                              # 在当前目录创建 .git 仓库

# 克隆远程仓库
git clone https://github.com/user/repo.git
git clone git@github.com:user/repo.git  # SSH 方式（需配置密钥）

# ⭐ 日常开发工作流
git status                            # 查看当前状态（最常用！）
git add file.txt                      # 将文件添加到暂存区
git add .                             # 添加所有更改
git add -p                            # 交互式选择要暂存的更改
git commit -m "feat: add login page"  # 提交到本地仓库
git push origin main                  # 推送到远程仓库
git pull origin main                  # 拉取远程更新
```

### 8.4 查看历史与差异

```bash
git log                               # 查看提交历史
git log --oneline                     # 每行一条（简洁版）
git log --graph --oneline --all       # 图形化分支历史
git log -p                            # 显示每次提交的具体修改
git log --author="John"               # 按作者筛选
git log --since="2025-01-01"          # 按时间筛选

git diff                              # 工作区 vs 暂存区
git diff --staged                     # 暂存区 vs 上次提交
git diff HEAD                         # 工作区 vs 上次提交（所有未提交更改）
git diff branch1..branch2             # 两个分支的差异

git show commit-hash                  # 查看某次提交的详细信息
git blame file.txt                    # 查看每行代码是谁写的
```

### 8.5 分支管理 ⭐

```bash
git branch                            # 列出本地分支
git branch -a                         # 列出所有分支（含远程）
git branch feature-login              # 创建新分支
git checkout feature-login            # 切换到分支
git checkout -b feature-login         # 创建并切换（二合一）
git switch feature-login              # Git 2.23+ 推荐方式
git switch -c feature-login           # 创建并切换（新语法）

git merge feature-login               # 将 feature-login 合并到当前分支
git merge --no-ff feature-login       # 禁止快进合并（保留分支历史）
git branch -d feature-login           # 删除已合并的分支
git branch -D feature-login           # 强制删除分支

git branch -m old-name new-name       # 重命名分支
```

### 8.6 撤销操作

```bash
# 撤销工作区修改（文件回到上次提交的状态）
git checkout -- file.txt              # 旧语法
git restore file.txt                  # 新语法（Git 2.23+）

# 撤销暂存区的文件
git reset HEAD file.txt               # 旧语法
git restore --staged file.txt         # 新语法

# 修改最后一次提交（提交信息错了 / 漏了文件）
git commit --amend -m "new message"

# 撤销提交（保留更改在工作区）
git reset --soft HEAD~1               # 撤销最近 1 次提交，更改回到暂存区

# 撤销提交并丢弃更改
git reset --hard HEAD~1               # ⚠️ 不可恢复！更改全部丢失

# 用新提交来撤销（安全方式）
git revert HEAD                       # 创建一个"反向"提交来撤销
```

### 8.7 远程仓库操作

```bash
git remote -v                         # 查看远程仓库地址
git remote add origin <url>           # 添加远程仓库
git remote remove origin              # 移除远程仓库

git push origin main                  # 推送
git push -u origin main               # 首次推送并设置上游（之后只需 git push）
git push --force-with-lease           # 安全强制推送（比 --force 安全）

git fetch origin                      # 拉取远程信息（不合并）
git pull origin main                  # 拉取并合并（= fetch + merge）
git pull --rebase origin main         # 拉取并变基（保持线性历史，推荐）
```

### 8.8 储藏与清理

```bash
git stash                             # 暂存当前工作区修改
git stash save "WIP: fixing bug"      # 带描述的暂存
git stash list                        # 列出所有储藏
git stash pop                         # 恢复最近的储藏并删除记录
git stash pop stash@{1}               # 恢复指定储藏
git stash drop                        # 删除最近的储藏
git stash clear                       # 清空所有储藏
```

### 8.9 标签

```bash
git tag v1.0.0                        # 创建轻量标签
git tag -a v1.0.0 -m "Release v1.0"   # 创建附注标签
git tag                               # 列出所有标签
git push origin v1.0.0                # 推送单个标签
git push origin --tags                # 推送所有标签
git tag -d v1.0.0                     # 删除本地标签
```

### 8.10 .gitignore 文件

```bash
# .gitignore 示例
node_modules/          # 忽略整个目录
*.log                  # 忽略所有 .log 文件
.env                   # 忽略 .env 文件
!.env.example          # 但不忽略 .env.example
dist/                  # 忽略构建输出
```

### 8.11 提交信息规范（Conventional Commits）

```
feat: 添加用户登录功能         # 新功能
fix: 修复密码验证的 bug        # 修复
docs: 更新 API 文档            # 文档
style: 修复代码格式            # 格式（不影响逻辑）
refactor: 重构用户模块         # 重构
test: 添加登录测试             # 测试
chore: 更新依赖版本            # 杂项
```

---

## 九、Docker 基础入门

Docker 是一个容器化平台，让你可以把应用和其依赖打包在一起，在任何 Linux 机器上运行。

### 9.1 核心概念

```
镜像 (Image)   = 应用程序的"模板"（类似 ISO 文件）
容器 (Container)= 镜像的运行实例（类似虚拟机，但更轻量）
仓库 (Registry) = 存储和分发镜像的地方（Docker Hub）
Dockerfile     = 构建镜像的"配方"文件
docker-compose = 编排多个容器的工具
```

### 9.2 安装 Docker

```bash
# Ubuntu/Debian（使用官方脚本，最简单）
curl -fsSL https://get.docker.com | sudo sh

# 或手动安装
sudo apt update
sudo apt install docker.io docker-compose-v2

# 将用户加入 docker 组（免 sudo）
sudo usermod -aG docker $USER
# 退出重新登录后生效

# 验证安装
docker --version
docker run hello-world
```

### 9.3 镜像管理

```bash
docker images                          # 列出本地镜像
docker pull nginx:latest              # 从 Docker Hub 拉取镜像
docker pull nginx:1.25                # 拉取指定版本
docker rmi nginx:latest               # 删除镜像
docker rmi $(docker images -q)        # 删除所有镜像
docker image prune                    # 删除未使用的镜像
docker search mysql                   # 搜索 Docker Hub 上的镜像
```

### 9.4 容器管理 ⭐

```bash
# 运行容器
docker run -d --name mynginx -p 8080:80 nginx
# -d        = 后台运行（detach）
# --name    = 给容器起个名字
# -p 8080:80 = 将主机的 8080 端口映射到容器的 80 端口

docker run -it ubuntu bash            # 交互式进入容器
docker run -d -v /host/path:/container/path nginx  # 挂载目录（数据持久化）
docker run -d -e MYSQL_ROOT_PASSWORD=123456 mysql  # 设置环境变量
docker run -d --restart=always nginx  # 容器退出后自动重启

# 查看容器
docker ps                             # 查看运行中的容器
docker ps -a                          # 查看所有容器（包括已停止的）
docker ps -q                          # 只显示容器 ID

# 容器操作
docker stop mynginx                   # 停止容器
docker start mynginx                  # 启动已停止的容器
docker restart mynginx                # 重启
docker rm mynginx                     # 删除容器（需先停止）
docker rm -f mynginx                  # 强制删除运行中的容器
docker rm $(docker ps -aq)            # 删除所有容器

# 进入容器
docker exec -it mynginx bash          # 进入运行中的容器
docker logs mynginx                   # 查看容器日志
docker logs -f mynginx                # 实时追踪日志
docker logs --tail 100 mynginx        # 最近 100 行
docker inspect mynginx                # 查看容器详细信息
docker stats                          # 实时查看容器资源使用
```

### 9.5 Dockerfile — 构建自己的镜像

```dockerfile
# Dockerfile 示例：一个简单的 Node.js 应用
FROM node:18-alpine                   # 基础镜像

WORKDIR /app                          # 设置工作目录

COPY package*.json ./                 # 先复制依赖文件（利用缓存）
RUN npm install                       # 安装依赖

COPY . .                              # 复制源代码

EXPOSE 3000                           # 声明端口

CMD ["node", "index.js"]              # 启动命令
```

```bash
# 构建镜像
docker build -t myapp:v1 .            # -t 指定名称和标签，. 表示当前目录
docker build -t myapp:v1 --no-cache . # 不使用缓存重新构建

# 运行自己的镜像
docker run -d -p 3000:3000 --name myapp myapp:v1
```

### 9.6 Docker Compose — 多容器编排

```yaml
# docker-compose.yml 示例：WordPress + MySQL
version: '3.8'
services:
  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: secret
      MYSQL_DATABASE: wordpress
    volumes:
      - db_data:/var/lib/mysql

  wordpress:
    image: wordpress:latest
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: root
      WORDPRESS_DB_PASSWORD: secret
      WORDPRESS_DB_NAME: wordpress
    depends_on:
      - db

volumes:
  db_data:
```

```bash
docker-compose up -d                  # 启动所有服务（后台）
docker-compose down                   # 停止并删除所有服务
docker-compose down -v                # 同时删除数据卷
docker-compose ps                     # 查看服务状态
docker-compose logs -f                # 查看所有服务日志
docker-compose restart                # 重启所有服务
```

### 9.7 常用场景

```bash
# 运行 MySQL
docker run -d --name mysql \
  -e MYSQL_ROOT_PASSWORD=password \
  -p 3306:3306 \
  -v mysql_data:/var/lib/mysql \
  mysql:8.0

# 运行 Redis
docker run -d --name redis -p 6379:6379 redis:7

# 运行 Nginx（挂载自定义配置）
docker run -d --name nginx -p 80:80 \
  -v ./nginx.conf:/etc/nginx/nginx.conf \
  -v ./html:/usr/share/nginx/html \
  nginx

# 清理（释放磁盘空间）
docker system prune -a               # ⚠️ 删除所有未使用的镜像、容器、网络
docker volume prune                   # 删除未使用的数据卷
```

---

## 十、数据库基础

### 10.1 MySQL

#### 安装

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install mysql-server
sudo systemctl start mysql
sudo systemctl enable mysql

# 安全初始化（设置 root 密码等）
sudo mysql_secure_installation
```

#### 基本操作

```sql
-- 登录
mysql -u root -p

-- 数据库操作
SHOW DATABASES;                              -- 查看所有数据库
CREATE DATABASE mydb;                         -- 创建数据库
CREATE DATABASE mydb CHARACTER SET utf8mb4;    -- 指定字符集（推荐）
USE mydb;                                     -- 切换数据库
DROP DATABASE mydb;                           -- 删除数据库

-- 表操作
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SHOW TABLES;                                  -- 查看所有表
DESCRIBE users;                               -- 查看表结构
ALTER TABLE users ADD COLUMN age INT;         -- 添加列
DROP TABLE users;                             -- 删除表

-- 数据操作（CRUD）
INSERT INTO users (username, email) VALUES ('john', 'john@example.com');
INSERT INTO users (username, email) VALUES
    ('jane', 'jane@example.com'),
    ('bob', 'bob@example.com');

SELECT * FROM users;
SELECT id, username FROM users WHERE id = 1;
SELECT * FROM users WHERE email LIKE '%@example.com';
SELECT * FROM users ORDER BY created_at DESC LIMIT 10;

UPDATE users SET email = 'newemail@example.com' WHERE id = 1;
DELETE FROM users WHERE id = 1;

-- 用户管理
CREATE USER 'appuser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON mydb.* TO 'appuser'@'localhost';
FLUSH PRIVILEGES;                             -- 刷新权限
```

#### 备份与恢复

```bash
# 备份
mysqldump -u root -p mydb > mydb_backup.sql
mysqldump -u root -p --all-databases > all_backup.sql

# 恢复
mysql -u root -p mydb < mydb_backup.sql
```

### 10.2 PostgreSQL

#### 安装

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql

# 切换到 postgres 用户
sudo -i -u postgres
psql                                    # 进入 PostgreSQL 命令行
```

#### 基本操作

```sql
-- 在 psql 中
\l                                      -- 列出所有数据库
CREATE DATABASE mydb;                   -- 创建数据库
\c mydb                                 -- 连接到数据库
\dt                                     -- 列出所有表
\d users                                -- 查看表结构

-- 创建表
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- 数据操作（与 MySQL 类似）
INSERT INTO users (username, email) VALUES ('john', 'john@example.com');
SELECT * FROM users WHERE id = 1;
UPDATE users SET email = 'new@example.com' WHERE id = 1;
DELETE FROM users WHERE id = 1;
```

#### 备份与恢复

```bash
# 备份
pg_dump mydb > mydb_backup.sql
pg_dump -U postgres mydb > mydb_backup.sql

# 恢复
psql mydb < mydb_backup.sql
psql -U postgres mydb < mydb_backup.sql
```

### 10.3 SQLite（零配置、嵌入式）

```bash
# 安装
sudo apt install sqlite3

# 使用
sqlite3 mydb.sqlite                      # 创建/打开数据库
# SQLite 内：
.tables                                  # 查看所有表
.schema users                            # 查看表结构
.mode column                             # 列对齐输出
.headers on                              # 显示列头
.quit                                    # 退出
```

---

## 十一、网络排错深入

### 11.1 连通性测试

```bash
# ping — 测试网络层连通性
ping -c 4 8.8.8.8                       # 测试外网连通
ping -c 4 google.com                    # 测试 DNS 解析+连通

# traceroute — 追踪数据包路径
traceroute google.com                   # 显示每一跳的路由
traceroute -n google.com                # 不解析主机名（更快）
traceroute -p 80 google.com             # 指定端口

# mtr — ping + traceroute 的结合（推荐）
mtr google.com                          # 实时显示路由和丢包率
mtr -r -c 10 google.com                 # 报告模式，发 10 个包
mtr -n google.com                       # 不解析主机名
```

### 11.2 DNS 排错

```bash
# 测试 DNS 解析
nslookup google.com                     # 简单查询
nslookup google.com 8.8.8.8             # 指定 DNS 服务器

# dig — 详细 DNS 诊断
dig google.com                          # 完整 DNS 查询
dig google.com +short                   # 只显示 IP
dig -x 8.8.8.8                          # 反向解析（IP → 域名）
dig google.com ANY                      # 所有记录类型
dig google.com +trace                   # 追踪 DNS 解析全过程
dig @8.8.8.8 google.com                 # 指定 DNS 服务器查询

# 查看 DNS 配置
cat /etc/resolv.conf                    # 当前 DNS 设置
systemd-resolve --status                # systemd 管理的 DNS（Ubuntu 18+）

# hosts 文件
cat /etc/hosts                          # 本地 DNS 映射
sudo vim /etc/hosts                     # 编辑（用于本地测试域名）
```

### 11.3 端口与连接诊断

```bash
# 查看监听端口
ss -tuln                                # TCP/UDP 监听端口
ss -tulnp                               # 带进程名
ss -t state established                 # 已建立的连接
ss -s                                   # 连接摘要统计

# 查看具体端口
ss -tuln | grep ':80 '                  # 谁在监听 80 端口
sudo lsof -i :80                        # 同上，更详细
sudo lsof -i TCP:80                     # 只看 TCP
sudo fuser 80/tcp                       # 另一种方式

# 测试端口连通性
nc -zv 192.168.1.1 22                   # TCP 端口是否开放
nc -zvu 192.168.1.1 53                  # UDP 端口测试
nc -zv -w 3 google.com 443              # 3 秒超时

# telnet — 传统但仍有用的端口测试
telnet example.com 80                   # 测试 HTTP 端口
# GET / HTTP/1.1 然后按两次回车来测试 Web 服务
```

### 11.4 tcpdump — 网络抓包 ⭐

```bash
# 基础抓包（需要 sudo）
sudo tcpdump -i eth0                    # 监听 eth0 接口
sudo tcpdump -i any                     # 监听所有接口
sudo tcpdump -i any -n                  # 不解析主机名和端口名

# 过滤
sudo tcpdump -i any port 80             # 只抓 80 端口
sudo tcpdump -i any port 80 or port 443 # 80 或 443
sudo tcpdump -i any host 192.168.1.100  # 特定主机
sudo tcpdump -i any src host 10.0.0.1   # 源地址
sudo tcpdump -i any dst host 10.0.0.1   # 目标地址
sudo tcpdump -i any tcp                 # 只抓 TCP 包
sudo tcpdump -i any icmp                # 只抓 ICMP（ping）
sudo tcpdump -i any 'tcp[tcpflags] & (tcp-syn|tcp-fin) != 0'  # SYN 或 FIN 包

# 保存与读取
sudo tcpdump -i any -w capture.pcap     # 保存到文件
sudo tcpdump -i any -w capture.pcap -C 100  # 每 100MB 分割
tcpdump -r capture.pcap                 # 读取文件
tcpdump -r capture.pcap -n port 80      # 读取时过滤

# 实用场景
sudo tcpdump -i any -n 'port 443'       # 检查 HTTPS 请求是否发出
sudo tcpdump -i any -n 'arp'            # 检查 ARP 请求
```

### 11.5 HTTP 调试

```bash
# curl 详细调试
curl -v https://api.example.com         # 查看完整请求和响应
curl -I https://example.com             # 只看响应头
curl -w "\n%{http_code}\n" example.com  # 只输出 HTTP 状态码
curl -o /dev/null -s -w "%{http_code}\n" example.com  # 静默获取状态码

# 测试 API
curl -X POST https://api.example.com \
  -H "Content-Type: application/json" \
  -d '{"key":"value"}' \
  -w "\nTime: %{time_total}s\n"         # 显示请求耗时

# HTTPie（更友好的 curl 替代，需安装）
# http GET example.com
# http POST example.com name=john
```

### 11.6 带宽与性能测试

```bash
# iperf3 — 网络带宽测试
# 服务器端：iperf3 -s
# 客户端：iperf3 -c 192.168.1.100

# speedtest-cli — 互联网速度测试
# pip install speedtest-cli
speedtest-cli

# iftop — 实时流量监控
sudo iftop -i eth0

# nethogs — 按进程查看带宽占用
sudo nethogs eth0
```

### 11.7 网络配置诊断

```bash
# 查看网络接口
ip addr show                            # IP 地址
ip link show                            # 接口状态
ip route show                           # 路由表
ip neigh show                           # ARP 缓存

# 网卡状态
ethtool eth0                            # 网卡详细信息
ethtool -S eth0                         # 网卡统计（丢包/错误等）

# 连接数统计
ss -s                                   # 连接总数
ss -tan state time-wait | wc -l         # TIME-WAIT 连接数
ss -tan state established | wc -l       # 已建立连接数

# 防火墙规则检查
sudo iptables -L -n -v                  # iptables 规则
sudo ufw status verbose                 # UFW 状态
sudo firewall-cmd --list-all            # firewalld 状态
```

---

## 十二、Vim/Nano 编辑器详解

### 12.1 Vim 完整操作手册

Vim 是 Linux 上最强大的文本编辑器。学习曲线陡峭，但一旦掌握，效率极高。

#### 模式概念

```
普通模式 (Normal)   ← 默认模式，用于导航和操作（按 Esc 回到此模式）
插入模式 (Insert)   ← 编辑文字（按 i / a / o 等进入）
可视模式 (Visual)   ← 选择文本（按 v / V / Ctrl+v 进入）
命令模式 (Command)  ← 执行命令（按 : 进入）
```

#### 基础移动

```
h / j / k / l    = 左 / 下 / 上 / 右
w                = 下一个单词开头
b                = 上一个单词开头
e                = 单词结尾
0                = 行首
^                = 行首第一个非空字符
$                = 行尾
gg               = 文件开头
G                = 文件结尾
:数字            = 跳转到指定行（如 :42 跳到第 42 行）
Ctrl+f           = 下一页
Ctrl+b           = 上一页
Ctrl+d           = 下半页
Ctrl+u           = 上半页
{                = 上一段落
}                = 下一段落
%                = 跳到匹配的括号
```

#### 插入模式

```
i                = 光标前插入
a                = 光标后插入
I                = 行首插入
A                = 行尾插入
o                = 下一行插入（开新行）
O                = 上一行插入（开新行）
s                = 删除当前字符并插入
S                = 删除当前行并插入
cw               = 删除到词尾并插入
```

#### 编辑操作

```
x                = 删除光标处字符
dw               = 删除一个单词
dd               = 删除当前行
d$ / D           = 删除到行尾
d0               = 删除到行首
dG               = 删除到文件尾
dgg              = 删除到文件头
yy               = 复制当前行
yw               = 复制一个单词
y$               = 复制到行尾
p                = 光标后粘贴
P                = 光标前粘贴
u                = 撤销
Ctrl+r           = 重做
.                = 重复上一次操作（超级有用！）
>>               = 增加缩进
<<               = 减少缩进
~                = 切换大小写
```

#### 搜索与替换

```
/pattern         = 向下搜索
?pattern         = 向上搜索
n                = 下一个匹配
N                = 上一个匹配
*                = 搜索光标下的单词（向下）
#                = 搜索光标下的单词（向上）

:s/old/new/g     = 当前行全局替换
:%s/old/new/g    = 整个文件替换
:%s/old/new/gc   = 整个文件替换（逐个确认）
:5,10s/old/new/g = 第 5-10 行替换
```

#### 可视模式

```
v                = 字符选择
V                = 行选择
Ctrl+v           = 块选择（列编辑）

# 选中后可以：
# d = 删除   y = 复制   > = 增加缩进   < = 减少缩进
# :s/old/new/g = 在选中范围内替换
```

#### 窗口与标签页

```
:split file.txt  = 水平分割窗口
:vsplit file.txt = 垂直分割窗口
Ctrl+w h/j/k/l   = 窗口间移动
Ctrl+w q         = 关闭当前窗口
:tabnew file.txt = 新标签页
gt               = 下一个标签页
gT               = 上一个标签页
```

#### 文件与命令操作

```
:w               = 保存
:w file.txt      = 另存为
:q               = 退出
:q!              = 强制退出（不保存）
:wq / :x / ZZ    = 保存并退出
:e file.txt      = 打开文件
:r file.txt      = 将文件内容插入当前位置
:!command        = 执行 Shell 命令
:r !command      = 将命令输出插入当前位置
```

#### Vim 配置 (~/.vimrc)

```vim
" 基础配置
set number               " 显示行号
set relativenumber       " 显示相对行号
set cursorline           " 高亮当前行
set autoindent           " 自动缩进
set expandtab            " Tab 转空格
set tabstop=4            " Tab 显示宽度
set shiftwidth=4         " 缩进宽度
set hlsearch             " 高亮搜索结果
set incsearch            " 增量搜索
set ignorecase           " 搜索忽略大小写
set smartcase            " 有大写时不忽略大小写
syntax on                " 语法高亮
```

### 12.2 Nano — 新手友好的编辑器

如果你觉得 Vim 太难，Nano 是开箱即用的选择。

```bash
nano file.txt               # 打开文件
nano +100 file.txt          # 打开并跳转到第 100 行

# Nano 快捷键（^ 表示 Ctrl）
# ^G  = 帮助          ^O  = 保存文件
# ^X  = 退出          ^W  = 搜索
# ^K  = 剪切当前行    ^U  = 粘贴
# ^\  = 查找并替换    ^C  = 显示光标位置
# ^_  = 跳转到行号     M-U = 撤销（M = Alt）
# M-E = 重做          M-A = 选择文本
# M-6 = 复制当前行
```

---

## 十三、Shell 美化与效率工具

以下工具可以大幅提升终端使用体验，全部可选安装。

### 13.1 Oh My Zsh — Zsh 框架

```bash
# 安装 Zsh
sudo apt install zsh

# 安装 Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# 常用插件（在 ~/.zshrc 中配置）
# plugins=(git docker z sudo extract history zsh-autosuggestions zsh-syntax-highlighting)

# 主题（推荐 powerlevel10k）
# ZSH_THEME="powerlevel10k/powerlevel10k"
```

### 13.2 fzf — 模糊搜索神器 ⭐

```bash
# 安装
sudo apt install fzf                    # Debian/Ubuntu

# 使用
fzf                                     # 模糊搜索当前目录文件
Ctrl+T                                  # 模糊搜索并粘贴文件路径
Ctrl+R                                  # 模糊搜索历史命令（替代默认 Ctrl+R）
vim $(fzf)                              # 模糊搜索并用 vim 打开

# 与 git 配合
git checkout $(git branch | fzf)        # 模糊选择分支切换
git add $(git ls-files -m | fzf)        # 模糊选择文件暂存
```

### 13.3 现代命令替代品

```bash
# bat — 带语法高亮和行号的 cat（需安装: sudo apt install bat）
bat file.txt                    # 语法高亮显示
bat --show-all file.txt         # 显示不可见字符
# 注意：Ubuntu 上命令可能是 batcat

# exa / eza — 现代化的 ls（需安装: sudo apt install exa）
exa -la                         # 替代 ls -la
exa --tree --level=2            # 树形显示
exa -l --git                    # 显示 git 状态

# ripgrep (rg) — 超快的 grep 替代品（需安装: sudo apt install ripgrep）
rg "keyword"                    # 递归搜索
rg -l "keyword"                 # 只列出文件名
rg --type py "def main"         # 只在 Python 文件中搜索
rg -C 3 "error"                 # 显示上下文

# fd — 超快的 find 替代品（需安装: sudo apt install fd-find）
fd "*.txt"                      # 替代 find . -name "*.txt"
fd -e py                        # 所有 .py 文件
fd -t d                         # 所有目录

# zoxide — 智能目录跳转（需安装: sudo apt install zoxide）
z project                       # 跳转到最常访问的匹配目录
zi                              # 交互式选择
# 安装后需在 ~/.bashrc 或 ~/.zshrc 中初始化
```

### 13.4 tldr — 简化的命令帮助

```bash
# 安装
sudo apt install tldr

# 使用（替代冗长的 man 手册，提供最常用示例）
tldr tar                        # tar 常用示例
tldr git                        # git 常用示例
tldr find                       # find 常用示例
tldr rsync                      # rsync 常用示例
```

### 13.5 broot — 交互式目录树

```bash
# 安装（推荐用 cargo 或官方安装脚本）
# 使用：直接运行 broot，用方向键导航
broot                           # 交互式目录浏览
```

### 13.6 其他实用工具

```bash
# htop — 彩色进程管理器
sudo apt install htop

# ncdu — 可视化磁盘使用分析（类似 du 但可交互）
sudo apt install ncdu
ncdu /                          # 分析根目录空间占用

# jq — 命令行 JSON 处理器
sudo apt install jq
curl -s api.example.com/data | jq .        # 格式化 JSON
curl -s api.example.com/data | jq '.items[].name'  # 提取字段

# httpie — 更友好的 HTTP 客户端
sudo apt install httpie
http GET example.com
http POST example.com name=john

# tmux — 终端复用器（保持会话）
sudo apt install tmux

# thefuck — 自动修正打错的命令
sudo apt install thefuck
# 打错命令后输入 fuck，自动修正
```

---

## 十四、常用快捷键

### 终端快捷键

| 快捷键 | 功能 |
|-------|------|
| `Ctrl + C` | 终止当前命令 |
| `Ctrl + D` | 退出终端 / EOF |
| `Ctrl + Z` | 暂停当前进程（放到后台） |
| `Ctrl + L` | 清屏（相当于 `clear`） |
| `Ctrl + A` | 光标移到行首 |
| `Ctrl + E` | 光标移到行尾 |
| `Ctrl + U` | 删除光标前所有内容 |
| `Ctrl + K` | 删除光标后所有内容 |
| `Ctrl + W` | 删除光标前一个单词 |
| `Ctrl + R` | 搜索历史命令（最常用！多按几次翻找） |
| `Ctrl + _` | 撤销上次编辑 |
| `Tab` | 自动补全 |
| `Tab Tab` | 列出所有可能的补全 |
| `↑ / ↓` | 浏览历史命令 |
| `!!` | 重复上一条命令 |
| `!$` | 上一条命令的最后一个参数 |
| `!nginx` | 执行最近以 nginx 开头的命令 |
| `Alt + .` | 插入上一条命令的最后一个参数 |

---

## 十五、章节练习题汇总

### 文件与目录操作

1. 在 `/tmp` 下创建目录结构 `project/src` 和 `project/docs`（一条命令完成）
2. 查找 `/var/log` 下所有 `.log` 文件，按大小排序，显示最大的 5 个
3. 把 `/home` 下所有 30 天前的 `.tmp` 文件找出来并删除

### 文本处理

1. 统计 Apache/Nginx 访问日志中访问次数最多的 10 个 IP
2. 从一个 CSV 文件中提取第 2 列和第 4 列，保存为新文件
3. 用 `grep` 找出配置文件中所有非注释、非空行的有效配置行

### 权限管理

1. 创建一个脚本 `backup.sh`，设置为只有所有者可读写执行，其他人无任何权限
2. 将 `/var/www/html` 目录及其所有内容的所有者改为 `www-data:www-data`

### 进程管理

1. 找出占用内存最多的 5 个进程，显示 PID、内存使用率和命令
2. 编写一条命令，优雅地停止所有名为 `worker` 的进程

### Shell 脚本

1. 编写脚本：接收一个目录路径作为参数，统计该目录下的文件数量和总大小
2. 编写脚本：每小时检查一次磁盘使用率，超过 80% 时发送警告
3. 编写脚本：传入文件名，自动备份为 `文件名.日期.bak`

### 系统管理

1. 创建一个 systemd 服务，用于启动你的自定义脚本
2. 设置一个定时任务：每天凌晨 3 点备份数据库，并删除 7 天前的备份
3. 用一条命令查看最近 30 分钟内所有服务的错误日志

### 安全

1. 配置 SSH 只允许密钥登录，禁止 root 直接登录，修改默认端口
2. 用 UFW 设置防火墙：允许 22/80/443 端口，拒绝其他所有入站连接
3. 找出系统中所有 SUID 文件，检查是否有可疑的

### Git

1. 创建一个新仓库，添加 `.gitignore`（忽略 `node_modules` 和 `.env`），做 3 次有意义的提交
2. 创建 `develop` 分支，在上面开发新功能，然后合并回 `main`
3. 用 `git rebase -i` 把最近 3 次提交合并成 1 次

### Docker

1. 用 Docker 运行一个 Nginx 容器，把本机 8080 端口映射到容器 80 端口
2. 编写 Dockerfile 构建一个简单的 Python/Node.js Web 应用镜像
3. 用 docker-compose 编排 WordPress + MySQL 环境

### 数据库

1. 在 MySQL 中创建一个 `blog` 数据库，包含 `articles` 表（id, title, content, created_at）
2. 用一条 SQL 查询找出最近 7 天发布的文章，按时间倒序排列
3. 执行一次 MySQL 全量备份 + 恢复测试

### 网络排错

1. 诊断：某个 Web 服务无法访问，请列出从本机到目标服务的排错步骤
2. 用 `tcpdump` 抓取所有发往 443 端口的包，保存为文件后用 Wireshark 分析
3. 用 `mtr` 诊断到 `google.com` 的网络路径，找出可能的丢包点

### Vim

1. 在 Vim 中打开一个 1000 行的文件，跳转到第 500 行，删除该行到文件末尾的内容
2. 在 Vim 中用一条命令将所有 `foo` 替换为 `bar`（全局、逐个确认）
3. 配置 `.vimrc`：显示行号、语法高亮、自动缩进

---

## 附录 A：命令速查表（打印版）

| 场景 | 命令 |
|------|------|
| 我在哪 | `pwd` |
| 有什么文件 | `ls -la` |
| 去某目录 | `cd /path` |
| 创建目录 | `mkdir -p a/b/c` |
| 创建文件 | `touch file.txt` |
| 复制 | `cp -r source dest` |
| 移动/重命名 | `mv old new` |
| 删除 | `rm -rf folder/` ⚠️ |
| 查看文件 | `cat file.txt` / `less file.txt` |
| 看文件末尾 | `tail -f log.txt` |
| 搜索文件 | `find . -name "*.txt"` |
| 搜索内容 | `grep -r "keyword" .` |
| 磁盘空间 | `df -h` |
| 目录大小 | `du -sh *` |
| 进程 | `ps aux` / `htop` |
| 杀进程 | `kill -9 PID` |
| 权限 | `chmod 755 file` |
| 所有者 | `chown user:group file` |
| 下载 | `wget URL` / `curl -O URL` |
| 网络连接 | `ss -tuln` |
| 防火墙 | `sudo ufw status` |
| 用户管理 | `sudo useradd -m user` |
| 安装软件 | `sudo apt install pkg` |
| 服务管理 | `sudo systemctl start nginx` |
| 开机自启 | `sudo systemctl enable nginx` |
| 定时任务 | `crontab -e` |
| 历史命令 | `history` |
| 帮助 | `man command` / `command --help` |

---

## 附录 B：学习路线建议

```
第 1 周  → 基础导航：pwd, ls, cd, mkdir, touch, rm, cp, mv
第 2 周  → 文本处理：cat, less, head, tail, grep, wc
第 3 周  → 正则表达式：元字符、POSIX/PCRE、grep -E、sed -E、awk
第 4 周  → 权限与用户：chmod, chown, sudo, useradd, passwd
第 5 周  → 管道与重定向：|, >, >>, 2>&1, xargs
第 6 周  → 进程管理：ps, top, kill, jobs, nohup
第 7 周  → 包管理：apt install/update/remove/search
第 8 周  → 网络：curl, wget, ping, ssh, ss
第 9 周  → Shell 脚本：变量、条件、循环、函数
第 10 周 → Vim 编辑器：模式、移动、编辑、搜索替换、配置
第 11 周 → 系统管理：systemctl, journalctl, crontab
第 12 周 → Git 版本控制：clone, add, commit, branch, merge, rebase
第 13 周 → Docker 基础：镜像、容器、Dockerfile、docker-compose
第 14 周 → 数据库：MySQL/PostgreSQL 安装与 CRUD
第 15 周 → 网络排错：traceroute, mtr, tcpdump, DNS 诊断
第 16 周 → 实战项目：搭建全栈环境（Nginx + 数据库 + Docker + Git）
```

---

> **最后的建议**：
> 1. **不要死记硬背**，用 `man 命令名` 或 `命令 --help` 随时查帮助
> 2. **先用虚拟机练习**（VirtualBox + Ubuntu），不怕搞坏系统
> 3. **每天用**，哪怕只是替代文件管理器操作文件
> 4. **遇到问题先搜**：`command error message + linux + stackoverflow`
> 5. **多写脚本**，把重复的操作自动化，这是 Linux 的精华

---

*文档版本：v2.0 | 生成日期：2025-08-03 | 15 章 | 3000+ 行 | 200+ 命令示例 | 含练习题*
