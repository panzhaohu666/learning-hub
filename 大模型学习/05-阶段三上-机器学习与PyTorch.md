# 阶段三 · 上 · 每日学习指南

阶段三·上 · 每日学习指南

### 机器学习基础 + PyTorch 精通（第 8-11 周）

> 🎉 **欢迎来到整个学习计划的核心地基！**

> 阶段三共有 9 周（第 8-16 周），分为上下两部分。你现在在"上"——从零开始理解机器学习，然后掌握 PyTorch。

> 这些知识是你未来理解 Transformer、大语言模型、Agent 系统的**绝对前提**。没有它们，后面的内容就像在沙滩上盖楼。

>

> **心态提示**：第 8-9 周会很"数学"，但别怕——你会亲手实现每一个算法，数学只是帮你理解"为什么这样写代码"的工具，不是考试内容。

### 第8周 · 主题：机器学习基础

### 第8周 · 星期一：线性回归 —— 手写梯度下降

---

### 手机摸鱼 · 上午 30 分钟

阅读主题：线性回归 + 梯度下降

> 🧠 **为什么学这个？**

> 线性回归是机器学习的"Hello World"。梯度下降是训练**所有**神经网络的核心算法。

> ChatGPT 的 1750 亿参数，也是用梯度下降（及其变体）训练的。你今天学的，和训练 GPT 用的是同一个思想。

核心知识点

**1. 什么是线性回归？**

最简单的机器学习模型。目标：找一条直线 y = wx + b，

让它尽可能"穿过"所有数据点。

数据：(x₁,y₁), (x₂,y₂), ..., (xₙ,yₙ)

预测值：ŷᵢ = wxᵢ + b

误差：ŷᵢ 和真实 yᵢ 的差距

> 💡 **Aha Moment**：机器学习不是什么魔法。它就是"猜参数 → 看差多少 → 调整参数 → 再猜"的循环。你把"调整参数"这个过程自动化了，这就是机器学习。

**2. 损失函数（Loss Function）—— 均方误差 MSE**

MSE = (1/n) × Σ(ŷᵢ - yᵢ)²

这个值越小，说明模型预测越准。我们的目标就是找到使 MSE 最小的 w 和 b。

> 📐 **用具体数字感受**：

> 假设真实值 y=10，你的模型预测 ŷ=8，误差=2，平方=4

> 如果预测 ŷ=12，误差=-2，平方还是 4

> MSE 不在乎你"偏高"还是"偏低"，只在乎"差多少"（平方消掉了正负号）

**3. 梯度下降（Gradient Descent）—— 怎么找到最好的 w 和 b？**

> 🏔️ **盲人下山的故事（核心类比，读三遍！）**

>

> 想象你蒙着眼睛站在一座山上。你的目标是走到山谷的最低点。

> 你唯一的工具：用脚感受脚下的坡度——哪里最陡，就往哪里走一小步。

>

> 步骤：

> 1. 站在原地，感受四面八方哪个方向下坡最陡（**计算梯度**）

> 2. 向那个方向迈一小步（**更新参数**）

> 3. 在新位置重新感受坡度（**下一轮迭代**）

> 4. 重复，直到感觉脚下是平的（**收敛到最低点**）

>

> 学习率（learning rate）就是你的"步长"：

> - 太小（lr=0.0001）：每一步只挪 1 毫米，走到天黑还没到谷底 → **收敛太慢**

> - 太大（lr=1.0）：一步跨出 10 米，可能从山的这一边跨到另一边，来回跳 → **震荡甚至发散**

> - 合适（lr=0.01）：稳步向下，高效到达 → **完美收敛**

>

> 这就是你选择学习率时在做的事——给"盲人"一个合适的步长。

数学上：

w_new = w_old - learning_rate × ∂MSE/∂w

b_new = b_old - learning_rate × ∂MSE/∂b

其中 ∂MSE/∂w 就是"坡度"（梯度），指示 MSE 在 w 方向的变化率。

> ⚠️ **常见陷阱**：很多人以为梯度下降保证找到"全局最低点"。不对！如果你的损失函数不是凸的（有很多坑），梯度下降可能卡在"局部最低点"。好在 MSE 是凸函数，所以线性回归不用担心这个问题。后面的神经网络就不是凸的了——那时你会看到 Adam 优化器如何用"动量"来跳出局部最优。

**4. 学习率（Learning Rate）的关键性**

太小：收敛极慢，梯度下降 10 万次还没到谷底

太大：一步跨过谷底，在谷两边来回震荡甚至发散

合适：高效到达谷底

经验值：0.01 起步，不行再调。

**MSE 对 w 和 b 的梯度（推导结果，记住即可）**

对于 y = wx + b，MSE = (1/n) Σ(wxᵢ + b - yᵢ)²

∂MSE/∂w = (2/n) × Σ (wxᵢ + b - yᵢ) × xᵢ

∂MSE/∂b = (2/n) × Σ (wxᵢ + b - yᵢ)

> 📝 **直观理解这两个公式**：

> - ∂MSE/∂w = 误差 × 输入 —— 如果输入 x 很大，w 的梯度也很大（因为 x 放大误差）

> - ∂MSE/∂b = 误差 —— b 的梯度就是平均误差本身

> ✅ **Self-Check**（离开手机前问自己）：

> 1. 如果 loss 曲线在下降但非常缓慢，你应该调大还是调小学习率？

> 2. 如果 loss 在剧烈震荡（忽上忽下），你应该调大还是调小学习率？

> （答案：1.调大 2.调小）

### 晚上电脑 · 2 小时

19:35-21:00  纯 NumPy 手写线性回归

> 🎯 今晚的目标：用纯 NumPy（不用任何 ML 库）手写梯度下降。你会看到 loss 从几百降到接近 0——这是你第一次"训练"一个模型。

建文件 linear_regression_scratch.py：

```python
if epoch % 100 == 0:


plt.tight_layout()

plt.savefig('linear_regression.png')

plt.show()
```

> 🧪 **实验时间**（必须做！这是理解的关键）：

>

> **实验 1：改变学习率**

> lr = 0.001（太小）→ loss 下降极慢，600 轮还没到底

> lr = 0.1（太大）→ loss 可能震荡甚至发散，loss 曲线像心电图

> lr = 0.01 → 刚好收敛，loss 光滑下降

>

> **实验 2：改变初始值**

> 不同的 w, b 初始值（比如 w=100, b=-50）→ 最终都收敛到 w≈3, b≈2（凸函数的性质）

> 这就是"无论从哪座山开始，只要沿着下坡走，都能到同一个谷底"

>

> **实验 3：增加噪声**

> 把 `np.random.randn(n,1)*2` 改成 `*10` → loss 最终值变高（因为数据本身更乱，模型再强也无法完美预测纯噪声）

>

> 🎉 **恭喜！** 你刚刚实现了训练 ChatGPT 的核心算法。ChatGPT 的训练循环和上面的代码**结构完全一样**——只是模型从 y = wx+b 变成了 1750 亿参数的 Transformer，loss 从 MSE 变成了交叉熵。

- [ ] 今日完成检查

- [ ] 手写梯度下降收敛成功，w ≈ 3.0, b ≈ 2.0

- [ ] 理解学习率如何影响收敛（做了 3 个实验）

- [ ] 能推导 MSE 对 w 和 b 的偏导数

- [ ] 能向朋友解释"盲人下山"类比

### 第8周 · 星期二：逻辑回归 —— 分类问题

---

### 手机摸鱼 · 上午 30 分钟

阅读主题：逻辑回归

> 🧠 **为什么学这个？**

