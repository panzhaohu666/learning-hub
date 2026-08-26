# Git 与 GitHub 完全指南（零基础到实战）

> 适用对象：Git / GitHub 完全新手，没用过任何版本控制工具 | 涵盖：版本控制概念、安装与配置、本地仓库、提交规范、分支与合并、回滚与恢复、远程仓库、GitHub Pull Request 完整流程、.gitignore、灾难自救、个人品牌、每周 push 最小工作流、命令速查表 + 章节练习
> 配套仓库：[panzhaohu666/learning-hub](https://github.com/panzhaohu666/learning-hub)，本书所有示例均以该仓库为演练对象。
> 原则：📱 手机碎片阅读（概念/图解），💻 电脑实操（命令）。全程不依赖视频。

---

## 目录

1. [版本控制概念](#一版本控制概念)
2. [安装与初始配置](#二安装与初始配置)
3. [本地仓库：第一次提交](#三本地仓库第一次提交)
4. [提交规范：写看得懂的 commit](#四提交规范写看得懂的-commit)
5. [分支与合并](#五分支与合并)
6. [回滚与恢复：后悔药手册](#六回滚与恢复后悔药手册)
7. [远程仓库与 GitHub](#七远程仓库与-github)
8. [GitHub 核心：Pull Request 完整流程](#八github-核心pull-request-完整流程)
9. [.gitignore 实战](#九gitignore-实战)
10. [常见灾难自救](#十常见灾难自救)
11. [个人品牌：让 GitHub 成为你的名片](#十一个人品牌让-github-成为你的名片)
12. [每周 push 一次的最小工作流](#十二每周-push-一次的最小工作流)
13. [常用命令速查表](#十三常用命令速查表)
14. [章节练习](#十四章节练习)

---

## 一、版本控制概念

> 📱 手机碎片阅读（5 分钟）：本章没有命令，在地铁上、排队时读完即可。看懂三张图，后面所有章节都是围绕这三张图展开的。

### 1.1 一个真实的灾难场景

假设你正在写毕业论文，电脑桌面上的文件是这样的：

```
毕业论文_最终版.docx
毕业论文_最终版2.docx
毕业论文_最终版3.docx
毕业论文_真的最终版.docx
毕业论文_最终版v5改2.docx
毕业论文_final_别再改了.docx
```

你是不是也干过这种事？这种命名方式的后果：

| 问题 | 后果 |
|------|------|
| 版本混乱 | 改到最后根本分不清哪个是最新的 |
| 改错了回不去 | 删掉的一段话想恢复，找不到备份 |
| 团队协作崩溃 | 两个人同时改一份文件，后保存的覆盖先保存的 |
| 没有历史 | 写不出来"这段是什么时候加的、为什么加的" |

写代码比写论文复杂得多，几千个文件每天都在变，所以程序员发明了**版本控制系统（Version Control System，VCS）**。

### 1.2 版本控制能帮你做什么

| 能力 | 说明 | 对应你要的习惯 |
|------|------|----------------|
| 记录快照 | 每次改动存一个"存档点"，随时回退 | 替代"最终版v5"命名法 |
| 完整历史 | 每个文件谁在什么时间改了什么，一目了然 | 替代人工记忆 |
| 并行开发 | 不同功能在不同分支上开发，互不干扰 | 替代"先备份一份再改" |
| 远程备份 | 代码同步到云端，电脑坏了也不丢 | 替代 U 盘拷贝 |
| 协作门禁 | 别人的改动必须经过审核才能合并 | 替代微信传文件 |

### 1.3 集中式 vs 分布式

Git 之前的主流方案是**集中式**版本控制（代表：SVN）。Git 是**分布式**版本控制。

```
集中式（SVN）：

┌──────────────┐
│  中央服务器    │  ← 唯一的"真相"，所有人都连它
│  (代码仓库)    │
└──────┬───────┘
       │
   ┌───┴───┬───┬───┐
   │       │   │   │
 ┌─┴─┐  ┌─┴─┐│ ┌─┴─┐
 │程序员A│ │程序员B││ │程序员C│
 └───┘  └───┘│ └───┘
             │
          ⚠️ 服务器挂了 = 全部瘫痪，没网就啥也干不了


分布式（Git）：

┌──────────────┐
│ GitHub 远程仓库 │  ← 只是"大家约定的交换站"
└──────────────┘
   ↑ push    ↑ push
   ↓ pull    ↓ pull
┌───────┐   ┌───────┐
│ 电脑A  │   │ 电脑B  │
│ 完整仓库 │   │ 完整仓库 │
└───────┘   └───────┘
   每台电脑都是完整副本，离线也能提交
```

| 对比项 | 集中式（SVN） | 分布式（Git） |
|--------|--------------|---------------|
| 提交需要联网吗 | 需要 | 不需要，本地就有完整历史 |
| 服务器挂了 | 全部瘫痪 | 每个人手里的副本都能顶上 |
| 完整历史在本地 | 没有 | 有，离线可查可回滚 |
| 分支创建 | 慢、笨重 | 秒级、轻量 |
| 主流度 | 老项目遗留 | 事实标准，GitHub/GitLab/Gitee 全部基于它 |

结论：**学版本控制，学 Git 一个就够了。**

### 1.4 Git 的三个区域

这是全书最重要的图，所有命令都是在不同区域之间搬运文件：

```
┌─────────────┐   git add   ┌─────────────┐   git commit   ┌─────────────┐
│   工作区      │ ──────────→ │   暂存区      │ ────────────→ │   本地仓库    │
│ Working Dir │             │ Staging Area│               │ Local Repo   │
│ (你看到的文件) │             │ (准备提交的   │               │ (提交历史)    │
│             │             │  文件清单)    │               │              │
└─────────────┘             └─────────────┘               └──────┬───────┘
       ↑                         │                               │ git push
       │ git restore             │ git restore --staged          ↓
       └─────────────────────────┴─────────────────────   ┌─────────────┐
                                                         │  远程仓库    │
                                                         │ GitHub      │
                                                         └─────────────┘
```

用"寄快递"来记：

| 区域 | 类比 |
|------|------|
| 工作区 | 你家里打包好的箱子 |
| 暂存区 | 快递站的"待发货"货架 |
| 本地仓库 | 快递已经发车，有运单号（commit hash） |
| 远程仓库 | 快递送到 GitHub 的仓库里 |

**commit 就是存档点**。每存一次档，Git 就把当时所有文件的快照永久记录，并生成一个 40 位十六进制的唯一编号（commit hash，通常看前 7 位）。

### 1.5 一次提交背后的原理（快照思维）

Git 每提交一次，记录的不是"和上次的差异"，而是**整个项目的快照**，只是相同内容用指针复用，不重复存。

```
commit a1b2c3 (第3次提交)  ─── snapshot: 全部文件的完整状态
    │
commit 9f8e7d (第2次提交)  ─── snapshot: 全部文件的完整状态
    │
commit 5c4b3a (第1次提交)  ─── snapshot: 全部文件的完整状态
```

每个 commit 还记录了：作者、时间、提交信息（commit message）、**父提交指针**。父指针把所有 commit 串成一条时间线：

```
5c4b3a ──→ 9f8e7d ──→ a1b2c3 ──→ HEAD
(第1次)     (第2次)     (第3次)    (当前所在位置)
```

> 💡 **HEAD** 是 Git 里最重要的概念：它就是一个指针，指向"你现在站在哪个 commit 上"。记住这句话，后面回滚章节全要靠它。

### 1.6 本章小结

- 版本控制解决"改坏了回不去"、"版本分不清"两大核心痛点。
- Git 是分布式，每台电脑有完整历史，离线可用，这是它战胜 SVN 的原因。
- 文件在三个区域流动：**工作区 → 暂存区 → 本地仓库 → 远程仓库**。
- **commit = 存档点**，HEAD = 当前所在位置。
- 后面的所有命令，都在干"把文件从一个区域搬到另一个区域"这件事。

---

## 二、安装与初始配置

> 💻 电脑实操（30-40 分钟）：一次性配置好，之后十年不用再碰。本节分两步：装 Git（2.1-2.3）、连 GitHub（2.4-2.9）。

### 2.1 安装 Git

**Linux（Debian/Ubuntu 系，本仓库主环境）：**

```bash
sudo apt update
sudo apt install git -y
```

**Linux（RHEL/CentOS/Fedora 系）：**

```bash
sudo dnf install git -y        # 新版 Fedora/RHEL/CentOS Stream
# sudo yum install git -y      # 旧版 CentOS 7
```

**Linux（Arch 系）：**

```bash
sudo pacman -S git
```

**macOS：**

```bash
xcode-select --install        # 自带 git，只需装命令行工具
# 或
brew install git              # 装了 Homebrew 的话用这个更新到最新
```

**Windows：**

```bash
# 方式一：winget（Win10/11 自带）
winget install --id Git.Git -e

# 方式二：去官网下载安装包
# https://git-scm.com/download/win
# 安装时一路默认即可，推荐勾选"Add to PATH"和"Use Git from the Windows Command Prompt"
```

### 2.2 验证安装

```bash
git --version
# 输出类似：git version 2.43.0
```

看到版本号就成功了。如果提示 `command not found`，说明 PATH 没配好，重新安装并勾选"Add to PATH"。

### 2.3 首次必须配置（不做后面全报错）

Git 要求每个 commit 必须知道"是谁提交的"，所以要先设置身份。**这两条不做，commit 会失败或显示未知作者。**

```bash
git config --global user.name "panzhaohu666"        # 改成你的 GitHub 用户名
git config --global user.email "你的邮箱@example.com"  # 改成你的 GitHub 注册邮箱
```

> ⚠️ **邮箱务必和 GitHub 注册邮箱一致**，否则你的 commit 在 GitHub 上不会显示为"你的贡献"，绿格子也不计入。后面个人品牌章节会讲绿格子，现在先把地基打对。

**验证配置：**

```bash
git config --global user.name
git config --global user.email
git config --list                 # 查看全部配置
```

### 2.4 配置的作用域：三个层级

| 参数 | 作用范围 | 场景 |
|------|---------|------|
| `--system` | 整台机器所有用户 | 服务器统一配置，个人几乎不用 |
| `--global` | 当前用户所有仓库 | ✅ 最常用，身份信息放这里 |
| `--local` | 当前仓库（默认） | 某个项目要不同的作者/邮箱时 |

```bash
git config --local user.name "工作专用账号"   # 只在当前仓库生效
git config --unset --global user.name        # 删除某条配置
```

### 2.5 推荐一并设置的配置

```bash
# 默认分支名设为 main（GitHub 新仓库默认就是 main）
git config --global init.defaultBranch main

# 默认编辑器（commit 信息需要编辑时打开哪个编辑器）
git config --global core.editor "vim"     # 或 "nano"，新手建议 nano

# 别名：把长命令缩短，极大提升效率
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.cm commit
git config --global alias.lg "log --oneline --graph --all"
git config --global alias.last "log -1 HEAD --stat"

# 彩色输出（默认开，确认一下）
git config --global color.ui auto

# 记住 HTTPS 密码一段时间（免去每次输入）
git config --global credential.helper cache
```

配置了别名之后，`git st` = `git status`，`git lg` = 图形化日志，后面示例里我会混用。

### 2.6 连接 GitHub 的两种方式

配置完本地 Git，接下来让本机能和 GitHub 安全通信。Git 有两种连接方式：

| 对比项 | HTTPS | SSH |
|--------|-------|-----|
| 连接命令 | 每次 push/pull 输用户名密码（或 token） | 配一次密钥，之后无密码 |
| 安全性 | token 相当于密码，别外泄 | 密钥对，私钥留本地 |
| 适合 | 偶尔用、公共电脑 | ✅ 长期开发，推荐 |
| 首次配置成本 | 低 | 中（配一次以后全免） |

**本教程推荐 SSH**。配好之后，`git push` 再也不用输任何东西，这是"每周 push 一次"习惯能坚持下来的关键之一。

### 2.7 生成 SSH 密钥对

SSH 的原理是**公钥/私钥对**：私钥留在你的电脑上（相当于印章），公钥交给 GitHub（相当于盖章验证机）。GitHub 通过比对验证你确实持有私钥。

```bash
# 1. 检查是否已有密钥（有的话可以跳过生成）
ls -la ~/.ssh/
# 如果看到 id_ed25519 和 id_ed25519.pub，说明之前生成过，跳到 2.8

# 2. 生成密钥（ed25519 是目前推荐算法）
ssh-keygen -t ed25519 -C "你的邮箱@example.com"

# 按提示操作：
#   Enter file in which to save the key: → 直接回车（默认 ~/.ssh/id_ed25519）
#   Enter passphrase: → 直接回车（想更安全可以设，但会每次要密码，新手先留空）

# 3. 启动 ssh-agent 并把私钥加入（Linux/macOS）
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

生成成功会出现一张 ASCII 图形，并提示密钥保存在：

```
你的主目录/.ssh/id_ed25519      ← 私钥，绝对不能外泄
你的主目录/.ssh/id_ed25519.pub  ← 公钥，可以给别人
```

> ⚠️ 私钥（没有 .pub 的那个）等于你 GitHub 账号的钥匙。不要发到网上、不要提交进 git 仓库、不要发到聊天软件。泄露了立即去 GitHub 删除对应公钥并重新生成。

### 2.8 把公钥添加到 GitHub（网页操作）

1. 打开 [github.com](https://github.com) 登录。
2. 右上角头像 → **Settings**（设置）。
3. 左侧找到 **SSH and GPG keys**。
4. 点绿色按钮 **New SSH key**。
5. Title 填一个备注，比如 `我的笔记本`。
6. 在电脑上执行 `cat ~/.ssh/id_ed25519.pub`，把输出内容**完整复制**（以 `ssh-ed25519 AAAA...` 开头，一整行），粘贴到网页的 Key 框里。
7. 点 **Add SSH key**。

### 2.9 验证 SSH 连接

```bash
ssh -T git@github.com
```

第一次会提示确认指纹，输入 `yes` 回车。看到下面这行就是成功了：

```
Hi panzhaohu666! You've successfully authenticated, but GitHub does not provide shell access.
```

> 💡 提示 "Permission denied (publickey)" 时，按顺序检查：1) 公钥有没有完整复制进 GitHub；2) ssh-agent 里有没有私钥（`ssh-add -l` 看列表）；3) `ssh-add ~/.ssh/id_ed25519` 重新加一次。

### 2.10 配置常见问题速查

| 现象 | 原因 | 解决 |
|------|------|------|
| commit 报错 "Please tell me who you are" | 没设 user.name/email | 执行 2.3 的两条命令 |
| push 要求输密码 | 用了 HTTPS 连接 | 按 2.7-2.9 换 SSH，或用 token 登录 |
| `ssh: connect to host github.com port 22: Connection timed out` | 网络屏蔽 22 端口 | 改用 HTTPS，或配 SSH over 443（见 GitHub 文档） |
| 提交者显示 Unknown | user.email 和 GitHub 邮箱不一致 | 用 GitHub 注册邮箱重设 `user.email` |

**本小节完成标志**：`ssh -T git@github.com` 显示认证成功。到了这里，你已经可以开始真正的 Git 之旅了。

---

## 三、本地仓库：第一次提交

> 💻 电脑实操（40-60 分钟）：跟着做一遍，你会建立对"工作区/暂存区/仓库"三区域的肌肉记忆。本节所有命令都是日常最高频的，务必亲手敲，别复制粘贴。

### 3.1 初始化一个仓库：git init

先在电脑上建一个练习目录，我们模拟建一个和 learning-hub 一样的笔记仓库：

```bash
mkdir ~/git-practice
cd ~/git-practice
git init
```

输出 `Initialized empty Git repository in /home/你/home/git-practice/.git/`。

`git init` 会在当前目录创建一个隐藏的 `.git/` 文件夹，**仓库的心脏**就藏在这里（所有历史、所有版本都在里面）。

```bash
ls -a        # 能看到 .git/ 目录
```

> 💡 想把一个普通文件夹变成 Git 仓库，就这一条命令。仓库 = 文件夹 + `.git/`。

### 3.2 第一次提交：完整的四步

```bash
# 第 1 步：创建一个文件
echo "# 我的学习笔记" > README.md

# 第 2 步：查看状态
git status
# 输出：
# On branch main
# No commits yet
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         README.md

# 第 3 步：加入暂存区
git add README.md

# 第 4 步：提交
git commit -m "初始化：新建 README"
```

看到输出：

```
[main (root-commit) 5c4b3a] 初始化：新建 README
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
```

**第一个 commit 诞生了**。`5c4b3a` 是它的短 hash，`[main]` 说明这次提交在 main 分支上，`root-commit` 表示这是本仓库的第一个提交。

### 3.3 git status：随时问"我改了什么"

`git status` 是最常用的命令，没有之一。它告诉你文件处于什么状态：

| 状态 | 英文术语 | 含义 |
|------|---------|------|
| 未跟踪 | Untracked | 新文件，Git 从没见过它（还没 add 过） |
| 已修改 | Modified | 跟踪过的文件被改动了 |
| 已暂存 | Staged | 已经 add 了，等着 commit |
| 已提交 | Committed | 已经 commit 存档 |

```bash
# 修改一下 README.md 再看状态
echo "## 学习目标" >> README.md
git status
```

输出：

```
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md
```

`modified` 且显示在 `Changes not staged for commit`（未暂存区）下面，说明改动还在工作区。`git add` 之后，改动会显示到 `Changes to be committed`（待提交区）下面，说明进了暂存区。

> 💻 习惯建议：**每次操作前先 `git status`**，改文件前看一眼、提交前看一眼、push 前看一眼。这是职业程序员都不会省的一步。

### 3.4 git add：把改动搬进暂存区

```bash
git add README.md          # 只暂存一个文件
git add .                  # 暂存当前目录及其子目录的所有改动
git add -A                 # 暂存所有改动，包括删除（最彻底，推荐）
git add -u                 # 只暂存已跟踪文件的修改/删除，不添加新文件
git add -p                 # 交互式逐个确认每块改动要不要暂存（精细控制）
```

> ⚠️ `git add .` 和 `git add -A` 的区别：`git add .` 只暂存当前目录及其子目录的改动，如果改动在上级目录就漏了。`git add -A` 暂存整个仓库所有位置的改动。**统一用 `git add -A` 最省心**。

### 3.5 git commit：存档

```bash
git commit -m "更新 README：补充学习目标"          # 单行信息
git commit -m "标题" -m "正文第一行" -m "正文第二行"   # 多个 -m 拼出标题+正文
git commit -am "直接提交已跟踪文件的改动"            # -a 跳过 add（只对已跟踪文件有效）
```

> ⚠️ `git commit -am` 有个坑：**新文件不会被打包进去**。它只暂存"已经被跟踪"的文件的改动。新文件还得先 `git add`。

commit 之后，`git status` 会显示干净状态：

```
On branch main
nothing to commit, working tree clean
```

"working tree clean" 是程序员最爱看到的一句话：所有改动都安全存档了。

### 3.6 git diff：看看到底改了什么

`git diff` 是代码审查的显微镜，逐行显示差异。

```bash
git diff                  # 工作区 vs 暂存区（还没 add 的改动）
git diff --staged         # 暂存区 vs 上一次提交（已经 add 还没 commit 的改动）
git diff --cached         # 同上，等价写法
git diff HEAD             # 工作区 vs 上次提交（所有未提交的改动）
git diff HEAD~1 HEAD      # 上上次提交 vs 上次提交（最近一次 commit 改了什么）
```

输出格式解读（以 `git diff --staged` 为例）：

```
diff --git a/README.md b/README.md
index e69de29..1d76b15 100644
--- a/README.md            ← a/ 表示修改前的文件
+++ b/README.md            ← b/ 表示修改后的文件
@@ -0,0 +1 @@
+# 我的学习笔记            ← 带 + 号的是新增行
```

记忆法：`-` 是删掉的旧内容，`+` 是新增的新内容，`@@` 是改动位置的行号坐标。

### 3.7 git log：翻阅提交历史

```bash
git log                    # 完整历史
git log --oneline          # 一屏看所有提交（每个提交一行）⭐
git log --oneline --graph  # 带分支图形的历史
git log --oneline --graph --all   # 含所有分支（别名 git lg 就是这个）⭐
git log -3                 # 只看最近 3 次提交
git log -p                 # 看每次提交的完整差异（非常长，慎用）
git log --stat             # 看每次提交改了哪些文件、几行
git log --author="panzhaohu666"   # 只看某人的提交
git log --since="2 weeks ago"     # 最近两周的提交
git log --grep="README"           # 按提交信息搜索
```

`git log --oneline` 输出示例：

```
5c4b3a 更新 README：补充学习目标
a1b2c3 初始化：新建 README
```

### 3.8 查看特定提交和文件历史

```bash
git show 5c4b3a             # 看某个提交的详情（谁、何时、改了什么）
git show 5c4b3a --stat      # 只看统计信息
git show HEAD               # 看当前提交
git show HEAD~1             # 看上一个提交

git blame README.md         # 每个文件每一行是谁在哪个提交写的 ⭐
git grep "学习目标"          # 在当前快照里搜索内容
git log --oneline -- README.md   # 只看某个文件的提交历史
```

### 3.9 重命名与删除文件

```bash
git mv old.md new.md        # 重命名（Git 会识别为 rename）
git rm old.md               # 删除并自动暂存这次删除
git rm --cached secret.txt  # 从跟踪列表移除但不删文件（.gitignore 章节会细讲）
```

### 3.10 完整演练：从零建一个笔记仓库

把上面所有命令串成一个真实场景，跟着做一遍：

```bash
# 场景：你的第一个知识库，模仿 learning-hub
mkdir ~/notes
cd ~/notes
git init

# 写点东西
echo "# 我的知识库" > README.md
mkdir Python
echo "# Python 笔记" > Python/基础.md

# 看状态 → 暂存 → 提交
git status
git add -A
git commit -m "初始化：创建 README 和 Python 笔记目录"

# 再改一版
echo "## 变量与数据类型" >> Python/基础.md
git diff                      # 看看改动
git add -A
git commit -m "完善：Python 基础笔记 v1 — 新增变量与数据类型"

# 看历史
git log --oneline --graph
git lg                        # 如果你配了别名
```

看到类似输出：

```
* a2b3c4 完善：Python 基础笔记 v1 — 新增变量与数据类型
* 1f2e3d 初始化：创建 README 和 Python 笔记目录
```

恭喜，你已经在用真实的版本控制了。现在你的电脑里有一个完整的 Git 仓库，随时可以回滚、查看历史、开始协作。

### 3.11 本节命令速记卡

| 想做什么 | 命令 |
|---------|------|
| 初始化仓库 | `git init` |
| 看状态 | `git status` |
| 暂存改动 | `git add -A` |
| 存档 | `git commit -m "信息"` |
| 看差异 | `git diff` |
| 看历史 | `git log --oneline` |
| 看特定提交 | `git show <hash>` |

---

## 四、提交规范：写看得懂的 commit

> 📱 手机碎片阅读（10 分钟）+ 💻 实操（20 分钟）：规范不是死规则，是本仓库"真实 commit"里沉淀出来的习惯。看完这一章，你会明白为什么 commit 信息比代码本身还难写。

### 4.1 为什么 commit 信息这么重要

commit 信息是写给**未来的自己**和**团队其他成员**看的。三个月后回看代码，唯一能快速定位"这段逻辑为什么存在"的线索就是 commit 信息。

对比两种提交：

```
✗ 坏例子：update、fix、改了一下、test、、、、
✓ 好例子：完善：Python 基础笔记 v2 — 新增列表推导式并附示例
```

三个月后 `git log --oneline` 扫一遍，好例子一眼就知道每步在干嘛，坏例子等于没有历史。

### 4.2 本仓库的真实 commit 风格

本仓库（learning-hub）的提交信息全部用中文，主要格式是 **"动作：对象 — 说明"**。三种最常见形态：

```
完善：Git 完全指南 v1 — 新增分支合并章节
更新 README：补充贡献指南的 PR 流程
修复：阶段一代码示例中的 OpenAI 客户端初始化错误
```

| 组成部分 | 含义 | 示例 |
|---------|------|------|
| 动作前缀 | 这次提交干了什么类型的事 | 完善 / 更新 / 修复 / 初始化 |
| 冒号后对象 | 改的是哪个文件/哪个模块 | Git 完全指南 / README |
| 版本号（可选） | 同一文件多次完善时递增 | v1 / v2 / v5 |
| 破折号后说明 | 一句话说清具体改了什么 | 新增分支合并章节 |

**为什么这么写**：

- **中文**：仓库内容全中文，读者是中文学习者，信息中文最直接。
- **动作前置**：扫日志时一眼看到"这次是修复还是新增"。
- **带对象**：不用打开文件就知道动了哪。
- **破折号补充**：标题说不完的细节放说明里。

> 💡 本仓库还有一条隐含约定：**每次提交只做一件事**。比如"更新 README"就只更新 README，不要把新增笔记、改代码、调格式全塞进一个 commit。一个 commit 一个主题，回滚时才能精准撤销。

### 4.3 与行业标准（Conventional Commits）对照

如果你将来进入企业开发，会遇到英语的规范格式（Conventional Commits）：

```
feat: 添加用户登录功能         # 新功能
fix: 修复密码验证的 bug        # 修复 bug
docs: 更新 API 文档            # 文档
style: 修复代码格式            # 格式调整
refactor: 重构用户模块         # 重构（不改变行为）
test: 添加登录测试             # 测试
chore: 更新依赖版本            # 杂项
```

两种风格本质相同，只是语言不同。**个人仓库 / 本仓库用中文风格，团队协作按团队规范走**。核心原则永远是：信息明确、能被看懂。

### 4.4 好的 commit 信息清单

写 commit 前，问自己五个问题：

| 问题 | 好提交的回答 |
|------|-------------|
| 改了什么？ | "完善：Python 基础笔记" |
| 为什么改？ | "— 补充列表推导式，因为刷 LeetCode 总用到" |
| 影响范围？ | 明确说出改了 README 还是改了代码 |
| 有没有上下文？ | 让三个月后的自己能秒懂 |
| 是不是只做了一件事？ | 是的 |

### 4.5 新手最常犯的五个错误

| 错误 | 例子 | 正确做法 |
|------|------|---------|
| 信息太空 | `update` / `fix` / `111` | 带上对象和说明：`修复：README 里失效的链接` |
| 夹杂英文乱码 | `dahfghdas` | 写人话，中英文都行但要说人话 |
| 把无关改动塞一起 | 同时改代码+改文档+改格式 | 拆成多个 commit |
| 提交信息写情绪 | `终于他妈的跑通了` | 情绪留在聊天，commit 写事实 |
| 改完才想起提交 | 一晚上一个 commit | 一个主题完成就提交，多次提交 |

### 4.6 commit 模板（可选进阶）

想让信息结构统一，可以写一个模板文件：

```bash
git config --global commit.template ~/.gitmessage
```

先创建 `~/.gitmessage`：

```
动作：对象

说明：
- 改了什么
- 为什么改
```

之后每次 `git commit` 不带 `-m` 时，会自动打开这个模板让你填空。

### 4.7 本章作业

在 3.10 建的练习仓库里，再造两次提交，信息必须符合本仓库风格：

```bash
# 1. 给 README 补一段"使用说明"，提交：
#    git commit -m "完善：README v1 — 新增使用说明"

# 2. 新增一个笔记文件并提交：
#    git commit -m "初始化：新增 Linux 命令速查笔记"
```

提交完执行 `git log --oneline`，你的历史应该是一排清晰的中文标题。**从此以后，你每次 commit 都按这个风格来，这是给未来自己最好的礼物。**

---

## 五、分支与合并

> 📱 概念阅读（10 分钟）+ 💻 实操（40 分钟）：分支是 Git 最强大的功能，也是从"单人存档"走向"多人协作"的桥梁。这一章结束后，你就能看懂 README 里 `feature/your-feature-name` 这种分支名的含义了。

### 5.1 分支是什么：一张图看懂

一句话：**分支就是一个可移动的指针**，指向某个 commit。`main`（或 `master`）是默认分支，你可以在任意点拉出一条新分支，在上面自由改动，不影响主线。

```
main:       ●───●───●───────────────●
                          ↑
feature-x:               ●───●───●
                          ↑ 拉出分支后在这里开发
```

用"平行宇宙"来理解：

- `main` 分支是主宇宙，所有正式内容在这。
- `feature-x` 是平行宇宙，你在里面随便实验。
- 实验成功了，把平行宇宙**合并（merge）**回主宇宙。
- 实验失败了，直接删除平行宇宙，主宇宙毫发无损。

### 5.2 查看分支

```bash
git branch               # 列出本地分支（* 号标记当前所在分支）
git branch -a            # 列出所有分支（含远程的 origin/*）
git branch -vv           # 查看分支的追踪关系（跟踪哪个远程分支）
git branch -r            # 只看远程分支
```

### 5.3 创建与切换分支

```bash
# 老式语法（checkout）
git branch feature-notes        # 创建分支（不切换）
git checkout feature-notes      # 切换到分支
git checkout -b feature-notes   # 创建并切换（二合一，最常用）

# 新式语法（switch，Git 2.23+，语义更清晰，推荐）
git switch feature-notes        # 切换分支
git switch -c feature-notes     # 创建并切换
git switch -                    # 切回上一个分支
```

> 💡 本仓库 README 贡献流程用的就是老式二合一：`git checkout -b feature/your-feature-name`。两种语法在 GitHub 流程里都通用，你随意，但要看得懂 README 那条命令。

**分支命名规范**（本仓库和主流开源项目通用）：

| 前缀 | 用途 | 示例 |
|------|------|------|
| `feature/` | 新功能 | `feature/git-guide` |
| `fix/` | 修复 | `fix/readme-typo` |
| `docs/` | 文档 | `docs/pr-flow` |
| `chore/` | 杂项 | `chore/update-gitignore` |

### 5.4 分支从哪里来

`git switch -c` 会在**当前所在 commit** 处拉出新分支。所以拉分支前先确认自己站在哪：

```bash
git log --oneline -1        # 看当前 HEAD 指向哪
git switch -c feature/notes # 从当前提交拉出分支
```

如果你想从别的 commit 拉分支：

```bash
git switch -c feature/old 5c4b3a    # 从指定 commit 拉分支
```

### 5.5 合并：merge 的两种形态

合并就是把另一个分支的改动合进当前分支。两种结果形态：

**形态一：快进合并（Fast-forward）**。目标分支没有新提交，主线可以直接"指针前移"：

```
合并前：                       合并后：
main: ●───●───●                main: ●───●───●───●───●
                \                        (指针直接推进)
feature:         ●───●
```

```bash
git switch main
git merge feature/notes
# 输出：Fast-forward
```

**形态二：三方合并（3-way merge）**。两个分支都有各自的新提交，Git 找一个共同祖先，把两边改动拼起来，生成一个**合并提交**：

```
合并前：                         合并后：
main: ●───●───●───A             main: ●───●───●───A───●(合并提交)
                \                              /      /
feature:         ●───B              feature:  ●───B──┘
```

```bash
git merge feature/notes
# 输出：Merge made by the 'ort' strategy.
```

**控制合并形态**：

```bash
git merge --no-ff feature/notes   # 强制生成合并提交（保留"这是一次合并"的记录）
git merge --ff-only feature/notes # 只允许快进，不能快进就报错
```

> 💡 团队里常要求 `--no-ff`，因为合并提交能保留"功能是从哪条线合进来的"历史。个人仓库随意。

### 5.6 合并冲突：手把手解决一次

**冲突（conflict）** = Git 无法自动判断保留哪边，因为它发现两个分支**改了同一文件的同一位置**。不用怕，Git 会把冲突内容标记出来，你亲自拍板。

**第一步：制造一个冲突**（跟着做）

```bash
# 在练习仓库里
git switch main
echo "第一行：main 的版本" > conflict.txt
git add conflict.txt
git commit -m "初始化：新建冲突练习文件"

git switch -c fix/conflict
echo "第一行：fix 分支的版本" > conflict.txt
git commit -am "修复：conflict.txt 第一行"

git switch main
echo "第一行：main 又改了一次" > conflict.txt
git commit -am "完善：conflict.txt 第一行"

# 现在 main 和 fix/conflict 改了同一行
git merge fix/conflict
```

**第二步：看到冲突**。Git 会报：

```
Auto-merging conflict.txt
CONFLICT (content): Merge conflict in conflict.txt
Automatic merge failed; fix conflicts and then commit the result.
```

此时 `git status` 显示 `both modified: conflict.txt`（两边都改过）。

**第三步：打开文件，处理冲突标记**。`cat conflict.txt` 看到：

```
<<<<<<< HEAD
第一行：main 又改了一次
=======
第一行：fix 分支的版本
>>>>>>> fix/conflict
```

| 标记 | 含义 |
|------|------|
| `<<<<<<< HEAD` | 冲突开始，下面是我这边（main）的内容 |
| `=======` | 分界线 |
| `>>>>>>> fix/conflict` | 冲突结束，上面是对方分支的内容 |

**第四步：手动决定保留谁**。把文件改成你想要的样子，**必须删除所有 `<<<<<<<`、`=======`、`>>>>>>>` 标记**：

```bash
# 用编辑器改成（或命令行 echo）
第一行：main 又改了一次 + fix 分支的版本结合
```

**第五步：标记为已解决并提交**：

```bash
git add conflict.txt
git commit -m "合并：conflict.txt 冲突解决，保留双方内容"
```

> 💡 冲突解决后 `git commit` 不需要写 `-m` 之外的任何参数，Git 已准备好默认的合并提交信息。

**冲突中的逃生门**：解决到一半想放弃？

```bash
git merge --abort    # 放弃本次合并，回到合并前的状态
```

### 5.7 删除分支

```bash
git branch -d feature/notes     # 删除已合并的分支（安全）
git branch -D feature/notes     # 强制删除（分支有未合并的提交时用，⚠️ 内容会丢）
git push origin --delete feature/notes   # 删除远程分支
```

> 💡 用 `-d` 时如果 Git 提示"分支还有未合并的提交"，是在保护你：确认真的不要了再换 `-D`。

### 5.8 merge 与 rebase：两种整合思路

`rebase`（变基）是另一种把分支改动整合回主线的思路，和 merge 区别很大：

```
merge 结果（有合并提交，历史真实但有点绕）：
main:   ●───●───A───●(合并)
                 /    /
feature:        ●───B

rebase 结果（把 feature 的提交"重放到"主线最新点，历史是直线）：
main:   ●───●───A───●───●───●
feature 的提交被平移过来，重新排队
```

```bash
git switch feature/notes
git rebase main          # 把 feature 的提交重放到 main 最新点
git switch main
git merge feature/notes  # 此时一定是快进合并
```

| 对比 | merge | rebase |
|------|-------|--------|
| 历史形态 | 有分支痕迹、有合并提交 | 线性，干净 |
| 安全度 | 高，不改历史 | 会重写提交（⚠️ 已 push 的别 rebase） |
| 冲突处理 | 一次解决 | 每个提交可能都要解决一遍 |
| 团队协作 | ✅ 推荐 | 个人/小团队可用 |

> ⚠️ 铁律：**已经 push 到远程的提交，永远不要 rebase**。rebase 会重写历史，如果别人已经拉走了你的提交，两边会对不上。个人没 push 过的本地提交随意。

### 5.9 图形化看分支历史

```bash
git log --oneline --graph --all
# 输出：
# *   5f6a7b (HEAD -> main) 合并：conflict.txt 冲突解决，保留双方内容
# |\
# | * 8a9b0c (fix/conflict) 完善：conflict.txt 第一行
# * | 3d4e5f 完善：conflict.txt 第一行
# |/
# * 1a2b3c 初始化：新建冲突练习文件
```

`*` 是提交，`|` 和 `\` 是分支线，`(HEAD -> main)` 表示当前在主分支。多练几次，这张图会成为你的导航地图。

---

## 六、回滚与恢复：后悔药手册

> 📱 概念阅读（10 分钟）+ 💻 实操（50 分钟）：Git 最让新手安心的特性就是**几乎所有操作都能撤销**。读完这一章，你会不再害怕犯错。犯错不可怕，不会恢复才可怕。

### 6.1 前提认知：Git 不会轻易弄丢你的东西

Git 有 **reflog（引用日志）**：它把每一次 HEAD 移动（提交、切换、重置）都记下来了，保留至少 90 天。这意味着：

> **即使你 `reset --hard` 了、删了分支、弄丢了提交，只要在 90 天内，都能找回。**

```bash
git reflog
# 输出示例：
# 5f6a7b (HEAD -> main) HEAD@{0}: commit: 完善：Python 基础笔记 v1
# 1f2e3d HEAD@{1}: commit (initial): 初始化：创建 README
```

每行格式：`<hash> HEAD@{编号}: 操作: 说明`。`HEAD@{0}` 是最近一次，`HEAD@{1}` 是上一次。

### 6.2 撤销工作区的修改（还没 add）

改了文件但不想要了，想回到上一次提交的样子：

```bash
git restore file.txt           # 新语法（Git 2.23+）
git checkout -- file.txt       # 老语法，效果相同
git restore .                  # 撤销当前目录所有工作区改动
```

> ⚠️ 这条命令**丢弃**工作区的改动，恢复后改的东西就没了（回不到 reflog 里，因为从没提交过）。用它之前确认不是想要的内容。

### 6.3 撤销暂存（已经 add，还没 commit）

加错文件了，想从暂存区撤出来：

```bash
git restore --staged file.txt   # 从暂存区撤出，文件保留改动
git reset HEAD file.txt         # 老写法，效果相同
```

### 6.4 git reset：让指针后退（三种模式）

`git reset` 的本质是**把 HEAD 指针和分支指针往后移**，三个模式区别在于"后退时文件怎么处理"：

```
                ┌────────────────────────────────────────────────┐
                │  reset 前：暂存区和工作区都有未提交的改动          │
                └────────────────────────────────────────────────┘

--soft   HEAD 后退，暂存区、工作区全部保留（改动回到"已暂存"状态）
--mixed  HEAD 后退，暂存区清空，工作区保留（默认模式，改动回到"已修改"状态）
--hard   HEAD 后退，暂存区、工作区全部清空（改动被丢弃）⚠️ 最危险
```

| 模式 | 适用场景 | 危险度 |
|------|---------|--------|
| `--soft` | 提交后发现"应该再拆成几个提交" | 低 |
| `--mixed`（默认） | 提交后发现"我改错了，想重新整理" | 低 |
| `--hard` | 确定的错误提交，内容没用了 | 高，但 reflog 可救 |

```bash
git reset --soft HEAD~1       # 撤销最近一次提交，改动留在暂存区
git reset HEAD~1              # 撤销最近一次提交，改动回到工作区
git reset --hard HEAD~1       # ⚠️ 撤销最近一次提交，改动彻底丢弃
git reset --hard 5c4b3a       # 回到任意提交（先看 reflog 找到 hash）
git reset --hard origin/main  # 强制对齐远程版本
```

> 💡 `HEAD~1` 表示"上一个提交"，`HEAD~3` 表示"往前 3 个"。也可以直接写 hash。

### 6.5 git revert：用新提交来撤销（安全推送）

`reset` 会**改写历史**（指针后退了）。如果错误提交已经 push 到远程、别人可能拉走，改写历史会引发灾难。这时用 `revert`：

```bash
git revert 5c4b3a            # 生成一个"反向"提交，把 5c4b3a 的改动撤销掉
git revert --no-edit HEAD    # 撤销最近的提交，不打开编辑器
git revert -m 1 <合并提交的hash>  # 撤销一个合并提交（-m 1 保留 main 线）
```

```
revert 前：  ●───●───●───●（错误提交）
revert 后：  ●───●───●───●───●（反向提交，历史完整，可以放心 push）
```

**决策一句话**：

| 情况 | 用 |
|------|-----|
| 提交还没 push，历史只有你自己 | `reset` |
| 提交已经 push，别人可能拉走了 | `revert` |

### 6.6 修改最后一次提交：git commit --amend

**场景一：commit 信息写错了**：

```bash
git commit --amend -m "修复：正确的提交信息"
```

**场景二：提交时漏了一个文件**：

```bash
git add 忘加的文件.md
git commit --amend --no-edit    # --no-edit 保留原来的信息
```

`--amend` 不会创建新提交，而是**把当前暂存区内容合并进上一次提交**（其实生成了新 hash，但历史看起来只有一次提交）。

> ⚠️ 和 reset 一样：已经 push 的提交，`amend` 会改写历史，请只在本地提交上使用。

### 6.7 git stash：把改动临时收起来

**场景**：你在分支 A 上改了一半代码，突然要切到分支 B 修个紧急 bug。改动还没成型不想提交，切换分支又会带走未提交的改动。这时用 stash 把改动"藏"起来：

```bash
git stash                       # 暂存当前所有改动（工作区恢复干净）
git stash push -m "WIP: 登录模块进行中"   # 带说明的暂存（推荐）
git stash list                  # 查看所有暂存

git stash pop                   # 恢复最近一次暂存并从列表删除
git stash apply                 # 恢复但不删除列表记录（多份暂存时用）
git stash apply stash@{1}       # 恢复指定的一份
git stash drop                  # 删除最近一份暂存
git stash clear                 # ⚠️ 清空所有暂存
git stash show -p stash@{0}     # 查看某份暂存的具体差异
```

**进阶**：如果 stash 时所在的旧分支已经乱了，直接把 stash 变成新分支：

```bash
git stash branch feature/notes  # 基于 stash 创建分支并恢复改动
```

### 6.8 真实错误场景演练

**场景 A：提交后发现"这个文件不该提交"**

```bash
git reset --soft HEAD~1    # 撤销提交，改动回到暂存区
git restore --staged 不该提交的文件   # 把那个文件撤出暂存区
git commit -m "完善：只提交该提交的内容"  # 重新提交正确的部分
```

**场景 B：commit 信息打错字了**

```bash
git commit --amend -m "修复：正确的信息"
```

**场景 C：reset --hard 误删了一大堆改动**

```bash
git reflog                  # 找到你 reset 之前的那个 hash
git reset --hard <那个hash>  # 回到原地，一切恢复
```

**场景 D：删错分支，分支上还有重要提交**

```bash
git reflog                  # 找被删分支最后指向的提交 hash
git switch -c 新分支名 <那个hash>   # 从该提交重新拉出分支
```

**场景 E：stash 了一堆东西忘了内容**

```bash
git stash list
git stash show -p stash@{0}   # 看看里面是啥
git stash apply stash@{0}     # 恢复
```

### 6.9 本节速记表

| 想撤销什么 | 命令 | 风险 |
|-----------|------|------|
| 工作区改动（未 add） | `git restore file` | 低 |
| 暂存区（已 add 未 commit） | `git restore --staged file` | 低 |
| 最近一次提交（未 push） | `git reset --soft HEAD~1` / `--hard` | 中/高 |
| 已 push 的错误提交 | `git revert HEAD` | 低 |
| 最后一次提交信息/漏文件 | `git commit --amend` | 中 |
| 一切被弄丢的东西 | `git reflog` 找 hash | 救星 |

---

## 七、远程仓库与 GitHub

> 📱 概念阅读（10 分钟）+ 💻 实操（40 分钟）：从这一章开始，你的代码走出本地，进入云端。这也是"每周 push 一次"习惯的技术基础。

### 7.1 远程仓库是什么

远程仓库就是**托管在服务器上的另一份完整仓库**（GitHub/Gitee/GitLab 等平台提供）。本地仓库和远程仓库通过 **remote** 关联。

```
本地电脑                             GitHub
┌────────────┐   git push ──────→  ┌────────────┐
│ 本地仓库     │                    │ 远程仓库     │
│ origin/main│ ←────── git pull ── │ origin/main│
└────────────┘                    └────────────┘
```

`origin` 是 Git 给第一个远程仓库的**默认名字**（可以叫别的，但约定俗成叫 origin）。

### 7.2 添加与管理 remote

在 GitHub 上新建一个空仓库（网页操作：右上角 `+` → New repository，名字如 `notes`，不要勾 README，保持空），然后：

```bash
# 在本地仓库里关联远程
git remote add origin git@github.com:panzhaohu666/notes.git

# 查看
git remote -v
# origin  git@github.com:panzhaohu666/notes.git (fetch)
# origin  git@github.com:panzhaohu666/notes.git (push)

# 管理
git remote rename origin github     # 重命名
git remote remove origin            # 移除关联
```

> ⚠️ HTTPS 方式：`git remote add origin https://github.com/panzhaohu666/notes.git`。SSH 就用 `git@github.com:用户名/仓库名.git`。我们配了 SSH，推荐 SSH 方式。

### 7.3 git clone：把别人的仓库复制到本地

```bash
# 克隆本仓库试试（SSH 方式）
git clone git@github.com:panzhaohu666/learning-hub.git

# HTTPS 方式
git clone https://github.com/panzhaohu666/learning-hub.git

# 克隆到指定目录
git clone git@github.com:panzhaohu666/learning-hub.git my-hub
```

`clone` 会一次性把远程仓库的**完整历史**下载到本地，并且自动帮你配好 `origin`，还自动建立了本地 `main` 对远程 `origin/main` 的**追踪关系**。

### 7.4 git push：把本地提交推上去

```bash
git push origin main              # 把本地 main 推到远程 origin 的 main
git push -u origin main           # 首次推送用 -u，建立追踪关系（之后只需 git push）
git push                          # 建立追踪后直接 push 即可
git push origin feature/notes     # 推特定分支
git push --tags                   # 推送所有标签
```

首次推送时：

```bash
git push -u origin main
# 输出：
# Enumerating objects: 5, done.
# ...
# To github.com:panzhaohu666/notes.git
#  * [new branch]      main -> main
# branch 'main' set up to track 'origin/main'.
```

`-u`（`--set-upstream`）干了两件事：推送 + 设置追踪。之后 `git push` / `git pull` 不用再写分支名。

### 7.5 git pull 与 git fetch：拉取远程更新

```bash
git pull                 # 拉取远程更新并合并到当前分支（= fetch + merge）
git pull origin main     # 显式指定
```

`fetch` 和 `pull` 的区别：

```
git fetch：把远程最新提交下载到本地"远程分支"（origin/main），
          但不动你的工作区，你可以先看看再决定怎么合并。

git pull：fetch 之后自动执行 merge，直接改变你的工作区。
```

```bash
git fetch origin                # 下载远程更新到 origin/main
git log --oneline origin/main   # 查看远程那边多了什么
git merge origin/main           # 确认没问题后合并到当前分支
```

> 💡 团队协作时推荐"fetch + 看 + merge"三步走，避免 pull 自动合并搞出意外。

### 7.6 追踪关系（upstream）详解

追踪 = 你的本地分支和某个远程分支"绑定"。

```bash
git branch -vv                 # 查看所有分支的追踪关系
# * main 5f6a7b [origin/main] 完善：Python 基础笔记 v1
#                               ↑ 这表示 main 追踪 origin/main

git branch -u origin/main              # 给当前分支设置追踪
git branch --unset-upstream            # 取消追踪
git config --get branch.main.remote    # 查看追踪的远程
```

有了追踪，`git push` / `git pull` / `git status` 才能知道"和谁对比"。

### 7.7 pull 的两种策略：merge 还是 rebase

```bash
git pull                    # 默认 = fetch + merge（生成合并提交）
git pull --rebase           # = fetch + rebase（保持历史线性）
```

什么时候用哪个：

| 场景 | 建议 |
|------|------|
| 远程有新提交，你本地也有新提交 | `git pull --rebase`（历史干净） |
| 团队规范要求保留合并记录 | `git pull`（merge） |
| 你完全没改本地内容 | 都一样 |

**永久设置**：

```bash
git config --global pull.rebase true    # 全局默认用 rebase
```

### 7.8 最常见的报错：rejected（非快进）

**报错场景**：远程有了新提交，你本地没有，push 被拒：

```
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to '...'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref.
```

**意思**：远程的 main 比你的新，你直接 push 会覆盖别人的提交，Git 拒绝。

**解决**（按顺序）：

```bash
git pull --rebase        # 先拉取并把自己的提交重放到最新
git push                 # 再推送
```

如果有冲突，解决方式和 merge 一样，`git status` 会显示冲突文件，处理后 `git add` + `git rebase --continue`。

> ⚠️ 不要轻易用 `git push --force` 强推。它会把远程历史覆盖成你的版本，如果别人拉走过远程的提交，会出大乱子。非用不可时用安全版 `git push --force-with-lease`（仅在你确认远程没人动过时才允许）。

### 7.9 push / pull / fetch 三兄弟总结

| 命令 | 方向 | 干的事 | 影响 |
|------|------|--------|------|
| `push` | 本地 → 远程 | 上传本地提交 | 改变远程 |
| `pull` | 远程 → 本地 | 下载 + 合并 | 改变工作区 |
| `fetch` | 远程 → 本地 | 只下载不合并 | 只更新 origin/* 分支 |

**把 learning-hub 克隆下来实践一把**：

```bash
git clone git@github.com:panzhaohu666/learning-hub.git
cd learning-hub
git log --oneline -5          # 看看真实仓库的提交信息风格
git branch -a                 # 看看有哪些分支
```

这正好呼应下一章：你要贡献这个仓库，就得先 clone 一份、改、push、发起 Pull Request。

---

## 八、GitHub 核心：Pull Request 完整流程

> 📱 概念阅读（15 分钟）+ 💻 实操（60 分钟）：这一章是本书的**重中之重**。学完你就能完整执行本仓库 README 里的"贡献流程"。请先把 7.9 的 clone 做完，再开始本章。

### 8.1 GitHub 是什么

GitHub 是目前全球最大的代码托管平台，本质是一个 Git 远程仓库的托管网站，外加一整套协作工具。本仓库（learning-hub）就托管在上面。

GitHub 上最常见的动作：

| 动作 | 含义 | 类比 |
|------|------|------|
| Star | 收藏/点赞别人的仓库 | 小红书收藏 |
| Fork | 把别人的仓库复制一份到你的账号下 | 转载到你的主页 |
| Watch | 订阅仓库动态 | 关注 |
| Issue | 提出问题、bug、建议 | 工单系统 |
| Pull Request | 请求把你的改动合并进别人的仓库 | 投稿 |
| Code Review | 在 PR 里审查代码 | 审稿 |

### 8.2 注册与基础设置

1. 打开 [github.com](https://github.com) → Sign up，用邮箱注册。
2. 头像 → Settings → 设置用户名（Username）、头像。
3. Settings → Emails：确认注册邮箱，这是绿格子归属的关键。
4. 验证 SSH（回到第二章 2.8）。
5. 顺手把第二章 2.3 的 `user.email` 设成 GitHub 邮箱。

### 8.3 Fork：把别人的仓库复制到你名下

访问 `https://github.com/panzhaohu666/learning-hub`，点右上角 **Fork** 按钮。

Fork 之后你就有了一份 **`你的用户名/learning-hub`** 的副本，归你所有，你可以随便改。

```
GitHub 上同时存在两个仓库：

panzhaohu666/learning-hub   ← 原仓库（"上游"，你的 PR 最终要合到这里）
你的用户名/learning-hub     ← 你的 Fork（你的改动基地）
```

### 8.4 Pull Request 完整流程（严格按 README 贡献流程）

本仓库 README 的"贡献流程"是这么写的：

```bash
# 1. Fork 本仓库
# 2. 创建你的特性分支
git checkout -b feature/your-feature-name

# 3. 提交你的改动（commit message 用中文）
git commit -m "修复：阶段一代码示例中的 OpenAI 客户端初始化错误"

# 4. 推送到你的 Fork
git push origin feature/your-feature-name

# 5. 发起 Pull Request，描述你做了什么、为什么要这样做
```

下面把这 5 步逐步拆开，每一步都告诉你在哪里、做什么。

**第 1 步：Fork（网页操作）**：按 8.3，在你的账号下得到一份副本。

**第 2 步：克隆你的 Fork 并创建特性分支（终端操作）**：

```bash
# 克隆你自己的 Fork（注意是"你的用户名"，不是 panzhaohu666）
git clone git@github.com:你的用户名/learning-hub.git
cd learning-hub

# 创建特性分支（README 的规范命名：feature/你的功能名）
git checkout -b feature/fix-python-example

# 确认当前分支
git branch
# * feature/fix-python-example
```

> 💡 为什么必须开新分支？因为你不能在 main 上直接给上游仓库提 PR，而且独立分支让"这次改一个主题"清清楚楚。这是开源协作的铁规矩。

**第 3 步：修改 + 提交（终端操作）**：

```bash
# 编辑你要改的文件（比如修复 01-总纲.md 里的一个错别字）
# 然后：
git status                  # 确认改了什么
git diff                    # 确认改得对不对
git add -A
git commit -m "修复：01-总纲.md 中的一处错别字"
```

commit 信息用中文，格式按第四章：`动作：对象 — 说明`。

**第 4 步：推送到你的 Fork（终端操作）**：

```bash
git push origin feature/fix-python-example
```

第一次推新分支时，Git 可能提示：

```
fatal: The current branch feature/fix-python-example has no upstream branch.
```

意思是这条分支还没和远程绑定。Git 会教你下一步，或者直接跑：

```bash
git push -u origin feature/fix-python-example
```

推送成功后会看到：

```
remote: Create a pull request for 'feature/fix-python-example' on GitHub by visiting:
remote:   https://github.com/你的用户名/learning-hub/pull/new/feature/fix-python-example
```

**第 5 步：发起 Pull Request（网页操作）**：

GitHub 推送成功后会直接给你一个"Compare & pull request"的黄色按钮（在你的 Fork 仓库页面顶部），点它。

进入 PR 创建页，填三样东西：

| 字段 | 怎么写 |
|------|--------|
| 标题 | 一句话说清：`修复：阶段一代码示例中的 OpenAI 客户端初始化错误` |
| 描述 | 做了什么、为什么做、怎么验证的 |
| 目标 | 确认方向是 `panzhaohu666/learning-hub` ← `你的用户名/learning-hub` |

点 **Create pull request**，你的第一个 PR 就诞生了！

**之后的等待**：

- 仓库维护者会收到通知，可能直接合并，也可能留言让你修改。
- 如果要求修改：回到本地 `feature/fix-python-example` 分支，改完再 `git add` + `git commit` + `git push origin feature/fix-python-example`，**PR 会自动更新**（因为 PR 跟着分支走）。
- 合并后，维护者可以选择删除你的特性分支。

### 8.5 Fork 之后如何保持同步

你的 Fork 停留在 fork 那一刻。原仓库更新了，你本地想跟上：

```bash
# 添加"上游"远程（第一次）
git remote add upstream git@github.com:panzhaohu666/learning-hub.git

# 之后每次同步
git switch main                 # 回到主分支
git pull upstream main          # 从上游拉取最新
git push origin main            # 同步到你的 Fork

# 远程一览（现在有两个远程）
git remote -v
# origin    git@github.com:你的用户名/learning-hub.git (fetch)
# upstream  git@github.com:panzhaohu666/learning-hub.git (fetch)
```

> 💡 术语：`origin` = 你自己的 Fork，`upstream` = 原仓库。这是开源世界的通用叫法，GitHub 的 "Sync fork" 按钮就是干这个的。

### 8.6 提 Issue 的规范

不想直接改代码，只发现问题 → 提 Issue：

1. 仓库页面点 **Issues** → **New issue**。
2. 标题要能概括问题，比如 `[建议] Linux 指南缺少 tar 解压到指定目录的示例`。
3. 正文模板（本仓库 README 推荐的风格）：
   - 起点：我在做什么
   - 过程：卡在哪、看到了什么
   - 期望：希望改成什么样

**Issue 礼仪**：
- 先搜索有没有人提过同样的 Issue（避免重复）。
- 一个 Issue 只讲一个问题。
- 友好，别人是义务维护，不是客服。

### 8.7 Code Review：怎么审、怎么被审

**作为 PR 作者**，收到 review 意见时：

```bash
# 态度：每条意见都回复，哪怕只是"已修复"或"我不这么认为，因为..."
# 修改流程：
git switch feature/xxx          # 回到特性分支
# 改代码
git add -A
git commit -m "修复：根据 review 意见调整逻辑"
git push origin feature/xxx     # PR 自动更新
```

**作为 reviewer**（别人给你发 PR 或你审查别人）：
- 在 GitHub 的 PR 页面，点 **Files changed** 逐行看。
- 点行号旁的 `+` 可以发表评论。
- 意见分级：必须改（Blocking）/ 建议（Suggestion）/ 可选（Nitpick）。
- 表达方式：`这里的边界条件没处理，建议补上` 而不是 `你这写的什么垃圾`。

### 8.8 团队协作进阶：分支保护（了解即可）

大型项目的 main 分支会开启**分支保护**（Branch Protection）：

| 规则 | 作用 |
|------|------|
| 不允许直接 push main | 所有改动必须走 PR |
| 要求至少 1 人审查通过 | 代码质量门禁 |
| 要求 CI 检查通过 | 自动测试必须过 |
| 要求 PR 与 main 保持同步 | 减少冲突 |

你现在的阶段不需要配这个，知道有这种机制就行。等你维护自己的项目、有协作者时再回来配。

---

## 九、.gitignore 实战

> 💻 实操（30 分钟）：.gitignore 是"哪些文件不该进仓库"的过滤清单。本仓库就有一个真实的 .gitignore，这一章我们逐行拆解它。

### 9.1 为什么需要 .gitignore

有些文件**不应该**被提交进 git：

| 文件类型 | 为什么不提交 |
|---------|-------------|
| 临时文件 | 编译产物、缓存，别人下载仓库没必要得到 |
| 密钥配置 | `.env` 里有数据库密码，提交=泄露 |
| 环境专属 | `.vscode/`、`.idea/` 是编辑器设置，因人而异 |
| 大数据 | 模型权重、数据集动辄几个 GB，git 存不下也没意义 |
| 依赖目录 | `node_modules/` 几十万文件，靠命令就能重新生成 |

`.gitignore` 就是一个文本文件，列出"Git 要忽略的文件"，让它们永远不进入暂存区。

### 9.2 .gitignore 语法速查

| 写法 | 含义 | 示例 |
|------|------|------|
| `# 注释` | 注释 | `# Python 缓存` |
| `文件名` | 忽略匹配的文件/目录 | `secret.txt` |
| `目录名/` | 忽略整个目录（斜杠结尾） | `node_modules/` |
| `*.扩展名` | 通配符，忽略所有该扩展名 | `*.log` |
| `*` | 匹配任意字符 | `*.py[cod]` |
| `?` | 匹配单个字符 | `temp?.txt` |
| `**` | 匹配任意层级的目录 | `**/__pycache__/` |
| `/开头` | 只匹配仓库根目录 | `/build/`（仅根目录下的 build） |
| `!` | 取反，例外不忽略 | `!.env.example` |
| 目录后不加 `/` | 忽略同名文件和目录 | `data` |

**规则生效顺序**：后面的规则覆盖前面的。先忽略一大片，再用 `!` 放行个别的。

### 9.3 本仓库的真实 .gitignore 逐段解读

这是 learning-hub 仓库根目录下的 `.gitignore`（真实内容），我们逐段看为什么这么写：

```
# Python
__pycache__/          # Python 运行时会生成的字节码缓存目录，人人可重新生成
*.py[cod]             # *.pyc / *.pyo / *.pyd 编译后的 Python 文件
*.so                  # 编译出的共享库
.venv/                # 虚拟环境（pip/conda 生成的独立 Python 环境）
venv/                 # 同上，另一种命名
*.egg-info/           # Python 包元数据目录

# Jupyter
.ipynb_checkpoints/   # Jupyter 笔记本自动生成的检查点文件

# OS
.DS_Store             # macOS 系统自动生成的文件夹描述文件
Thumbs.db             # Windows 资源管理器缩略图数据库

# IDE
.vscode/              # VS Code 编辑器个人设置
.idea/                # JetBrains 系列（PyCharm 等）个人设置
*.swp                 # vim 交换文件（vim 崩溃时的恢复文件）
*.swo                 # vim 交换文件（第二份）

# Obsidian
.obsidian/            # Obsidian 笔记软件的本仓库配置（.obsidian 是仓库内的配置目录）

# Models / Data (too large for git)
*.pt                  # PyTorch 模型权重
*.bin                 # 二进制模型文件
*.safetensors         # HuggingFace 新版模型权重格式
*.gguf                # llama.cpp 量化模型格式
data/                 # 数据目录
models/               # 模型目录
checkpoints/          # 训练检查点目录
*.ckpt                # 检查点文件

# Environment
.env                  # 环境变量文件（可能含密钥）⚠️ 重点
.env.local            # 本地环境变量
```

**解读要点**：

- 这个仓库既存文字笔记又跑 Python 代码，所以同时有 IDE、Python、模型三类忽略规则。
- `data/`、`models/` 目录下可能是几 GB 的权重文件，git 会爆炸，必须忽略。
- `.env` 和 `.env.local` 是**最容易出安全事故**的两行：里面常存 API key、数据库密码。

### 9.4 常用模板速查（按技术栈）

**Python**：

```
__pycache__/
*.py[cod]
.venv/
venv/
.env
```

**Node.js**：

```
node_modules/
dist/
.env
npm-debug.log*
```

**Java**：

```
target/
*.class
.idea/
*.iml
```

**Go**：

```
bin/
*.exe
*.test
```

**通用**：

```
.DS_Store
Thumbs.db
*.log
*~
*.swp
```

> 💡 更多模板去 `https://github.com/github/gitignore` 找，官方维护的超全模板库。

### 9.5 验证规则是否生效

```bash
# 方法一：git status 看是否还出现
git status

# 方法二：用 git check-ignore 精确查询（-v 显示是哪条规则匹配的）
git check-ignore -v .env
# .env:9:.env        ← 表示第 9 行的规则 .env 匹配了它

git check-ignore -v __pycache__/x.py
```

`git check-ignore -v` 是排障神器：写错规则时能立刻看出到底哪条规则在起作用。

### 9.6 已经提交了不想提交的文件怎么办

情况：文件之前没加 .gitignore，已经 commit 甚至 push 了。

```bash
# 1. 把它从 git 跟踪中移除（文件本身保留在磁盘上）
git rm --cached .env

# 2. 把规则写进 .gitignore
echo ".env" >> .gitignore

# 3. 提交
git add .gitignore
git commit -m "修复：移除误跟踪的 .env 并加入 .gitignore"
git push
```

> ⚠️ 注意：`git rm --cached` 只解除跟踪，文件还在你电脑上。而 `git rm`（不带 --cached）会连磁盘文件一起删掉。**历史提交里仍然有这份文件**，如果里面有密钥，还需要走灾难自救章节的"清除历史"方案，并立刻去平台改密码。

**一次性解除所有误跟踪文件**（配合 .gitignore 重来）：

```bash
git rm -r --cached .        # 解除所有文件跟踪（不动磁盘文件）
git add -A                  # 重新暂存，此时 .gitignore 规则生效
git commit -m "修复：重新应用 .gitignore 规则"
```

### 9.7 全局 .gitignore：所有仓库通用的忽略

有些规则（比如 `.DS_Store`、`*.swp`）每个仓库都想忽略，不用每个仓库都写一遍：

```bash
git config --global core.excludesfile ~/.gitignore_global
echo ".DS_Store" >> ~/.gitignore_global
echo "*.swp" >> ~/.gitignore_global
```

之后所有仓库自动忽略这些文件。仓库内的 `.gitignore` 仍然优先（先本地后全局）。

### 9.8 本章作业

在练习仓库里实操：

```bash
# 1. 创建一个"不该提交"的文件
echo "SECRET_KEY=abc123" > .env
echo "hello" > temp.log

# 2. 写 .gitignore 忽略它们
printf '.env\n*.log\n' > .gitignore

# 3. 验证
git status                  # 应该看不到 .env 和 temp.log
git check-ignore -v .env    # 应该显示规则来源

# 4. 提交
git add -A
git commit -m "初始化：新增 .gitignore"
```

---

## 十、常见灾难自救

> 📱 概念阅读（10 分钟）+ 💻 实操（40 分钟）：这一章汇集新手在真实使用中最容易捅的篓子。每个场景都是"我错了，怎么救"。记住一个总原则：**先别慌，先 reflog**。

### 10.1 灾难总原则

| 级别 | 可救性 | 手段 |
|------|--------|------|
| 本地提交乱套 | ✅ 几乎都能救 | reflog / reset |
| 已 push 的内容有问题 | ✅ 能救但会留痕 | revert / force-with-lease |
| 密钥已 push | ⚠️ 立刻止血 + 旋转密钥 | 删历史 + 改密码 |
| 没 commit 的改动被覆盖 | ❌ 基本没救 | 所以 commit 要勤 |

### 10.2 场景一：误把代码 commit 到 main

**症状**：本想在 `feature/x` 分支开发，结果在 main 上提交了一堆。

**方案：把 main 回退，把提交搬到新分支**：

```bash
# 1. 从当前 main 创建分支，保住"误提交"的代码
git switch -c feature/x

# 2. 回到 main，把它重置回误提交之前
git switch main
git reset --hard 误提交之前的hash   # 用 git reflog 查这个 hash

# 3. 现在 main 干净了，代码都在 feature/x 上
```

> 💡 如果误提交已经 push 到远程 main 了：先做上面两步，然后 `git push --force-with-lease origin main`。团队环境慎用，先和成员打招呼。

### 10.3 场景二：commit message 写错了

```bash
git commit --amend -m "修复：正确的提交信息"
```

已 push 的情况：`git push --force-with-lease origin main`（确认没人拉过）。

### 10.4 场景三：误删分支（分支上还有重要提交）

```bash
# 症状：git branch -D 删掉了 feature/important
# 1. 找分支最后指向的提交
git reflog
# 输出里找到类似：1a2b3c feature/important@{0}: branch: Created from main
# 或者最近的提交记录里找到那个分支的最后 hash

# 2. 从该提交重新拉出分支
git switch -c feature/important 1a2b3c
```

> 💡 只要你知道 hash（reflog 里有），分支的"尸体"就能复活。

### 10.5 场景四：误执行了 git reset --hard

```bash
# 症状：reset --hard 后刚改的代码全没了
# 1. 找 reset 前的位置
git reflog
# 5f6a7b HEAD@{0}: reset: moving to 1a2b3c   ← 就是这条，回退前在 5f6a7b

# 2. 回去
git reset --hard 5f6a7b
```

**完整恢复一切**：

```bash
git reset --hard @{1}     # @{1} 表示 reflog 里的"上一个位置"
```

### 10.6 场景五：push 错了内容到远程

```bash
# 如果只是想撤销最近一次 push 的提交（保留历史记录）：
git revert HEAD
git push

# 如果想把错误的提交彻底从历史抹掉（⚠️ 确认没人拉过）：
git reset --hard 正确的hash
git push --force-with-lease origin main
```

### 10.7 场景六：把密钥/敏感信息提交上去了

**这是最严重的事故，处理顺序非常重要**：

```bash
# 第 1 步（立刻）：去密钥对应的平台改密码/吊销 token
#   → 密码泄露了，改 git 历史只是亡羊补牢，密钥必须旋转！

# 第 2 步：从跟踪移除
git rm --cached .env
echo ".env" >> .gitignore

# 第 3 步：提交并推送
git add .gitignore
git commit -m "修复：移除误提交的敏感文件"
git push

# 第 4 步（可选，但强烈建议）：清理历史中的敏感内容
```

**清理历史**的现代推荐方案是 `git filter-repo`：

```bash
# 安装（Debian/Ubuntu）
sudo apt install git-filter-repo

# 在仓库根目录执行，把 .env 从整个历史中抹掉
git filter-repo --invert-paths --path .env --force

# 然后重新添加远程并强制推送
git remote add origin <你的远程地址>
git push --force-with-lease origin main
```

> ⚠️ 如果你的仓库已经公开、且密码真的在里面，清理历史后**默认 GitHub 不删除已 fork 副本里的旧内容**，所以第一步"改密码"才是真正的止血。简单场景下做到前三步即可。

### 10.8 场景七：合并冲突解到一半想放弃

```bash
git merge --abort       # 放弃 merge，回到合并前
git rebase --abort      # 放弃 rebase，回到 rebase 前
git cherry-pick --abort # 放弃 cherry-pick
```

> 💡 记一个口诀：任何"进行到一半"的操作都有 `--abort` 逃生口。

### 10.9 场景八：stash 了东西但想不起来是啥 / 找不到了

```bash
git stash list                 # 列出所有 stash
git stash show -p stash@{0}    # 查看内容
git stash apply stash@{0}      # 恢复
# 如果刚才误执行了 git stash clear（清空了）：
# 没救了，clear 的清空不可恢复。所以 clear 前务必确认。
```

### 10.10 场景九：改错文件想恢复成"某次提交的样子"

```bash
git restore --source=5c4b3a file.txt   # 把 file.txt 恢复成 5c4b3a 时的内容
git restore --source=HEAD~1 .          # 整个目录恢复到上一次提交
```

### 10.11 灾难自救决策表

| 出事了 | 第一步 | 第二步 |
|--------|--------|--------|
| 任何本地丢失 | `git reflog` | `git reset --hard <hash>` |
| 误 commit 到 main | 拉分支保住代码 | reset 回 main |
| message 写错 | `git commit --amend -m` | push 用 force-with-lease |
| 误删分支 | `git reflog` 找 hash | 重新 `switch -c` |
| push 错内容 | `git revert` | push |
| 密钥泄露 | **改密码！** | 移除文件 + 清理历史 |
| 冲突搞砸 | `--abort` 全家桶 | 重来 |

---

## 十一、个人品牌：让 GitHub 成为你的名片

> 📱 手机碎片阅读（15 分钟）+ 💻 实操（30 分钟）：GitHub 是程序员的简历、作品集、实验室。这一章教你用最少的精力，把 GitHub 打理成能给别人看的名片。

### 11.1 为什么 GitHub 是你的名片

招聘面试时，面试官最常说的话之一就是："把你的 GitHub 给我看看。"

GitHub 主页能展示三样东西：

| 展示面 | 传达的信息 |
|--------|-----------|
| 贡献绿格子 | 这人是不是长期坚持写代码（不是三分钟热度） |
| 置顶项目 | 这人做过什么、做到了什么程度 |
| Profile README | 这人是谁、在做什么、怎么联系 |

对学习计划而言还有一个实际作用：**绿格子是"允许降级，不允许归零"原则的量化仪表盘**。每周 push 一次，格子就不断档。

### 11.2 Profile README：让主页"开口说话"

方法：创建一个**和你的用户名同名**的仓库（比如你的用户名是 `panzhaohu666`，就建仓库 `panzhaohu666`），勾选 "Add a README file"。这个 README 会自动显示在你的 GitHub 主页顶部。

```bash
# 克隆同名仓库到本地
git clone git@github.com:你的用户名/你的用户名.git
cd 你的用户名

# 用 Markdown 写你的个人介绍
```

**一份好的 Profile README 结构**：

```markdown
# 👋 你好，我是 [你的名字]

## 🧑‍💻 关于我
- 正在系统学习大模型开发 / 备战软考
- 白天上班，晚上 2 小时 + 周末学习

## 🔭 我正在做什么
- 在 [learning-hub](https://github.com/panzhaohu666/learning-hub) 记录学习路线
- 阶段三：手写 Transformer

## 📊 GitHub 数据
（用 github-readme-stats 生成的统计卡片）

## 📫 联系我
- 邮箱：xxx@example.com
```

**实用工具**（都是现成的开源服务，README 里贴图即可）：

| 工具 | 用途 |
|------|------|
| github-readme-stats | 自动生成统计卡片（提交数/语言占比） |
| github-profile-trophy | 奖杯墙 |
| shields.io | 各种徽章（构建状态、版本号） |
| skill-icons | 技能图标集 |

### 11.3 绿格子：Contribution Graph 的真相

绿格子（贡献图）是**按照提交邮箱**计数的，不是按账号：

- ✅ 你的 `user.email` 和 GitHub 邮箱一致，提交才计入格子。
- ✅ 提交到自己的仓库、别人的仓库、fork 的仓库都算。
- ❌ 提交者邮箱对不上，代码白交，格子不亮。
- ❌ 只 fork 不改代码，不算贡献。

```bash
# 检查你的提交邮箱
git config --global user.email
# 必须和 https://github.com/settings/emails 里列出的邮箱一致
```

### 11.4 让绿格子"真实而好看"

| 做法 | 效果 | 评价 |
|------|------|------|
| 每周至少 push 一次 | 格子不断档 | ✅ 本仓库的硬性习惯 |
| 一次 push 一个完整的 commit | 格子饱满 | ✅ 真实 |
| 为了刷格子一天 push 20 次空改动 | 数字好看 | ❌ 造假，一眼看穿 |
| 修改 git 历史伪造日期 | 假全勤 | ❌ 严重诚信问题 |

> 💡 绿格子的意义不是"连续天数"，而是**长期主义**。断一周不会怎样，重置后继续。本仓库的哲学："允许降级，不允许归零"。

### 11.5 项目 README 怎么写出彩

你的项目主页（比如 Mini-GPT 项目）README 决定了别人 30 秒内会不会想点进去：

| 部分 | 内容 |
|------|------|
| 项目名 + 一句话介绍 | 这个项目是干嘛的 |
| 徽章（可选） | License / 版本 / 构建状态 |
| 演示截图/GIF | ⭐ 最重要，一张图胜过千言 |
| 快速开始 | 怎么安装、怎么跑 |
| 使用示例 | 代码片段 |
| 项目结构 | 目录树 |
| 技术栈 | 用了什么 |
| License | MIT 等 |

### 11.6 用 learning-hub 作为你的第一张名片

本仓库本身就是个人品牌建设的**现成素材**：

1. **星标+学习**：Star 这个仓库，让它出现在你的 Star 列表。
2. **Fork + 贡献**：走一遍第八章的完整 PR 流程，你的贡献记录会出现在仓库的贡献者列表。
3. **吃透内容再输出**：把学习笔记整理成自己的仓库，哪怕一开始只是"抄"了结构，也是你的起点。
4. **置顶**：把你的项目（哪怕很小）置顶在主页 Profile 的 Pinned 区。

### 11.7 常见误区

| 误区 | 真相 |
|------|------|
| 等我学完了再建 GitHub | 现在就该有，GitHub 是过程不是结果 |
| 代码不好不意思放 | 学习过程的代码同样有价值，README 注明"学习项目"即可 |
| 只放项目不放 Profile README | 主页空空如也，访客不知道你是谁 |
| 用别人的项目充门面 | Fork 不算你的成果，自己的提交才是 |
| 提交信息随便写 | 你的 commit 历史就是你的"开发日志" |

---

## 十二、每周 push 一次的最小工作流

> 📱 概念阅读（5 分钟）+ 💻 实操（20 分钟，以后每周 5-10 分钟）：这一章直接对接学习计划里的硬性要求。先把话说清楚：**"每周至少 push 一次代码"不是学习负担，是保底机制**。

### 12.1 这条要求从哪来

本仓库 README 的 FAQ 里写着（原文引用）：

> **最关键的底线是：允许降级，不允许归零。只要这周至少 push 了一次代码到 GitHub，这周就没有白过。**

大模型学习计划和软件设计师备考计划里，GitHub 被引用了 58 次以上，核心就一个意思：**用提交记录喂饱绿格子，用绿格子反推自己没停。**

### 12.2 最小工作流：每周 7 分钟

把下面这组命令设成你的"每周仪式"（不需要每天都做）：

```bash
# ① 进入你的笔记/项目仓库
cd ~/notes

# ② 先看看这周有没有欠账（新增/改动的文件）
git status
git diff

# ③ 不管改动多小，都要形成一次有意义的提交
#   哪怕只是补充了一行笔记、修了一个错别字
git add -A
git commit -m "完善：本周学习记录 v1 — 补充 Transformer 注意力机制笔记"

# ④ 推上去，绿格子+1
git push
```

**这 4 步的精髓**：

| 步骤 | 为什么 |
|------|--------|
| 看 status/diff | 培养"提交前检查"的职业习惯 |
| 必须有信息 | 提交信息按第四章规范，写清楚这周学了啥 |
| 允许小 | 一行笔记也是提交，重要的是"每周有产出存档" |
| push | 不上 GitHub 就不算"绿格子"，commit 只是本地 |

### 12.3 一键脚本（可选进阶）

把最小工作流写成脚本，每周只敲一行：

```bash
#!/bin/bash
# ~/bin/weekly-push.sh
cd ~/notes || exit 1

if [ -z "$(git status --porcelain)" ]; then
    echo "✅ 工作区干净，这周已经没欠账了"
    exit 0
fi

git add -A
git commit -m "完善：每周例行存档 $(date +%Y-%m-%d)"
git push
echo "✅ 已推送，本周打卡完成"
```

```bash
chmod +x ~/bin/weekly-push.sh
~/bin/weekly-push.sh        # 每周跑一次
```

### 12.4 各种意外下的降级预案

按"允许降级，不允许归零"的原则，把各种意外都准备好退路：

| 意外 | 降级方案 | 还是没归零吗 |
|------|---------|-------------|
| 这周只学了 10 分钟 | 把 10 分钟学的东西写成 3 行笔记提交 | ✅ |
| 这周完全没学 | 用 Obsidian 补一篇"本周回顾"提交 | ✅ |
| 电脑不在身边 | 用手机 GitHub 网页编辑仓库里一个文件直接 commit | ✅ |
| 断网 | 本地 commit 先存着，下周补 push | ✅（commit 已存档） |
| SSH 坏了 | 改用 HTTPS + token push | ✅ |
| 仓库没了 | 重建仓库 + `git remote add origin` + push | ✅ |

> 💡 关键认知：**commit 在本地就完成了存档，push 只是同步**。就算 push 断了，这周的产出也已经安全地存在你电脑上。降级到"本地 commit"也不算归零，但**请务必尽早补 push**，因为只有 push 才计入绿格子。

### 12.5 让 push 变成习惯的机制

光靠意志力会失效，设计机制才不会断：

1. **固定时间**：绑定一个已有习惯，比如"周六下午学习结束后，顺手 push"。
2. **手机提醒**：日历上设每周重复提醒"git push 打卡"。
3. **Obsidian 联动**：你每天记笔记，笔记文件就在仓库里，push 只是收尾动作。
4. **绿格子威慑**：打开主页看一眼，断档的格子很刺眼，会催你动手。
5. **降低门槛**：仓库里放一个 `学习日志/` 目录，每周往里面追加一个日期文件，这就是最低成本的提交素材。

### 12.6 对接两个学习计划

**大模型学习计划**（每周 ~18.5h）：

| 时间段 | push 内容建议 |
|--------|--------------|
| 周一至周五（电脑 2h） | 当天写的代码/实验笔记 |
| 周六 | 本周整体回顾，整理成文档提交 |
| 保底 | 哪怕只提交当天的学习日志 |

**软件设计师备考计划**（每周 ~8h）：

| 时间段 | push 内容建议 |
|--------|--------------|
| 每天 | 做错的真题 + 考点笔记 |
| 周末 | 错题本整理成 Markdown 提交 |

**通用模板**：

```bash
# 每天学习的最后 5 分钟
git add -A
git commit -m "完善：学习日志 $(date +%Y-%m-%d) — 今日完成 <一句话>"
git push
```

### 12.7 本章自检清单

- [ ] 我有一个 GitHub 仓库（自己的笔记仓库即可）
- [ ] SSH 配置好，`git push` 无需输密码
- [ ] `user.email` 和 GitHub 邮箱一致（绿格子才计数）
- [ ] 我知道这周学了什么，并且能写进 commit 信息
- [ ] 我设置了每周提醒（日历/Obsidian/手机）
- [ ] 本周已经 push 过至少一次

---

## 十三、常用命令速查表

> 📱 手机碎片阅读（随时查阅）：这一章是全书命令的浓缩版。手机上看一遍，电脑上遇到命令记不清了就回来查。

### 13.1 配置

| 命令 | 作用 |
|------|------|
| `git config --global user.name "名字"` | 设置用户名 |
| `git config --global user.email "邮箱"` | 设置邮箱（要和 GitHub 一致） |
| `git config --global init.defaultBranch main` | 默认分支名 |
| `git config --global alias.st status` | 设置别名 |
| `git config --list` | 查看所有配置 |
| `ssh-keygen -t ed25519 -C "邮箱"` | 生成 SSH 密钥 |
| `ssh -T git@github.com` | 测试 SSH 连接 |

### 13.2 本地仓库

| 命令 | 作用 |
|------|------|
| `git init` | 初始化仓库 |
| `git status` | 查看状态 ⭐ |
| `git add -A` | 暂存所有改动 |
| `git add 文件名` | 暂存指定文件 |
| `git commit -m "信息"` | 提交 |
| `git commit -am "信息"` | 提交已跟踪文件的改动 |
| `git log --oneline --graph --all` | 图形化历史 |
| `git show <hash>` | 查看某次提交 |
| `git blame 文件` | 每行是谁写的 |

### 13.3 比较差异

| 命令 | 作用 |
|------|------|
| `git diff` | 工作区 vs 暂存区 |
| `git diff --staged` | 暂存区 vs 上次提交 |
| `git diff HEAD` | 工作区 vs 上次提交 |
| `git diff 分支A..分支B` | 两个分支的差异 |

### 13.4 分支与合并

| 命令 | 作用 |
|------|------|
| `git branch` | 列出分支 |
| `git branch -a` | 列出所有分支（含远程） |
| `git checkout -b 分支名` | 创建并切换分支 |
| `git switch -c 分支名` | 创建并切换分支（新版） |
| `git switch 分支名` | 切换分支 |
| `git merge 分支名` | 合并分支到当前 |
| `git merge --no-ff 分支名` | 强制生成合并提交 |
| `git merge --abort` | 放弃合并 |
| `git branch -d 分支名` | 删除已合并分支 |
| `git branch -D 分支名` | 强制删除分支 |

### 13.5 撤销与恢复

| 命令 | 作用 |
|------|------|
| `git restore 文件` | 撤销工作区改动 |
| `git restore --staged 文件` | 撤销暂存 |
| `git reset --soft HEAD~1` | 撤销提交，改动留暂存区 |
| `git reset HEAD~1` | 撤销提交，改动回工作区 |
| `git reset --hard <hash>` | ⚠️ 强制回到某提交 |
| `git revert <hash>` | 用反向提交撤销 |
| `git commit --amend -m "新信息"` | 修改最后一次提交 |
| `git reflog` | 查看操作日志（救命的） |
| `git restore --source=<hash> 文件` | 恢复文件到某提交版本 |

### 13.6 远程协作

| 命令 | 作用 |
|------|------|
| `git remote -v` | 查看远程仓库 |
| `git remote add origin <地址>` | 添加远程 |
| `git remote add upstream <地址>` | 添加上游仓库（fork 同步用） |
| `git clone <地址>` | 克隆仓库 |
| `git push -u origin main` | 首次推送并绑定追踪 |
| `git push` | 推送 |
| `git pull` | 拉取并合并 |
| `git pull --rebase` | 拉取并变基 |
| `git fetch origin` | 只下载远程更新 |
| `git push --force-with-lease` | 安全强推（慎用） |

### 13.7 stash 与清理

| 命令 | 作用 |
|------|------|
| `git stash push -m "说明"` | 暂存改动 |
| `git stash list` | 查看暂存列表 |
| `git stash pop` | 恢复最近暂存并删除 |
| `git stash apply` | 恢复但不删除 |
| `git stash drop` | 删除某份暂存 |
| `git rm --cached 文件` | 解除跟踪（保留文件） |
| `git check-ignore -v 文件` | 查询忽略规则来源 |

### 13.8 标签

| 命令 | 作用 |
|------|------|
| `git tag v1.0.0` | 打轻量标签 |
| `git tag -a v1.0.0 -m "说明"` | 打附注标签 |
| `git push --tags` | 推送所有标签 |
| `git tag -d v1.0.0` | 删除本地标签 |

---

## 十四、章节练习

> 💻 综合实操（60-90 分钟）：所有练习按顺序做完，你就是一个能独立完成本仓库全部要求（每周 push + 贡献流程）的 Git 使用者了。每个练习都在前面的章节里能找到答案。

### 练习一：概念理解（第一章）

1. Git 和 SVN 的本质区别是什么？为什么 Git 离线也能提交？
2. 文件在 Git 里依次经过哪四个区域？
3. 什么是 HEAD？它指向什么？

### 练习二：环境搭建（第二章）

1. 安装 Git，`git --version` 能看到版本号。
2. 设置 `user.name` 和 `user.email`，邮箱必须和 GitHub 一致。
3. 生成 SSH 密钥，添加到 GitHub，`ssh -T git@github.com` 验证通过。
4. 配置三个别名：`st`、`lg`、`co`。

**通关标准**：`ssh -T git@github.com` 显示 `Hi 你的用户名!`。

### 练习三：本地仓库（第三章）

在 `~/notes` 建一个仓库，完成以下提交序列：

```bash
# 提交 1：初始化 README
# 提交 2：新增 Python 笔记，含"变量与数据类型"
# 提交 3：修改 README，补充使用说明
```

每步之间用 `git status`、`git diff`、`git log --oneline` 观察状态变化。

**通关标准**：`git log --oneline` 显示 3 条有意义的提交。

### 练习四：提交规范（第四章）

把练习三里的提交信息改造成本仓库风格（"完善：对象 v1 — 说明" / "初始化：..."）。

**通关标准**：`git log --oneline` 里的信息是一眼能看懂的中文标题。

### 练习五：分支与合并（第五章）

1. 从 main 创建 `feature/notes`，在里面新增一个文件并提交。
2. 切回 main，制造一次冲突（两个分支改同一文件同一行）。
3. 解决冲突，提交合并。
4. 用 `git log --oneline --graph --all` 观察分支图形。

**通关标准**：graph 里能看到 `|/` 分支分叉痕迹。

### 练习六：回滚恢复（第六章）

1. 误提交后 `git reset --soft HEAD~1` 撤销，改动留在暂存区。
2. 把一次改动 `git stash` 起来，再 `git stash pop` 恢复。
3. 故意 `git reset --hard` 一次，然后用 `git reflog` 找回来。

**通关标准**：reflog 让你"丢失"的东西全部找回。

### 练习七：远程仓库（第七章）

1. 在 GitHub 新建一个空仓库 `notes`。
2. 把练习三的本地仓库 push 上去（`git push -u origin main`）。
3. 从 GitHub 网页修改一个文件，再用 `git pull` 拉回来。

**通关标准**：本地和远程历史完全一致，`git status` 显示 clean。

### 练习八：Pull Request 完整流程（第八章）⭐ 终极练习

1. Fork `panzhaohu666/learning-hub`。
2. `git clone` 你的 Fork，创建分支 `feature/improve-readme`。
3. 改一处内容（比如给某个章节加一句你的理解），中文 commit。
4. `git push -u origin feature/improve-readme`。
5. 打开 PR，描述你改了什么、为什么改。

**通关标准**：你在 GitHub 上拥有一个真实的 PR 链接。就算没被合并，这个流程你已经完整走通了。如果 PR 被要求修改，按 review 意见改完再 push，体会 PR 自动更新的过程。

### 练习九：.gitignore（第九章）

在练习仓库里创建 `.env` 和 `temp.log`，用 `.gitignore` 忽略它们，用 `git check-ignore -v` 验证规则来源。

**通关标准**：`git status` 里永远看不到 `.env` 和 `temp.log`。

### 练习十：灾难自救（第十章）

自导自演三个灾难并自救：

1. 误删分支 → reflog 找回。
2. commit 信息写错 → amend 修复。
3. 误把密钥文件 add 进暂存区 → `git restore --staged` 撤出 + 加入 .gitignore。

**通关标准**：每个灾难 5 分钟内解决，全程不慌。

### 练习十一：个人品牌（第十一章）

1. 创建和用户名同名的仓库，写 Profile README。
2. 更新学习计划仓库的贡献者表格（走一遍 PR 流程，把"你的名字"填进贡献者列表）。
3. 确认你的绿格子开始有颜色。

**通关标准**：你的 GitHub 主页打开后，10 秒内能让人知道你是谁、在学什么。

### 练习十二：每周 push 工作流（第十二章）

1. 配置好你的"每周仪式"命令序列。
2. 从今天开始，连续 4 周每周至少 push 一次。

**通关标准**：4 周后绿格子连成一片，你已养成终身受用的习惯。

### 综合实战：毕业作品

创建一个你自己的项目仓库，要求：

- 结构清晰，README 内容完整（按 11.5 的结构）
- `.gitignore` 覆盖你的技术栈
- 提交信息全部符合第四章规范
- 至少包含一次分支合并、一次冲突解决、一次 stash 使用
- 设置好远程并 push

完成后把链接发到 learning-hub 的 Issue（`[成功故事]` 格式，见 README），你的名字就进了贡献者名单。

---

> **"版本控制拯救的不是你的代码，是你改坏了代码之后重新开始的勇气。"**
>
> 坚持不下去的时候，记住学习计划的防崩预案：
> **允许降级，不允许归零。每周至少 push 一次，这周就没有白过。**
>
> 下一站：[Linux 完全操作指南](../Linux学习/Linux完全操作指南.md) · 返回 [learning-hub 主页](../README.md)
