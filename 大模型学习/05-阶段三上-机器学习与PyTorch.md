# 阶段三 · 上 · 每日学习指南

阶段三·上 · 每日学习指南
### 机器学习基础 + PyTorch 精通（第 8-11 周）


### 第8周 · 主题：机器学习基础


### 第8周 · 星期一：线性回归 —— 手写梯度下降
---
### 手机摸鱼 · 上午 30 分钟
阅读主题：线性回归 + 梯度下降

核心知识点

1. 什么是线性回归？

最简单的机器学习模型。目标：找一条直线 y = wx + b，
让它尽可能"穿过"所有数据点。

数据：(x₁,y₁), (x₂,y₂), ..., (xₙ,yₙ)
预测值：ŷᵢ = wxᵢ + b
误差：ŷᵢ 和真实 yᵢ 的差距

2. 损失函数（Loss Function）—— 均方误差 MSE

MSE = (1/n) × Σ(ŷᵢ - yᵢ)²

这个值越小，说明模型预测越准。我们的目标就是找到
使 MSE 最小的 w 和 b。

3. 梯度下降（Gradient Descent）—— 怎么找到最好的 w 和 b？

想象你蒙着眼站在山顶，要找最低点——
你感受脚下的坡度，往最陡的下坡方向走一小步，
重复这个动作，最终会到达谷底。

数学上：
w_new = w_old - learning_rate × ∂MSE/∂w
b_new = b_old - learning_rate × ∂MSE/∂b

其中 ∂MSE/∂w 就是"坡度"（梯度），指示 MSE 在 w 方向的变化率。

4. 学习率（Learning Rate）的关键性
太小：收敛极慢，梯度下降 10 万次还没到谷底
太大：一步跨过谷底，在谷两边来回震荡甚至发散
合适：高效到达谷底

经验值：0.01 起步，不行再调。

MSE 对 w 和 b 的梯度（推导结果，记住即可）

对于 y = wx + b，MSE = (1/n) Σ(wxᵢ + b - yᵢ)²

∂MSE/∂w = (2/n) × Σ (wxᵢ + b - yᵢ) × xᵢ
∂MSE/∂b = (2/n) × Σ (wxᵢ + b - yᵢ)

### 晚上电脑 · 2 小时
19:35-21:00  纯 NumPy 手写线性回归

建文件 linear_regression_scratch.py：

```python
    import numpy as np
    import matplotlib.pyplot as plt
```

```python
# 1. 生成模拟数据 y = 3x + 2 + 噪声
    np.random.seed(42)
    n = 100
    X = np.linspace(0, 10, n).reshape(-1, 1)
    true_w, true_b = 3.0, 2.0
    noise = np.random.randn(n, 1) * 2
    y = true_w * X + true_b + noise
```

```python
# 2. 初始化参数
    w = np.random.randn()  # 随机初始值
    b = np.random.randn()
    lr = 0.01              # 学习率
    epochs = 1000
    losses = []
```

```python
# 3. 梯度下降循环
    for epoch in range(epochs):
        # 前向传播：计算预测值
        y_pred = w * X + b
```

```python
# 计算损失
        loss = np.mean((y_pred - y) ** 2)
        losses.append(loss)
```

```python
# 反向传播：计算梯度
        dw = (2 / n) * np.sum((y_pred - y) * X)  # ∂L/∂w
        db = (2 / n) * np.sum(y_pred - y)         # ∂L/∂b
```

```python
# 更新参数
        w -= lr * dw
        b -= lr * db
```

if epoch % 100 == 0:
```python
print(f"Epoch {epoch}: w={w:.4f}, b={b:.4f}, loss={loss:.4f}")
```

```python
print(f"\n真实参数: w={true_w}, b={true_b}")
    print(f"学习参数: w={w:.4f}, b={b:.4f}")
```

```python
# 4. 可视化
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
```

```python
# 左图：数据和拟合直线
    axes[0].scatter(X, y, alpha=0.5, label='数据')
    axes[0].plot(X, w * X + b, 'r-', label=f'拟合: y={w:.2f}x+{b:.2f}')
    axes[0].legend()
    axes[0].set_title('线性回归结果')
```

```python
# 右图：loss 下降曲线
    axes[1].plot(losses)
    axes[1].set_title('Loss 下降曲线')
    axes[1].set_xlabel('Epoch')
    axes[1].set_ylabel('MSE')
```

plt.tight_layout()
plt.savefig('linear_regression.png')
plt.show()
```python
```

实验 1：改变学习率
lr = 0.001（太小）→ loss 下降极慢
lr = 0.1（太大）→ loss 可能震荡甚至发散
lr = 0.01 → 刚好收敛