> 线性回归输出的是任意实数（"房价是 250 万"），但很多问题需要输出"是/否"（"这封邮件是垃圾邮件吗？"）。逻辑回归 = 线性回归 + 一个"压缩函数"——把任意实数压到 0~1 之间，变成概率。

核心知识点

**1. 线性回归 → 分类问题的挑战**

线性回归输出任意实数。但分类问题需要输出概率（0~1）。

比如：预测一封邮件是垃圾邮件（1）还是正常（0）。

如果模型输出 2.7 或 -0.5，这没有意义。

> 💡 **Aha Moment**：逻辑回归不是什么"新模型"——它只是在线性回归 wx+b 外面包了一层 sigmoid。核心还是那条直线！理解这一点，你就理解了从回归到分类的桥梁。

**2. Sigmoid 函数 —— 把任意实数"压缩"到 (0,1)**

σ(z) = 1 / (1 + e^(-z))

z = 很大正数 → σ(z) ≈ 1

z = 0 → σ(z) = 0.5

z = 很大负数 → σ(z) ≈ 0

逻辑回归：ŷ = σ(wx + b)

> 📐 **用具体数字感受 sigmoid**：

> z = 5 → σ ≈ 0.993（模型非常确信是"正类"）

> z = 0 → σ = 0.500（模型完全不确定）

> z = -5 → σ ≈ 0.007（模型非常确信是"负类"）

>

> 注意 sigmoid 在 z=0 附近最"敏感"（输入变化引起输出大变化），在两端最"迟钝"——这就是后面要讲的**梯度消失**的根源。

**3. 损失函数 —— 交叉熵（Cross-Entropy）**

为什么不用 MSE？因为 sigmoid + MSE 会导致梯度消失问题（sigmoid 两端梯度≈0，MSE 的梯度也跟着≈0 → 学不动）。

交叉熵：

Loss = -[y×log(ŷ) + (1-y)×log(1-ŷ)]

- 当 y=1 时 Loss = -log(ŷ)：

预测 ŷ→1 → loss→0（对了，处罚小）

预测 ŷ→0 → loss→∞（错了，处罚巨大）

- 当 y=0 时 Loss = -log(1-ŷ)：

预测 ŷ→0 → loss→0（对了）

预测 ŷ→1 → loss→∞（错了）

> 🎯 **交叉熵的威力**：

> 如果真实标签是 y=1，而模型预测 ŷ=0.0001（极度错误），Loss = -log(0.0001) ≈ 9.2

> 如果真实标签是 y=1，而模型预测 ŷ=0.9999（几乎正确），Loss = -log(0.9999) ≈ 0.0001

> 差 92000 倍！交叉熵对"自信的错误"惩罚极其严厉——这正是我们想要的。

**4. 梯度推导结果（记住即可）**

∂Loss/∂w = (ŷ - y) × x     ← 注意！形式和线性回归的梯度一样！

∂Loss/∂b = (ŷ - y)

这就是交叉熵的优雅之处：梯度形式简洁，且和线性回归的梯度形式完全一致（都是 "预测 - 真实" 的形式）。不是巧合，是数学的精心设计。

> ⚠️ **常见陷阱**：很多人以为逻辑回归只能做二分类。用 softmax（下周学）+ 多类别交叉熵，它可以推广到多分类，那就是多分类逻辑回归——也叫 softmax 回归。

> ✅ **Self-Check**：

> 1. 为什么逻辑回归不用 MSE 作为损失函数？

> 2. sigmoid(0) = ?  sigmoid(-100) ≈ ?  sigmoid(100) ≈ ?

### 晚上电脑 · 2 小时

19:35-21:00  手写逻辑回归

```python

for epoch in range(1000):


w -= lr * dw

b -= lr * db

if epoch % 200 == 0:


```

> 🧪 **实验时间**：

> **实验 1：决策边界可视化**

> 把 `w[0]*x₁ + w[1]*x₂ + b = 0` 这条线画在散点图上——你会看到它完美地把两类数据分开。

>

> **实验 2：观察 sigmoid 的"自信度"**

> 打印几个样本的 y_pred 值：靠近决策边界的点，y_pred ≈ 0.5（不确定）；远离边界的点，y_pred ≈ 0 或 1（非常确定）。

> 🎉 **恭喜！** 你现在可以回答面试题了："逻辑回归和线性回归有什么区别？"——线性回归输出实数，逻辑回归在线性回归外面包了 sigmoid，输出概率。梯度形式完全一样，但损失函数从 MSE 换成了交叉熵。

- [ ] 今日完成检查

- [ ] 理解 sigmoid 的作用（把任意实数压缩到 0~1）

- [ ] 交叉熵公式能写出来

- [ ] 手写逻辑回归收敛成功（准确率 > 95%）

- [ ] 能解释为什么交叉熵 + sigmoid 比 MSE + sigmoid 好

### 第8周 · 星期三、四：决策树 + 随机森林

---

### 手机摸鱼 · 星期三上午

阅读主题：决策树

> 🧠 **为什么学这个？**

> 不是所有问题都适合用直线来分割。决策树可以学习复杂的非线性决策边界，而且**可解释**——你能看到模型做决策的每一步。在银行风控、医疗诊断等场景，可解释性比准确率更重要。

核心知识点

决策树的思路很简单——像玩"20个问题"：

根节点：这个动物的体重 > 10kg？

→ 是：这个动物会飞吗？

→ 是：可能是老鹰

→ 否：这个动物是哺乳动物吗？

→ ...

→ 否：这个动物有翅膀吗？

→ ...

关键概念：

- 信息熵：衡量数据"混乱程度"，熵越高越乱

H = -Σ pᵢ × log₂(pᵢ)

> 📐 **用数字理解熵**：

> 10 个样本，5 个猫 5 个狗 → p₁=0.5, p₂=0.5 → H = -(0.5×log₂0.5 + 0.5×log₂0.5) = -(0.5×(-1) + 0.5×(-1)) = 1.0（完全混乱）

> 10 个样本，10 个猫 → p₁=1.0 → H = -(1.0×0) = 0（完全纯净）

> 熵从 0（纯净）到 1（最混乱）。

- 信息增益：分裂前后的熵减少量，减少越多越好

IG = H(父) - Σ (|子|/|父|) × H(子)

每次分裂选择信息增益最大的特征。

> 💡 **Aha Moment**：决策树不是在"学"一个公式——它是在"问问题"。每个节点是一个 if-else 判断，整棵树就是一堆嵌套的 if-else。你完全可以把它翻译成 Python 代码：`if feature_1 > 3.5: if feature_2 < 1.2: return "猫" else: return "狗"`

> ⚠️ **常见陷阱**：如果不限制深度，决策树会把每个训练样本都"记住"——每个叶子节点一个样本 → 训练准确率 100%，测试准确率惨不忍睹。这就是过拟合。解决方案：限制 max_depth、min_samples_split，或者用随机森林。

### 手机摸鱼 · 星期四上午

阅读主题：随机森林

> 🧠 **为什么学这个？**

> 单棵决策树容易过拟合。随机森林 = 种 100 棵树，每棵看到的风景不同（不同数据 + 不同特征），然后投票。Kaggle 比赛里，随机森林 + XGBoost 至今仍是表格数据的王者。

- 随机森林 = 多棵决策树的"投票"

- 两重随机性：

① Bootstrap（有放回抽样）→ 每棵树看到的数据不同

② 随机选特征 → 每次分裂只在部分特征中选最优

- 为什么有效？每棵树"偏见"不同，投票结果抵消了过拟合

> 🗳️ **投票类比**：让 100 个人各自凭一小部分线索猜答案，然后少数服从多数——比让一个人看全部线索猜得更准。因为个人偏见被群体的多样性抵消了。

