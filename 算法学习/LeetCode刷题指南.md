# LeetCode 刷题指南（Python · 面试向）

> 适用对象：Python 学习者，无竞赛背景，正在准备大模型/算法岗位面试 | 涵盖：刷题方法论、复杂度分析、Python 刷题利器、14 类高频模式模板、LeetCode Hot 100 分类速查（80 题）、面试沟通流程、8 周刷题计划、章节练习

> 本指南对接《大模型学习 / 07-阶段四至七-Agent到面试.md》阶段七目标：LeetCode Hot 100 刷完。刷题语言统一为 Python 3.10+，第四章所有模板均为完整可运行代码，不依赖任何第三方库，直接 `python xxx.py` 即可跑。

> 使用原则：📱 手机看思路（通勤、排队、午休时读），💻 电脑写代码（晚上整块时间敲）。延续本库"无视频"原则：不看视频课，只读文字加手写代码。先理解，再默写，最后上机。

---

## 目录

1. [为什么刷题与刷题方法论](#一为什么刷题与刷题方法论)
2. [复杂度分析速成](#二复杂度分析速成)
3. [Python 刷题利器](#三python-刷题利器)
4. [高频模式模板](#四高频模式模板)
5. [Hot 100 分类速查](#五hot-100-分类速查)
6. [面试沟通流程](#六面试沟通流程)
7. [8周刷题计划（对接阶段七）](#七8周刷题计划对接阶段七)
8. [章节练习](#八章节练习)

---

## 一、为什么刷题与刷题方法论

### 1.1 为什么大模型岗位也要刷 LeetCode

你可能觉得：我是搞大模型的，又不是做搜索推荐的，为什么要刷算法题？

现实是残酷的。**国内大厂算法岗、AI 岗、大模型岗，笔试第一关几乎都是算法题**。你花 6 个月手写了 Mini-GPT、做了 LoRA 微调、搭了 RAG 系统，但笔试过不了，面试官根本看不到你的简历亮点。

更扎心的事实：**算法题是面试中最容易"刷分"的部分**。项目经历可以包装，八股文可以背，但算法题是现场写的，一写就露馅。反过来，只要你刷够了，算法题反而是最稳的得分项，因为它的套路高度重复。

面试官通过一道算法题考察四件事：

| 考察点 | 面试官在想什么 |
|--------|---------------|
| 代码能力 | 会不会写干净的 Python，有没有 bug |
| 沟通能力 | 能不能把思路讲清楚，会不会装懂 |
| 边界意识 | 空输入、极端值、重复元素有没有想到 |
| 复杂度意识 | 能不能分析时间和空间复杂度，能不能优化 |

所以刷题不是"背答案"，而是用最便宜的方式训练这四种能力。刷题刷到后期，你拿到一道题，第一反应是"这题考什么模式"，而不是"这道题我不会"。

### 1.2 没有竞赛背景，怎么定位自己

先给自己松绑：**你不参加 ACM，不需要成为竞赛选手**。

竞赛选手的目标是 30 分钟 AC 一道 Hard 压轴题。你的目标低得多，也实际得多：

```
你的目标：
✔ 20 分钟内做出一道面试常见的 Medium
✔ 能边写边讲思路
✔ 能说清复杂度
✔ 面试官追问时能接住
✘ 不用 5 分钟秒掉 Hard
✘ 不用记住几百个冷门模板
```

LeetCode 上有 3000+ 题，全刷不现实也没必要。真正值得刷的只有两批：**Hot 100**（高频题，覆盖 80% 面试场景）和 **剑指 Offer**（国内大厂最爱）。本指南围绕 Hot 100 展开，第四章把 Hot 100 里反复出现的 14 类模式全部整理成模板，你真正要做的是：**把 14 个模板吃透，把 80 道高频题练熟**。

一个诚实的预期管理：前两周你会觉得很难，一道简单题要 40 分钟，看题解还要 10 分钟才能懂。这完全正常。**第 3 周开始出现"似曾相识"，第 5 周开始形成肌肉记忆，第 7 周开始能自己做 Medium**。刷题是典型的"先苦后甜"，前面的痛苦是买后面的甜的。

### 1.3 刷题的正确顺序

很多人一上来就按题号从 1 刷到 100，这是最差的做法。正确顺序是：

```
第一步：先学模式（1-2 天）
   把本指南第四章的 14 个模板看一遍，每个模板的代码自己敲一遍
   目的：脑子里先有"模式地图"，做题时能对号入座

第二步：分类刷题（第 1-6 周）
   按 tag 刷，一次只练一类模式
   比如本周练哈希表，就只做哈希相关的题
   目的：强化单一模式，形成"看到特征 → 想到模板"的反射

第三步：混合刷题（第 7 周）
   随机抽题，不看 tag
   目的：训练"识别模式"的能力，这是面试真正考的东西

第四步：重做（贯穿全程）
   隔 3 天、隔 1 周、隔 1 个月各重做一遍
   重做时不准看题解，写不出来就记下来，下次再试
```

核心原则：**一道题刷 3 遍，胜过 3 道题各刷 1 遍**。

每天刷多少？阶段七给的建议是每天 2-3 题。工作日保持这个节奏，周末可以集中做 4-6 题加复盘。重要的是"每天都有"，而不是"某天刷爆"。

### 1.4 一道题的标准流程（5 步法）

拿到一道题，不要急着写代码。按这 5 步走，每道题 30-40 分钟：

```
Step 1  读懂题目（2 分钟）
   ✔ 输入是什么，输出是什么
   ✔ 数据范围多大（这决定算法方向）
   ✔ 有没有空输入、重复元素、溢出风险
   ✔ 把题目给的示例自己口算一遍

Step 2  想思路（5 分钟）
   ✔ 先想暴力解（哪怕很慢），写下来
   ✔ 再想怎么优化：能不能用哈希/排序/双指针
   ✔ 对号入座：这题属于第四章哪个模板
   ✔ 想不出就看题解，不丢人

Step 3  写代码（15-20 分钟）
   ✔ 先写骨架（函数签名、边界判断），再填细节
   ✔ 边写边在脑子里跑一遍示例
   ✔ 变量命名清晰，不追求"最短代码"

Step 4  跑测试（5 分钟）
   ✔ 跑题目给的示例
   ✔ 想 2-3 个边界用例：空输入、单元素、全重复、最大规模
   ✔ 有 bug 先自己看，别急着看答案

Step 5  复盘（5 分钟）
   ✔ 这题属于什么模式？
   ✔ 一句话思路是什么？（写进笔记）
   ✔ 复杂度是多少？
   ✔ 和哪道题很像？
```

其中 Step 2 是最重要的分水岭。初学者最常犯的错误是"拿到题就写"，结果写了一半发现思路不对，全删。**思路想清楚了再动手，代码只是把思路翻译成语法。**

### 1.5 怎么"读懂"题目

读题不是扫一遍就完了。请盯着这三个问题：

**问题 1：数据规模有多大？**

数据规模直接决定你能用什么复杂度的算法。这是刷题最重要的"读题技能"：

| 数据规模 n | 可接受的复杂度 | 对应算法 |
|-----------|--------------|---------|
| n ≤ 10 | O(n!) | 暴力枚举、全排列 |
| n ≤ 20 | O(2ⁿ) | 回溯、状态压缩 |
| n ≤ 500 | O(n³) | 三重循环、Floyd |
| n ≤ 5000 | O(n²) | 双重循环、DP 二维 |
| n ≤ 10⁵ | O(n log n) | 排序、二分、堆 |
| n ≤ 10⁶ | O(n) | 哈希、双指针、滑动窗口 |
| n 巨大 | O(log n) / O(1) | 二分、数学公式 |

**面试时如果题目没给范围，直接问面试官**："n 最大是多少？"这不是废话，这决定你的解法方向，问出来反而加分。

**问题 2：有没有坑？**

- 数组可能为空吗？
- 可能有重复元素吗？重复时返回哪个？
- 数字可能溢出吗？（Python 不用担心，但其他语言要）
- 输入是无序的吗？需要保持顺序吗？

**问题 3：示例看明白了吗？**

把示例手工走一遍，确认你理解的输出和题目一致。很多题"看起来懂了，一写就错"，就是示例没走。

### 1.6 📱 手机看思路 / 💻 电脑写代码

本库的"手机+电脑"双轨哲学在刷题上尤其有效，因为刷题的本质是"思路 + 手速"两件事，正好分别对应手机和电脑：

**📱 手机摸鱼时间（通勤、午休、排队）：**
- 读一道题，只写思路，不写代码
- 把第五章的 80 题思路当"卡片"翻，今天翻 5 张
- 默想模板：这个模式的核心代码是什么，在心里打草稿
- 把不会的题收藏，晚上重点练

**💻 晚上电脑时间（1.5-2 小时）：**
- 把白天看过的题真正写一遍
- 15 分钟写不出来，看题解，看完合上，自己重写
- 写完立刻跑测试，别偷懒

**为什么不能反过来？** 手机上看代码体验差，指头点来点去效率极低；电脑上纯看思路又浪费了写代码的机会。手机负责"想"，电脑负责"写"，各司其职。

### 1.7 常见误区与心态管理

**误区 1：只看题解，不动手**
看完题解觉得"哦原来这么简单"，然后跳过。结果 3 天后发现根本写不出来。**看懂 ≠ 会写**。唯一的标准是：合上题解，能自己写出来才算会。

**误区 2：上来就追求最优解**
一道题想出了 O(n) 的解，还要纠结 O(n log n) 是不是更好。新手阶段，能 AC 就是胜利。最优解是在会做的基础上慢慢优化的，不是第一步。

**误区 3：刷难题找挫败感**
Hard 题一刷就卡，卡完就怀疑人生。顺序应该是：Easy 建立手感 → Medium 形成模式 → Hard 偶尔挑战。**面试主力是 Medium**，把 Medium 刷透比啃三道 Hard 有用。

**误区 4：不总结，刷了就忘**
刷 10 题不总结 = 白刷。每道题花 5 分钟记录"模式 + 一句话思路 + 复杂度"，这 5 分钟的价值超过做题的 30 分钟。面试前你复习的就是这份笔记。

**心态 1：卡住很正常**
高手也卡题。卡住 20 分钟看题解，看完总结"我为什么没想到"，比死磕 2 小时有效。

**心态 2：忘是正常的**
3 天前的题忘了思路？太正常了。重做一遍，第二次的理解会比第一次深得多。遗忘不是敌人，重做才是记忆的方法。

**心态 3：你不需要刷完 3000 题**
Hot 100 就够了，剩下的是重复。刷完 Hot 100 再刷剑指 Offer，足够应付绝大多数面试。

### 1.8 复盘模板（存进 Obsidian）

建一个 `LeetCode刷题复盘.md`，每道题按下面的模板记。面试前一周，你只需要复习这个文件：

```
# 题目：两数之和
- 链接：https://leetcode.cn/problems/two-sum/
- 难度：简单 | 模式：哈希表
- 一句话思路：边遍历边存哈希表，查 target - x 是否出现过
- 复杂度：O(n) / O(n)
- 易错点：先查后存，避免同一个元素用两次
- 同类题：三数之和(15)、四数相加II(454)
- 重做记录：✔ 第1遍 | ✘ 第2遍(忘了哈希) | ✔ 第3遍
```

格式说明：
- **模式**：必须写，这是你形成模式识别能力的关键
- **一句话思路**：用"动词 + 结构"描述，比如"边扫边存"，不要抄题解长文
- **同类题**：把散落的题串成串，面试官爱问"你还做过类似的题吗"
- **重做记录**：用打勾打叉记录每一次重做结果，这是你最真实的进度条

### 1.9 本章小结

把这一章的要点压缩成一张卡片，贴在手机上：

```
刷题 = 学模式(第四章) → 按 tag 分类刷(第五章) → 重做(间隔重复)

每道题 5 步：读题 → 想思路 → 写代码 → 跑测试 → 复盘
读题三问：数据规模？有没有坑？示例走通没？

数据规模决定算法：
  n≤20 回溯 | n≤5000 平方级 | n≤10⁵ nlogn | n≤10⁶ 线性

每天 2-3 题，一道题刷 3 遍胜过 3 道题各刷 1 遍
```

---

## 二、复杂度分析速成

### 2.1 为什么复杂度比"快不快"更重要

你的代码运行快不快，取决于三件事：**数据规模、机器性能、算法效率**。机器性能是常量（同一台机器，1 秒就是 1 秒），数据规模由题目决定，你唯一能控制的就是算法效率。

复杂度就是描述算法效率的"数学刻度"。它回答一个问题：**当数据规模变成 10 倍时，你的程序时间会变成几倍？**

- 扫描一遍数组：10 倍数据 → 10 倍时间，线性增长
- 双重循环：10 倍数据 → 100 倍时间，平方增长
- 折半查找：10 倍数据 → 时间只多一点点，对数增长

面试必问"你的算法时间复杂度是多少？"，答不出来或者答错，会直接扣印象分。反过来，能清晰说出"O(n log n)，主要来自排序"，是加分项。

### 2.2 大 O 记号：从生活类比到正式理解

**生活类比**：你负责把 n 个盘子擦干放进柜子。

- 方法 A：一个接一个擦，放一个柜子。时间正比于 n，是 O(n)
- 方法 B：为了省事，每放一个盘子就把所有盘子重新排一遍序。排序成本 n log n，总成本 n log n，是 O(n log n)
- 方法 C：雇了 n² 个人，每个人都检查所有盘子。是 O(n²)

大 O 回答的不是"具体几秒"，而是"成本随 n 怎么涨"。

**正式定义**：如果存在常数 c 和 n₀，使得对所有 n > n₀，都有 f(n) ≤ c·g(n)，则说 f(n) = O(g(n))。不用背这个数学定义，记住三条实用规则：

```
规则 1：忽略常数项        O(2n) = O(n)，O(100n) = O(n)
规则 2：忽略低阶项        O(n² + n) = O(n²)
规则 3：只保留增长最快的项  O(3n³ + 2n² + 5) = O(n³)
```

判断一个复杂度的直觉：**n 从 1 变成 10 万，这个表达式的值变多少倍**。

### 2.3 常见复杂度从快到慢

从快到慢排列，每档配一个生活类比，帮助记忆：

| 复杂度 | 名称 | 生活类比 | n=10⁵ 时的感受 |
|--------|------|---------|---------------|
| O(1) | 常数 | 直接翻到书的第 100 页 | 瞬间 |
| O(log n) | 对数 | 猜数字游戏每次排除一半 | 约 17 步 |
| O(n) | 线性 | 从头到尾数一遍人数 | 10 万步 |
| O(n log n) | 线性对数 | 快速排序、归并排序 | 约 170 万步 |
| O(n²) | 平方 | 所有人两两握手 | 100 亿步，卡死 |
| O(2ⁿ) | 指数 | 每个盘子选"擦或不擦" | 宇宙毁灭都算不完 |
| O(n!) | 阶乘 | 给 n 个人排座位 | 同上，更夸张 |

**关键阈值**：计算机一秒大约能执行 10⁸ 次基础操作。所以：

```
n ≤ 10⁶   → 只能 O(n) 或更快
n ≤ 10⁵   → O(n log n) 可以
n ≤ 5000  → O(n²) 可以
n ≤ 20    → O(2ⁿ) 可以（回溯）
```

这就是为什么"读题看数据范围"那么重要。看到 n ≤ 10⁵，你要写 O(n²) 就注定超时，趁早换思路。

### 2.4 怎么算循环的复杂度

**情况 1：单层循环，i 从 0 到 n**

```python
for i in range(n):      # O(n)
    print(i)
```

**情况 2：嵌套循环，互不相关**

```python
for i in range(n):      # 外层 n 次
    for j in range(n):  # 内层 n 次，共 n²
        print(i, j)     # O(n²)
```

**情况 3：嵌套循环，每次减半**

```python
for i in range(n):          # 外层 n 次
    j = n
    while j > 0:            # 内层每次除 2，O(log n)
        j //= 2
# 总复杂度 O(n log n)
```

**情况 4：折半循环**

```python
i = n
while i > 0:        # n → n/2 → n/4 → ... → 1
    i //= 2         # 一共 log₂n 次，O(log n)
```

**情况 5：双指针，各自只走一遍**

```python
left, right = 0, n - 1
while left < right:   # 虽然有两个指针，但每个元素最多被访问一次
    if condition:
        left += 1
    else:
        right -= 1
# 总移动次数 ≤ n，O(n)，不是 O(n²)！
```

**情况 6：二分查找**

```python
left, right = 0, n - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] < target:
        left = mid + 1
    elif nums[mid] > target:
        right = mid - 1
    else:
        return mid
# 每次排除一半，O(log n)
```

**快速判断口诀**：
- 一个循环走 n 次 → O(n)
- 循环里每次减半 → O(log n)
- 两个独立循环嵌套 → O(n²)
- 一个循环走 n 次，里面做 O(1) 操作 → O(n)
- 一个循环走 n 次，里面做 O(log n) 操作 → O(n log n)

### 2.5 递归与主定理

递归的复杂度看**递归树**，也就是"每个节点花多少时间 × 一共多少个节点"。

**例子 1：二叉树的遍历**

```python
def visit(root):
    if not root:
        return
    visit(root.left)    # 递归左子树
    visit(root.right)   # 递归右子树
```

每个节点访问一次，一共 n 个节点，每次 O(1)，总复杂度 O(n)。

**例子 2：斐波那契的朴素递归**

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)  # 一棵指数级展开的递归树
```

每个节点分出两个子节点，树高 n，总节点数 O(2ⁿ)。这就是为什么朴素递归求 fib(50) 会卡死，而用 DP 只要 O(n)。

**例子 3：归并排序**

```python
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)  # merge 是 O(n)
```

树高 log₂n 层，每层总共 O(n) 的合并开销，总复杂度 O(n log n)。

**主定理（简化版）**：如果递归满足 T(n) = a·T(n/b) + O(n^d)，那么：

| 条件 | 复杂度 |
|------|--------|
| d > log_b(a) | O(n^d) |
| d = log_b(a) | O(n^d log n) |
| d < log_b(a) | O(n^log_b(a)) |

归并排序：a=2, b=2, d=1，log₂2=1=d，所以是 O(n log n)。二分查找：a=1, b=2, d=0，log₂1=0=d，所以是 O(log n)。这个简化版足够覆盖面试 95% 的情况。

### 2.6 空间复杂度

空间复杂度数的是**额外占了多少内存**，同样的符号体系。

```
O(1)     只用了几个变量，没有随 n 增长的结构
O(n)     用了长度为 n 的数组 / 哈希表 / 递归深度 n
O(n²)    用了 n×n 的二维数组
O(log n) 用了二分查找的递归栈（很少见，但要知道）
```

**常见陷阱**：

- **输入不算额外空间**。排序数组本身 O(n) 不算，但如果你复制了一份就是 O(n)
- **递归栈算空间**。深度为 n 的递归占 O(n) 栈空间，这就是为什么深递归可能栈溢出
- **原地算法 vs 拷贝算法**。面试官会问"能不能 O(1) 额外空间"，比如移动零、反转字符串

**面试常用语**："时间 O(n)，空间 O(1)，因为只用了几个指针变量。"

### 2.7 复杂度与数据规模速查表

把这张表打印出来，做题时贴在旁边：

| 目标复杂度 | 数据规模上限（1 秒） | 常见算法 |
|-----------|--------------------|---------|
| O(log n) | 无上限（10¹⁸ 都行） | 二分、快速幂 |
| O(√n) | 10¹⁴ | 判断素数 |
| O(n) | 10⁷-10⁸ | 哈希、滑动窗口、双指针、前缀和 |
| O(n log n) | 10⁵-10⁶ | 排序、堆、分治 |
| O(n²) | 5000 | 二维 DP、暴力双重循环 |
| O(n³) | 500 | 三重循环、Floyd |
| O(2ⁿ) | 20 | 回溯、状态压缩 |
| O(n!) | 10 | 全排列暴力 |

### 2.8 面试中怎么回答复杂度问题

面试官问"分析一下复杂度"，不是等你算个数字，而是看你会不会**有条理地拆解**。背一个口述模板：

```
口述模板：
"时间上，主循环遍历 n 个元素，每个元素做 O(1) 的哈希查表，
所以整体是 O(n)。空间上，用了一个哈希表，最坏存 n 个键值对，
所以是 O(n)。如果不用哈希表，先排序再用双指针的话，
时间 O(n log n)，空间 O(1)，但整体不如哈希方案快。"
```

三个加分细节：

1. **主动说"主要来自哪里"**。比如"O(n log n)，主要来自排序"，显得你真的懂，不是背的
2. **给出 trade-off**。"时间换空间"是算法题永恒的主题，主动说出来
3. **最坏情况 vs 平均情况**。哈希表平均 O(1)，最坏可能 O(n)，知道什么时候该提"平均"

### 2.9 本章小结

```
复杂度 = 算法效率的刻度，回答"n 变 10 倍，时间变几倍"

三规则：忽略常数、忽略低阶项、只看增长最快项
五档速记：O(1) < O(log n) < O(n) < O(n log n) < O(n²) << O(2ⁿ)

循环复杂度：走 n 次→O(n)，减半→O(log n)，嵌套→相乘
递归复杂度：数递归树的节点数（斐波那契=指数，归并=nlogn）

数据规模定算法：
  n≤10⁶ O(n) | n≤10⁵ O(nlogn) | n≤5000 O(n²) | n≤20 O(2ⁿ)

面试口述："时间 O(?)，主要来自 ?；空间 O(?)，用了 ?"
```

---

## 三、Python 刷题利器

刷题和写业务代码不太一样。业务代码追求可维护、可扩展、有类型、有注释；刷题追求的是**短、快、稳**。Python 自带的标准库里有几个模块，几乎每道题都用得上，它们就是你的"刷题兵器库"。

> 所有代码基于 Python 3.10+，只使用标准库，无需 pip install 任何东西。力扣的核心代码模式里这些库已经导入好了，但建议你自己也会手写 import。

### 3.1 collections.deque：双端队列

**为什么需要它**：列表 list 的 `pop(0)` 和 `insert(0, x)` 是 O(n) 的，因为后面的元素全要挪位。当 n 是 10⁵ 时，每次挪位就是灾难。deque 在两端都是 O(1)，是滑动窗口和 BFS 的标配。

```python
from collections import deque

# 创建
d = deque()                # 空队列
d = deque([1, 2, 3])       # 带初始值

# 两端操作（都是 O(1)）
d.append(4)                # 右端加，队尾入队
d.appendleft(0)            # 左端加
d.pop()                    # 右端出
d.popleft()                # 左端出，队头出队

# 其他常用
d[0]                       # 看队头，不弹出
d[-1]                      # 看队尾
len(d)                     # 长度
list(d)                    # 转回列表
```

**两个高频场景**：

场景 1，BFS 的队列：

```python
from collections import deque

q = deque([start])
while q:
    node = q.popleft()     # 永远从左边出
    # 扩展 node 的邻居，从右边入队
    q.append(neighbor)
```

场景 2，滑动窗口维护窗口内元素（见第四章 4.2 和 239 题）：

```python
from collections import deque

def max_sliding_window(nums, k):
    """滑动窗口最大值，用单调队列，O(n)"""
    q = deque()            # 存下标，队头永远是当前窗口最大值
    res = []
    for i, x in enumerate(nums):
        # 新元素入队前，弹出所有比它小的（它们不可能是答案了）
        while q and nums[q[-1]] <= x:
            q.pop()
        q.append(i)
        # 弹出已经滑出窗口的下标
        if q[0] <= i - k:
            q.popleft()
        # 窗口满 k 个时开始记录
        if i >= k - 1:
            res.append(nums[q[0]])
    return res
```

### 3.2 collections.Counter：计数器

**为什么需要它**：数每个元素出现几次是最高频的操作之一。Counter 不仅帮你数，还内置了排序、求交集等操作。

```python
from collections import Counter

# 基本用法
c = Counter("abracadabra")
# c = Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
c["a"]          # 5，不存在的键返回 0，不会报错
c["z"]          # 0
c.most_common(2)  # [('a', 5), ('b', 2)]，按次数从高到低

# 遍历
for ch, cnt in c.items():
    pass

# 计数相加、相减
c1 = Counter("abc")
c2 = Counter("bcd")
c1 + c2         # Counter({'b': 2, 'c': 2, 'a': 1, 'd': 1})
c1 - c2         # 只保留正数部分 Counter({'a': 1})
c1 & c2         # 交集：Counter({'b': 1, 'c': 1})，取最小值
c1 | c2         # 并集：取最大值

# 从列表构造
Counter([1, 2, 2, 3])   # Counter({2: 2, 1: 1, 3: 1})

# 从字典构造 / 指定初值
Counter({"a": 3})
Counter(a=3, b=1)

# 补全缺失键（当 0 处理）
c = Counter()
for ch in "abc":
    c[ch] += 1
```

**面试高频用法**：判断两个字符串是否是字母异位词（49 题）：

```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)   # 一行搞定
```

### 3.3 collections.defaultdict：带默认值的字典

**为什么需要它**：普通的 dict 访问不存在的键会抛 KeyError，你得先判断再赋值：

```python
# 普通写法：要写三行
d = {}
if key not in d:
    d[key] = []
d[key].append(x)

# defaultdict 写法：一行
from collections import defaultdict
d = defaultdict(list)   # 访问不存在的键，自动创建空 list
d[key].append(x)        # 直接可用
```

**常用默认工厂**：

```python
from collections import defaultdict

defaultdict(list)       # 缺失键自动变 []，用于分组
defaultdict(int)        # 缺失键自动变 0，用于计数
defaultdict(set)        # 缺失键自动变 set()，用于去重集合
defaultdict(str)        # 缺失键自动变 ""
```

**分组模板**（49 题字母异位词分组的核心）：

```python
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))   # 排序后的字符串作为"签名"
        groups[key].append(s)
    return list(groups.values())
```

**一个必须知道的坑**：`defaultdict` 的默认值只在你**访问**不存在的键时生成。如果你写 `d[missing]` 只是为了判断在不在，它会**顺手创建一个空键**。判断键是否存在请用 `in` 或 `get`：

```python
d = defaultdict(list)
if "k" in d:          # 正确，不会创建键
    pass
# d["k"]              # 不要这样判断，它会创建空列表键
```

### 3.4 collections.OrderedDict：有序字典

Python 3.7 之后普通 dict 本身就保证插入顺序，所以 OrderedDict 在日常刷题里用得少了。它唯一不可替代的场景是 **LRU 缓存**（146 题），因为 `move_to_end` 和 `popitem(last=False)` 能 O(1) 调整顺序：

```python
from collections import OrderedDict

def lru_cache_sim(capacity):
    cache = OrderedDict()

    def get(key):
        if key not in cache:
            return -1
        cache.move_to_end(key)      # 刚访问的移到末尾（表示最近使用）
        return cache[key]

    def put(key, value):
        if key in cache:
            cache.move_to_end(key)
        cache[key] = value
        if len(cache) > capacity:
            cache.popitem(last=False)  # 弹出最久没用的（最前面）
    return get, put
```

### 3.5 heapq：堆

**为什么需要它**：取 top-k、取中位数、合并有序序列，这些"时刻要最值"的问题，排序做一次 O(n log n)，而堆每次只 O(log n)。Python 的 heapq 是**最小堆**，`heap[0]` 永远是最小值。

```python
import heapq

# 创建：把列表变成堆（原地）
heap = [3, 1, 4, 1, 5]
heapq.heapify(heap)
# heap = [1, 1, 4, 3, 5]  满足堆性质，heap[0] 是最小值

# 入堆 / 出堆
heapq.heappush(heap, 2)      # O(log n)
smallest = heapq.heappop(heap)  # O(log n)，弹出并返回最小值

# 看堆顶但不弹出
heap[0]

# 合并多个有序列表（面试喜欢考底层原理）
merged = list(heapq.merge([1, 3, 5], [2, 4, 6]))
# [1, 2, 3, 4, 5, 6]

# 直接取 top-k
heapq.nlargest(3, [1, 5, 2, 8, 3])   # [8, 5, 3]
heapq.nsmallest(3, [1, 5, 2, 8, 3])  # [1, 2, 3]
```

**怎么做最大堆**：Python 只有最小堆。想要最大堆，存相反数：

```python
import heapq

# 找前 k 大：维护一个大小为 k 的最小堆，堆顶就是第 k 大
def find_kth_largest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)                 # 现在是最小堆，堆顶是最小值
    for x in nums[k:]:
        if x > heap[0]:                 # 比堆顶大就替换
            heapq.heapreplace(heap, x)  # 弹出堆顶并入堆 x
    return heap[0]                      # 堆顶就是第 k 大
```

**堆里存元组**：堆会按元组的第一个元素比较，常用于"按值排序但需要保留其他信息"：

```python
# 合并 k 个有序链表：堆里存 (节点值, 链表序号, 节点)
heap = [(list_head.val, i, list_head) for i, list_head in enumerate(lists)]
heapq.heapify(heap)
```

注意：Python 比较元组时，第一个元素相等会继续比第二个，所以如果只有 (值, 节点) 且值相等会去比较 ListNode，而 ListNode 不能比较，会报错。**第三位加个自增 id 或直接用下标打破平局**，这是面试常见的坑。

### 3.6 bisect：二分查找

**为什么需要它**：手写二分容易写错边界。bisect 帮你写好，而且语义清楚。前提：**列表必须有序**。

```python
import bisect

nums = [1, 3, 5, 5, 7, 9]

bisect.bisect_left(nums, 5)    # 2，第一个 >= 5 的位置（找左边界）
bisect.bisect_right(nums, 5)   # 4，第一个 > 5 的位置（找右边界）
bisect.bisect(nums, 5)         # 4，等价于 bisect_right

bisect.insort(nums, 6)         # 插入并保持有序，nums 变成 [1,3,5,5,6,7,9]
```

**面试高频套路**：用 bisect 求"元素 x 在有序数组里出现的次数"：

```python
import bisect

def count_occurrences(nums, x):
    left = bisect.bisect_left(nums, x)    # 第一个 x 的位置
    right = bisect.bisect_right(nums, x)  # 最后一个 x 后面的位置
    return right - left                   # 出现次数
```

**bisect_left 的语义要记牢**："第一个 ≥ target 的位置"。它配合"前缀和 + 二分"能解很多区间题。比如"找和不超过 target 的最长连续子数组"，先算前缀和数组（递增），再对每个位置二分。

### 3.7 排序：sorted / sort / key

```python
# 基本
sorted([3, 1, 2])             # [1, 2, 3]，返回新列表
nums.sort()                   # 原地排序，更省内存
sorted([3, 1, 2], reverse=True)  # [3, 2, 1]

# 按 key 排序（不改变元素本身）
students = [("Alice", 22), ("Bob", 19), ("Cathy", 21)]
sorted(students, key=lambda s: s[1])          # 按年龄
sorted(students, key=lambda s: -s[1])         # 按年龄降序
sorted(students, key=lambda s: (s[1], s[0]))  # 先年龄再名字

# 字符串按长度
sorted(["abc", "a", "ab"], key=len)           # ['a', 'ab', 'abc']

# 按自定义规则：比如按绝对值
sorted([-3, 1, -2], key=abs)                  # [1, -2, -3]
```

**面试注意**：
- 需要同时知道"排序前的位置"吗？用 `sorted(enumerate(nums), key=lambda x: x[1])`
- 稳定排序：值相等保持原相对顺序，`sort` 是稳定的。这在某些题里是突破口
- 对字典排序：`sorted(d.items(), key=lambda kv: kv[1])` 按值排

### 3.8 其他高频内置技巧

**遍历技巧**：

```python
# enumerate：同时要下标和值
for i, x in enumerate(nums):
    pass

# zip：同时遍历两个列表
for a, b in zip(nums1, nums2):
    pass
# zip 到最短处停。想补齐用 itertools.zip_longest

# reversed / [::-1]
reversed(nums)         # 反向迭代器
nums[::-1]             # 反转后的新列表
```

**判断技巧**：

```python
any([True, False])     # True，只要有一个真
all([True, True])      # True，全部为真
# 常用于：any(nums[i] == x for i in ...) 生成器版，不会先建列表

# 判断质数套路
def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:   # 只检查到根号 x
        if x % i == 0:
            return False
        i += 1
    return True
```

**数学常量**：

```python
import math
math.inf                # 正无穷，初始化"最小值"时用：ans = math.inf
float("inf")            # 同上
math.floor / math.ceil  # 向下/向上取整
math.gcd(a, b)          # 最大公约数
```

**字符串技巧**：

```python
s.lower() / s.upper()          # 大小写
s.isalnum() / s.isalpha() / s.isdigit()  # 判断字符类型
" ".join(list_of_words)        # 列表拼回字符串
s.split()                      # 按空白切
s.split(",")                   # 按逗号切
ord("a")                       # 97，字符转 ASCII
chr(97)                        # 'a'，ASCII 转字符
s[::-1]                        # 反转字符串（面试最爱考）
```

**字典技巧**：

```python
d.get(key, default)        # 安全取值，不存在的键返回 default
d.setdefault(key, default) # 键不存在才写入 default，返回当前值
d.pop(key, default)        # 弹出键，不存在返回 default 不报错
d.items() / d.keys() / d.values()
```

**三维操作小心**：`[[0] * n] * m` 是错的！外层的 `* m` 复制的是**同一个列表的引用**，改一个全变。正确写法：

```python
# 错误示范
grid = [[0] * n] * m     # 三行是同一个列表！

# 正确写法
grid = [[0] * n for _ in range(m)]   # 每行独立
```

这个坑出现频率极高，面试写二维 DP 时务必用列表推导式。

### 3.9 两种输入输出模式

力扣默认是**核心代码模式**：你只需要实现函数，输入输出测试框架帮你处理。但很多公司笔试是 **ACM 模式**：所有输入从标准输入读，自己解析，自己打印。必须两个都会。

**核心代码模式**（力扣默认）：

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 只管实现，不用管输入输出
        seen = {}
        for i, x in enumerate(nums):
            if target - x in seen:
                return [seen[target - x], i]
            seen[x] = i
```

**ACM 模式**（笔试常见）：

```python
import sys

def main():
    # 读入所有数据
    data = sys.stdin.read().split()   # 一次性读全部，按空白切
    # 或者一行行读：
    # line = sys.stdin.readline().strip()

    # 第一行通常是一个数 n
    n = int(data[0])
    # 第二行是 n 个数的数组
    nums = list(map(int, data[1:1 + n]))

    # 解题逻辑
    ans = sum(nums)

    # 输出
    print(ans)

if __name__ == "__main__":
    main()
```

**ACM 模式标准读入模板**：

```python
import sys

def solve():
    input = sys.stdin.readline
    # 单行读入
    n = int(input())                         # 读一个整数
    nums = list(map(int, input().split()))   # 读一行整数数组
    # 多行读入（直到 EOF）
    for line in sys.stdin:
        line = line.strip()
        if not line:
            break
        a, b = map(int, line.split())
        print(a + b)

if __name__ == "__main__":
    solve()
```

**调试建议**：ACM 模式本地调试时，把输入直接贴进一个 `input.txt`，然后运行 `python xxx.py < input.txt`，比手动敲快得多。

### 3.10 本章小结

```
deque：       两端 O(1)，滑动窗口 + BFS 标配
Counter：     数次数 + most_common，变位词一行判断
defaultdict： 分组计数不用先判空，注意 in 判断别误建键
OrderedDict： LRU 专用（move_to_end + popitem）
heapq：       最小堆，top-k 用"大小为 k 的堆"；最大堆存负数；
              存元组加下标打破平局
bisect：      bisect_left 找左边界，bisect_right 找右边界
排序：        sorted 返回新列表，sort 原地，key=lambda 按规则
大坑：        [[0]*n]*m 是引用拷贝，二维数组用列表推导式
模式：        力扣核心代码模式只写函数；笔试 ACM 模式自己读输入
```

---

## 四、高频模式模板

这是本指南的核心章节。14 类模式覆盖了 Hot 100 里 90% 的题目，每个模式都配有**完整可运行的 Python 代码**，全部基于标准库，Python 3.10+ 直接能跑。

**怎么用这一章**：
1. 第一遍通读，理解每个模式"解决什么问题、识别特征是什么"
2. 第二遍把每个模板代码**手敲一遍**（别复制粘贴，手敲才能记住）
3. 第三遍合上文件，默写模板，写不出来的标红
4. 之后做第五章的题时，随时回来对照

每个模板的结构：识别特征 → 模板代码 → 复杂度 → 典型题目 → 易错点。

### 4.1 双指针（Two Pointers）

**识别特征**：有序数组、配对求和、反转、去重、链表找环。关键词：有序、两数、反转。

双指针分两种：

- **相向双指针**：一个从左往右，一个从右往左，向中间靠拢。用于有序数组求和、反转
- **同向双指针（快慢指针）**：一个快一个慢。用于链表找环、去重、找中点

**模板一：相向双指针（有序数组两数之和）**

```python
def two_sum_sorted(nums, target):
    """nums 已有序，找两个数使和为 target，返回下标"""
    left, right = 0, len(nums) - 1
    while left < right:
        cur = nums[left] + nums[right]
        if cur == target:
            return [left, right]
        elif cur < target:
            left += 1          # 和太小，左指针右移让和变大
        else:
            right -= 1         # 和太大，右指针左移让和变小
    return []                  # 无解
```

核心逻辑就一句：**有序数组里，左指针右移和变大，右指针左移和变小**。每次移动都排除了一个元素，所以是 O(n)。

**模板二：快慢指针（环形链表）**

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:      # 快指针走两步，要检查 next 是否为空
        slow = slow.next           # 慢指针走一步
        fast = fast.next.next      # 快指针走两步
        if slow is fast:
            return True            # 相遇说明有环
    return False                   # 快指针走到头说明无环
```

**典型题目**：11 盛最多水的容器、15 三数之和、88 合并两个有序数组、141 环形链表、283 移动零。

**易错点**：
- 相向双指针的前提是有序（或用排序先创造有序）
- 快慢指针判断条件 `fast and fast.next` 的顺序不能反，`fast.next` 可能为空
- 双指针的总移动次数 ≤ n，复杂度是 O(n) 不是 O(n²)

### 4.2 滑动窗口（Sliding Window）

**识别特征**：连续子数组 / 子串，求最大、最小、满足某条件。关键词：最长、最短、连续、子串。

滑动窗口是"数组上的双指针"，维护一个 `[left, right]` 的窗口，通过扩张和收缩窗口来遍历所有可能的连续区间，把 O(n²) 暴力降到 O(n)。

**模板一：可变窗口（最长无重复子串）**

```python
def length_of_longest_substring(s):
    """返回不含重复字符的最长子串长度"""
    from collections import defaultdict
    window = defaultdict(int)      # 窗口内每个字符的出现次数
    left = 0
    ans = 0
    for right, ch in enumerate(s):
        window[ch] += 1            # 右指针扩张，ch 进窗口
        while window[ch] > 1:      # 出现重复：收缩左边界直到不重复
            window[s[left]] -= 1
            left += 1
        ans = max(ans, right - left + 1)   # 更新答案
    return ans
```

**模板二：固定窗口（窗口内最大值）**

```python
from collections import deque

def max_sliding_window(nums, k):
    """每个长度为 k 的窗口内的最大值"""
    q = deque()                    # 单调递减队列，存下标
    res = []
    for i, x in enumerate(nums):
        while q and nums[q[-1]] <= x:   # 队尾比 x 小就弹出（不可能是答案）
            q.pop()
        q.append(i)
        if q[0] <= i - k:          # 队头滑出窗口
            q.popleft()
        if i >= k - 1:             # 窗口满 k 个才记录
            res.append(nums[q[0]])
    return res
```

**通用滑动窗口框架**（面试时按这个框架说，显得有条理）：

```python
def sliding_window_template(nums, k):
    left = 0
    for right in range(len(nums)):      # 1. 右指针扩张
        # 2. 把 nums[right] 加入窗口，更新窗口状态
        while 窗口不满足条件:            # 3. 收缩左指针直到满足
            # 把 nums[left] 移出窗口
            left += 1
        # 4. 此时窗口满足条件，记录答案
    return 答案
```

**典型题目**：3 无重复字符的最长子串、76 最小覆盖子串、239 滑动窗口最大值、438 找到字符串中所有字母异位词。

**易错点**：
- 先想清楚"窗口合法条件"是什么，收缩逻辑围绕它写
- 更新答案的位置有两种：收缩前（求最短）或收缩后（求最长），别搞混
- 窗口用 `defaultdict(int)` 计次数，别用 set，因为字符可能重复进出

### 4.3 哈希表（Hash Table）

**识别特征**：找配对、找重复、计数、去重、O(1) 查询。关键词：配对、出现次数、是否出现过。

哈希表是"空间换时间"的典范：用 O(n) 的空间，把查找从 O(n) 降到 O(1)。几乎任何"找另一个数"的问题，第一反应都应该是哈希表。

**模板：两数之和（最经典）**

```python
def two_sum(nums, target):
    """返回两个下标，使 nums[i] + nums[j] == target"""
    seen = {}                    # 值 -> 下标
    for i, x in enumerate(nums):
        if target - x in seen:   # 补数在不在之前的记录里
            return [seen[target - x], i]
        seen[x] = i              # 先查再存，避免同一个元素配对
    return []
```

**计数 + 判重模板**：

```python
# 计数
from collections import Counter
freq = Counter(nums)

# 判重
def contains_duplicate(nums):
    return len(set(nums)) != len(nums)

# 找出现次数超过一半的元素（多数元素）
def majority_element(nums):
    counts = Counter(nums)
    return max(counts, key=counts.get)   # 键是元素，值最大者
```

**典型题目**：1 两数之和、49 字母异位词分组、128 最长连续序列、136 只出现一次的数字、169 多数元素、287 寻找重复数、347 前 K 个高频元素、448 消失的数字。

**易错点**：
- 两数之和"先查再存"的顺序不能反，否则同一个元素可能和自己配对
- 哈希表的 key 必须是可哈希的（list 不行，要转 tuple）
- 面试被问复杂度时主动说"平均 O(1)，最坏 O(n)（哈希冲突）"

### 4.4 前缀和（Prefix Sum）

**识别特征**：连续子数组求和、子数组和为 k、区域和查询。关键词：和为 k、子数组、连续区间求和。

前缀和思想：`prefix[i]` 表示前 i 个元素的和，那么 `nums[i..j]` 的和 = `prefix[j+1] - prefix[i]`，O(1) 求任意区间和。

**模板：和为 k 的子数组个数（560 题）**

```python
def subarray_sum(nums, k):
    """连续子数组和为 k 的个数"""
    from collections import defaultdict
    prefix = defaultdict(int)
    prefix[0] = 1              # 前缀和为 0 出现过一次（空子数组）
    s = 0
    ans = 0
    for x in nums:
        s += x                 # 当前前缀和
        ans += prefix[s - k]   # 有 prefix[s-k] 个"起点"能让区间和为 k
        prefix[s] += 1         # 记录当前前缀和出现次数
    return ans
```

核心逻辑：**边算前缀和边查 `s - k` 出现过多少次**。`defaultdict(int)` 让缺失的键自动返回 0，所以 `prefix[s - k]` 不用判断存在性。

**模板：区域和查询**

```python
def range_sum(nums, queries):
    """queries = [(l, r)]，快速求每个 nums[l..r] 的和"""
    n = len(nums)
    prefix = [0] * (n + 1)     # prefix[i] = nums[0..i-1] 的和
    for i, x in enumerate(nums):
        prefix[i + 1] = prefix[i] + x
    return [prefix[r + 1] - prefix[l] for l, r in queries]
```

**典型题目**：53 最大子数组和（动态规划变体）、238 除自身以外数组的乘积（前后缀乘积）、560 和为 K 的子数组。

**易错点**：
- 一定先塞 `prefix[0] = 1`，否则"从头开始的子数组"会漏算
- 前缀和数组长度 n+1，`prefix[i]` 对应前 i 个，别和下标搞混
- 需要乘积时用前后缀两个数组各扫一遍，注意处理 0

### 4.5 栈与单调栈（Stack & Monotonic Stack）

**识别特征**：括号匹配、逆波兰表达式、找"下一个更大/更小元素"。关键词：括号、下一个更大、下一个更小。

栈是"先进后出"的线性结构。**单调栈**是栈的进阶：栈内元素保持单调（递增或递减），用于高效求"每个元素右边第一个比它大/小的元素"，把 O(n²) 降到 O(n)。

**模板一：有效的括号（20 题）**

```python
def is_valid(s):
    """括号字符串是否合法"""
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in pairs:                # 遇到右括号
            if not stack or stack.pop() != pairs[ch]:
                return False           # 栈空或栈顶不匹配
        else:
            stack.append(ch)           # 左括号入栈
    return not stack                   # 栈空说明全部匹配
```

**模板二：单调栈（每日温度 739 题）**

```python
def daily_temperatures(temperatures):
    """每个温度后几天能遇到更高的温度"""
    n = len(temperatures)
    ans = [0] * n
    stack = []                     # 单调递减栈，存下标
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            prev = stack.pop()     # 找到"下一个更大"了，结算
            ans[prev] = i - prev
        stack.append(i)
    return ans
```

单调栈的思维模式：**新元素比栈顶大时，栈顶元素的下一个更大元素就是当前元素**，弹出结算。剩下的栈内元素是"还没找到下一个更大"的，保持递减。

**模板三：单调栈（接雨水 42 题，按行结算）**

```python
def trap(height):
    """计算能接的雨水总量"""
    stack = []
    water = 0
    for i, h in enumerate(height):
        while stack and h > height[stack[-1]]:
            top = stack.pop()        # 弹出"谷底"（中间矮柱）
            if not stack:
                break                # 左边没有更高的柱子，接不住水
            left = stack[-1]
            width = i - left - 1
            bounded = min(height[left], h) - height[top]
            water += width * bounded
        stack.append(i)
    return water
```

**典型题目**：20 有效的括号、42 接雨水、155 最小栈、394 字符串解码、739 每日温度。

**易错点**：
- 栈里存下标而不是值（值一样也能定位，还能算宽度）
- 单调栈出栈的时机：新元素"严格大于/小于"栈顶时（边界条件想清楚）
- 括号题最后一定要 `return not stack`，别只检查中间的 false

### 4.6 二分查找（Binary Search）

**识别特征**：有序数组、找目标、找边界、找第 k 个。关键词：有序、log n、"旋转数组"。

二分查找的前提是**单调性**：数组有序，或者存在一个"可以二分判断"的性质。核心是"每次排除一半"，O(log n)。

**模板一：经典二分（找 target）**

```python
def binary_search(nums, target):
    """在有序数组中找 target，返回下标，找不到返回 -1"""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

**模板二：找左右边界（34 题）**

```python
def search_range(nums, target):
    """找 target 的第一个和最后一个位置"""
    def bisect_left_bound():
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1        # mid 太小，排除左边
            else:                     # mid >= target，右边界收缩
                right = mid - 1
        return left                   # left 是第一个 >= target 的位置

    def bisect_right_bound():
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1        # mid 太小时排除
            else:
                right = mid - 1
        return left                   # left 是第一个 > target 的位置

    first = bisect_left_bound()
    if first >= len(nums) or nums[first] != target:
        return [-1, -1]
    return [first, bisect_right_bound() - 1]
```

**模板三：旋转有序数组（33 题）**

```python
def search_rotated(nums, target):
    """在旋转过的有序数组中找 target"""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:          # 左半段有序
            if nums[left] <= target < nums[mid]:
                right = mid - 1              # target 在有序的左半段
            else:
                left = mid + 1
        else:                                 # 右半段有序
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
```

**典型题目**：33 搜索旋转排序数组、34 在排序数组中查找元素的第一个和最后一个位置、240 搜索二维矩阵 II（对角线二分思路）、287 寻找重复数（二分答案）。

**易错点**：
- `while left <= right` 和 `while left < right` 两种写法，边界处理完全不同，**认准一种写到熟**
- 求 mid 用 `(left + right) // 2`，防溢出的写法是 `left + (right - left) // 2`
- "二分答案"题型：对答案本身二分，用 check 函数判断可行性，这是进阶玩法，面试加分

### 4.7 链表（Linked List）

**识别特征**：反转、合并、环、删除节点、倒数第 n 个。关键词：链表、next、指针。

链表题的灵魂是**画图**。指针断链前先保存引用，否则会丢。链表题的通用套路是**哑节点（dummy）**：在头节点前加一个假节点，省去对"头节点特殊处理"的讨论。

**模板一：反转链表（206 题）**

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    """迭代反转整条链表"""
    prev = None
    cur = head
    while cur:
        nxt = cur.next     # 1. 先保存下一个（马上要断链）
        cur.next = prev    # 2. 当前节点指向前一个
        prev = cur         # 3. prev 前移
        cur = nxt          # 4. cur 前移
    return prev            # 新头是原链表的尾
```

**模板二：合并两个有序链表（21 题）**

```python
def merge_two_lists(l1, l2):
    """合并两个升序链表"""
    dummy = ListNode()     # 哑节点，避免处理头节点
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2   # 剩下的直接接上
    return dummy.next
```

**模板三：快慢指针找环入口（142 题）**

```python
def detect_cycle(head):
    """返回环的入口节点，无环返回 None"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:              # 相遇：有环
            ptr = head
            while ptr is not slow:    # 数学结论：头节点和相遇点同时走，相遇处就是入口
                ptr = ptr.next
                slow = slow.next
            return ptr
    return None
```

**典型题目**：2 两数相加、19 删除链表的倒数第 N 个结点、21 合并两个有序链表、141 环形链表、142 环形链表 II、146 LRU 缓存、160 相交链表、206 反转链表、234 回文链表。

**易错点**：
- 断链前必先保存 `nxt = cur.next`
- 改链表结构尽量用 dummy 节点，省得单独处理 head
- 循环条件里先判 `cur` 再判 `cur.next`，避免 None 报错

### 4.8 二叉树遍历（Tree Traversal）

**识别特征**：二叉树、前序/中序/后序/层序、深度、对称、翻转。关键词：树、root、遍历。

二叉树是递归的天然载体。遍历分两种流派：递归（好写好懂，但有栈溢出风险）和迭代（复杂但可控）。面试要求**两种都会写**，前序、中序、后序、层序四种都要能默写。

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

**前序遍历（根左右）递归版**：

```python
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)
```

**中序遍历（左根右）迭代版（重点背这个）**：

```python
def inorder_iter(root):
    res, stack = [], []
    cur = root
    while stack or cur:
        while cur:                 # 一路向左压栈
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()          # 弹出最左节点
        res.append(cur.val)        # 访问它
        cur = cur.right            # 转向右子树
    return res
```

中序迭代是面试最爱考的，因为它的非递归写法最需要理解"栈模拟递归"。

**后序遍历（左右根）**：递归版就是 `[root.val]` 放到最后。迭代版常用"前序的变形"：先按"根右左"收集再反转。

**层序遍历（BFS，102 题）**：

```python
from collections import deque

def level_order(root):
    """按层输出，每层一个列表"""
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):    # 关键：先固定本层节点数
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res
```

**深度模板（104 题）**：

```python
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

**典型题目**：98 验证二叉搜索树、101 对称二叉树、102 二叉树的层序遍历、104 二叉树的最大深度、105 从前序与中序遍历构造二叉树、124 二叉树中的最大路径和、226 翻转二叉树、236 最近公共祖先、543 二叉树的直径。

**易错点**：
- 递归终止条件 `if not root` 一定写在第一行
- 层序遍历里 `for _ in range(len(q))` 必须先取长度，因为 q 在循环中会变
- 验证 BST 不能只比当前节点，要带上下界（`min_val, max_val` 参数）

### 4.9 DFS 回溯（Backtracking）

**识别特征**：组合、排列、子集、分割、棋盘、解空间树。关键词：全排列、子集、组合、方案数。

回溯 = DFS + 撤销，核心是"尝试、回退、再尝试"。模板固定，套就完了。它解决的是"枚举所有方案"的问题，复杂度通常是指数级，但 n 小（≤ 20）就没事。

**模板：子集（78 题）**

```python
def subsets(nums):
    """返回所有子集"""
    res = []
    path = []                       # 当前路径（一个候选方案）

    def backtrack(start):
        res.append(path[:])         # 记录当前方案（必须切片拷贝）
        for i in range(start, len(nums)):
            path.append(nums[i])    # 选
            backtrack(i + 1)        # 递归，下一层从 i+1 开始（不回头）
            path.pop()              # 撤销，回到上一步

    backtrack(0)
    return res
```

**模板：全排列（46 题）**

```python
def permute(nums):
    """返回所有排列"""
    res = []
    path = []
    used = [False] * len(nums)

    def backtrack():
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return res
```

**回溯三件套（背下来）**：

```python
def backtrack(参数):
    if 达到终止条件:
        记录结果
        return
    for 候选 in 可选集合:
        剪枝（可选）        # 提前排除不可能的，如去重
        做选择             # 加入 path / 标记 used
        backtrack(下一层)
        撤销选择           # path.pop() / used[i] = False
```

**去重套路（含重复元素时）**：先排序，然后跳过重复分支。注意：组合/子集和排列的去重判据**不一样**，别混用。

组合 / 子集（用 `start` 参数，对应 40 组合总和 II、90 子集 II）——跳过"本层内"与前一个相同的元素：

```python
nums.sort()
for i in range(start, len(nums)):
    if i > start and nums[i] == nums[i - 1]:
        continue      # 跳过重复分支，防止生成重复方案
    ...
```

排列（用 `used` 数组，对应 47 全排列 II）——跳过"与前一个相同且前一个还没用过"的元素：

```python
nums.sort()
for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
        continue      # 相同的值，且前一个同值元素还没用，说明这一层会重复
    if used[i]:
        continue
    used[i] = True
    path.append(nums[i])
    dfs(path)
    path.pop()
    used[i] = False
```

**典型题目**：22 括号生成、39 组合总和、46 全排列、78 子集、79 单词搜索。

**易错点**：
- 记录结果时一定 `res.append(path[:])`，直接 `append(path)` 存的是同一个对象的引用，最后全变成空
- 子集和组合用 `start` 参数控制不回头；排列用 `used` 数组
- 撤销操作必须和选择对称，漏一个就错

### 4.10 BFS（广度优先搜索）

**识别特征**：最短步数、层数、岛屿、图的连通分量、迷宫最短路径。关键词：最短、层、队列。

BFS 一层一层往外扩，天然适合"最短路径"问题，因为第一层找到的一定是最近的。用队列实现。

**模板：网格 BFS（岛屿数量 200 题）**

```python
from collections import deque

def num_islands(grid):
    """二维网格中'1'（陆地）组成的岛屿个数"""
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and not visited[r][c]:
                count += 1
                q = deque([(r, c)])
                visited[r][c] = True
                while q:
                    x, y = q.popleft()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if (0 <= nx < rows and 0 <= ny < cols
                                and grid[nx][ny] == "1"
                                and not visited[nx][ny]):
                            visited[nx][ny] = True
                            q.append((nx, ny))
    return count
```

**模板：最短步数（图 / 迷宫）**

```python
def shortest_path(graph, start, target):
    """无权图的最短路径长度"""
    q = deque([start])
    visited = {start}
    steps = 0
    while q:
        for _ in range(len(q)):      # 一层一层地走
            node = q.popleft()
            if node == target:
                return steps
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        steps += 1
    return -1
```

**DFS 也能做连通分量题**，两种写法对比：

```python
def num_islands_dfs(grid):
    def dfs(r, c):
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != "1":
            return
        grid[r][c] = "0"             # 沉没：把访问过的陆地标记成水
        dfs(r + 1, c); dfs(r - 1, c)
        dfs(r, c + 1); dfs(r, c - 1)

    rows, cols = len(grid), len(grid[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)
    return count
```

**典型题目**：102 二叉树的层序遍历、200 岛屿数量、207 课程表（拓扑排序）。

**易错点**：
- 入队时立刻标记 visited，别等出队再标记（否则会重复入队）
- 网格题的方向数组 `(1,0),(-1,0),(0,1),(0,-1)` 写熟
- 需要"最短步数"时用按层 BFS，需要"所有方案"时用 DFS/回溯

### 4.11 动态规划（Dynamic Programming）

**识别特征**：最优值、方案数、记忆化搜索、状态转移。关键词：最大、最小、多少种、爬楼梯、打家劫舍、背包。

DP 的套路固定：**定义状态 → 写转移方程 → 定初始条件 → 定答案**。难点在第一步"定义状态"，这需要练习。

**模板一：一维 DP（爬楼梯 70 题）**

```python
def climb_stairs(n):
    """每次爬 1 或 2 阶，到第 n 阶有几种方法"""
    if n <= 2:
        return n
    a, b = 1, 2                  # a = dp[1], b = dp[2]
    for _ in range(3, n + 1):
        a, b = b, a + b          # dp[i] = dp[i-1] + dp[i-2]
    return b
```

**模板二：一维 DP 完整版（打家劫舍 198 题）**

```python
def rob(nums):
    """相邻房子不能同时偷，求最大金额"""
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        # 偷第 i 家：dp[i-2] + nums[i]；不偷：dp[i-1]
    return dp[-1]
```

**模板三：0/1 背包（416 分割等和子集）**

```python
def can_partition(nums):
    """能否把数组分成两个和相等的子集"""
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True                      # 和为 0 一定可以（空集）
    for x in nums:
        for s in range(target, x - 1, -1):   # 逆序！0/1 背包的精髓
            if dp[s - x]:
                dp[s] = True
    return dp[target]
```

**0/1 背包 vs 完全背包**：外层循环遍历物品，内层容量遍历方向不同。

```
0/1 背包（每个物品用一次）：内层容量逆序  for s in range(target, x-1, -1)
完全背包（每个物品无限用）：内层容量正序  for s in range(x, target+1)
```

**模板四：二维 DP（不同路径 62 题）**

```python
def unique_paths(m, n):
    """从左上角到右下角，只能向右向下，共多少条路径"""
    dp = [[1] * n for _ in range(m)]   # 第一行第一列都是 1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]
```

**典型题目**：5 最长回文子串、62 不同路径、70 爬楼梯、72 编辑距离、121/122 买卖股票、139 单词拆分、152 乘积最大子数组、198 打家劫舍、221 最大正方形、300 最长递增子序列、322 零钱兑换、416 分割等和子集、494 目标和。

**易错点**：
- 先想清楚 `dp[i]` 代表什么，写转移方程前先写注释
- 初始条件（边界）最容易漏：dp[0]、第一行第一列
- 0/1 背包容量逆序、完全背包正序，这是背诵点
- 一维滚动数组优化（爬楼梯、打家劫舍）能省空间，面试主动提加分

### 4.12 堆（Heap）

**识别特征**：前 k 大/小、top-k、中位数、合并有序序列。关键词：第 k 大、前 k 个、topK。

堆解决"动态求最值"和"top-k"问题，每次操作 O(log n)，比"每次排序"的 O(n log n) 快一个量级。

**模板：数组第 K 大（215 题）**

```python
import heapq

def find_kth_largest(nums, k):
    """第 k 大的元素"""
    heap = nums[:k]
    heapq.heapify(heap)              # 大小为 k 的最小堆
    for x in nums[k:]:
        if x > heap[0]:
            heapq.heapreplace(heap, x)   # 淘汰堆顶（当前第 k 大）
    return heap[0]
```

**模板：前 K 个高频元素（347 题）**

```python
from collections import Counter
import heapq

def top_k_frequent(nums, k):
    """出现频率最高的 k 个元素"""
    freq = Counter(nums)             # 先计数
    # 用大小为 k 的最小堆，堆里存 (次数, 元素)
    heap = []
    for num, cnt in freq.items():
        if len(heap) < k:
            heapq.heappush(heap, (cnt, num))
        elif cnt > heap[0][0]:
            heapq.heapreplace(heap, (cnt, num))
    return [num for _, num in heap]
```

**模板：合并 K 个有序链表（23 题思路）**

```python
def merge_k_lists(lists):
    """把 k 个升序链表合并成一条升序链表"""
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
            # 注意 i 用来打破平局：元组比较到第 3 位才到 node，
            # 避免直接比较 ListNode 报错
    dummy = ListNode()
    tail = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next
```

**典型题目**：215 数组中的第 K 个最大元素、295 数据流的中位数（两个堆）、347 前 K 个高频元素。

**易错点**：
- Python heapq 是**最小堆**，做最大堆存负数
- 堆存元组时，如果可能比较到第 3 位的对象，务必加下标打破平局
- 求"第 k 大"用大小为 k 的堆；求"前 k 个最大"同理，都是小堆顶当门槛

### 4.13 贪心（Greedy）

**识别特征**：每一步局部最优 = 全局最优，排序后处理，区间类问题。关键词：最多、最少、尽量、区间、跳跃。

贪心的难点是**证明**："为什么局部最优能推出全局最优"。面试时不会要求严格证明，但要说得出直觉。识别它靠积累：跳跃游戏、区间重叠、最少箭射气球这类题，记住"排序 + 贪心选择"的套路。

**模板一：跳跃游戏（55 题）**

```python
def can_jump(nums):
    """每一步能跳 0..nums[i] 格，能否到达最后"""
    farthest = 0
    for i, x in enumerate(nums):
        if i > farthest:          # 当前位置已经够不到了
            return False
        farthest = max(farthest, i + x)   # 不断刷新最远可达
    return True
```

**模板二：合并区间（56 题）**

```python
def merge(intervals):
    """合并所有重叠的区间"""
    intervals.sort(key=lambda x: x[0])   # 按起点排序
    res = []
    for start, end in intervals:
        if not res or start > res[-1][1]:
            res.append([start, end])     # 不重叠，开新区间
        else:
            res[-1][1] = max(res[-1][1], end)   # 重叠，合并（取最大终点）
    return res
```

**模板三：最多能完成多少任务（区间不重叠 / 活动选择）**

```python
def erase_overlap_intervals(intervals):
    """最少删掉几个区间能让剩下的互不重叠"""
    intervals.sort(key=lambda x: x[1])   # 按终点排序（贪心选择）
    keep = 0
    last_end = float("-inf")
    for start, end in intervals:
        if start >= last_end:            # 可以保留
            keep += 1
            last_end = end
    return len(intervals) - keep
```

**典型题目**：55 跳跃游戏、56 合并区间、122 买卖股票的最佳时机 II、763 划分字母区间。

**易错点**：
- 贪心题几乎都要**先排序**，排序的 key（起点/终点/差值）往往就是突破口
- "合并区间"和"最多保留区间"的排序 key 不同，前者按起点，后者按终点，别混
- 贪心不对时，马上切回 DP 或二分答案，别死磕

### 4.14 位运算（Bit Manipulation）

**识别特征**：出现一次/两次、幂运算、二进制计数、集合状态压缩。关键词：异或、位、出现一次、2 的幂。

位运算面试就考几个固定招式，全部背熟：

```python
# 异或的性质（重点）：
#   a ^ a = 0      自己异或自己 = 0
#   a ^ 0 = a      异或 0 不变
#   异或满足交换律和结合律：a^b^a = b（成对的出现会被抵消）

# 与、或、非、移位：
x & 1        # 判断奇偶：1 为奇数，0 为偶数
x & (x-1)    # 把最低位的 1 变成 0（清掉最后一个 1）
x | y        # 置位
x ^ y        # 翻转位
x << k       # 左移 k 位 = 乘以 2^k
x >> k       # 右移 k 位 = 整除 2^k
```

**模板一：只出现一次的数字（136 题）**

```python
def single_number(nums):
    """只有一个数字出现 1 次，其余都出现 2 次"""
    result = 0
    for x in nums:
        result ^= x          # 成对的全部抵消，剩下单身汉
    return result
```

**模板二：比特位计数（338 题）**

```python
def count_bits(n):
    """0..n 每个数的二进制中 1 的个数"""
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
        # i>>1 是去掉最低位后的数，它的 1 个数已经算过；
        # i&1 是最低位是不是 1
    return dp
```

**模板三：判断 2 的幂 / 3 的幂**

```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
    # 2 的幂的二进制只有一个 1，n & (n-1) 清掉唯一那个 1 后变成 0
```

**典型题目**：136 只出现一次的数字、338 比特位计数。

**易错点**：
- Python 的整数无限大，负数右移是算术右移（补 1），和 C/Java 不同，遇到负数移位要小心
- 异或只适用于"成对抵消"的场景，三个相同的不适用
- 面试问到位运算题，先背三条性质再做题

### 4.15 模式速查卡

把这张卡存手机里，做题卡壳时翻：

```
数组问题：
  有序 + 配对求和     → 双指针（4.1）
  连续子数组求最值     → 滑动窗口（4.2）
  连续子数组求和       → 前缀和（4.4）
  找配对/判重/计数     → 哈希表（4.3）
  有序 + 找目标        → 二分查找（4.6）
  前 k 大/小           → 堆（4.12）
  区间重叠             → 贪心（4.13）

链表问题：             → 哑节点 + 画图 + 快慢指针（4.7）
树的问题：             → 递归遍历 / 层序 BFS（4.8）
  最短步数 / 岛屿       → BFS（4.10）
  组合/排列/子集        → DFS 回溯（4.9）
  最大值/方案数         → 动态规划（4.11）
  下一个更大元素        → 单调栈（4.5）
  出现一次             → 位运算（4.14）
```

---

## 五、Hot 100 分类速查

> ⚠️ **本章规则**：共 **80 题**，按 10 类分组，每组配 📱 手机看思路 / 💻 电脑写码。每题一行主格式 + 两行提示，共 3-4 行。带 ⭐ 的是 10 道"模板地标题"，在第五章给出完整代码，其余只给思路。80 题是硬上限，刷完即止，贪多嚼不烂。

> 怎么用：📱 通勤时把本章当卡片翻，只看思路不看代码；💻 晚上按 ⭐ 顺序把 10 道地标题完整写出来，其余 70 题按 4.15 速查卡对号入座。每道题在 Obsidian 里记"模式 + 一句话思路 + 复杂度"（见 1.8）。

---

### 5.1 哈希表（8 题）

> 特征：配对、判重、计数。模板见 4.3。

- **1. 两数之和（简单）⭐**：哈希表存"值 → 下标"，边遍历边查 target - x → O(n)/O(n)
  - 📱 配对问题先想哈希；"先查再存"防止同一个元素和自己配对
  - 💻 完整代码见下方模板块；变体：三数之和、四数相加 II

```python
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []
```

- **49. 字母异位词分组（中等）**：排序后的字符串当 key，defaultdict(list) 分组 → O(nk log k)/O(nk)
  - 📱 "同构签名"思想：把相等的元素归一化成一个 key
  - 💻 也可用计数元组当 key，省排序
- **128. 最长连续序列（中等）**：set 去重，只从"序列起点"（num-1 不在集合里）向后数 → O(n)/O(n)
  - 📱 关键在"只从起点开始数"，保证每个元素只被扫一次
  - 💻 面试常问"为什么不是 O(n²)"，答案就是起点判断
- **136. 只出现一次的数字（简单）**：全员异或，成对的互相抵消 → O(n)/O(1)
  - 📱 异或三性质：a^a=0、a^0=a、交换结合律
  - 💻 位运算压轴题，背住模板即可（4.14）
- **169. 多数元素（简单）**：Counter 计数取最大，或摩尔投票法 O(1) 空间 → O(n)/O(1)
  - 📱 投票法：候选人票数相消，剩下的就是多数元素
  - 💻 进阶问"O(1) 空间怎么做"时，用投票法
- **287. 寻找重复数（中等）**：值域二分，统计 ≤ mid 的个数，多了就缩右边界 → O(n log n)/O(1)
  - 📱 不能改数组、O(1) 空间的条件下，"二分答案"是通用杀招
  - 💻 等价写法：把数组当链表，快慢指针找环入口
- **347. 前 K 个高频元素（中等）**：Counter 计数 + 大小为 k 的最小堆 → O(n log k)/O(n)
  - 📱 top-k 一律想堆：第 k 大用 k 大小的小堆，堆顶是门槛
  - 💻 模板在 4.12，注意堆里存 (次数, 元素)
- **448. 找到所有数组中消失的数字（简单）**：用下标做标记，出现过的把对应位置值取负 → O(n)/O(1)
  - 📱 "原地哈希"：数组本身当哈希表，值的信息编码进符号位
  - 💻 遍历两次：第一次标记，第二次收集正值下标

### 5.2 双指针（6 题）

> 特征：有序、配对、反转、移动。模板见 4.1。

- **11. 盛最多水的容器（中等）**：左右指针从两端向内，移动较矮的一侧，面积取最大 → O(n)/O(1)
  - 📱 为什么移矮的？因为高的移动只会让面积变小，矮的移动才有变大的可能
  - 💻 面积 = 短边 × 距离，双指针每次排除一条不可能最优的线
- **15. 三数之和（中等）⭐**：排序 + 固定一个数 + 双指针扫剩余区间，跳过重复 → O(n²)/O(n) 空间（排序）
  - 📱 三数拆成"固定 + 两数"，去重靠排序后跳过相同值
  - 💻 完整代码见下方模板块；注意去重的三个位置

```python
def three_sum(nums):
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:   # 去重：固定数不重复
            continue
        left, right = i + 1, n - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s < 0:
                left += 1
            elif s > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:    # 去重
                    left += 1
                while left < right and nums[right] == nums[right + 1]:  # 去重
                    right -= 1
    return res
```

- **42. 接雨水（困难）**：双指针维护左右最大高度，哪边矮结算哪边的水量 → O(n)/O(1)
  - 📱 每格水量 = min(左最大, 右最大) - 自身高度；矮边先结算因为它的约束已定
  - 💻 也可用单调栈（4.5 模板三），双指针是更优解
- **75. 颜色分类（中等）**：三指针（荷兰国旗），0 往左放、2 往右放 → O(n)/O(1)
  - 📱 一次遍历原地排三色：low 指向 0 区、high 指向 2 区，cur 扫中间
  - 💻 边界易错：交换 2 后 cur 不前进（因为换回来的数还要处理）
- **88. 合并两个有序数组（简单）**：从后往前填，谁大放末尾，避免覆盖 → O(m+n)/O(1)
  - 📱 "从后往前"是原地合并的钥匙，省去额外数组
  - 💻 三个指针：p1 指 nums1 有效位、p2 指 nums2、p 指写入位
- **283. 移动零（简单）**：快慢指针，非零前移，末尾统一补零 → O(n)/O(1)
  - 📱 slow 记录下一个非零的落点，fast 负责找非零
  - 💻 变体：把 0 换成"指定元素"，同法通用

### 5.3 滑动窗口（4 题）

> 特征：连续子数组/子串 + 最长最短。模板见 4.2。

- **3. 无重复字符的最长子串（中等）⭐**：窗口内计数字符，出现重复就收缩左边界 → O(n)/O(n)
  - 📱 可变窗口：右指针扩张，不满足"无重复"就收缩到满足为止
  - 💻 完整代码见下方模板块；用 defaultdict(int) 计数

```python
def length_of_longest_substring(s):
    from collections import defaultdict
    window = defaultdict(int)
    left = ans = 0
    for right, ch in enumerate(s):
        window[ch] += 1
        while window[ch] > 1:
            window[s[left]] -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans
```

- **76. 最小覆盖子串（困难）**：滑动窗口 + 字符计数，满足覆盖后尽量收缩，记录最短 → O(n)/O(n)
  - 📱 两个计数：目标串需要的次数 vs 窗口内已有的次数，`need == 0` 即覆盖
  - 💻 收缩条件用"缺失字符数"，别每步都全量比较
- **239. 滑动窗口最大值（困难）**：单调递减双端队列存下标，队头永远是窗口最大值 → O(n)/O(n)
  - 📱 队列里淘汰所有比新元素小的，因为它们永远轮不到当最大值
  - 💻 模板在 4.2，核心两句：while 弹队尾、if 弹队头
- **438. 找到字符串中所有字母异位词（中等）**：定长窗口，字符计数和 p 完全一致时记录起点 → O(n)/O(n)
  - 📱 定长窗口 + 计数比较；滑一步只改两个字符的计数
  - 💻 变体 567 题（字符串的排列）同思路

### 5.4 前缀和（3 题）

> 特征：连续子数组求和。模板见 4.4。

- **53. 最大子数组和（中等）⭐**：Kadane：`cur = max(x, cur + x)`，取历史最大 → O(n)/O(1)
  - 📱 "当前子数组加不加 x"，加就延续，不加就重新开始；等价于前缀和取最小
  - 💻 完整代码见下方模板块；这是"一维 DP"最朴素的形态

```python
def max_sub_array(nums):
    cur = best = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)     # 延续还是重新开始
        best = max(best, cur)
    return best
```

- **238. 除自身以外数组的乘积（中等）**：前缀积 × 后缀积各扫一遍，两个方向乘起来 → O(n)/O(1)（输出不算）
  - 📱 左边所有数的乘积 × 右边所有数的乘积 = 答案
  - 💻 用一个答案数组先存左积，再从右往左乘右积
- **560. 和为 K 的子数组（中等）**：前缀和 + 哈希表，统计 s - k 出现过的次数 → O(n)/O(n)
  - 📱 看到"连续子数组和为 k"立刻反应前缀和；记得先塞 prefix[0] = 1
  - 💻 模板在 4.4，`ans += prefix[s - k]` 一行是灵魂

### 5.5 数组、排序与贪心（8 题）

> 特征：排序、区间、跳跃、边界。模板见 4.6、4.13。

- **31. 下一个排列（中等）**：从右找第一个"升序对"，交换，再把后缀反转 → O(n)/O(1)
  - 📱 "下一个字典序更大"的标准三步：找拐点、交换、反转
  - 💻 背熟模板，这题代码没得商量，就是套路
- **33. 搜索旋转排序数组（中等）**：二分，先判断 mid 在左半段还是右半段，再决定缩哪边 → O(log n)/O(1)
  - 📱 旋转数组总有"一半是有序的"，在有序的那半判断 target 是否在其中
  - 💻 模板在 4.6 模板三；核心是 `nums[left] <= nums[mid]` 判断左半有序
- **34. 在排序数组中查找元素的第一个和最后一个位置（中等）**：两次二分，一次找左边界一次找右边界 → O(log n)/O(1)
  - 📱 左边界 = 第一个 ≥ target，右边界 = 第一个 > target 再减 1
  - 💻 模板在 4.6 模板二，或直接用 bisect_left / bisect_right
- **55. 跳跃游戏（中等）**：贪心维护最远可达下标，当前位置够不着就返回 False → O(n)/O(1)
  - 📱 只问"能不能到"，维护一个最远距离就够，不需要具体路径
  - 💻 模板在 4.13 模板一
- **56. 合并区间（中等）**：按起点排序，逐个合并或开新 → O(n log n)/O(n)
  - 📱 区间题先排序；重叠条件 `start <= res[-1][1]`，合并取终点最大
  - 💻 模板在 4.13 模板二
- **215. 数组中的第 K 个最大元素（中等）**：大小为 k 的最小堆，或快速选择 → O(n log k)/O(k)
  - 📱 top-k 的堆模板：堆顶是第 k 大，比它大就替换
  - 💻 模板在 4.12；进阶可提快速选择平均 O(n)
- **279. 完全平方数（中等）**：BFS 逐层加平方数找最短，或一维 DP → O(n√n)/O(n)
  - 📱 从 0 出发每次加一个完全平方数，最短路就是最少个数
  - 💻 DP：`dp[i] = min(dp[i - j*j] + 1)`
- **763. 划分字母区间（中等）**：先记录每个字母最后出现位置，贪心扩张当前段 → O(n)/O(1)
  - 📱 段的最右边界 = 段内所有字母最后出现位置的最大值，到边界就切
  - 💻 两次遍历：先记 last 位置，再扫一遍扩张边界

### 5.6 链表（10 题）

> 特征：反转、合并、环、LRU。模板见 4.7。

- **2. 两数相加（中等）**：模拟竖式加法，进位 carry 循环带 → O(max(m,n))/O(1)
  - 📱 链表按位加：`sum = l1.val + l2.val + carry`，carry 进下一位
  - 💻 注意两个链表长度不等、最后还有进位的情况
- **19. 删除链表的倒数第 N 个结点（中等）**：快指针先走 n 步，再快慢一起走到尾 → O(n)/O(1)
  - 📱 倒数第 n 个 = 快指针先走 n 步后，慢指针跟着走到头时慢指针的位置
  - 💻 用哑节点处理"删除头节点"的边界
- **21. 合并两个有序链表（简单）⭐**：哑节点 + 双指针逐个接，剩下的直接续上 → O(m+n)/O(1)
  - 📱 链表题第一反应先建 dummy，省掉所有头节点特判
  - 💻 完整代码见下方模板块

```python
def merge_two_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next
```

- **141. 环形链表（简单）**：快慢指针，快指针走两步，相遇就有环 → O(n)/O(1)
  - 📱 环形跑道追及问题：快的一定能追上慢的
  - 💻 模板在 4.7 模板二；判空：`while fast and fast.next`
- **142. 环形链表 II（中等）**：快慢相遇后，头节点与相遇点同步走，相遇处即入口 → O(n)/O(1)
  - 📱 数学结论：从头和从相遇点各走一步，第一次相遇就是环入口
  - 💻 模板在 4.7 模板三
- **146. LRU 缓存（中等）**：OrderedDict，get 时 move_to_end，超容量 popitem(last=False) → O(1)/O(capacity)
  - 📱 面试高频设计题：哈希表查得快 + 双向链表记顺序
  - 💻 标准库写法在 3.4，手写双向链表版是加分项
- **148. 排序链表（中等）**：归并排序，快慢指针找中点，递归合并 → O(n log n)/O(log n) 栈深
  - 📱 O(1) 空间下不能用快排的随机访问，归并是链表排序正解
  - 💻 找中点：快指针一次走两步
- **160. 相交链表（简单）**：双指针各走完自己链表再接对方，相遇即交点 → O(m+n)/O(1)
  - 📱 两指针走过的路程相等时一定相遇；a 走完走 b，b 走完走 a
  - 💻 不相交则同时到 None，返回 None
- **206. 反转链表（简单）⭐**：prev/cur/nxt 三指针，边遍历边反转 → O(n)/O(1)
  - 📱 链表题之母：反转、回文、K 组翻转全依赖它
  - 💻 完整代码见下方模板块；断链前先保存 nxt

```python
def reverse_list(head):
    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    return prev
```

- **234. 回文链表（简单）**：快慢找中点 + 反转后半 + 逐对比较 → O(n)/O(1)
  - 📱 三步走：找中点、反转后半、双指针比较
  - 💻 或"栈存前半"的简化版，但 O(n) 空间，进阶用反转版

### 5.7 栈与单调栈（4 题）

> 特征：括号、下一个更大/更小、解码。模板见 4.5。

- **20. 有效的括号（简单）⭐**：左括号入栈，右括号查栈顶匹配 → O(n)/O(n)
  - 📱 栈的入门题：最近匹配的用栈顶，天然符合"后进先出"
  - 💻 完整代码见下方模板块；最后记得 `return not stack`

```python
def is_valid(s):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack
```

- **155. 最小栈（中等）**：辅助栈同步存"当前最小值"，取最小 O(1) → O(1)/O(n)
  - 📱 主栈 push 时，辅助栈 push min(当前值, 辅助栈顶)
  - 💻 进栈时同步进最小值，出栈时同步出
- **394. 字符串解码（中等）**：数字栈 + 字符串栈，遇到 ] 弹栈拼接 → O(n)/O(n)
  - 📱 嵌套结构用栈：`3[a2[c]]` 从内向外展开
  - 💻 两个栈分别存"次数"和"之前的字符串"，遇到 ] 拼一次
- **739. 每日温度（中等）**：单调递减栈存下标，遇到更高温就弹出结算天数 → O(n)/O(n)
  - 📱 "下一个更大元素"的标准姿势：新元素比栈顶大就弹出结算
  - 💻 模板在 4.5 模板二，栈里存下标

### 5.8 二叉树（12 题）

> 特征：遍历、深度、构造、路径。模板见 4.8。

- **98. 验证二叉搜索树（中等）**：中序遍历严格递增，或递归传 (min, max) 上下界 → O(n)/O(n)
  - 📱 BST 的中序遍历是递增序列，这是最顺的判定法
  - 💻 只比左右子树会漏"右子树里有比根小的"，必须带上下界
- **101. 对称二叉树（简单）**：递归比较 left.left 对 right.right → O(n)/O(n)
  - 📱 对称 = 镜像是自己，一棵树判断变两棵树比较
  - 💻 递归终止：双空 True，单空 False，值不等 False
- **102. 二叉树的层序遍历（中等）⭐**：BFS，for _ in range(len(q)) 按层收集 → O(n)/O(n)
  - 📱 层序 = 广度优先，关键是用"当前队列长度"锁住一层
  - 💻 完整代码见下方模板块

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    res, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res
```

- **104. 二叉树的最大深度（简单）**：递归 `1 + max(左深, 右深)` → O(n)/O(n)
  - 📱 树的题先把"空节点返回 0"写出来，一半的递归就写完了
  - 💻 可改层序 BFS 数层数，两种都行
- **105. 从前序与中序遍历序列构造二叉树（中等）**：前序定根，中序分左右，哈希表存中序下标 → O(n)/O(n)
  - 📱 前序第一个是根，根在中序的位置把数组切成左右子树，递归建
  - 💻 中序下标用 dict 存，查找 O(1)；用下标区间切分而不是切片
- **114. 二叉树展开为链表（中等）**：前序遍历把左子树移到右边，原右子树接到左子树末尾 → O(n)/O(1) 或 O(n)
  - 📱 递归/迭代：每步把当前节点的左子树整体挪到右边，再接回右子树
  - 💻 先序遍历顺序正好是展开后的链表顺序
- **124. 二叉树中的最大路径和（困难）**：后序递归，节点贡献 = 值 + 单侧最大分支，全局取最大 → O(n)/O(n)
  - 📱 路径可以在任意节点拐弯：`值 + 左分支 + 右分支`，但要先算两侧的单侧贡献
  - 💻 递归返回"单侧最大贡献"，全局变量记录"经过当前节点的最大路径"
- **226. 翻转二叉树（简单）**：递归交换左右子树 → O(n)/O(n)
  - 📱 Homebrew 作者面试挂掉的题，今天你会了
  - 💻 空节点返回自身，交换 left/right 后递归
- **236. 二叉树的最近公共祖先（中等）**：后序递归，左子树找到、右子树找到或等于自身 → O(n)/O(n)
  - 📱 递归时左右都找到了，当前节点就是 LCA
  - 💻 三种返回：找到 p、找到 q、都没找到返回 None
- **543. 二叉树的直径（简单）**：后序计算"左深 + 右深"，取最大 → O(n)/O(n)
  - 📱 直径 = 某节点左子树深度 + 右子树深度，遍历所有节点取最大
  - 💻 递归同时返回深度和更新全局最大直径
- **617. 合并二叉树（简单）**：递归，一个为空直接返回另一个 → O(n)/O(n)
  - 📱 同步遍历两棵树，都空才停
  - 💻 节点存在性判断优先于值运算
- **437. 路径总和 III（中等）**：前缀和 + 哈希表 + 回溯，路径方向向下 → O(n)/O(n)
  - 📱 树上的"和为 k 的子数组"，把前缀和思想搬到树上，回溯时增删计数
  - 💻 记得恢复现场：递归返回前把当前前缀和计数减一

### 5.9 图 / DFS / BFS / 回溯（8 题）

> 特征：岛屿、连通、排列组合、搜索。模板见 4.9、4.10。

- **200. 岛屿数量（中等）⭐**：DFS/BFS 沉没法，遇 1 计数并把它所在岛屿全淹没 → O(mn)/O(mn)
  - 📱 连通分量问题：访问过的格子改成 '0'，避免重复计数
  - 💻 完整代码见下方模板块；方向数组写熟

```python
def num_islands(grid):
    def dfs(r, c):
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or grid[r][c] != "1":
            return
        grid[r][c] = "0"                  # 沉没
        dfs(r + 1, c); dfs(r - 1, c)
        dfs(r, c + 1); dfs(r, c - 1)

    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)
    return count
```

- **207. 课程表（中等）**：拓扑排序（BFS 入度法），能排完 n 门课则无环 → O(V+E)/O(V+E)
  - 📱 有向图判环：先修关系成图，入度为 0 的先修课先上
  - 💻 用入度表 + 队列，出队时把后继入度减一
- **208. 实现 Trie（中等）**：字典树，每节点 dict 存子节点 + is_end 标记 → O(L) 每操作/O(字符数)
  - 📱 前缀树：字符串公共前缀只存一份，自动补全的底层
  - 💻 insert 沿路建节点，search 查完整词，startsWith 只查前缀
- **22. 括号生成（中等）**：回溯，右括号数 < 左括号数时剪枝 → O(4ⁿ/√n)/O(n)
  - 📱 两个计数器：可放的左括号、可放的右括号，右不能超过左
  - 💻 模板：`if left < n: 加左`，`if right < left: 加右`
- **39. 组合总和（中等）**：回溯，候选可重复选，start 从当前 i 开始不回头 → 指数级/O(n)
  - 📱 与 78 子集的区别：`backtrack(i)` 而不是 `backtrack(i+1)`
  - 💻 先排序可剪枝：当前数大于剩余目标就直接 break
- **46. 全排列（中等）**：回溯 + used 数组，路径满长度记录 → O(n·n!)/O(n)
  - 📱 排列和组合的区别：排列用 used 数组、每层都从 0 开始
  - 💻 模板在 4.9 模板二；有重复元素的题要先排序去重
- **78. 子集（中等）**：回溯，每次先把当前路径记入结果 → O(2ⁿ)/O(n)
  - 📱 子集是回溯入门题：选或不选，路径拷贝时用 path[:]
  - 💻 模板在 4.9 模板一
- **79. 单词搜索（中等）**：回溯 + 方向数组 + visited，同格不可重用 → O(mn·4ᴸ)/O(L)
  - 📱 每个格子当起点试 DFS，匹配 word 前缀继续，错了回退
  - 💻 同格复用检查：原地标记（改成占位符）再恢复

### 5.10 动态规划（17 题）

> 特征：最优值、方案数、状态转移。模板见 4.11。

- **5. 最长回文子串（中等）**：中心扩展，枚举每个中心（含两字符中心）向两边扩 → O(n²)/O(1)
  - 📱 回文先想中心扩展，比二维 DP 省空间；中心有 2n-1 个
  - 💻 两个中心类型：单字符、双字符，分别扩展
- **62. 不同路径（中等）**：二维 DP，`dp[i][j] = dp[i-1][j] + dp[i][j-1]` → O(mn)/O(n)
  - 📱 走到每格的路径数 = 从上面来 + 从左边来
  - 💻 可滚动为一维数组，面试提空间优化加分
- **70. 爬楼梯（简单）⭐**：斐波那契，滚动变量 a, b = b, a + b → O(n)/O(1)
  - 📱 第 n 阶 = 第 n-1 阶走 1 步 + 第 n-2 阶走 2 步，就是斐波那契
  - 💻 完整代码见下方模板块；这是"一维 DP + 滚动优化"的范式

```python
def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
```

- **72. 编辑距离（中等）**：二维 DP，增删改三种操作取最小 → O(mn)/O(mn)
  - 📱 `dp[i][j]` 表示 word1 前 i 个变 word2 前 j 个的最小步数
  - 💻 转移：相等则继承左上，否则 `min(左, 上, 左上) + 1`
- **121. 买卖股票的最佳时机（简单）**：记录历史最低价，算每天卖出能赚的最大差 → O(n)/O(1)
  - 📱 只能买卖一次：不断更新"最低买入价"和"最大利润"
  - 💻 遍历时 `profit = max(profit, price - min_price)`
- **122. 买卖股票的最佳时机 II（中等）**：贪心累加所有上涨段 → O(n)/O(1)
  - 📱 不限次数：只要有上涨就赚，把每天的"正差价"全加起来
  - 💻 面试问"为什么能这样"，答：每次上升段拆成相邻日差的和
- **139. 单词拆分（中等）**：一维 DP，`dp[i]` 表示前 i 个字符可拆分，查后缀在字典里 → O(n²)/O(n)
  - 📱 把单词表转 set，逐个检查"以 i 结尾的子串"能否接上
  - 💻 `dp[j] and s[j:i] in word_set` 即 dp[i] 为真
- **152. 乘积最大子数组（中等）**：同时维护当前最大和最小乘积（负负得正）→ O(n)/O(1)
  - 📱 和最大子数组和的区别：负数会让最大变最小，所以要双向维护
  - 💻 `cur_max = max(x, x*cur_max, x*cur_min)`，再交换维护
- **198. 打家劫舍（中等）**：`dp[i] = max(dp[i-1], dp[i-2] + nums[i])` → O(n)/O(1)
  - 📱 每家两个选择：偷（拿前家隔一家）或不偷（保留前一家最优）
  - 💻 模板在 4.11 模板二，滚动变量省空间
- **221. 最大正方形（中等）**：二维 DP，`dp[i][j] = min(左, 上, 左上) + 1` → O(mn)/O(mn)
  - 📱 正方形边长由"最小的邻居"决定，短板效应
  - 💻 dp 值即边长，答案是 dp 的最大值的平方
- **300. 最长递增子序列（中等）**：贪心 + 二分：维护 tails 数组，bisect_left 替换 → O(n log n)/O(n)
  - 📱 经典 O(n²) DP 可做，但 tails + bisect 是进阶必会
  - 💻 tails 存"长度为 i 的子序列的最小末尾"，保持递增
- **322. 零钱兑换（中等）**：完全背包，`dp[amount] = min(dp[amount - coin] + 1)` → O(n·amount)/O(amount)
  - 📱 硬币无限用：容量正序遍历（完全背包特征）
  - 💻 初始化 dp[0]=0，其余用 inf 标记"凑不出"
- **337. 打家劫舍 III（中等）**：树形 DP，递归返回 (偷本节点, 不偷本节点) → O(n)/O(n)
  - 📱 每个节点两种状态：偷则不能偷子节点，不偷则子节点取最优
  - 💻 后序递归，返回长度为 2 的元组，父节点据此决策
- **338. 比特位计数（简单）**：`dp[i] = dp[i>>1] + (i & 1)` → O(n)/O(n)
  - 📱 去掉最低位后的数已经算过，加上最低位是否为 1
  - 💻 模板在 4.14 模板二
- **416. 分割等和子集（中等）**：0/1 背包，容量 = 总和一半，逆序遍历 → O(n·target)/O(target)
  - 📱 "能否凑出总和一半"是标准的 0/1 背包布尔问题
  - 💻 模板在 4.11 模板三；总和为奇数直接 False
- **494. 目标和（中等）**：转化为背包：正数和 = (target + 总和) / 2 → O(n·sum)/O(sum)
  - 📱 所有 + 的和为 P，则 P - (总和 - P) = target，解出 P 转成 416 题
  - 💻 先判 (target + total) 是否为偶数且非负
- **647. 回文子串（中等）**：中心扩展，统计所有中心能扩展出的回文个数 → O(n²)/O(1)
  - 📱 每个中心向两边数，回文个数 = 中心个数 × 每中心扩展次数
  - 💻 与 5 题共用中心扩展模板，一个求最长一个求数量

---

### 5.11 本章小结

80 题 = 10 类，各类数量：哈希 8、双指针 6、滑动窗口 4、前缀和 3、数组排序贪心 8、链表 10、栈 4、二叉树 12、图与搜索 8、动态规划 17。

```
刷题顺序建议：
  第一周先啃：哈希(1) → 链表(206) → 栈(20) → 双指针(15) → 滑动窗口(3)
  第二周开始：二叉树全套 → 图与回溯 → 动态规划分周啃
  地标题（⭐ 共 10 道）优先写完整代码，其余按思路卡复习
```

> 📱 手机复习口诀：看到题先想模式，模式定复杂度，复杂度对得上数据规模再动手。80 题不求全会默写，求"看到题能说出模式 + 思路方向"。

---

## 六、面试沟通流程

刷题是"输入"，面试表现是"输出"。很多人题刷得很好，一上机就紧张得说不出话。这一章教你**把脑子里的思路变成面试官听得懂的节奏**。

> 核心认知：算法面试不是"做题考试"，是"边做边讲"。面试官看你 30-45 分钟，除了答案对不对，更在意你的思考过程和沟通方式。一道做对但讲不清的题，得分可能不如一道"思路正确、代码有小 bug 但全程讲得清楚"的题。

### 6.1 面试现场的时间结构

一场算法面（45 分钟）的典型节奏：

```
0-5 分钟     自我介绍 + 热场（聊天，不是做题）
5-8 分钟     读题 + 确认理解（你提问，面试官回答）
8-20 分钟    讨论思路（先暴力后优化，边想边说）
20-40 分钟   写代码 + 测试 + debug
40-45 分钟   追问 + 复杂度 + 反问环节
```

注意中间那条：**讨论思路占的时间比写代码还长**。面试官期待你先说思路再动手，不是闷头就写。如果你上来就写，哪怕写对了，面试官也会觉得你"只会背题，不会思考"。

### 6.2 拿到题目的 30 秒

拿到题目先别急着看示例。按顺序做三件事：

```
第一件事：复述题目
   "所以你的意思是，输入是一个整数数组和一个 target，
    要返回两个下标，使这两个位置的数相加等于 target，对吧？"
   （复述 = 确认理解 + 让面试官知道你读懂了 + 给自己思考时间）

第二件事：问清楚关键信息
   "数组有序吗？"
   "元素有重复吗？重复时返回哪一组？"
   "n 最大是多少？这决定我用什么算法。"
   "需要返回下标还是返回值？"

第三件事：给一个暴力解
   "最简单的话，我可以用双重循环 O(n²) 枚举所有配对。"
   （先给暴力解展示"能思考"，再优化展示"会优化"）
```

这三步做完，面试官对你的印象已经打上"思路清晰"的标签。**不要跳过"复述题目"**，它是整个面试最重要的定心丸。

### 6.3 边想边说：把内心戏讲出来

想思路的时候不要沉默。沉默 5 秒以上，面试官就开始怀疑你卡住了。正确的姿势是"有声思考"：

```
坏示范（沉默 3 分钟后）："我想不出来。"
好示范：
   "看到'两数之和'，我第一反应是哈希表，因为配对问题用哈希能把
    查找降到 O(1)。但有个细节：先查还是先存？如果先存，可能遇到
    同一个元素自己和自己配对的情况，所以应该先查 target - x，
    再把自己存进去。复杂度 O(n)，空间 O(n)。"
```

卡住的时候更要说话：

```
"我现在在想一个边界情况：如果数组里没有解怎么办？按题意应该
 不会出现，但我还是会防御性地返回一个空列表。"
"哈希表空间是 O(n)，我在想能不能压缩成 O(1)……如果先排序，
 用双指针，空间就是 O(1) 了，但时间是 O(n log n)。"
```

**卡住了怎么办**：
1. 回到"我已知什么、要算什么"，从头梳理
2. 换一个更小的例子，手工走一遍
3. 主动求助面试官："我能不能给一个小提示？"大部分面试官会帮，这不是扣分项

### 6.4 写代码时的沟通

开始写代码前，先说一句"那我来写吧，大概思路是……"，让面试官有预期。写的过程中保持以下习惯：

```
1. 先写骨架，再填细节
   "我先把函数签名和边界判断写出来，然后填主逻辑。"

2. 变量名有意义
   用 left/right 而不是 l/r，用 visited 而不是 v
   （面试官和你的代码第一次见面，可读性 = 沟通能力）

3. 写关键行时小声解释
   写到 dp[i] = max(dp[i-1], dp[i-2] + nums[i]) 时说：
   "这里两种选择：偷这一家，或者不偷。"

4. 别写太快，也别边写边删
   写完一段看一遍再写下一段，发现错了就用语言解释
   "这里我原来想用 while，想想还是 for 更清晰，改一下。"
```

**写代码最大的禁忌**：写完才解释。写的过程就是解释的过程。

### 6.5 测试与 debug 沟通

代码写完**不要立刻说"完成了"**。正确流程：

```
1. "我拿示例跑一遍。"（用题目示例，手动走一遍，嘴上说出来）
2. "再测几个边界：空数组、只有一个元素、全是重复元素。"
3. "复杂度分析：外层循环 O(n)，哈希操作平均 O(1)，所以总时间
    O(n)，空间 O(n) 因为哈希表最坏存 n 个键值对。"
```

如果代码有 bug：

```
"这个用例输出不对。看第 5 行，left 指针在等于的情况没有前进，
 会死循环。修正方法是在相等分支里同时移动 left 和 right。"
```

**Debug 的沟通要点**：先定位再动手，别在没说清问题的情况下乱改。改完一定重新跑一次测试。

### 6.6 复杂度口述模板

面试官十有八九会问复杂度。给一个通用的三段式回答：

```
第一段：时间
   "时间上，主循环遍历 n 个元素，循环体内是 O(1) 操作，
    所以是 O(n)。"

第二段：空间
   "空间上，额外用了一个哈希表，最坏情况存 n 个键值对，
    所以是 O(n)。如果改成排序加双指针，空间是 O(1)，但时间
    变成 O(n log n)。"

第三段：能否优化（主动说）
   "目前这个解法在时间复杂度上已经是最优了，因为必须遍历
    每个元素至少一次。空间上如果想省，可以考虑……"
```

如果面试官追问"还能更快吗"，不要慌：

```
"如果数组是有序的，可以用二分把查找降到 O(log n)，整体 O(log n)。
 但题目没说有序，所以排序加二分是 O(n log n)，不如哈希的 O(n)。"
```

### 6.7 常见追问与应对

**追问 1："如果输入特别大怎么办？"**

```
"那就不能用 O(n²) 的算法，我会优先保证复杂度能撑住数据规模。
 如果内存也紧张，考虑流式处理或分批。"
```

**追问 2："如果有重复元素呢？"**

```
"回到题目约束：如果要求返回任意一组，哈希表方案不受影响；
 如果要求返回所有组合，就要在排序后跳过重复元素（去重逻辑）。"
```

**追问 3："你的解法有什么缺点？"**

```
"哈希表有平均 O(1) 的查找，但最坏情况哈希冲突会退化到 O(n)。
 如果对最坏情况敏感，可以改成排序加双指针，保证 O(n log n)。"
```

**追问 4："还能优化吗？"**

```
把"时间换空间 / 空间换时间"的 trade-off 讲一遍，展示你懂权衡。
面试官问这个不是要你优化到极致，是看你会不会分析。
```

### 6.8 白板 vs 在线编辑器

国内面试两种形式都常见：

```
在线编辑器（牛客/力扣/公司平台）：
  ✔ 写完能跑测试，注意先写核心逻辑再处理输入输出
  ✔ ACM 模式记得自己处理 input()，先写一个最小可跑版本
  ✔ 跑测试前说"我先测几个用例"

白板（或共享文档）：
  ✔ 没有运行环境，代码只能靠"读"，所以更要写清楚
  ✔ 不写编译器都懂的简写，写完整、规范的代码
  ✔ 用伪代码先过一遍逻辑，再转成正式代码
  ✔ 边说边写，把"这段在做什么"讲出来，因为没人能跑
```

白板面试是"讲题 + 写题"的双重考验，练法就是：**找个人当面试官，或者对着空气把第六章整套流程走一遍**。

### 6.9 模拟面试脚本（自己练）

每周至少做一次完整的模拟面试，自己扮演双方：

```
题目池：第五章 80 题 + 剑指 Offer 高频题
流程（45 分钟）：
  0-3 分钟    自我介绍（"我叫 X，主要用 Python，做过 LLM 项目"）
  3-5 分钟    复述题目 + 提问（有序吗？规模？）
  5-10 分钟   暴力解 + 优化思路
  10-30 分钟  写代码（边写边讲）
  30-35 分钟  跑测试 + 边界用例
  35-40 分钟  复杂度分析（三段式）
  40-45 分钟  追问模拟（"有重复元素呢？能再快点吗？"）
```

录下来或者开着电脑计时。你会发现第一次模拟至少卡壳 3 次，卡住的地方就是你要补的短板，往往是"讲不出思路"而不是"不会做"。

### 6.10 本章小结

```
算法面试 = 边做边讲，不是闷头做题

四步节奏：
  复述题目 → 问清信息 → 给暴力解 → 再给优化
写码三要：
  先骨架后细节、变量名有意义、关键行出声解释
测试两必：
  跑示例 + 跑边界，主动做复杂度分析（三段式）
追问应对：
  重复元素、大数据、缺点、优化，四个方向背熟话术
```

---

## 七、8周刷题计划（对接阶段七）

> 本计划对接《大模型学习 / 07-阶段四至七》阶段七目标：LeetCode Hot 100 刷完。阶段七是"第 26 周 + 全程"，也就是从你读到这一章开始，边学 LLM 边刷，最后集中冲刺。这个 8 周计划可以并行放在阶段五、六进行，第 8 周收尾正好接上第 26 周。

> 节奏：📱 白天手机看思路（每天 30 分钟，翻第五章速查卡），💻 晚上写代码（每天 1.5-2 小时，2-3 题）。每周六做一次模拟面试（第六章 6.9 脚本）。

| 周次 | 主题 | 对应模板 | 题目（来自第五章） | 周目标 |
|------|------|---------|-------------------|--------|
| 第 1 周 | 方法论 + 哈希 + 数组 | 4.1-4.4 | 1, 49, 128, 136, 169, 287, 347, 448, 53, 238, 560 | 掌握 5 步法，能说出复杂度三段式 |
| 第 2 周 | 双指针 + 滑动窗口 | 4.1, 4.2 | 11, 15, 42, 75, 88, 283, 3, 76, 239, 438 | 双指针和滑动窗口模板默写 |
| 第 3 周 | 链表 + 栈 | 4.5, 4.7 | 2, 19, 21, 141, 142, 146, 148, 160, 206, 234, 20, 155, 394, 739 | 反转链表、哑节点、单调栈三件套 |
| 第 4 周 | 二叉树 | 4.8 | 98, 101, 102, 104, 105, 114, 124, 226, 236, 543, 617, 437 | 四种遍历默写，递归与迭代都会 |
| 第 5 周 | 图 + DFS/BFS + 回溯 | 4.9, 4.10 | 200, 207, 208, 22, 39, 46, 78, 79 | 回溯三件套，沉没法岛屿 |
| 第 6 周 | 动态规划 | 4.11 | 5, 62, 70, 72, 121, 122, 139, 152, 198, 221, 300, 322, 337, 338, 416, 494, 647 | 一维 DP、背包、树形 DP 三种套路 |
| 第 7 周 | 堆 + 贪心 + 综合复习 | 4.12, 4.13 | 31, 33, 34, 55, 56, 215, 279, 763 | 堆与贪心模板，错题重做 |
| 第 8 周 | 冲刺模拟 | 全模板 | 重做全部错题 + 模拟面试 | 每类模式各随机抽 1 题，共 10 题限时完成 |

### 7.1 第 1 周：方法论 + 哈希表 + 前缀和

> 🎯 本周目标：建立刷题习惯，掌握哈希表和前缀和两大"空间换时间"武器。

**📱 手机任务（每天 30 分钟）**：
- 第 1-2 天：精读本指南第一章、第二章，把复杂度速查表截图存手机
- 第 3-7 天：每天翻第五章 5.1 哈希表 + 5.4 前缀和的思路卡，共 11 题

**💻 电脑任务（第 1-7 天，每天 2-3 题）**：
- 按顺序做：1 ⭐（完整写）→ 49 → 128 → 136 → 169 → 287 → 347 → 448 → 53 ⭐ → 238 → 560
- 每天开始前：手写一遍 `two_sum` 和 `max_sub_array`（各 5 分钟）
- 每天结束：按 1.8 模板在 Obsidian 记录

**周六**：第一次模拟面试（第六章 6.9 脚本），题：两数之和、最大子数组和。

**周日复盘**：
- [ ] 5 步法能脱口而出
- [ ] 复杂度三段式（时间/空间/优化）能说 30 秒
- [ ] 两数之和、最大子数组和能默写

### 7.2 第 2 周：双指针 + 滑动窗口

> 🎯 本周目标：掌握"同向/相向双指针"和"滑动窗口收缩"两个最常用数组技巧。

**📱 手机任务**：每天翻 5.2 + 5.3 的 10 题思路卡，重点记"为什么移动这个指针"的理由。

**💻 电脑任务**：
- 双指针：11 → 15 ⭐ → 42 → 75 → 88 → 283
- 滑动窗口：3 ⭐ → 76 → 239 → 438
- 每天开始前：默写 `three_sum` 去重版、`length_of_longest_substring`

**周六**：模拟面试，题：三数之和、盛最多水的容器。

**周日复盘**：
- [ ] 能解释"三数之和为什么要排序去重"
- [ ] 能画出滑动窗口收缩过程
- [ ] 接雨水 42 能讲出双指针和单调栈两种思路

### 7.3 第 3 周：链表 + 栈

> 🎯 本周目标：链表是面试最高频题型之一，这一周把它拿下。

**📱 手机任务**：每天翻 5.6 + 5.7 的 14 题思路卡，脑子里过"反转链表三步"。

**💻 电脑任务**：
- 链表：206 ⭐（必默写）→ 21 ⭐ → 141 → 142 → 160 → 19 → 2 → 234 → 148 → 146
- 栈：20 ⭐ → 155 → 739 → 394
- 每天开始前：默写 `reverse_list`、`is_valid`

**周六**：模拟面试，题：反转链表、有效的括号。

**周日复盘**：
- [ ] 反转链表三种写法（迭代/递归/哑节点）至少会两种
- [ ] 能解释 LRU 为什么用哈希 + 双向链表
- [ ] 单调栈能讲清"什么时候弹出结算"

### 7.4 第 4 周：二叉树

> 🎯 本周目标：树是递归思维的训练场，二叉树全家桶一周拿下。

**📱 手机任务**：每天翻 5.8 的 12 题思路卡，背"空节点返回"模板。

**💻 电脑任务**：
- 遍历：104 → 102 ⭐ → 226 → 101（先简单，建立信心）
- 进阶：98 → 236 → 543 → 617 → 437（高频）
- 构造：105 → 114 → 124（压轴）
- 每天开始前：默写 `level_order`、`max_depth`

**周六**：模拟面试，题：二叉树的层序遍历、验证二叉搜索树。

**周日复盘**：
- [ ] 前中后序递归 + 层序迭代都能独立写出
- [ ] 中序迭代版能不看笔记写出来
- [ ] 能说清"为什么验证 BST 要带上下界"

### 7.5 第 5 周：图 + DFS/BFS + 回溯

> 🎯 本周目标：回溯三件套 + BFS 模板，解决组合、排列、搜索类问题。

**📱 手机任务**：每天翻 5.9 的 8 题思路卡，背回溯模板的"选择/撤销"对称性。

**💻 电脑任务**：
- 回溯：78 → 46 → 39 → 22（由易到难）→ 79（压轴）
- 图：200 ⭐ → 207 → 208
- 每天开始前：默写 `subsets`、`num_islands`（沉没法）

**周六**：模拟面试，题：全排列、岛屿数量。

**周日复盘**：
- [ ] 回溯三件套（终止/选择/撤销）能默写
- [ ] 子集和排列的差异（start vs used）能讲清
- [ ] BFS 的"入队即标记"能说清原因

### 7.6 第 6 周：动态规划（本周最重）

> 🎯 本周目标：DP 是 Hot 100 里占比最高的类型，用一周拿下四类套路。

**📱 手机任务**：每天翻 5.10 的 17 题思路卡，先背"状态是什么、转移是什么"。

**💻 电脑任务**（DP 题要慢做，重理解）：
- 一维入门：70 ⭐ → 121 → 122 → 198 → 152
- 二维：62 → 72 → 221
- 进阶一维：300 → 139 → 5 → 647
- 背包：416 → 494 → 322
- 树形：337
- 每天开始前：默写 `climb_stairs` 滚动版、`can_partition`

**周六**：模拟面试，题：爬楼梯、最长递增子序列。

**周日复盘**：
- [ ] 能画出爬楼梯、打家劫舍的状态转移
- [ ] 0/1 背包和完全背包的遍历方向区别能讲清
- [ ] 416、494 能说出"为什么是背包题"

### 7.7 第 7 周：堆 + 贪心 + 综合复习

> 🎯 本周目标：补齐堆和贪心，然后开始"混合刷题"训练模式识别。

**📱 手机任务**：每天翻 5.5 的 8 题思路卡 + 4.15 速查卡。

**💻 电脑任务**：
- 堆：215 → 347（4.12 模板）
- 贪心/数组：55 → 56 → 763 → 31 → 33 → 34 → 279
- 复习：把前 6 周标记为 ✘ 的题全部重做（每天 1-2 道）

**周六**：模拟面试，题：数组中的第 K 个最大元素、合并区间。

**周日复盘**：
- [ ] 堆的"大小为 k 的堆"模板默写
- [ ] 不再看分类，能说出每道题的模式
- [ ] 错题重做率达到 80%

### 7.8 第 8 周：冲刺模拟（对接第 26 周）

> 🎯 本周目标：限时训练 + 模拟面试，把"会做"变成"考场上能做出来"。

**📱 手机任务**：每天用 4.15 速查卡做"模式识别游戏"：随机抽 10 题，只看题名说出模式、复杂度、一句话思路。

**💻 电脑任务**：
- 限时训练（每天 60 分钟，独立完成 3 题，不限 tag）
- 每天一次完整模拟面试（45 分钟，第六章脚本）
- 整理"面试前一周错题清单"，每类选 2 道最不熟的再啃一遍

**周六**：完整模拟笔试（90 分钟，5 题，覆盖 5 个不同模式）。

**周日复盘**：
- [ ] 模拟笔试正确率 ≥ 3/5
- [ ] 能连续 30 分钟边写边讲不卡壳
- [ ] Obsidian 复盘笔记超过 80 条

### 7.9 与阶段七的衔接

```
阶段七（第 26 周）的时间安排参考：
  白天：手机刷第五章速查卡 + 背面试题（ML/DL 八股）
  晚上：重做错题 + 整理项目（GitHub 项目包装）+ 模拟面试
  周六：完整模拟面试（算法 + 项目 + 行为面试）

第 26 周结束时检查清单（对齐阶段七 ✅）：
  - [ ] LeetCode Hot 100 刷完（本计划 80 题 + 精选 20 题）
  - [ ] 每天 2-3 题节奏保持
  - [ ] 边写边讲的能力成型
  - [ ] 复杂度三段式随口能说
```

> 提示：刷完本计划 80 题后，如果想补量，优先刷剑指 Offer 的数组/链表/二叉树/DP 部分，这些是国内大厂笔试的最爱，和 Hot 100 重叠度高，刷起来快。

---

## 八、章节练习

> 本库一贯理念：学多少，练多少。以下是按章节配套的练习，全部"先想后写、写完对照"。每章练习对应一个检查点，做完打勾。答案要点在 8.8，先自己做再看。

### 8.1 第一章练习：方法论

**练习 1-1 复杂度速判**：不看第二章，凭直觉回答：n 从 1 变成 10⁵，下列表达式各变多少倍？

```
(a) 100n + 50
(b) n log₂n
(c) n² / 2
(d) 3n² + 5n
(e) 2ⁿ
```

**练习 1-2 读题三问**：对下面的题，写出你该问的三个问题：

> 给定一个整数数组 nums 和一个整数 k，返回数组中和为 k 的连续子数组的个数。

**练习 1-3 5 步法演练**：用 5 步法解"两数之和"，每一步写下你的产出（读题笔记、思路、代码、测试用例、复盘记录），录屏或录音检查自己"边做边讲"的表现。

### 8.2 第二章练习：复杂度分析

**练习 2-1 算复杂度**：写出下列代码的时间复杂度（不看答案）：

```python
# (a)
def f(nums):
    s = 0
    for x in nums:
        s += x
    return s

# (b)
def g(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n):
            print(nums[i], nums[j])

# (c)
def h(nums):
    i = 0
    n = len(nums)
    while i < n:
        i *= 2  # 注意初始 i=0
    # 提示：这题的坑是什么？

# (d)
def k(nums):
    n = len(nums)
    for i in range(n):
        j = 1
        while j < n:
            j *= 2
```

**练习 2-2 空间复杂度**：下列代码的额外空间复杂度是多少？

```python
# (a)
def p(nums):
    return [x * 2 for x in nums]

# (b)
def q(nums):
    res = []
    for x in nums:
        res.append(x)
    return res

# (c)
def r(root):
    if not root:
        return 0
    return 1 + max(r(root.left), r(root.right))
```

**练习 2-3 数据规模定算法**：n ≤ 10⁵，target 要找两个数和为 k，给 O(n²) 还是 O(n) 的方案？为什么？

### 8.3 第三章练习：Python 工具

**练习 3-1 deque**：不查资料，用 deque 实现一个"最近 5 次浏览记录"：每访问一个新页面，如果记录里已有就移除再插到最前，只保留 5 条。

**练习 3-2 Counter**：用 Counter 写一个函数，判断两个字符串是否是字母异位词（然后对比"排序法"和"计数法"的复杂度）。

**练习 3-3 defaultdict**：用 defaultdict 实现：给定一个单词列表，按首字母分组输出 {首字母: [单词...]}。

**练习 3-4 heapq**：实现"流式 top-3"：不断输入数字，随时能输出当前输入过的最大的 3 个数（维护一个大小为 3 的堆）。

**练习 3-5 bisect**：写一个函数，在有序数组中统计 target 出现的次数，要求 O(log n)（用 bisect_left 和 bisect_right）。

**练习 3-6 二维数组**：创建 3×4 的全 0 矩阵，用正确写法；再写出"改 [0][0] 会连累三行"的错误写法，理解区别。

### 8.4 第四章练习：模式模板

**练习 4-1 默写模板**：合上文件，在 15 分钟内默写下列 8 个模板（每个 20-30 行）：

```
① two_sum          ② three_sum（含去重）
③ length_of_longest_substring（滑动窗口）
④ reverse_list      ⑤ level_order
⑥ subsets（回溯）   ⑦ num_islands（沉没法）
⑧ climb_stairs（滚动数组）
```

**练习 4-2 模式识别**：给下列题目特征，写出对应模式（答案在 8.8）：

```
(a) "有序数组中找 target"            → ?
(b) "找下一个更大的元素"              → ?
(c) "连续子数组和为 k 的个数"          → ?
(d) "二叉树按层输出"                  → ?
(e) "排列/组合/子集"                  → ?
(f) "第 k 大 / top-k"               → ?
(g) "只出现一次的数字"                → ?
(h) "相邻房子不能同时偷的最大金额"       → ?
```

**练习 4-3 一题多解**：接雨水 42 题，写出双指针和单调栈两种解法，各跑一遍示例，对比两种思路。

**练习 4-4 复杂度标注**：把第四章 14 个模板的时空复杂度做成一张表（不看文件写），写不出来的回去翻。

### 8.5 第五章练习：速查表自测

**练习 5-1 分类连线**：不看 5.11，把下列 20 题按 10 类分类（答案在 8.8）：

```
1, 3, 15, 20, 21, 42, 46, 49, 53, 70,
78, 102, 128, 146, 206, 215, 300, 322, 560, 739
```

**练习 5-2 一句话思路**：随机抽 10 题，每道 30 秒内说出"模式 + 一句话思路 + 复杂度"，做不到的题记下来，回看对应思路卡。

**练习 5-3 地标题全写**：把 10 道 ⭐ 题的完整代码各写一遍，写不出就重抄一遍再默写，直到全部过关（重点：1、3、15、20、21、53、70、102、200、206）。

**练习 5-4 反查**：从模式反查题目：给一个模式（比如"滑动窗口"），你能列出本指南里所有属于它的题吗？（核对 5.3 滑动窗口 4 题）

### 8.6 第六章练习：面试沟通

**练习 6-1 复述题**：找一道新题（不在本指南里），先对着镜子复述题目 30 秒，再用手机录音，回听自己复述得清不清楚。

**练习 6-2 三段式**：任选 3 道已刷过的题，写出"时间/空间/能否优化"三段式回答稿，背熟其中一段，录下来听。

**练习 6-3 模拟面试**：按 6.9 脚本做一次 45 分钟完整模拟，重点记录"沉默超过 5 秒的时刻"，下次避免。

**练习 6-4 追问演练**：找同伴或自己扮演面试官，对"两数之和"连续追问：重复元素？数组有序？返回所有组合？n 很大？空间能省吗？逐一回答。

### 8.7 第八章综合练习：限时组合卷

90 分钟，5 题，覆盖 5 个模式，模拟笔试：

```
第 1 题（简单·哈希）：两数之和变体：返回所有不重复的配对。
第 2 题（中等·链表）：反转链表的第 m 到 n 个节点。
第 3 题（中等·滑动窗口）：长度最小的子数组（和 ≥ target）。
第 4 题（中等·二叉树）：二叉树的锯齿形层序遍历（蛇形走位）。
第 5 题（中等·DP）：0-1 背包恰好装满的方案数（组合数）。
```

时间分配建议：每道 15 分钟写代码，5 分钟测试，10 分钟冗余。做完按 1.8 模板给每道题写复盘。

### 8.8 练习答案要点

**8.1 答案**：

```
1-1  (a) 约 10⁵ 倍（O(n)）  (b) 约 17 万倍（O(n log n)）
     (c) 约 10¹⁰ 倍（O(n²)） (d) 约 10¹⁰ 倍（O(n²)，忽略低阶项）
     (e) 天文数字（O(2ⁿ)，10⁵ 不可能算完）

1-2  三个问题：
     ① 子数组必须连续吗？（连续才用滑动窗口/前缀和）
     ② 元素可能为负吗？（有负数时滑动窗口失效，改前缀和）
     ③ n 最大是多少？k 的范围？（决定用 O(n) 还是 O(n log n)）
```

**8.2 答案**：

```
2-1  (a) O(n)             (b) O(n²)
     (c) 死循环！i 从 0 开始，i *= 2 永远是 0。这题的"坑"就是无限循环
     (d) O(n log n)：外层 n 次，内层每次乘 2 走 log n 步

2-2  (a) O(n)（新列表）
     (b) O(n)（复制了一份）
     (c) O(n)（递归深度 = 树高，最坏退化成链）

2-3  用 O(n) 的哈希表方案。n ≤ 10⁵ 时 O(n²) 是 10¹⁰ 次操作，
     远超 1 秒的 10⁸ 上限，必然超时。读题看数据规模再定算法。
```

**8.4 答案（模式识别）**：

```
(a) 二分查找(4.6)   (b) 单调栈(4.5)   (c) 前缀和(4.4)
(d) BFS 层序(4.8)   (e) DFS 回溯(4.9) (f) 堆(4.12)
(g) 位运算(4.14)    (h) 动态规划(4.11)
```

**8.5 答案（分类）**：

```
哈希表：1, 49, 128          滑动窗口：3, 438
双指针：15, 42              前缀和：53, 560
栈：20, 739                 链表：21, 146, 206
二叉树：102                 图/回溯：46, 78
堆：215                     动态规划：70, 300, 322
```

> 说明：15、42 也可归栈/其他类，分类不是唯一的，能说出"为什么归这类"即可。这就是模式识别的训练意义。

---

### 8.9 结语

到这里，整份指南就结束了。最后送你三句话，也是三份告别提醒：

```
第一句：刷题没有捷径，但有一条"最短路径"。
  先学模式、按 tag 刷、重做三遍，这条路是最短路径。

第二句：算法题不是考智商，是考重复。
  你不需要天赋异禀，你需要的是"把 80 题和 14 个模板重复到肌肉记忆"。
  面试时你写反转链表像写自己的名字，就赢了。

第三句：把刷题当成训练，而不是任务。
  每天 2-3 题，坚持 8 周，你会看到第 3 周之后的质变。
  阶段七的面试冲刺，你准备好了。
```

> 📚 延伸：本指南只覆盖 Python 刷题。算法之外，阶段七还需要准备 ML/DL 面试题、Transformer 专题、项目包装和行为面试，这些都在《大模型学习 / 07-阶段四至七-Agent到面试.md》的"阶段七"章节。刷题是敲门砖，把学到的东西讲出来才是offer。

> 🎉 完成本指南所有章节练习后，你就具备了独立进入阶段七冲刺的能力。祝刷题顺利，面试顺利。