实验 2：改变初始值
不同的 w, b 初始值 → 最终都收敛到相同结果（凸函数的性质）

实验 3：增加噪声
噪声变大 → loss 最终值变高（因为数据本身更乱）

- [ ] 今日完成检查
- [ ] 手写梯度下降收敛成功
- [ ] 理解学习率如何影响收敛
- [ ] 能推导 MSE 对 w 和 b 的偏导数
### 第8周 · 星期二：逻辑回归 —— 分类问题
---
### 手机摸鱼 · 上午 30 分钟
阅读主题：逻辑回归

核心知识点

1. 线性回归 → 分类问题的挑战

线性回归输出任意实数。但分类问题需要输出概率（0~1）。

比如：预测一封邮件是垃圾邮件（1）还是正常（0）。
如果模型输出 2.7 或 -0.5，这没有意义。

2. Sigmoid 函数 —— 把任意实数"压缩"到 (0,1)

σ(z) = 1 / (1 + e^(-z))

z = 很大正数 → σ(z) ≈ 1
z = 0 → σ(z) = 0.5
z = 很大负数 → σ(z) ≈ 0

逻辑回归：ŷ = σ(wx + b)

3. 损失函数 —— 交叉熵（Cross-Entropy）

为什么不用 MSE？因为 sigmoid + MSE 会导致梯度消失问题。

交叉熵：
Loss = -[y×log(ŷ) + (1-y)×log(1-ŷ)]

- 当 y=1 时 Loss = -log(ŷ)：
预测 ŷ→1 → loss→0（对了，处罚小）
预测 ŷ→0 → loss→∞（错了，处罚巨大）

- 当 y=0 时 Loss = -log(1-ŷ)：
预测 ŷ→0 → loss→0（对了）
预测 ŷ→1 → loss→∞（错了）

4. 梯度推导结果（记住即可）
∂Loss/∂w = (ŷ - y) × x     ← 注意！形式和线性回归的梯度一样！
∂Loss/∂b = (ŷ - y)

这就是交叉熵的优雅之处：梯度形式简洁。

### 晚上电脑 · 2 小时
19:35-21:00  手写逻辑回归

```python
    import numpy as np
```

```python
# Sigmoid 函数
    def sigmoid(z):
        return 1 / (1 + np.exp(-z))
```

```python
# 生成二分类数据
    np.random.seed(42)
    n = 200
    # 两类数据，分别在 (2,2) 和 (-2,-2) 附近
    X_pos = np.random.randn(n//2, 2) + np.array([2, 2])
    X_neg = np.random.randn(n//2, 2) + np.array([-2, -2])
    X = np.vstack([X_pos, X_neg])
    y = np.hstack([np.ones(n//2), np.zeros(n//2)]).reshape(-1, 1)
```

```python
# 初始化参数
    w = np.random.randn(2, 1)  # 2 个特征
    b = np.random.randn()
    lr = 0.1
```

for epoch in range(1000):
```python
# 前向传播
        z = X @ w + b           # (n, 2) @ (2, 1) = (n, 1)
        y_pred = sigmoid(z)     # 概率预测
```

```python
# 交叉熵损失
        eps = 1e-8  # 防止 log(0)
        loss = -np.mean(y * np.log(y_pred + eps) + (1-y) * np.log(1 - y_pred + eps))
```

```python
# 梯度
        dw = (1/n) * (X.T @ (y_pred - y))
        db = (1/n) * np.sum(y_pred - y)
```

w -= lr * dw
b -= lr * db

if epoch % 200 == 0:
```python
# 准确率
            y_class = (y_pred > 0.5).astype(int)
            acc = np.mean(y_class == y)
            print(f"Epoch {epoch}: loss={loss:.4f}, acc={acc:.4f}")
```

```python
print(f"最终参数: w={w.flatten()}, b={b:.4f}")
    print(f"决策边界: {w[0][0]:.2f}x₁ + {w[1][0]:.2f}x₂ + {b:.2f} = 0")
    ```
```

- [ ] 今日完成检查
- [ ] 理解 sigmoid 的作用
- [ ] 交叉熵公式能写出来
- [ ] 手写逻辑回归收敛成功
### 第8周 · 星期三、四：决策树 + 随机森林
---
### 手机摸鱼 · 星期三上午
阅读主题：决策树

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

- 信息增益：分裂前后的熵减少量，减少越多越好
IG = H(父) - Σ (|子|/|父|) × H(子)

每次分裂选择信息增益最大的特征。

### 手机摸鱼 · 星期四上午
阅读主题：随机森林

- 随机森林 = 多棵决策树的"投票"
- 两重随机性：
① Bootstrap（有放回抽样）→ 每棵树看到的数据不同
② 随机选特征 → 每次分裂只在部分特征中选最优
- 为什么有效？每棵树"偏见"不同，投票结果抵消了过拟合

### 电脑 · 星期三+星期四晚上
用 sklearn 实战：
```
```python
  from sklearn.tree import DecisionTreeClassifier
  from sklearn.ensemble import RandomForestClassifier
  from sklearn.model_selection import train_test_split, cross_val_score
  from sklearn.metrics import classification_report, confusion_matrix
```

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
```python
print(f"  {name}: {importance:.4f}")
  ```