> ✅ **Self-Check**（星期四中午前）：

> 1. 随机森林的"两重随机性"是什么？

> 2. 为什么随机森林比单棵决策树不容易过拟合？

### 电脑 · 星期三+星期四晚上

用 sklearn 实战：

```python
# 加载数据集

from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(

data.data, data.target, test_size=0.2, random_state=42

)

# 决策树

dt = DecisionTreeClassifier(max_depth=5, random_state=42)

dt.fit(X_train, y_train)

print("决策树准确率:", dt.score(X_test, y_test))

# 随机森林

rf = RandomForestClassifier(n_estimators=100, random_state=42)

rf.fit(X_train, y_train)

print("随机森林准确率:", rf.score(X_test, y_test))

# 交叉验证（更可靠评估）

scores = cross_val_score(rf, data.data, data.target, cv=5)

print(f"5 折交叉验证: {scores.mean():.4f} ± {scores.std():.4f}")

# 特征重要性

for name, importance in zip(data.feature_names, rf.feature_importances_):

if importance > 0.03:


```

- [ ] 今日完成检查

- [ ] 决策树和随机森林代码跑通

- [ ] 能解释信息熵和信息增益

- [ ] 理解 Bootstrap 的作用

### 第8周 · 星期五 + 星期六：评估指标 + 完整 ML Pipeline

---

### 手机摸鱼 · 星期五

阅读主题：模型评估指标

> 🧠 **为什么学这个？**

> "准确率 99%"听起来很好？但如果 100 个人里只有 1 个人生病，模型说"所有人健康"——准确率 99%，但漏掉了唯一那个病人。**评估指标是 ML 的"良心"**，选错指标会导致灾难性后果。

核心知识点

**混淆矩阵：**

                 预测正    预测负

| 实际正 |   TP    |   FN    |

| 实际负 |   FP    |   TN    |

> 🏥 **癌症检测的教训**：

> 1000 人中，10 人患病。

> 模型说"全部没病" → TP=0, FN=10, FP=0, TN=990

> 准确率 = (0+990)/1000 = 99% ← 看起来很漂亮！

> 召回率 = 0/(0+10) = 0% ← 但实际上一个病人都没找到！

>

> **这就是为什么不均衡数据集不能用准确率。**

准确率 = (TP+TN) / 总数  —— 样本不均衡时不可靠

精确率 = TP / (TP+FP)    —— 预测为正的有多少是真正

召回率 = TP / (TP+FN)    —— 真正为正的有多少被找出

F1 = 2×P×R / (P+R)       —— 精确率和召回率的调和平均

> 💡 **Aha Moment**：精确率和召回率是**鱼与熊掌**——调高阈值可以提高精确率但降低召回率，降低阈值则相反。F1 是它们的调和平均，帮你找一个平衡点。

> 🎯 **业务场景决定指标选择**：

> - 癌症检测 → 宁可误报，不能漏报 → 追求高**召回**

> - 垃圾邮件过滤 → 宁可漏过，不能误杀 → 追求高**精确率**

> - 推荐系统 → 关心 Top-K 的准确性 → 用 Precision@K

所以评估模型要看业务场景：

- 癌症检测 → 宁可误报，不能漏报 → 追求高召回

- 垃圾邮件过滤 → 宁可漏过，不能误杀 → 追求高精确率

> ✅ **Self-Check**：

> 1. "所有预测为正" → 召回率 = ?  精确率 = ?（取决于真实正样本比例）

> 2. 机场安检（找危险品）该追求精确率还是召回率？

### 星期六 · 3.5h

完整 ML Pipeline

```python
# 1 个完整 Pipeline

pipeline = Pipeline([


# 自动调参

param_grid = {

'classifier__n_estimators': [50, 100, 200],

'classifier__max_depth': [None, 10, 20],

}

grid = GridSearchCV(pipeline, param_grid, cv=5, scoring='f1')

grid.fit(X_train, y_train)

print(f"最佳参数: {grid.best_params_}")

print(f"最佳分数: {grid.best_score_:.4f}")

print(f"测试集分数: {grid.score(X_test, y_test):.4f}")
```

> 🏆 **Pipeline 的价值**：把"数据预处理 → 模型训练 → 评估"串成一条流水线。这样你不会在测试集上不小心用到训练集的统计信息（数据泄露），这是 ML 项目中最容易犯的错误之一。

可选：在 Kaggle 提交 Titanic 或 House Prices 比赛。

> 🎉 **第 8 周完成！** 你从手写梯度下降开始，到用 sklearn Pipeline 做完整 ML 项目。这些基础会在 PyTorch 周里反复用到——每当你调用 `loss.backward()`，你心里知道它在做你手写过的梯度计算。

- [ ] 第8周完成检查

- [ ] 线性回归/逻辑回归手写梯度下降 OK

- [ ] 决策树/随机森林 sklearn 实战 OK

- [ ] 懂精确率、召回率、F1、ROC/AUC，能讲出"癌症检测"的例子

- [ ] ML Pipeline 完整跑通

### 第9周 · 主题：机器学习深入 + 特征工程

-  本周目标：补齐 ML 最后一个缺口──

> 无监督学习（K-Means）、正则化（L1/L2）、特征工程、过拟合诊断。本周结束后，你将拥有一个完整的 ML 工具箱。

### 第9周 · 星期一：K-Means 聚类（无监督学习）

---

### 手机摸鱼 · 上午 30 分钟

核心知识点

> 🧠 **为什么学这个？**

> 前面的算法都需要标签（y 值）。但现实中大量数据没有标签——用户行为日志、图片、文本。K-Means 能在没有任何标签的情况下，自动发现数据中的"群组"。这就是**无监督学习**。

**1. 有监督 vs 无监督**

有监督：数据有标签 → 线性回归、逻辑回归、决策树

无监督：数据没有标签 → 聚类、降维

**2. K-Means 算法步骤**

① 随机选 K 个点作为"聚类中心"

② 把每个数据点分配给最近的中心

③ 重新计算每个簇的中心（取均值）

④ 重复 ②③ 直到中心不再变化

> 🚩 **抢地盘游戏类比**：

> K 个人（聚类中心）站在操场不同位置。所有人都向最近的队长靠拢→队长移到自己的队员的正中间→队员重新找最近的队长→... 直到队伍稳定。

> 💡 **Aha Moment**：K-Means 不需要任何标签！它只靠数据点之间的距离来分组。这就是无监督学习的魅力——你不需要人工标注，算法自己从数据中发现结构。

**3. 选择 K 值：肘部法则**

画 K 值 vs 簇内误差平方和（inertia）的曲线，

找到"拐点"（误差下降变缓的地方）就是最佳 K。

> 📐 **肘部法则的直觉**：K 越大，每个簇越紧，inertia 越小。但 K 从 1 到 2 的改进远大于 K 从 9 到 10。那条曲线像人的手臂——"肘部"就是最佳 K。

> ⚠️ **常见陷阱**：K-Means 对初始中心位置敏感（可能收敛到不同的局部最优）。解决办法：跑多次取最好结果（sklearn 的 `n_init` 参数），或用 K-Means++ 初始化。另外，K-Means 假设簇是"球形"的——如果数据是月牙形，它会分错。

> ✅ **Self-Check**：如果数据是 3 个明显的簇，但你设 K=5，会发生什么？两个簇各被"切开"。

### 晚上电脑 · 2 小时

```python
# 生成聚类数据

X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=42)

# ===== 手写 K-Means =====

class MyKMeans:


for _ in range(self.max_iters):


self.labels_ = labels

return self

# 测试

kmeans = MyKMeans(n_clusters=4)

kmeans.fit(X)

print(f"聚类中心:\n{kmeans.centroids}")

# 肘部法则：找最佳 K

inertias = []

for k in range(1, 9):

km = MyKMeans(n_clusters=k)

km.fit(X)

inertias.append(np.sum((X - km.centroids[km.labels_])**2))

plt.plot(range(1, 9), inertias, 'bo-')

plt.xlabel('K'); plt.ylabel('Inertia')

plt.savefig('elbow_method.png')
```

> 🎉 手写 K-Means 完成！你实现了一个被 Spotify 用来分组用户音乐品味、被电商用来做用户分群的算法。

### 第9周 · 星期二：L1 vs L2 正则化

---

### 手机摸鱼

核心知识点

> 🧠 **为什么学这个？**

> 模型过拟合 = 模型记住了训练数据的噪声。正则化 = 给模型戴个"紧箍咒"——你拟合数据可以，但不能让参数太大。L1 和 L2 是两种不同的"紧箍咒"，面试几乎必问。

**1. 过拟合的根源：模型记住了训练数据的噪声**

训练集 loss 很低，测试集 loss 很高 → 过拟合

**2. L2 正则化（Ridge / 权重衰减）**

Loss_total = Loss_original + λ × Σ(w²)

效果：所有参数被"压缩"但不归零。

> 🎈 **气球类比**：

> 不加正则化：模型像充满了气的气球，每个褶皱都想贴合（fit 噪声）

> L2 正则化：给气球放一点气，它还是圆的，但没那么"贴"了——泛化更好

几何直觉：损失函数的等高线被一个"圆"约束，

最优解在切点上，参数更小但都非零。

**3. L1 正则化（Lasso）**

Loss_total = Loss_original + λ × Σ(|w|)

效果：不重要的参数直接变成 0 → 自动特征选择！

> 💎 **菱形 vs 圆的直觉（面试黄金回答）**：

> L2 的约束区域是一个"圆"，等高线碰到圆上，参数都不为 0

> L1 的约束区域是一个"菱形"（有尖角！），等高线更容易碰到角上——角上某些参数恰好是 0

> → L1 产生稀疏解，自动把不重要的特征"掐死"

几何直觉：约束是一个"菱形"，等高线更容易碰到角点，

角点上某些参数正好为 0。

**面试考点：L1 vs L2**

L2：所有参数缩小但不归零，适合"所有特征都有贡献"的场景

L1：产生稀疏解，自动选特征，适合"只有少数特征是重要的"场景

> 💡 **Aha Moment**：L1 和 L2 不仅是正则化技术，它们背后是两种"世界观"——L2 认为"一切都有贡献，只是程度不同"，L1 认为"少数重要，多数可以忽略"。选择哪个，取决于你对数据的假设。

> ⚠️ **常见陷阱**：不要把 L1/L2 正则化和数据标准化搞混！正则化是对**权重**加惩罚，标准化是对**输入数据**做变换。两者解决不同的问题，但经常配合使用。

> ✅ **Self-Check**：

> 1. 如果 λ=0，正则化效果是什么？（没有正则化）

> 2. 如果 λ 非常大，会发生什么？（所有参数被压到接近 0，模型退化成常数值）

### 晚上电脑

```python
# 生成带噪声的高阶多项式数据（容易过拟合的场景）

np.random.seed(42)

n = 30

X = np.linspace(0, 1, n).reshape(-1, 1)

y = np.sin(2 * np.pi * X).ravel() + np.random.randn(n) * 0.3

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 对比 3 种模型

for name, model in [

("无正则化", LinearRegression()),

("L2 (Ridge, α=0.1)", Ridge(alpha=0.1)),

("L1 (Lasso, α=0.01)", Lasso(alpha=0.01, max_iter=5000)),

]:

pipe = make_pipeline(PolynomialFeatures(degree=15), StandardScaler(), model)

pipe.fit(X_train, y_train)

train_r2 = pipe.score(X_train, y_train)

test_r2 = pipe.score(X_test, y_test)


```

> 🧪 观察 Lasso 的系数：大部分变成了精确的 0！这就是 L1 的"特征选择"魔力。

### 第9周 · 星期三：特征工程

---

### 手机摸鱼

核心知识点

> 🧠 **为什么学这个？**

> 业界名言："数据和特征决定了机器学习的上限，而模型和算法只是逼近这个上限。" 垃圾数据 + 顶级模型 < 好特征 + 简单模型。特征工程是 ML 中最被低估的技能。

**1. 数值特征处理**

标准化（StandardScaler）：(x-μ)/σ → 均值 0 方差 1

归一化（MinMaxScaler）：(x-min)/(max-min) → 缩放到 [0,1]

选哪个？梯度下降类模型用标准化，距离类模型（KNN/K-Means）用归一化

> 💡 **Aha Moment**：为什么要标准化？想象你有两个特征——"年龄"（0-100）和"收入"（5000-500000）。没标准化时，模型会认为"收入"比"年龄"重要 5000 倍，因为它的数值大。标准化后每个特征都在同一量纲上，模型才能公平对待它们。

**2. 类别特征处理**

独热编码（One-Hot）：颜色=[红,蓝,绿] → 红=[1,0,0], 蓝=[0,1,0]

标签编码（Label）：红=0, 蓝=1, 绿=2

选哪个？无序类别用 One-Hot，有序类别（低中高）用 Label

> ⚠️ **常见陷阱**：如果你把无序类别（如"城市"）用 Label 编码成 0,1,2,3，模型会认为"北京=0, 上海=1"之间有大小关系，实际上没有。这会导致模型学到虚假的模式。

**3. 文本特征处理**

TF-IDF：词频 × 逆文档频率

核心思想：一个词在本文档中出现多(TF高)但在其他文档出现少(IDF高)，

这个词对本文档很重要。

### 晚上电脑

```python
# 模拟混合类型数据

df = pd.DataFrame({

'age': [25, 30, 22, 45, 33],

'income': [5000, 8000, 3000, 15000, 9000],

'city': ['北京', '上海', '北京', '深圳', '上海'],


# 数值列 → 标准化；无序类别列 → OneHot；有序类别 → Ordinal

from sklearn.preprocessing import OrdinalEncoder

preprocessor = ColumnTransformer([

('num', StandardScaler(), ['age', 'income']),

('cat_onehot', OneHotEncoder(sparse_output=False), ['city']),

('cat_ordinal', OrdinalEncoder(categories=[['初级','中级','高级','资深']]), ['level']),

])

X_processed = preprocessor.fit_transform(df)

print(f"处理后形状: {X_processed.shape}")

print(f"One-Hot 后的城市列: {preprocessor.named_transformers_['cat_onehot'].get_feature_names_out()}")
```

### 第9周 · 星期四：过拟合诊断 + 学习曲线

---

### 手机摸鱼

核心知识点

> 🧠 **为什么学这个？**

> 训练模型是容易的。判断模型是"不够聪明"还是"过于死记硬背"才是真正的技能。学习曲线是你诊断模型健康状况的"心电图"。

**诊断三种状态：**

> 📊 **学习曲线速查表**：

>

> 状态           | 训练 loss | 测试 loss | 两条曲线之间

> ───────────────┼──────────┼──────────┼────────────

> 欠拟合         | 高       | 高       | 很接近（gap 小）

> 过拟合         | 低       | 高       | 距离很远（gap 大）

> 刚好           | 低       | 低       | 合理接近

欠拟合（Underfitting）：训练 loss 高 + 测试 loss 高

→ 模型太简单 / 特征不够 / 训练不充分

→ 解决：增加模型复杂度、增加特征、多训几轮

过拟合（Overfitting）：训练 loss 低 + 测试 loss 高

→ 模型记住了训练数据的噪声