```

### 第8周 · 星期五 + 星期六：评估指标 + 完整 ML Pipeline
---
### 手机摸鱼 · 星期五
阅读主题：模型评估指标

核心知识点

混淆矩阵：
预测正    预测负
| 实际正 | TP | FN |
| 实际负 | FP | TN |

准确率 = (TP+TN) / 总数  —— 样本不均衡时不可靠
精确率 = TP / (TP+FP)    —— 预测为正的有多少是真正
召回率 = TP / (TP+FN)    —— 真正为正的有多少被找出
F1 = 2×P×R / (P+R)       —— 精确率和召回率的调和平均

例：癌症检测
1000 人中，10 人患病。
模型说"全部没病" → 准确率 99%，但召回率 0%，毫无用处！

所以评估模型要看业务场景：
- 癌症检测 → 宁可误报，不能漏报 → 追求高召回
- 垃圾邮件过滤 → 宁可漏过，不能误杀 → 追求高精确率

### 星期六 · 3.5h
完整 ML Pipeline
```
```python
  # ml_pipeline.py —— 从数据到模型评估的完整流程
  from sklearn.pipeline import Pipeline
  from sklearn.preprocessing import StandardScaler
  from sklearn.ensemble import RandomForestClassifier
  from sklearn.model_selection import GridSearchCV
```