→ 解决：正则化、Dropout、数据增强、早停、减少参数

刚好（Good Fit）：训练 loss 低 + 测试 loss 低

→ 完美状态！

> 💡 **Aha Moment**：学习曲线不仅告诉你"是否"过拟合，还告诉你"加数据有没有用"。如果两条线之间的 gap 在缩小（随着数据增加），说明"加更多数据"是有效的。如果 gap 不缩小，说明问题在别处（如模型太简单/特征不够）。

学习曲线：横轴=训练样本数，纵轴=loss

过拟合时：训练 loss 很低（一条平线），测试 loss 很高且不降

欠拟合时：训练和测试 loss 都很高，且几乎持平

### 晚上电脑

```python

def plot_learning_curve(model, X, y, title):

train_sizes, train_scores, test_scores = learning_curve(

model, X, y, cv=5, train_sizes=np.linspace(0.1, 1.0, 10),

scoring='neg_mean_squared_error'

)

train_mean = -train_scores.mean(axis=1)

test_mean = -test_scores.mean(axis=1)

plt.plot(train_sizes, train_mean, 'o-', label='训练')

plt.plot(train_sizes, test_mean, 'o-', label='测试')

plt.xlabel('训练样本数'); plt.ylabel('MSE')

plt.title(title); plt.legend(); plt.grid()

plt.savefig(f'{title}.png'); plt.close()

# 过拟合模型（高阶多项式，无正则化）

overfit_model = make_pipeline(PolynomialFeatures(15), LinearRegression())

plot_learning_curve(overfit_model, X, y, '严重过拟合')

# 正则化后

regularized_model = make_pipeline(PolynomialFeatures(15), Ridge(alpha=0.1))

plot_learning_curve(regularized_model, X, y, 'L2正则化后')
```

- [ ] 今日完成检查

- [ ] 能画出学习曲线并判断过拟合/欠拟合

- [ ] 知道三种状态分别怎么解决

### 第9周 · 星期五-六：Kaggle 实战

---

### 星期五

复习周一到周四所有代码，确保每段都能理解运行。

手机：回顾混淆矩阵→精确率/召回率→ROC/AUC 的关系（阶段 8 周学过）

### 星期六 · 3.5h

14:00-17:00 Kaggle 提交：House Prices 或 Titanic

> 🏆 **Kaggle 是什么**：全球最大的数据科学竞赛平台。你今天提交的预测，会得到一个排名——这是你第一个"真实世界"的 ML 成果。

1. 加载数据 → 探索分析（df.describe(), 缺失值统计, 相关性热力图）

2. 特征工程（填充缺失、独热编码、标准化、创建新特征）

3. 训练多模型对比（Linear/Ridge/Lasso/RandomForest/XGBoost）

4. 交叉验证评估 → 选最佳模型 → 生成提交文件

5. 上传 Kaggle，看排名

> 💡 **一个新视角**：从今天开始，你看 Kaggle 排行榜不再只是看"数字"——你懂了你提交的文件是怎么生成的、Pipeline 是怎么串起来的、分数是怎么评估的。你已经是一个"内行"了。

17:00-17:30 整理本周所有代码到 GitHub，更新 Obsidian 笔记

> 🎉 **第 9 周完成！** 你完成了 ML 基础的全部内容——从手写梯度下降到 Kaggle 竞赛提交。这些知识会让你后面学习 PyTorch 和深度学习时事半功倍。每个 `loss.backward()` 和 `optimizer.step()`，你现在都知道它们在做什么。

- [ ] 第9周完成检查

- [ ] K-Means 手写实现 + 肘部法则

- [ ] L1 vs L2 对比实验完成，区别能说清楚（包括"菱形 vs 圆"的几何直觉）

- [ ] 特征工程（标准化/OneHot/TF-IDF）流程熟练

- [ ] 能画学习曲线并诊断过拟合

- [ ] Kaggle 成功提交

### 第10周 · 主题：PyTorch 基础（Tensor → Autograd → nn.Module）

说明：本周开始切换到 PyTorch。前面两周的 ML 基础会让你

理解 PyTorch 底层在做什么，而不是只会"调包"。

> 🎉 **PyTorch 来了！** 这是整个学习计划最重要的工具。Transformer、LLM、Agent——后面所有的代码都用 PyTorch 写。好消息是：你前面两周的 ML 基础，让你不是从零开始——你只是换了一个"计算器"（从 NumPy 手动算梯度 → PyTorch 自动算）。

-  本周目标 ──

1. Tensor 操作形成肌肉记忆（像 NumPy 一样熟练）

2. 理解 Autograd（自动求导）的原理

3. 掌握 nn.Module 和训练循环

### 第10周 · 星期一：Tensor 操作（从 NumPy 平滑过渡）

---

### 手机摸鱼 · 上午 30 分钟

阅读主题：PyTorch Tensor —— GPU 上的 NumPy

> 🧠 **为什么学这个？**

> PyTorch 是深度学习界的"通用语言"。Tensor 就是 PyTorch 版本的 numpy array，但它能跑在 GPU 上，能自动追踪梯度。你在 NumPy 上的所有技能都不会白费——99% 的操作都是一样的。

核心知识点

**1. NumPy → PyTorch 对照表（存下来当备忘录！）**

NumPy                    PyTorch

np.array([1,2,3])       torch.tensor([1,2,3])

np.zeros((3,4))         torch.zeros(3,4)

np.ones((2,3))          torch.ones(2,3)

np.arange(10)           torch.arange(10)

np.random.randn(3,4)    torch.randn(3,4)

arr.shape               tensor.shape

arr.reshape(2,6)        tensor.reshape(2,6) 或 tensor.view(2,6)

arr.T                   tensor.T

arr @ mat               tensor @ mat

arr.sum()               tensor.sum()

| arr.mean(axis=0) | tensor.mean(dim=0) | ← **注意：axis→dim** |

> 💡 **Aha Moment**：如果你会用 NumPy，你已经会了 PyTorch 的 80%。唯一的两个大区别：(1) `axis` 改名成了 `dim`，(2) Tensor 可以搬到 GPU 上。就这么简单。

**2. 关键区别**

- PyTorch Tensor 可以跑在 GPU 上：


- view vs reshape：

view 要求内存连续（更高效但可能失败）

reshape 不要求（更安全，推荐先多用 reshape）

- requires_grad：

设置后 PyTorch 追踪对该 Tensor 的所有操作，

从而自动计算梯度。

**3. Tensor 的 device（设备）管理**


> ⚠️ **常见陷阱**：Tensor 在 CPU 上，模型在 GPU 上 → 报错。所有参与计算的 tensor 必须在同一个 device 上。养成习惯：模型和数据一创建就 `.to(device)`。

> ✅ **Self-Check**：np.mean(arr, axis=1) 等价于 torch.mean(tensor, ___)？

### 晚上电脑 · 2 小时

建文件 pytorch_tensor_workout.py，和 NumPy 练习对照做：

```python
# ----- 创建 -----

t1 = torch.tensor([1, 2, 3, 4])

t2 = torch.zeros(3, 4)

t3 = torch.ones(2, 3)

t4 = torch.eye(4)          # 单位矩阵

t5 = torch.arange(0, 10, 2)

t6 = torch.linspace(0, 1, 5)

t7 = torch.randn(3, 4)     # 正态分布

t8 = torch.randint(0, 10, (3, 4))  # 整数随机

print("设备:", t1.device)

print("GPU可用:", torch.cuda.is_available())

# ----- 属性 -----

print(t7.shape, t7.dtype, t7.device, t7.numel())

# ----- 索引（和 NumPy 一样）-----

print("第一行:", t7[0])

print("第二列:", t7[:, 1])

print("大于0的元素:", t7[t7 > 0])

# ----- 变形 -----

print(t7.reshape(2, 6).shape)

print(t7.view(2, -1).shape)    # -1 表示自动推断

# ----- 数学运算 -----

a = torch.randn(3, 4)

b = torch.randn(3, 4)

print("a+b:", (a + b).shape)

print("a@b.T:", (a @ b.T).shape)  # 矩阵乘法

# ----- 沿维度操作 -----

print("每行max:", a.max(dim=1))    # 返回 (values, indices)

print("每列mean:", a.mean(dim=0))

# ----- GPU -----

if torch.cuda.is_available():

a_gpu = a.to('cuda')


```

重要：把上面的每一个操作都亲手敲一遍，

形成肌肉记忆。不要复制粘贴！

> 🎯 额外挑战：把你在阶段一的 NumPy 练习用 PyTorch 重写一遍。你会发现几乎不需要动脑筋——Tensor 就是 GPU 上的 ndarray。

- [ ] 今日完成检查

- [ ] 能熟练创建/索引/变形 PyTorch Tensor

- [ ] 理解 dim 参数（和 NumPy 的 axis 一样）

- [ ] GPU 移动操作成功

### 第10周 · 星期二：Autograd —— PyTorch 的灵魂

---

### 手机摸鱼 · 上午 30 分钟

阅读主题：自动求导（Autograd）

> 🧠 **为什么学这个？**

> Autograd 是 PyTorch 最核心的功能，也是你从"NumPy 用户"变成"深度学习工程师"的分水岭。如果没有 Autograd，训练一个 Transformer 需要手动推导几百层的梯度——这几乎是不可能的任务。

**1. 痛点：手算梯度太痛苦**

第 8 周手写梯度下降时，你需要手动推导：

∂MSE/∂w = (2/n) × Σ(...)

∂MSE/∂b = (2/n) × Σ(...)

对于简单的线性回归还好，但对于 Transformer：

- 几十个矩阵乘法

- Softmax、LayerNorm、Dropout

- 每层的梯度公式都不一样

手动推导几乎不可能不出错。

> 🎢 **从手算到自动的飞跃**（对比一下你就懂了）：

>

> 线性回归手动梯度：2 行代码，2 个公式，推导耗时 5 分钟

> 2 层 MLP 手动梯度：10 行代码，链式法则 3 步，推导耗时 30 分钟

> Transformer 手动梯度：数千行代码，几十层链式法则，推导耗时... 不可能

>

> Autograd 把"不可能"变成了"2 行代码（loss.backward()）"。

**2. PyTorch Autograd 的解决方案**

你只需要写"前向传播"代码，PyTorch 自动计算所有梯度。

原理：计算图（Computational Graph）。

你写：z = x * y + w

PyTorch 自动构建：

x ──┐

├── (*) ── temp ──┐

y ──┘                 ├── (+) ── z

w ────────────────────┘

然后 backprop 时自动沿着计算图的方向反推梯度。

这叫"动态计算图"——图在执行时动态构建，灵活高效。

> 💡 **Aha Moment**：Autograd 不是黑魔法。它在每次运算时，偷偷记录了"这个操作是怎么做的"和"梯度怎么反向传"。当你调用 `.backward()` 时，它沿着记录反向走一遍，自动用链式法则算出所有梯度。本质上就是你在第 8 周手写的梯度推导——只不过 PyTorch 替你做了。

**3. requires_grad 和 backward()**


训练时：


> 🧠 **训练循环的 5 步心法（背下来，变成肌肉记忆！）**

>

> 这就是后面所有模型训练的核心。不管你训练的是 MLP 还是 GPT-4：

>

> **① zero_grad()** — 清空上一轮的梯度残渣（不然会累加！）

> **② forward** — 输入经过模型，得到预测和 loss

> **③ loss.backward()** — 自动计算所有参数的梯度

> **④ optimizer.step()** — 用梯度更新参数

> **⑤（评估时额外）** — `with torch.no_grad():` 关掉梯度追踪

>

> 这 5 步构成了所有深度学习训练的"呼吸节奏"。刻进你的手指记忆。

**4. 两个关键陷阱**

① 忘记 zero_grad() → 梯度会累加（PyTorch 的默认行为）

② 不想要梯度时没加 torch.no_grad() → 内存泄漏

> ⚠️ **梯度累加陷阱（重点！）**：

> PyTorch 默认**累加**梯度而不是覆盖。这是设计 feature（有些场景需要累积多步再更新），但对新手是个坑。

> ```python

> # 错误！

> for i in range(3):

>     loss = model(x)  # 算 loss

>     loss.backward()  # 梯度累加到 .grad 上！

>     optimizer.step() # 用累加的梯度更新 → 效果 = lr × 3

> ```

> 正确做法：每次 step 前先 `optimizer.zero_grad()`。

> ✅ **Self-Check**：

> 1. `.backward()` 之后，梯度存在哪里？（存在 `.grad` 属性里）

> 2. 如果连续两次 `.backward()` 不 `zero_grad()`，x.grad 会怎样？（是两次梯度的和）

### 晚上电脑 · 2 小时

任务 1：验证 Autograd 的梯度计算是否正确

```python
# 用第8周的线性回归验证

n = 100

X = torch.linspace(0, 10, n).reshape(-1, 1)

true_w, true_b = 3.0, 2.0

y = true_w * X + true_b + torch.randn(n, 1) * 2

# 需要计算梯度的参数

w = torch.randn(1, requires_grad=True)

b = torch.randn(1, requires_grad=True)

lr = 0.01

for epoch in range(500):


if epoch % 100 == 0:


print(f"学习参数: w={w.item():.4f}, b={b.item():.4f}")
```

任务 2：验证"梯度累加"现象


任务 3：理解 no_grad() 的作用

```python
# 带梯度追踪

with torch.no_grad():


```

> 🎉 你现在知道了 PyTorch 最核心的秘密：`requires_grad` 标记哪些需要追踪，`.backward()` 自动算梯度，`.zero_grad()` 清零。这三件套贯穿你后面所有代码。

- [ ] 今日完成检查

- [ ] 理解 requires_grad、backward()、zero_grad() 三件套

- [ ] 能解释"梯度累加"现象（不 zero_grad 会怎样）

- [ ] Autograd 版线性回归收敛成功（w≈3.0, b≈2.0）

### 第10周 · 星期三：nn.Module + 自定义网络

---

### 手机摸鱼 · 上午 30 分钟

阅读主题：nn.Module —— PyTorch 的"积木"

> 🧠 **为什么学这个？**

> `nn.Module` 是 PyTorch 里所有神经网络层的基类。掌握它 = 掌握 PyTorch 的"乐高积木系统"。每一个你写的模型、你用的预训练模型（BERT、GPT）都是一个 `nn.Module`。

核心知识点

**1. nn.Module 是什么？**

所有神经网络层的基类。你的模型继承它后，自动获得：

- parameters()：列出所有可训练参数

- forward()：子类必须实现，定义前向计算

- to(device)：一键移动所有参数到 GPU

- train() / eval()：切换训练/评估模式（影响 Dropout/BN）

**2. 最简单的自定义 Module**

```python

class SimpleMLP(nn.Module):


```

> 💡 **Aha Moment**：`nn.Module` 的设计哲学：`__init__` 定义"有什么层"，`forward` 定义"怎么连起来"。后面所有复杂的模型——CNN、RNN、Transformer——都遵循这个模式。层变复杂了，但结构不变。

**3. 常用层速查**

nn.Linear(in, out)       全连接层：y = xW^T + b

nn.Conv2d(in, out, k)    2D卷积