# 1 个完整 Pipeline
pipeline = Pipeline([
```python
('scaler', StandardScaler()),     # 标准化
      ('classifier', RandomForestClassifier(random_state=42))
  ])
```

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
```python
```

可选：在 Kaggle 提交 Titanic 或 House Prices 比赛。

- [ ] 第8周完成检查
- [ ] 线性回归/逻辑回归手写梯度下降 OK
- [ ] 决策树/随机森林 sklearn 实战 OK
- [ ] 懂精确率、召回率、F1、ROC/AUC
- [ ] ML Pipeline 完整跑通
### 第9周 · 主题：机器学习深入 + 特征工程


-  本周目标：补齐 ML 最后一个缺口──
### 第9周 · 星期一：K-Means 聚类（无监督学习）
---
### 手机摸鱼 · 上午 30 分钟
核心知识点

1. 有监督 vs 无监督

有监督：数据有标签 → 线性回归、逻辑回归、决策树
无监督：数据没有标签 → 聚类、降维

2. K-Means 算法步骤

① 随机选 K 个点作为"聚类中心"
② 把每个数据点分配给最近的中心
③ 重新计算每个簇的中心（取均值）
④ 重复 ②③ 直到中心不再变化

像玩"抢地盘"：K 个队长站好位置→队员选最近的队长→
队长挪到队员中心→队员重新选→...→稳定。

3. 选择 K 值：肘部法则

画 K 值 vs 簇内误差平方和（inertia）的曲线，
找到"拐点"（误差下降变缓的地方）就是最佳 K。

### 晚上电脑 · 2 小时
```python
  import numpy as np
  import matplotlib.pyplot as plt
  from sklearn.datasets import make_blobs
```

# 生成聚类数据
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=42)

# ===== 手写 K-Means =====
class MyKMeans:
```python
def __init__(self, n_clusters=3, max_iters=100):
          self.K = n_clusters
          self.max_iters = max_iters
```

```python
def fit(self, X):
          n_samples, n_features = X.shape
          # ① 随机初始化中心（从数据中随机选 K 个点）
          rng = np.random.default_rng(42)
          self.centroids = X[rng.choice(n_samples, self.K, replace=False)]
```

for _ in range(self.max_iters):
```python
# ② 分配：每个点归属最近的中心
              distances = np.linalg.norm(X[:, None] - self.centroids, axis=2)  # (n, K)
              labels = np.argmin(distances, axis=1)
```

```python
# ③ 更新：重新计算中心
              new_centroids = np.array([X[labels == k].mean(axis=0) for k in range(self.K)])
```

```python
# ④ 判断收敛
              if np.allclose(self.centroids, new_centroids):
                  break
              self.centroids = new_centroids
```

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
```python
```

### 第9周 · 星期二：L1 vs L2 正则化
---
### 手机摸鱼
核心知识点

1. 过拟合的根源：模型记住了训练数据的噪声

训练集 loss 很低，测试集 loss 很高 → 过拟合

2. L2 正则化（Ridge / 权重衰减）

Loss_total = Loss_original + λ × Σ(w²)

效果：所有参数被"压缩"但不归零。
几何直觉：损失函数的等高线被一个"圆"约束，
最优解在切点上，参数更小但都非零。

3. L1 正则化（Lasso）

Loss_total = Loss_original + λ × Σ(|w|)

效果：不重要的参数直接变成 0 → 自动特征选择！
几何直觉：约束是一个"菱形"，等高线更容易碰到角点，
角点上某些参数正好为 0。

面试考点：L1 vs L2
L2：所有参数缩小但不归零，适合"所有特征都有贡献"的场景
L1：产生稀疏解，自动选特征，适合"只有少数特征是重要的"场景

### 晚上电脑
```python
  import numpy as np
  from sklearn.linear_model import Ridge, Lasso, LinearRegression
  from sklearn.preprocessing import StandardScaler, PolynomialFeatures
  from sklearn.model_selection import train_test_split
  from sklearn.pipeline import make_pipeline
```

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
```python
print(f"{name}: 训练 R²={train_r2:.3f}, 测试 R²={test_r2:.3f}")
      # 预期：无正则化 → 训练 R² 很高但测试很低（严重过拟合）
      #       L2 → 过拟合缓解
      #       L1 → 很多系数为 0
  ```
```

### 第9周 · 星期三：特征工程
---
### 手机摸鱼
核心知识点

1. 数值特征处理

标准化（StandardScaler）：(x-μ)/σ → 均值 0 方差 1
归一化（MinMaxScaler）：(x-min)/(max-min) → 缩放到 [0,1]
选哪个？梯度下降类模型用标准化，距离类模型（KNN/K-Means）用归一化

2. 类别特征处理

独热编码（One-Hot）：颜色=[红,蓝,绿] → 红=[1,0,0], 蓝=[0,1,0]
标签编码（Label）：红=0, 蓝=1, 绿=2
选哪个？无序类别用 One-Hot，有序类别（低中高）用 Label

3. 文本特征处理

TF-IDF：词频 × 逆文档频率
核心思想：一个词在本文档中出现多(TF高)但在其他文档出现少(IDF高)，
这个词对本文档很重要。

### 晚上电脑
```
```python
  from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder, LabelEncoder
  from sklearn.feature_extraction.text import TfidfVectorizer
  from sklearn.compose import ColumnTransformer
  from sklearn.pipeline import Pipeline
  import pandas as pd
```

# 模拟混合类型数据
df = pd.DataFrame({
'age': [25, 30, 22, 45, 33],
'income': [5000, 8000, 3000, 15000, 9000],
'city': ['北京', '上海', '北京', '深圳', '上海'],
```python
'level': ['初级', '高级', '初级', '资深', '中级'],  # 有顺序
  })
```

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
```python
```

### 第9周 · 星期四：过拟合诊断 + 学习曲线
---
### 手机摸鱼
核心知识点

诊断三种状态：

欠拟合（Underfitting）：训练 loss 高 + 测试 loss 高
→ 模型太简单 / 特征不够 / 训练不充分
→ 解决：增加模型复杂度、增加特征、多训几轮

过拟合（Overfitting）：训练 loss 低 + 测试 loss 高
→ 模型记住了训练数据的噪声
→ 解决：正则化、Dropout、数据增强、早停、减少参数

刚好（Good Fit）：训练 loss 低 + 测试 loss 低
→ 完美状态！

学习曲线：横轴=训练样本数，纵轴=loss
过拟合时：训练 loss 很低（一条平线），测试 loss 很高且不降
欠拟合时：训练和测试 loss 都很高，且几乎持平

### 晚上电脑
```python
  from sklearn.model_selection import learning_curve
  import matplotlib.pyplot as plt
```

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
```python
```

- [ ] 今日完成检查
- [ ] 能画出学习曲线并判断过拟合/欠拟合
### 第9周 · 星期五-六：Kaggle 实战
---
### 星期五
复习周一到周四所有代码，确保每段都能理解运行。
手机：回顾混淆矩阵→精确率/召回率→ROC/AUC 的关系（阶段 8 周学过）

### 星期六 · 3.5h
14:00-17:00 Kaggle 提交：House Prices 或 Titanic
1. 加载数据 → 探索分析（df.describe(), 缺失值统计, 相关性热力图）
2. 特征工程（填充缺失、独热编码、标准化、创建新特征）
3. 训练多模型对比（Linear/Ridge/Lasso/RandomForest/XGBoost）
4. 交叉验证评估 → 选最佳模型 → 生成提交文件
5. 上传 Kaggle，看排名

17:00-17:30 整理本周所有代码到 GitHub，更新 Obsidian 笔记

- [ ] 第9周完成检查
- [ ] K-Means 手写实现 + 肘部法则
- [ ] L1 vs L2 对比实验完成，区别能说清楚
- [ ] 特征工程（标准化/OneHot/TF-IDF）流程熟练
- [ ] 能画学习曲线并诊断过拟合
- [ ] Kaggle 成功提交
### 第10周 · 主题：PyTorch 基础（Tensor → Autograd → nn.Module）


说明：本周开始切换到 PyTorch。前面两周的 ML 基础会让你
理解 PyTorch 底层在做什么，而不是只会"调包"。

-  本周目标 ──
1. Tensor 操作形成肌肉记忆（像 NumPy 一样熟练）
2. 理解 Autograd（自动求导）的原理
3. 掌握 nn.Module 和训练循环

### 第10周 · 星期一：Tensor 操作（从 NumPy 平滑过渡）
---
### 手机摸鱼 · 上午 30 分钟
阅读主题：PyTorch Tensor —— GPU 上的 NumPy

核心知识点

1. NumPy → PyTorch 对照表

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
| arr.mean(axis=0) | tensor.mean(dim=0) | ← 注意：axis→dim |

2. 关键区别

- PyTorch Tensor 可以跑在 GPU 上：
```python
tensor = tensor.to('cuda')  # 移到 GPU
       tensor = tensor.to('cpu')   # 移回来
```

- view vs reshape：
view 要求内存连续（更高效但可能失败）
reshape 不要求（更安全，推荐先多用 reshape）

- requires_grad：
设置后 PyTorch 追踪对该 Tensor 的所有操作，
从而自动计算梯度。

3. Tensor 的 device（设备）管理

```python
     device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
     tensor = torch.randn(3, 4, device=device)  # 直接在目标设备上创建
     ```
```

### 晚上电脑 · 2 小时
建文件 pytorch_tensor_workout.py，和 NumPy 练习对照做：

```
```python
  import torch
```

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
```python
print("在GPU上:", a_gpu.device)
      a_cpu = a_gpu.to('cpu')  # 移回来
  ```
```

重要：把上面的每一个操作都亲手敲一遍，
形成肌肉记忆。不要复制粘贴！

- [ ] 今日完成检查
- [ ] 能熟练创建/索引/变形 PyTorch Tensor
- [ ] 理解 dim 参数（和 NumPy 的 axis 一样）
- [ ] GPU 移动操作成功
### 第10周 · 星期二：Autograd —— PyTorch 的灵魂
---
### 手机摸鱼 · 上午 30 分钟
阅读主题：自动求导（Autograd）

核心知识点

1. 痛点：手算梯度太痛苦

第 8 周手写梯度下降时，你需要手动推导：
∂MSE/∂w = (2/n) × Σ(...)
∂MSE/∂b = (2/n) × Σ(...)

对于简单的线性回归还好，但对于 Transformer：
- 几十个矩阵乘法
- Softmax、LayerNorm、Dropout
- 每层的梯度公式都不一样

手动推导几乎不可能不出错。

2. PyTorch Autograd 的解决方案

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

3. requires_grad 和 backward()

```
```python
     x = torch.tensor(2.0, requires_grad=True)
     y = x ** 2 + 3 * x + 1  # y = x² + 3x + 1
```

```python
y.backward()            # 自动计算 dy/dx
     print(x.grad)           # dy/dx = 2x + 3 = 2*2 + 3 = 7
     ```
```

训练时：
```
```python
     for epoch in range(epochs):
         # 前向传播
         loss = compute_loss(model(X), y)
```

```python
# 反向传播（计算所有参数的梯度）
         loss.backward()
```

```python
# 更新参数
         with torch.no_grad():        # 更新时不需要追踪梯度
             w -= lr * w.grad
             b -= lr * b.grad
             w.grad.zero_()           # 清零梯度！忘记这步会累加
             b.grad.zero_()
     ```
```

4. 两个关键陷阱
① 忘记 zero_grad() → 梯度会累加（PyTorch 的默认行为）
② 不想要梯度时没加 torch.no_grad() → 内存泄漏

### 晚上电脑 · 2 小时
任务 1：验证 Autograd 的梯度计算是否正确

```
```python
  import torch
```

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
```python
# 前向传播
      y_pred = w * X + b
      loss = torch.mean((y_pred - y) ** 2)
```

```python
# 反向传播
      loss.backward()
```

```python
# 更新
      with torch.no_grad():
          w -= lr * w.grad
          b -= lr * b.grad
          w.grad.zero_()
          b.grad.zero_()
```

if epoch % 100 == 0:
```python
print(f"Epoch {epoch}: loss={loss.item():.4f}")
```

print(f"学习参数: w={w.item():.4f}, b={b.item():.4f}")
```python
```

任务 2：验证"梯度累加"现象

```python
  # 错误示范：不 zero_grad()
  x = torch.tensor(2.0, requires_grad=True)
  for i in range(3):
      y = x ** 2
      y.backward()
      print(f"第{i+1}次 backward 后 x.grad = {x.grad}")
      # 输出：2.0, 4.0, 6.0 —— 梯度累加了！
  ```
```

任务 3：理解 no_grad() 的作用

```
```python
  x = torch.tensor(2.0, requires_grad=True)
```

# 带梯度追踪
with torch.no_grad():
```python
y = x ** 2  # 这个操作不会被追踪
  print(y.requires_grad)  # False
  ```
```

- [ ] 今日完成检查
- [ ] 理解 requires_grad、backward()、zero_grad() 三件套
- [ ] 能解释"梯度累加"现象
- [ ] Autograd 版线性回归收敛成功
### 第10周 · 星期三：nn.Module + 自定义网络
---
### 手机摸鱼 · 上午 30 分钟
阅读主题：nn.Module —— PyTorch 的"积木"

核心知识点

1. nn.Module 是什么？

所有神经网络层的基类。你的模型继承它后，自动获得：
- parameters()：列出所有可训练参数
- forward()：子类必须实现，定义前向计算
- to(device)：一键移动所有参数到 GPU
- train() / eval()：切换训练/评估模式（影响 Dropout/BN）

2. 最简单的自定义 Module

```
```python
  import torch.nn as nn
```

class SimpleMLP(nn.Module):
```python
def __init__(self, input_dim, hidden_dim, output_dim):
          super().__init__()  # 必须调用父类 __init__
          self.fc1 = nn.Linear(input_dim, hidden_dim)    # 全连接层
          self.relu = nn.ReLU()
          self.fc2 = nn.Linear(hidden_dim, output_dim)
```

```python
def forward(self, x):
          x = self.fc1(x)      # (batch, input) → (batch, hidden)
          x = self.relu(x)
          x = self.fc2(x)      # (batch, hidden) → (batch, output)
          return x
  ```
```

3. 常用层速查

nn.Linear(in, out)       全连接层：y = xW^T + b
nn.Conv2d(in, out, k)    2D卷积
nn.ReLU()                激活函数
nn.Dropout(p)            Dropout 正则化
nn.BatchNorm1d(d)        批归一化
nn.LayerNorm(d)          层归一化（Transformer 里用）
nn.Embedding(vocab, dim) 词嵌入
nn.LSTM(in, hidden)      LSTM
nn.TransformerEncoder    完整的 Transformer Encoder

4. Sequential —— 简单的层叠
```
```python
  model = nn.Sequential(
      nn.Linear(784, 256),
      nn.ReLU(),
      nn.Linear(256, 10),
  )
  ```
```

### 晚上电脑 · 2 小时
任务 1：用 nn.Module 重写线性回归 + 逻辑回归

```
```python
  class LinearRegressor(nn.Module):
      def __init__(self):
          super().__init__()
          self.linear = nn.Linear(1, 1)
      def forward(self, x):
          return self.linear(x)
```

class LogisticRegressor(nn.Module):
```python
def __init__(self, input_dim):
          super().__init__()
          self.linear = nn.Linear(input_dim, 1)
      def forward(self, x):
          return torch.sigmoid(self.linear(x))
  ```
```

任务 2：手写一个和 PyTorch 内置功能等价的模块

```
```python
  class MyLinear(nn.Module):
      """手写 nn.Linear，理解内部实现"""
      def __init__(self, in_features, out_features):
          super().__init__()
          # 参数初始化
          self.weight = nn.Parameter(torch.randn(out_features, in_features) * 0.01)
          self.bias = nn.Parameter(torch.zeros(out_features))
```

```python
def forward(self, x):
          # y = x @ W^T + b
          return x @ self.weight.T + self.bias
```

# 测试：和官方 nn.Linear 对比
official = nn.Linear(10, 5)
my = MyLinear(10, 5)

x = torch.randn(3, 10)
# 如果参数相同，输出应该相同
my.weight.data = official.weight.data.clone()
my.bias.data = official.bias.data.clone()
print("官方输出:", official(x))
print("我的输出:", my(x))
```python
```

- [ ] 今日完成检查
- [ ] 理解 nn.Module 的生命周期（__init__ + forward）
- [ ] 能自定义 Module
- [ ] 手写 MyLinear 和官方输出一致
### 第10周 · 星期四：DataLoader + 完整训练循环
---
### 手机摸鱼 · 上午 30 分钟
阅读主题：DataLoader —— 高效的数据加载

核心知识点

1. Dataset 和 DataLoader 的分工

Dataset：负责读取 1 条数据（返回 (x, y)）
DataLoader：负责批量打包、打乱、多线程加载

```python
     from torch.utils.data import Dataset, DataLoader
```

```python
class MyDataset(Dataset):
         def __init__(self, X, y):
             self.X = X
             self.y = y
```

```python
def __len__(self):
             return len(self.X)
```

```python
def __getitem__(self, idx):
             return self.X[idx], self.y[idx]
```

dataset = MyDataset(X, y)
loader = DataLoader(dataset, batch_size=32, shuffle=True)

for batch_x, batch_y in loader:
```python
# batch_x: (32, features)
         # batch_y: (32,)
         ...
     ```
```

2. 完整训练循环（模板，背下来）

```
```python
  def train_epoch(model, loader, optimizer, loss_fn, device):
      model.train()
      total_loss = 0
      for x, y in loader:
          x, y = x.to(device), y.to(device)
```

```python
optimizer.zero_grad()          # 1. 清零梯度
          pred = model(x)                # 2. 前向传播
          loss = loss_fn(pred, y)        # 3. 计算损失
          loss.backward()                # 4. 反向传播
          optimizer.step()               # 5. 更新参数
```

total_loss += loss.item()
return total_loss / len(loader)

def evaluate(model, loader, loss_fn, device):
model.eval()
total_loss = 0
correct = 0
```python
with torch.no_grad():             # 评估时不需要梯度
          for x, y in loader:
              x, y = x.to(device), y.to(device)
              pred = model(x)
              loss = loss_fn(pred, y)
              total_loss += loss.item()
              correct += (pred.argmax(1) == y).sum().item()
      return total_loss / len(loader), correct / len(loader.dataset)
  ```
```

### 晚上电脑 · 2 小时
用上面的模板训练一个 MNIST 分类器：

```
```python
  import torch.nn as nn
  import torch.optim as optim
  from torchvision import datasets, transforms
  from torch.utils.data import DataLoader
```

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
```python
def __init__(self):
          super().__init__()
          self.net = nn.Sequential(
              nn.Flatten(),
              nn.Linear(784, 256), nn.ReLU(),
              nn.Linear(256, 128), nn.ReLU(),
              nn.Linear(128, 10)
          )
      def forward(self, x):
          return self.net(x)
```

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = MNISTModel().to(device)
optimizer = optim.Adam(model.parameters(), lr=0.001)
loss_fn = nn.CrossEntropyLoss()

for epoch in range(5):
train_loss = train_epoch(model, train_loader, optimizer, loss_fn, device)
test_loss, test_acc = evaluate(model, test_loader, loss_fn, device)
```python
print(f"Epoch {epoch+1}: train_loss={train_loss:.4f}, test_acc={test_acc:.4f}")
  ```
```

如果 MNIST 分类器能达到 97%+ 准确率，说明你的训练循环是正确的。

- [ ] 今日完成检查
- [ ] Dataset + DataLoader 使用正确
- [ ] 训练循环代码能背写
- [ ] MNIST 准确率 > 97%
### 第10周 · 星期五 + 星期六：模型保存 + Wandb + 调参
---
### 星期五
手机：优化器对比（SGD/Adam/AdamW）
电脑：加 checkpoint + wandb 到 MNIST

```
```python
  import wandb
  wandb.init(project="mnist-baseline", name="adam-lr0.001")
```

# 保存最佳模型
best_acc = 0
for epoch in range(epochs):
train_loss = train_epoch(...)
test_loss, test_acc = evaluate(...)

wandb.log({"train_loss": train_loss, "test_acc": test_acc, "epoch": epoch})

if test_acc > best_acc:
best_acc = test_acc
torch.save(model.state_dict(), "best_model.pt")
```python
print(f"保存最佳模型，准确率: {best_acc:.4f}")
```

# 加载模型
model.load_state_dict(torch.load("best_model.pt"))
```python
```

### 星期六 · 3.5h
调参实验：固定模型，只变超参数，记录效果

变量：
- 学习率：[0.1, 0.01, 0.001, 0.0001]
- batch_size：[32, 64, 128]
- 优化器：[SGD, Adam, AdamW]
- 隐藏层：[128, 256, 512]

输出调参报告到 Obsidian。

- [ ] 本周完成检查
- [ ] Tensor 操作熟练（像 NumPy）
- [ ] Autograd 理解（计算图/backward/zero_grad）
- [ ] 训练循环模板能背写
- [ ] Wandb 监控 + checkpoint
### 第11周 · 主题：PyTorch 进阶


### 第11周 · 星期一：手写 Softmax + 交叉熵
---
### 手机摸鱼
Softmax 公式（多分类的"概率化"）

Softmax 把任意实数向量变成"概率分布"（所有值在 0~1 之间，和为 1）。

softmax(zᵢ) = e^(zᵢ) / Σ e^(zⱼ)

例：z = [1, 2, 3]
e^z = [2.72, 7.39, 20.09]
和 = 30.2
softmax = [0.09, 0.24, 0.67]  ← 和为 1

交叉熵 Loss（和 Softmax 配合使用）

对于分类问题，假设真实标签是第 k 类，模型输出概率分布 p：

Loss = -log(pₖ)   # 只惩罚"真实类别"对应概率的对数

如果 pₖ → 1，loss → 0（对了，惩罚小）
如果 pₖ → 0，loss → ∞（错了，惩罚巨大）

### 晚上电脑
```python
  import torch
  import torch.nn.functional as F
```

def my_softmax(logits, dim=-1):
"""手写 softmax（数值稳定版本）"""
```python
# 减去最大值防止 exp 溢出
      logits_max = logits.max(dim=dim, keepdim=True)[0]
      exp = torch.exp(logits - logits_max)
      return exp / exp.sum(dim=dim, keepdim=True)
```

def my_cross_entropy(logits, targets):
"""手写交叉熵"""
probs = my_softmax(logits, dim=1)
```python
# 取真实标签对应的概率
      batch_size = logits.shape[0]
      correct_probs = probs[range(batch_size), targets]
      return -torch.log(correct_probs + 1e-8).mean()
```

# 验证：和 PyTorch 官方对比
logits = torch.randn(4, 10)  # batch=4, 10类
targets = torch.randint(0, 10, (4,))

my_soft = my_softmax(logits)
torch_soft = F.softmax(logits, dim=1)
print(f"Softmax 差异: {(my_soft - torch_soft).abs().max():.10f}")  # 应接近 0

my_loss = my_cross_entropy(logits, targets)
torch_loss = F.cross_entropy(logits, targets)
print(f"Loss 差异: {abs(my_loss - torch_loss):.10f}")  # 应接近 0
```python
```

### 第11周 · 星期二：手写 nn.Linear + nn.LayerNorm
---
### 手机摸鱼
LayerNorm 公式（Transformer 的核心组件）：
给定输入 x（在最后一个维度上做归一化）：
均值 μ = mean(x)
方差 σ² = var(x)
归一化：x̂ = (x - μ) / √(σ² + ε)
缩放和平移：y = γ × x̂ + β

其中 γ 和 β 是可学习参数，ε 是防除零的小常数。

### 晚上电脑
```python
  class MyLayerNorm(nn.Module):
      def __init__(self, normalized_shape, eps=1e-5):
          super().__init__()
          self.gamma = nn.Parameter(torch.ones(normalized_shape))
          self.beta = nn.Parameter(torch.zeros(normalized_shape))
          self.eps = eps
```

```python
def forward(self, x):
          # x: (batch, seq_len, d_model)
          mean = x.mean(dim=-1, keepdim=True)
          var = x.var(dim=-1, keepdim=True, unbiased=False)
          x_norm = (x - mean) / torch.sqrt(var + self.eps)
          return self.gamma * x_norm + self.beta
```

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
```python
```

- [ ] 完成检查：手写 Softmax / CrossEntropy / LayerNorm 与官方一致
### 第11周 · 星期三-六：CNN + 优化实验
---
### 星期三
用 PyTorch 搭 CNN 做 CIFAR-10 分类
### 星期四
优化器对比实验（SGD vs Adam vs AdamW）
### 星期五
学习率调度器（StepLR, CosineAnnealing）
### 星期六
用自定义 Module 搭 CNN + 训练 + 调参 + Wandb 监控
```python
  # CNN 架构参考
  class SimpleCNN(nn.Module):
      def __init__(self, num_classes=10):
          super().__init__()
          self.conv = nn.Sequential(
              nn.Conv2d(3, 32, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
              nn.Conv2d(32, 64, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
              nn.Conv2d(64, 128, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
          )
          self.fc = nn.Sequential(
              nn.Flatten(),
              nn.Linear(128 * 4 * 4, 256), nn.ReLU(), nn.Dropout(0.5),
              nn.Linear(256, num_classes)
          )
      def forward(self, x):
          return self.fc(self.conv(x))
  ```
```

- [ ] 第11周完成检查
- [ ] Softmax/CrossEntropy/LayerNorm 全部手写验证通过
- [ ] CNN 训练成功（CIFAR-10 > 70%）
- [ ] 调参实验有记录（Wandb 或 CSV）
### 阶段三·上 结束。准备进入阶段三·下（深度学习 + NLP + Transformer）


```