nn.ReLU()                激活函数

nn.Dropout(p)            Dropout 正则化

nn.BatchNorm1d(d)        批归一化

nn.LayerNorm(d)          层归一化（Transformer 里用）

nn.Embedding(vocab, dim) 词嵌入

nn.LSTM(in, hidden)      LSTM

nn.TransformerEncoder    完整的 Transformer Encoder

**4. Sequential —— 简单的层叠**


> ⚠️ **常见陷阱**：`__init__` 里忘记 `super().__init__()` 是新手排名第一的错误！没有这行，你的 Module 不会注册参数，`model.parameters()` 返回空列表。

> ✅ **Self-Check**：

> 1. `model.train()` 和 `model.eval()` 影响哪些层的行为？（Dropout 和 BatchNorm）

> 2. `model.to('cuda')` 移动了什么？（所有参数和 buffer）

### 晚上电脑 · 2 小时

任务 1：用 nn.Module 重写线性回归 + 逻辑回归

```python

class LogisticRegressor(nn.Module):


```

任务 2：手写一个和 PyTorch 内置功能等价的模块

```python
# 测试：和官方 nn.Linear 对比

official = nn.Linear(10, 5)

my = MyLinear(10, 5)

x = torch.randn(3, 10)

# 如果参数相同，输出应该相同

my.weight.data = official.weight.data.clone()

my.bias.data = official.bias.data.clone()

print("官方输出:", official(x))

print("我的输出:", my(x))
```

> 🎉 你现在不仅会用 PyTorch，还能手写它内部的实现！面试问到 "nn.Linear 内部做什么"，你直接把 MyLinear 的代码写出来就行了。

- [ ] 今日完成检查

- [ ] 理解 nn.Module 的生命周期（__init__ + forward）

- [ ] 能自定义 Module

- [ ] 手写 MyLinear 和官方输出一致

### 第10周 · 星期四：DataLoader + 完整训练循环

---

### 手机摸鱼 · 上午 30 分钟

阅读主题：DataLoader —— 高效的数据加载

> 🧠 **为什么学这个？**

> 真实数据不可能一次全加载进内存（想象一下训练数据有 1TB）。DataLoader 让你批量加载、自动打乱、多线程预处理——这是工业级训练的标配。

核心知识点

**1. Dataset 和 DataLoader 的分工**

Dataset：负责读取 1 条数据（返回 (x, y)）

DataLoader：负责批量打包、打乱、多线程加载

```python

dataset = MyDataset(X, y)

loader = DataLoader(dataset, batch_size=32, shuffle=True)

for batch_x, batch_y in loader:


```

> 💡 **Aha Moment**：Dataset 告诉你"一条数据长什么样"，DataLoader 帮你"批量取、打乱、多线程取"。两者各司其职。你只需要写 Dataset，DataLoader 自动帮你搞定剩下的。

**2. 完整训练循环（模板，背下来！）**

```python

total_loss += loss.item()

return total_loss / len(loader)

def evaluate(model, loader, loss_fn, device):

model.eval()

total_loss = 0

correct = 0


```

> 🎯 **训练模板的 5 行核心代码**（肌肉记忆）：

> ```

> optimizer.zero_grad()   # ① 清

> pred = model(x)         # ② 算

> loss = loss_fn(pred, y) # ③ 损

> loss.backward()         # ④ 反

> optimizer.step()        # ⑤ 更

> ```

> 以后不管训练什么模型，这 5 行永远不变。只有前面的模型定义和数据加载会变。

> ⚠️ **常见陷阱**：评估时必须 `model.eval()` + `torch.no_grad()`。忘记任何一个：(1) Dropout 仍然在训练模式 → 准确率偏低；(2) 梯度图仍然在构建 → 显存泄漏。

> ✅ **Self-Check**：`optimizer.zero_grad()` 和 `model.zero_grad()` 有什么区别？（optimizer 版本同时清零所有被它管理的参数的梯度，model 版本可能漏掉被外部管理的参数。用 optimizer 版本！）

### 晚上电脑 · 2 小时

用上面的模板训练一个 MNIST 分类器：

```python
# 数据加载

transform = transforms.Compose([

transforms.ToTensor(),

transforms.Normalize((0.1307,), (0.3081,))

])

train_data = datasets.MNIST('./data', train=True, download=True, transform=transform)

test_data = datasets.MNIST('./data', train=False, transform=transform)

train_loader = DataLoader(train_data, batch_size=64, shuffle=True)

test_loader = DataLoader(test_data, batch_size=1000)

# 模型

class MNISTModel(nn.Module):


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = MNISTModel().to(device)

optimizer = optim.Adam(model.parameters(), lr=0.001)

loss_fn = nn.CrossEntropyLoss()

for epoch in range(5):

train_loss = train_epoch(model, train_loader, optimizer, loss_fn, device)

test_loss, test_acc = evaluate(model, test_loader, loss_fn, device)


```

如果 MNIST 分类器能达到 97%+ 准确率，说明你的训练循环是正确的。

> 🎉 **你刚刚训练了人生第一个神经网络！** MNIST 是深度学习的"Hello World"，而你已经让它达到了 97%+ 的准确率。用第 8 周的知识想想：模型内部在做的是不是 "wx+b → ReLU → wx+b → ReLU → wx+b"？

- [ ] 今日完成检查

- [ ] Dataset + DataLoader 使用正确

- [ ] 训练循环代码能背写（5 行核心 + train_epoch + evaluate）

- [ ] MNIST 准确率 > 97%

### 第10周 · 星期五 + 星期六：模型保存 + Wandb + 调参

---

### 星期五

手机：优化器对比（SGD/Adam/AdamW）

> 🧠 **为什么有不同优化器？**

> 基本的 SGD = w -= lr × grad。但 Adam 更进一步——它为每个参数维护独立的"学习率"（自适应），还加了"动量"（像滚下山的球，越滚越快）。Adam 是目前的默认选择，AdamW 是 Adam + 真正有效的权重衰减（你会在阶段三下用到）。

电脑：加 checkpoint + wandb 到 MNIST

```python
# 保存最佳模型

best_acc = 0

for epoch in range(epochs):

train_loss = train_epoch(...)

test_loss, test_acc = evaluate(...)

wandb.log({"train_loss": train_loss, "test_acc": test_acc, "epoch": epoch})

if test_acc > best_acc:

best_acc = test_acc

torch.save(model.state_dict(), "best_model.pt")


# 加载模型

model.load_state_dict(torch.load("best_model.pt"))
```

### 星期六 · 3.5h

调参实验：固定模型，只变超参数，记录效果

变量：

- 学习率：[0.1, 0.01, 0.001, 0.0001]

- batch_size：[32, 64, 128]

- 优化器：[SGD, Adam, AdamW]

- 隐藏层：[128, 256, 512]

> 🧪 **调参的乐趣**：你会发现 Adam 比 SGD 收敛快很多，lr=0.1 可能直接炸掉，lr=0.0001 则慢如蜗牛。这就是为什么"调参"被称为深度学习中的"黑魔法"——没有固定公式，只有实验。

输出调参报告到 Obsidian。

> 🎉 **第 10 周完成！** 你现在有了一个完整的 PyTorch 工作流：Tensor → Autograd → nn.Module → DataLoader → 训练循环 → Wandb → 调参。这是后面所有内容的基础框架，而且你已经能自己训练一个 MNIST 分类器了。

- [ ] 本周完成检查

- [ ] Tensor 操作熟练（像 NumPy）

- [ ] Autograd 理解（计算图/backward/zero_grad/三件套）

- [ ] 训练循环模板能背写（5 行核心 + 两个函数）

- [ ] Wandb 监控 + checkpoint

### 第11周 · 主题：PyTorch 进阶

> 本周目标：深入 PyTorch 底层——手写核心组件（Softmax, LayerNorm），然后搭建 CNN。当你手写完这些组件，Transformer 的积木块就齐了。

### 第11周 · 星期一：手写 Softmax + 交叉熵

---

### 手机摸鱼

> 🧠 **为什么学这个？**

> Softmax 是分类问题中把"原始分数"变成"概率分布"的标准方法。LM Head（语言模型的输出层）就是 Softmax。你的手写实现必须在数值上和 PyTorch 官方一致——这是你代码正确性的证明。

Softmax 公式（多分类的"概率化"）

Softmax 把任意实数向量变成"概率分布"（所有值在 0~1 之间，和为 1）。

softmax(zᵢ) = e^(zᵢ) / Σ e^(zⱼ)

例：z = [1, 2, 3]

e^z = [2.72, 7.39, 20.09]

和 = 30.2

softmax = [0.09, 0.24, 0.67]  ← 和为 1

> 🔥 **关键细节**：为什么手写时先减去 max？`exp(1000)` 在 fp32 里直接爆成 inf。减去 max 不改变 softmax 结果（分子分母同时除以 e^max），但让数值稳定。

交叉熵 Loss（和 Softmax 配合使用）

对于分类问题，假设真实标签是第 k 类，模型输出概率分布 p：

Loss = -log(pₖ)   # 只惩罚"真实类别"对应概率的对数

如果 pₖ → 1，loss → 0（对了，惩罚小）

如果 pₖ → 0，loss → ∞（错了，惩罚巨大）

> ⚠️ **常见陷阱**：PyTorch 的 `F.cross_entropy` 内部**自带 softmax**！如果你已经手动 softmax 过，再用 `F.cross_entropy` 会 double softmax → 结果错误。正确用法：`F.cross_entropy(raw_logits, labels)`，不要先 softmax。

> ✅ **Self-Check**：为什么 softmax 实现中要减去最大值？

### 晚上电脑

```python

def my_softmax(logits, dim=-1):

"""手写 softmax（数值稳定版本）"""


def my_cross_entropy(logits, targets):

"""手写交叉熵"""

probs = my_softmax(logits, dim=1)


# 验证：和 PyTorch 官方对比

logits = torch.randn(4, 10)  # batch=4, 10类

targets = torch.randint(0, 10, (4,))

my_soft = my_softmax(logits)

torch_soft = F.softmax(logits, dim=1)

print(f"Softmax 差异: {(my_soft - torch_soft).abs().max():.10f}")  # 应接近 0

my_loss = my_cross_entropy(logits, targets)

torch_loss = F.cross_entropy(logits, targets)

print(f"Loss 差异: {abs(my_loss - torch_loss):.10f}")  # 应接近 0
```

### 第11周 · 星期二：手写 nn.Linear + nn.LayerNorm

---

### 手机摸鱼

> 🧠 **为什么学这个？**

> LayerNorm 是 Transformer 中除 Attention 外最重要的组件。"先归一化，再缩放"这个模式保证训练稳定。手写 LayerNorm 帮你真正理解 Transformer 的每个组件——不是"调包侠"。

LayerNorm 公式（Transformer 的核心组件）：

给定输入 x（在最后一个维度上做归一化）：

均值 μ = mean(x)

方差 σ² = var(x)

归一化：x̂ = (x - μ) / √(σ² + ε)

缩放和平移：y = γ × x̂ + β

其中 γ 和 β 是可学习参数，ε 是防除零的小常数。

> 💡 **Aha Moment**：LayerNorm 的 "归一化 + 可学习缩放" 模式是深度学习中反复出现的模式。BatchNorm、GroupNorm、RMSNorm（LLaMA 用的）都是这个思想的变体——先把数据"拉平"（均值 0 方差 1），再用可学习参数"拉伸"回去。这样既保证了训练稳定，又不丢失表达能力。

> ⚠️ **常见陷阱**：LayerNorm 和 BatchNorm 的区别是面试高频题。关键：BN 在 batch 维度归一化（受 batch size 影响），LN 在 feature 维度归一化（不受 batch size 影响）。Transformer 用 LN 因为 NLP 序列长度不一致、batch size 通常较小。

### 晚上电脑

```python
# 验证

x = torch.randn(2, 5, 8)  # batch=2, seq=5, dim=8

my_ln = MyLayerNorm(8)

torch_ln = nn.LayerNorm(8)

# 初始化相同参数

my_ln.gamma.data = torch_ln.weight.data.clone()

my_ln.beta.data = torch_ln.bias.data.clone()

output_my = my_ln(x)

output_torch = torch_ln(x)

print(f"差异: {(output_my - output_torch).abs().max():.10f}")
```

- [ ] 完成检查：手写 Softmax / CrossEntropy / LayerNorm 与官方一致

### 第11周 · 星期三-六：CNN + 优化实验

---

### 星期三

用 PyTorch 搭 CNN 做 CIFAR-10 分类

> 🧠 **CNN 的核心直觉**：

> 卷积核像一个小"探测器"，在图片上滑动，每次看一小块区域。

> - 浅层学到边缘/纹理/颜色（低级特征）

> - 中层学到形状/部件（中级特征）

> - 深层学到语义/物体（高级特征）

>

> 这就是深度学习的"层次化特征学习"——也是后面 Transformer 中 Multi-Head Attention 的灵感来源之一。

### 星期四

优化器对比实验（SGD vs Adam vs AdamW）

> 🏃 **SGD = 匀速下山，Adam = 带惯性的下山**

> SGD 每一步只看当前梯度，Adam 还"记住"之前的梯度方向（动量），而且为每个参数自适应调整步长。在复杂的损失曲面上，Adam 通常比 SGD 快得多。

### 星期五

学习率调度器（StepLR, CosineAnnealing）

> 📉 **为什么要降学习率？** 训练初期用大学习率快速收敛，后期用小学习率精细调优。CosineAnnealing 是当前最流行的调度器——学习率按照余弦曲线从大到小，平滑衰减。LLaMA 等大模型都用它。

### 星期六

用自定义 Module 搭 CNN + 训练 + 调参 + Wandb 监控


> 🎉 **阶段三·上 结束！** 回顾你走过的路：

> - 第 8 周：手写梯度下降（线性回归 + 逻辑回归）→ 你会推导梯度了

> - 第 9 周：K-Means、L1/L2 正则化、特征工程、Kaggle → 你有完整 ML 工具箱了

> - 第 10 周：Tensor → Autograd → nn.Module → 训练循环 → MNIST → 你入门 PyTorch 了

> - 第 11 周：手写 Softmax/LayerNorm + CNN → 你理解底层了

>

> **下一步**：阶段三·下——深度学习 + NLP + 手写 Transformer。你前面积累的所有知识（梯度下降、Autograd、nn.Module、LayerNorm）将在第 15 周汇聚成那个改变世界的架构：Transformer。

- [ ] 第11周完成检查

- [ ] Softmax/CrossEntropy/LayerNorm 全部手写验证通过

- [ ] CNN 训练成功（CIFAR-10 > 70%）

- [ ] 调参实验有记录（Wandb 或 CSV）

### 阶段三·上 结束。准备进入阶段三·下（深度学习 + NLP + Transformer）

> 🎊 **恭喜！你完成了阶段三·上。**

>

> 9 周 × 约 18 小时/周 = 约 162 小时。这是整份计划中最"硬核"的基础部分。你从零开始，一步步走到了能独立搭建 CNN、手写核心组件、用 Wandb 监控训练的水平。

>

> 现在，深呼吸。进入阶段三·下——**Transformer 在等着你。**

