# 阶段三 · 下 · 每日学习指南

阶段三·下 · 每日学习指南
### 深度学习 + NLP + 手写 Transformer（第 12-16 周）★核心中的核心★


说明：这 5 周是整份计划中最重要的部分。
第 15 周（手写 Transformer）是所有知识的中点，
之前一切都在为它打基础，之后一切都在它上面构建。

> 🔥 **这是一条分水岭。** 阶段三·上的 4 周 ML + PyTorch 是"准备弹药"，这 5 周是"上战场"。你将从深度学习基础一路杀到手写完整 Transformer——那个改变了整个 AI 行业的架构。
> 
> 第 15 周是最重要的一周。当你写完 Transformer，你会真正理解 ChatGPT 的核心。之后的 Agent、RAG、微调——都是在 Transformer 的基础上盖楼。

### 第12周 · 主题：深度学习基础与训练技巧


> 本周目标：理解反向传播（深度学习的发动机），掌握正则化/归一化技术，学会用 AMP 加速训练。这些是训练任何深度学习模型的"基本功"。

### 第12周 · 星期一：手写反向传播（纸笔推导 + 代码验证）
---
### 手机摸鱼 · 上午 30 分钟
阅读主题：反向传播 —— 深度学习的核心算法

> 🧠 **为什么学这个？**
> 反向传播是让深度学习成为可能的算法。没有它，训练超过 2 层的网络就是噩梦。你在第 8 周手写过 2 个参数的梯度下降——反向传播就是把这个过程**自动化地**扩展到任意层数。

核心知识点

**1. 反向传播的本质**

正向：输入 → 计算 → 输出 → 损失
反向：损失 → 逐层计算梯度 → 更新参数

> 🏭 **工厂流水线类比**：
> 正向 = 原料（输入）经过各车间（层）加工，最终变成产品（预测），质检员（损失函数）打分
> 反向 = 质检员告诉最后一个车间"你的环节误差贡献了多少"→ 这个车间再告诉前一个车间 → 一路传到第一个车间
> 每个车间根据自己"造成的误差比例"来调整自己的机器（参数）
>
> 这就是"反向传播"——误差信号从后往前传，每个层分到自己的"责任"。

数学工具：链式法则（Chain Rule）

dz/dx = dz/dy × dy/dx

对于多层网络：
Loss → ∂L/∂w₃ → ∂L/∂w₂ → ∂L/∂w₁
从最后一层"反向"传播到第一层。

**2. 一个具体例子（2 层 MLP）**

x → [Linear + ReLU] → h → [Linear] → ŷ
损失: L = (ŷ - y)²

推导 ∂L/∂w₂（第 2 层的权重梯度）：
① ∂L/∂ŷ = 2(ŷ - y)
② ∂ŷ/∂w₂ = h（因为 ŷ = w₂·h + b₂）
③ ∂L/∂w₂ = ∂L/∂ŷ × ∂ŷ/∂w₂ = 2(ŷ - y) × h

推导 ∂L/∂w₁（第 1 层的权重梯度）：
④ ∂ŷ/∂h = w₂
⑤ ∂h/∂w₁ = x × ReLU'(w₁·x)  （ReLU' = 输入>0时为1，否则为0）
⑥ ∂L/∂w₁ = ∂L/∂ŷ × ∂ŷ/∂h × ∂h/∂w₁
= 2(ŷ - y) × w₂ × x × ReLU'(w₁·x)

> 💡 **Aha Moment**：反向传播不是什么新算法——它只是把链式法则**系统化地应用到整个计算图上**。你在高中数学课上学过链式法则，深度学习只是把它用到了有几百层的函数上。PyTorch 的 Autograd 做的事情，就是自动帮你"写"这些链式法则的每一步。

**3. 关键洞察**

> 🚨 **梯度消失/爆炸——深层网络的诅咒**：
>
> 链式法则意味着：离输出越远的层，梯度可能越小（梯度消失）
> 或越大（梯度爆炸）。这是深层网络难训练的根本原因。
>
> 如果网络有 100 层，每层梯度都乘 0.8：
> 第一层的梯度 = 最后一层的梯度 × 0.8^99 ≈ 最后一层 × 2.5×10^-10
> → 第一层几乎收不到任何信号 → "我不知道该往哪个方向调" → 学不动
>
> 反之，如果每层梯度乘 1.2：1.2^99 ≈ 7.0×10^7 → 梯度爆炸 → 参数更新"一步迈出大气层" → 模型直接 NaN。
>
> **这就是为什么 Transformer 需要残差连接和 LayerNorm**——它们让梯度能"短路"通过深层网络，避免消失/爆炸。

- 梯度消失 → 用 ReLU 替代 sigmoid、BatchNorm、残差连接
- 梯度爆炸 → 梯度裁剪（Gradient Clipping）

> ⚠️ **常见陷阱**：很多初学者以为只要多堆层就能提高性能。结果 50 层网络准确率还不如 5 层——为什么？梯度消失了。先理解"为什么深层网络难训练"，再学"残差连接如何解决这个问题"。

> ✅ **Self-Check**：
> 1. 如果梯度消失，参数更新会发生什么？（参数几乎不更新，训练停滞）
> 2. 为什么 sigmoid 比 ReLU 更容易导致梯度消失？（sigmoid 两端导数≈0）

今日思考题
- 如果网络有 100 层，每层梯度都乘 0.8，第一层的梯度和最后一层的梯度
差多少？0.8^99 ≈ 2.5×10^-10 —— 这就是梯度消失的数学本质。

### 晚上电脑 · 2 小时
任务：用纸笔 + 代码验证一个 2 层 MLP 的反向传播

> 🎯 今晚你要做一件"硬核"的事：**不用 Autograd**，纯手动计算一个 2 层 MLP 的每个梯度，然后用 Autograd 验证——你的手动计算和 PyTorch 的自动计算结果必须一致（差异 < 10^-10）。

建文件 backprop_from_scratch.py：

```python
  import torch
  import torch.nn.functional as F

# 固定随机种子
torch.manual_seed(42)

# 小规模数据：2层 MLP，从零实现反向传播
n, d_in, d_hidden, d_out = 4, 3, 5, 2
X = torch.randn(n, d_in)
y = torch.randn(n, d_out)

# ----- 参数 -----
w1 = torch.randn(d_in, d_hidden, requires_grad=False) * 0.1
b1 = torch.zeros(d_hidden, requires_grad=False)
w2 = torch.randn(d_hidden, d_out, requires_grad=False) * 0.1
b2 = torch.zeros(d_out, requires_grad=False)

# ====== 前向传播（手动）======
z1 = X @ w1 + b1          # (4, 3) @ (3, 5) = (4, 5)
a1 = F.relu(z1)           # (4, 5)
z2 = a1 @ w2 + b2         # (4, 5) @ (5, 2) = (4, 2)
loss = F.mse_loss(z2, y)

# ====== 反向传播（手动推导 + 代码实现）======

# ① ∂L/∂z2
d_z2 = 2 * (z2 - y) / (n * d_out)  # MSE 对 z2 的梯度
#     = (2/n*d_out) * (z2 - y)

# ② ∂L/∂w2 = a1^T @ d_z2
d_w2 = a1.T @ d_z2  # (5, 4) @ (4, 2) = (5, 2)
d_b2 = d_z2.sum(dim=0)  # (2,)

# ③ ∂L/∂a1 = d_z2 @ w2^T
d_a1 = d_z2 @ w2.T  # (4, 2) @ (2, 5) = (4, 5)

# ④ ∂L/∂z1 = d_a1 * ReLU'(z1)
d_z1 = d_a1 * (z1 > 0).float()  # ReLU 导数：>0 时为 1，否则为 0

# ⑤ ∂L/∂w1 = X^T @ d_z1
d_w1 = X.T @ d_z1  # (3, 4) @ (4, 5) = (3, 5)
d_b1 = d_z1.sum(dim=0)  # (5,)

print("手动计算的梯度:")
print(f"  d_w1 shape: {d_w1.shape}")
print(f"  d_w2 shape: {d_w2.shape}")

# ====== 用 PyTorch Autograd 验证 ======
w1_a = w1.clone().requires_grad_(True)
b1_a = b1.clone().requires_grad_(True)
w2_a = w2.clone().requires_grad_(True)
b2_a = b2.clone().requires_grad_(True)

z1_a = X @ w1_a + b1_a
a1_a = F.relu(z1_a)
z2_a = a1_a @ w2_a + b2_a
loss_a = F.mse_loss(z2_a, y)
loss_a.backward()

# 验证：手动计算 vs Autograd
print(f"\nw1 梯度差异: {(d_w1 - w1_a.grad).abs().max():.10f}")
print(f"w2 梯度差异: {(d_w2 - w2_a.grad).abs().max():.10f}")
print(f"b1 梯度差异: {(d_b1 - b1_a.grad).abs().max():.10f}")
print(f"b2 梯度差异: {(d_b2 - b2_a.grad).abs().max():.10f}")
# 所有差异应接近 0

```
> 🎉 **如果所有差异都接近 0**，你刚刚完成了深度学习中最"硬核"的练习——手动推导并实现了反向传播！你现在知道每个 `loss.backward()` 背后到底在算什么了。面试被问到"反向传播是什么"，你可以直接在白板上推导这个 2 层 MLP。

- [ ] 今日完成检查
- [ ] 2 层 MLP 反向传播手动推导 + 代码实现
- [ ] 手动梯度和 Autograd 一致（差异 ≈ 0）
- [ ] 能用链式法则解释反向传播的每一步
### 第12周 · 星期二：Dropout + BatchNorm + LayerNorm
---
### 手机摸鱼 · 上午 30 分钟
阅读主题：正则化与归一化

> 🧠 **为什么学这个？**
> Dropout、BatchNorm、LayerNorm 是深度学习训练稳定性的"三驾马车"。没有它们，深层网络的训练就像在走钢丝——随时可能掉下来。Transformer 架构中 LayerNorm 更是无处不在。

核心知识点

**1. Dropout（随机失活）**

训练时，每个神经元以概率 p 被"关闭"（输出置为 0）。
每个 batch 关掉的神经元不同 → 相当于每次训练不同的子网络。

> 🎭 **"断臂求生"类比**：
> 想象你在训练一个乐团（神经网络）。每次排练（训练），你随机让几个乐手"闭嘴"（Dropout）。结果是每个人都不能依赖别人的声音——必须自己把谱子练熟。正式演出时（测试），所有人上场，默契十足。
>
> Dropout 阻止了神经元之间的"共谋"（co-adaptation）——每个神经元必须自己学到有用的特征，不能指望"邻居会补我的缺"。

为什么有效？
- 防止神经元之间"共谋"（co-adaptation）
- 等同于训练多个子网络并取平均（集成学习的效果）

测试时：不关闭任何神经元，但权重乘以 (1-p) 来补偿。

重要：Dropout 只在训练时生效！model.train() / model.eval()
影响 Dropout 的行为。

> ⚠️ **常见陷阱**：忘记 `model.eval()` 就来评估——Dropout 还在随机丢神经元 → 结果不稳定，准确率偏低。这在面试中也是一道常见题："为什么你的模型在训练和测试时表现差这么多？"

**2. BatchNorm vs LayerNorm（面试高频考点！）**

BatchNorm：在 batch 维度做归一化
LayerNorm：在 feature 维度做归一化

> 📊 **用 ASCII 可视化理解 BN vs LN**：
>
> 输入 (batch=3, features=4)：
> ```
>        feat1 feat2 feat3 feat4
> 样本1  [ 2     5     1     8  ]
> 样本2  [ 4     3     7     2  ]   ← BatchNorm：对每列做归一化
> 样本3  [ 6     1     9     4  ]       比如 feat1 的均值 = (2+4+6)/3 = 4
>                                        对 [2,4,6] 归一化
>
>        feat1 feat2 feat3 feat4
> 样本1  [ 2     5     1     8  ] ← LayerNorm：对每行做归一化
> 样本2  [ 4     3     7     2  ]     比如样本1 的均值 = (2+5+1+8)/4 = 4
> 样本3  [ 6     1     9     4  ]     对 [2,5,1,8] 归一化
> ```
>
> - BN："这个特征在所有样本中的均值是多少？"——依赖 batch
> - LN："这个样本在所有特征上的均值是多少？"——不依赖 batch

假设输入是 (batch=32, features=128)：

BatchNorm：对每个 features，用 32 个样本的均值和方差归一化
LayerNorm：对每个样本，用 128 个 features 的均值和方差归一化

为什么 Transformer 用 LayerNorm 不用 BatchNorm？
① NLP 的 batch 大小通常较小（受显存限制），小 batch 下 BN 不稳定
② 文本长度不固定，BN 需要 padding mask 处理，LN 天然支持
③ LN 对 batch size 不敏感，训练和推理行为一致

**3. LayerNorm 的训练/推理区别**

训练时：用当前 batch 的均值/方差
推理时：用训练时累积的 running mean/var（和 BatchNorm 一样）

> 💡 **Aha Moment**：LayerNorm 之所以在 Transformer 中"赢了"BN，是因为它天然适合序列数据。每个位置的归一化只依赖它自己，不需要等 batch 里的其他样本——这让它在 batch_size=1 时也能正常工作。这就是为什么大模型推理时（逐 token 生成）不受影响。

> ✅ **Self-Check**：
> 1. Dropout 在训练和测试时的行为有什么不同？
> 2. 如果 batch_size=1，BatchNorm 还能工作吗？LayerNorm 呢？

### 晚上电脑 · 2 小时
任务 1：实现 Dropout 并验证效果

```python
  class MyDropout(nn.Module):
      def __init__(self, p=0.5):
          super().__init__()
          self.p = p

def forward(self, x):
          if self.training:
              mask = (torch.rand_like(x) > self.p).float()
              return x * mask / (1 - self.p)  # 除以 (1-p) 补偿
          return x

# 验证 train/eval 模式的区别
drop = MyDropout(p=0.5)
x = torch.ones(1000)

drop.train()
train_out = drop(x)
print(f"训练模式，非零比例: {(train_out > 0).float().mean():.3f}")  # ≈ 0.5

drop.eval()
eval_out = drop(x)
print(f"评估模式，均值: {eval_out.mean():.3f}")  # ≈ 1.0

```
> 🔑 Dropout 除以 (1-p) 的原因：训练时一半神经元被关，总信号减半。除以 (1-p) 保持信号总强度不变，测试时就不需要任何补偿（直接原样输出）。

任务 2：对比 BN vs LN 的实验

训练 3 个相同的 MLP：
- 无归一化
- 带 BatchNorm
- 带 LayerNorm
对比收敛速度和最终准确率。

- [ ] 今日完成检查
- [ ] Dropout 手写实现，train/eval 模式切换正确
- [ ] BatchNorm vs LayerNorm 的区别能说清楚（面试题）
### 第12周 · 星期三-六：权重初始化 + 梯度裁剪 + 混合精度
---
### 星期三
权重初始化实验

> 🧠 **为什么学这个？**
> 参数初始值决定了训练的"起跑线"。错误的初始化 = 梯度一开始就消失/爆炸 = 模型永远训练不起来。Xavier 和 Kaiming 是两位研究者用数学推导出的"最佳起跑线"。

Xavier 初始化 vs Kaiming 初始化 vs 随机小值
验证不同初始化对训练速度的影响

> 💡 **Aha Moment**：Kaiming 初始化就是为 ReLU 设计的。因为 ReLU 会"砍掉"一半的激活值（负值变成 0），Kaiming 把方差放大 2 倍来补偿。如果你用 sigmoid，用 Xavier；用 ReLU/GELU，用 Kaiming。选错初始化 = 自找麻烦。

### 星期四
梯度裁剪 + Warmup
```python
    # Warmup：前 N 步学习率从 0 线性增长到目标值
    def warmup_lr(step, warmup_steps, target_lr):
        if step < warmup_steps:
            return target_lr * step / warmup_steps
        return target_lr

# 梯度裁剪：防止梯度爆炸
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

```
> 🔥 **Warmup 的直觉**：训练刚开始时，参数是随机的，梯度可能非常大。如果直接用目标学习率，一步就"迈出大气层"。Warmup 让学习率从 0 慢慢涨到目标值——给模型一个"热身"的机会。这个技巧在训练 Transformer 时**几乎是必须的**。

### 星期五
混合精度训练（AMP）


```python
    from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()
with autocast():  # 自动用 fp16 计算（更快）
        output = model(x)
        loss = criterion(output, y)

```
scaler.scale(loss).backward()
scaler.step(optimizer)
scaler.update()

> 🚀 **为什么 AMP 让你"白嫖"速度**：现代 GPU 的 fp16 算力是 fp32 的 8-16 倍。autocast 自动判断哪些操作用 fp16（安全且快），哪些用 fp32（需要精度）。GradScaler 解决"小梯度在 fp16 中下溢（变成 0）"的问题——把 loss 先放大再 backprop，梯度也跟着放大了。

### 星期六
深度学习调参完整实验
固定模型，系统调 4 个超参数：
lr × batch_size × dropout × weight_decay
输出调参报告 + Wandb 对比图

> 🎉 **第 12 周完成！** 你现在理解了深度学习的"心脏"（反向传播）、"免疫系统"（正则化）、"稳定器"（归一化）、"加速器"（AMP）。这些都是训练任何一个神经网络——包括 Transformer——的基本功。

- [ ] 第12周完成检查
- [ ] 反向传播能手动推导 2 层 MLP
- [ ] Dropout/BN/LN 手写实现
- [ ] 梯度裁剪 + AMP 会用
### 第13周 · 主题：深度学习进阶


-  本周目标：用 CNN/LSTM 做真实任务 ──
> 本周把深度学习应用到真实数据上。CNN 做图像，LSTM 做文本。你会发现：不同的数据形式（图像 vs 文本）需要不同的网络结构，但**训练循环完全一样**——因为那 5 行核心代码是通用的。

第13周 · 星期一：CNN 做 CIFAR-10（自定义数据集）

手机摸鱼：
CNN 核心组件：Conv2d（卷积提取特征）→ ReLU（非线性）→ MaxPool2d（降采样）
多层堆叠：浅层学边缘/纹理，深层学形状/语义
关键参数：kernel_size（卷积核大小）、stride（步长）、padding（填充）

> 🔍 **卷积 vs 全连接**：全连接层每个输出看所有输入（参数爆炸），卷积层每个输出只看一个小窗口（参数共享）。一张 224×224 的图片如果全连接，第一个隐藏层就需要 224×224×3×256 ≈ 3800 万个参数；用卷积只需 3×3×3×256 ≈ 7000 个参数。

带数据增强的 CNN：
```python
from torchvision import transforms

train_transform = transforms.Compose([
    transforms.RandomHorizontalFlip(p=0.5),   # 随机翻转（数据增强！）
    transforms.RandomCrop(32, padding=4),     # 随机裁剪
    transforms.ToTensor(),
    transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2470, 0.2435, 0.2616))
])
# 数据增强是防止过拟合最有效的手段之一，比调参更有效
```

> 💡 **Aha Moment**：数据增强本质上是在"免费制造更多训练数据"。你把每张图水平翻转一下 → 数据量翻倍。模型学到的是"这可能是猫，不管它朝左还是朝右"——鲁棒性自然提升。这也是为什么数据增强比调参更能防止过拟合。

第13周 · 星期二：RNN / LSTM 做文本情感分类

手机摸鱼：
RNN 循环：h_t = tanh(W_h·h_{t-1} + W_x·x_t)
问题：长序列梯度消失 → 记不住远距离依赖

> 🔁 **RNN 的本质**：不是"看到整个句子然后理解"，而是"一个字一个字地读，心里不断更新理解"。当前理解 h_t = 之前理解 h_{t-1} + 当前的词 x_t。RNN 的问题：读第 100 个字时，第 1 个字的影响已经被连乘了 99 次——要么消失（<1），要么爆炸（>1）。

LSTM 改进：引入"门控"机制（遗忘门/输入门/输出门），选择性记忆

> 🧠 **LSTM 的"记忆管理"类比**：
> 你在读一本长篇小说。读到第 500 页时：
> - 遗忘门："第 3 页那个路人的名字不重要，忘了它"
> - 输入门："主角今天发现的关键线索很重要，记住"
> - 输出门："现在该用哪些记忆来理解当前情节"
>
> LSTM 用这三个"门"来管理长距离信息流，解决了 RNN "记不住远距离依赖"的问题。

晚上代码：用真实中文数据集（如 ChnSentiCorp）训练 LSTM 分类器


```python
  class LSTMClassifier(nn.Module):
      def __init__(self, vocab_size, embed_dim, hidden_dim, num_classes):
          super().__init__()
          self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
          self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True,
                              bidirectional=True, dropout=0.3, num_layers=2)
          self.fc = nn.Sequential(
              nn.Linear(hidden_dim * 2, hidden_dim),
              nn.ReLU(), nn.Dropout(0.3),
              nn.Linear(hidden_dim, num_classes)
          )

def forward(self, x, lengths):
          # x: (batch, seq_len)
          embedded = self.embedding(x)
          # pack_padded_sequence 跳过 padding，加速计算
          packed = nn.utils.rnn.pack_padded_sequence(
              embedded, lengths.cpu(), batch_first=True, enforce_sorted=False)
          lstm_out, (h_n, c_n) = self.lstm(packed)
          # 取两个方向最后一层的 hidden state
          last_hidden = torch.cat([h_n[-2], h_n[-1]], dim=-1)  # (batch, hidden*2)
          return self.fc(last_hidden)

```
第13周 · 星期三：GRU 对比 LSTM

手机摸鱼：
GRU = LSTM 的简化版：合并遗忘门和输入门为"更新门"
参数量少 25%，训练更快，效果相当（小数据集上甚至更好）

> 🔑 **GRU vs LSTM**：LSTM 有 3 个门（遗忘/输入/输出），GRU 只有 2 个（重置/更新）。少一个门 = 少 25% 参数 = 更快训练。在小数据集上，GRU 甚至可能比 LSTM 更好（因为参数少 → 不容易过拟合）。大模型时代大家更爱用 Transformer，但在资源受限场景（如手机端），GRU 仍然是王者。

晚上：用相同数据、相同超参对比 LSTM vs GRU 的速度和准确率

第13周 · 星期四：AMP 混合精度原理 + PyTorch Lightning

手机摸鱼：
为什么 fp16 更快？现代 GPU（如 3090/A100）的 fp16 算力是 fp32 的 8-16 倍。
为什么不能全用 fp16？梯度下溢：小梯度在 fp16 中变成 0 → 参数不更新。
GradScaler：在 backward 前把 loss 放大（scale），backward 后再缩小（unscale），
这样小梯度就不会在 fp16 中下溢。

PyTorch Lightning：把训练循环抽象掉，只保留模型的 forward + configure_optimizers。
Trainer 自动处理 device/checkpoint/logging/multi-GPU。



```python
  # AMP 原理验证：观察 fp16 和 fp32 的数值差异
  x_fp32 = torch.tensor(1e-8, dtype=torch.float32)
  x_fp16 = torch.tensor(1e-8, dtype=torch.float16)
  print(f"fp32: {x_fp32.item():.15f}")  # 1e-8（保留）
  print(f"fp16: {x_fp16.item():.15f}")  # 0.0（下溢！）
  # 这就是为什么需要 GradScaler——防止小梯度在 fp16 中变成 0

```
第13周 · 星期五-六：GPU 显存管理 + 综合项目

星期五手机：了解 OOM 原因和处理
显存占用 = 模型参数 + 梯度 + 优化器状态 + 中间激活（activations）
Adam 优化器占用 = 模型参数的 2 倍（m 和 v 两个状态）
训练时总显存 ≈ 模型参数 × 4（前向+反向+优化器×2）+ batch 相关

> 📊 **显存账单（以 BERT-base 为例，110M 参数）：**
> - 模型参数：110M × 4 bytes (fp32) ≈ 440 MB
> - 梯度：440 MB（和参数一样大）
> - Adam 优化器状态：440 × 2 = 880 MB（m 和 v）
> - 中间激活（batch=16, seq=512）：≈ 8 GB
> - 总计 ≈ 10 GB → 需要至少 12GB 显存的 GPU
>
> 这就是为什么大模型训练要几十上百张 GPU——显存不是存参数的，是存"中间激活"的。

星期五晚上 + 星期六：
综合 DL 项目：图像分类或文本分类，包含以下完整流程
① 数据加载（自定义 Dataset）→ ② 数据增强 → ③ 模型定义
→ ④ 训练循环（AMP + gradient clipping）→ ⑤ Wandb 监控
→ ⑥ Checkpoint 保存/加载 → ⑦ 测试集评估 → ⑧ 混淆矩阵可视化



```python
  # 显存诊断工具
  print(torch.cuda.memory_summary())  # 详细显存报告
  print(f"已分配: {torch.cuda.memory_allocated()/1e9:.2f} GB")
  print(f"已缓存: {torch.cuda.memory_reserved()/1e9:.2f} GB")

# OOM 处理策略（优先级从高到低）
# 1. 减小 batch_size（最直接）
# 2. 启用 gradient_accumulation（小 batch 多步累积再更新）
# 3. 减小模型（hidden_dim 或 n_layers）
# 4. 用 fp16/bf16（省一半显存）
# 5. 用 gradient checkpointing（牺牲 20% 速度节省激活显存）

```
> 🎉 **第 13 周完成！** CNN 做图像、LSTM/GRU 做文本、AMP 加速、OOM 处理——你已经能独立完成一个深度学习项目了。更重要的是，你看到了"训练循环是通用的"：不管模型是 CNN、RNN 还是 Transformer，那 5 行核心代码不变。

- [ ] 第13周完成检查
- [ ] CNN 能处理带数据增强的自定义数据集
- [ ] LSTM/GRU 情感分类跑通，能对比效果
- [ ] 理解 AMP 原理 + 能处理 OOM
- [ ] 综合 DL 项目完成并 push
### 第14周 · 主题：NLP 基础 + BERT Fine-tune


-  本周目标：掌握 NLP 标准工具链 ──
> 本周是 Transformer 前的"NLP 热身"。你会学到文本怎么变成数字（tokenizer、词向量），以及如何用预训练模型（BERT、GPT-2）。这些是第 15 周手写 Transformer 之后你马上会做的事——"现在我知道里面怎么工作了，让我用它解决真实问题"。

### 星期一
文本预处理完整 pipeline
手机摸鱼：
中文分词难点：不像英文有空格分隔。jieba 是最常用中文分词库。
去停用词：的/了/是/在... 这些高频但对语义贡献小的词。
TF-IDF = 词频 × log(总文档数/包含该词的文档数)，用于找"重要但不常见"的词。

```python
  import jieba, re
  from collections import Counter

def preprocess_chinese(text):
# 1. 去除非中文字符
      text = re.sub(r'[^\u4e00-\u9fff]', ' ', text)
      # 2. 分词
      words = jieba.lcut(text)
      # 3. 去停用词
      stopwords = set(['的', '了', '在', '是', '我', '有', '和', '就',
                       '不', '人', '都', '一', '一个', '上', '也', '很', '到'])
      words = [w for w in words if w not in stopwords and len(w) > 1]
      return words

# 测试
text = "自然语言处理是人工智能的一个重要方向，近年来发展迅速"
print(preprocess_chinese(text))
# ['自然语言', '处理', '人工智能', '一个', '重要', '方向', '近年', '发展', '迅速']

```
### 星期二
Word2Vec / GloVe 词向量
手机摸鱼：
独热编码：词表 5 万 → 每个词是 5 万维向量（极度稀疏，无法表达语义）
词向量：把每个词映射到低维稠密空间（如 300 维），语义相近的词向量也相近
king - man + woman ≈ queen（向量运算表达了语义关系！）

> 🌍 **词向量的魔法**：想象一个 300 维的空间。在这个空间里：
> - "国王"和"王后"靠得很近
> - "国王 - 男人 + 女人"的坐标恰好落在"王后"附近
> - "北京 - 中国 + 法国" ≈ "巴黎"
>
> 这不是人为指定的——是模型从大量文本中"自动"学到的。这就是**分布式表示**的力量：词的"意思"被分布到了向量的每个维度上，而不是某个具体的符号。

```python
  import gensim.downloader as api

# 加载预训练词向量
wv = api.load('glove-wiki-gigaword-100')  # 100 维，约 400MB
# 或中文：wv = api.load('glove-wiki-gigaword-100')  # 无官方中文版，可用 Tencent AI Lab 的

# 语义相似度
print(wv.similarity('king', 'queen'))      # ~0.75
print(wv.similarity('king', 'computer'))   # ~0.1

# 类比推理
print(wv.most_similar(positive=['king', 'woman'], negative=['man'], topn=3))
# [('queen', ...), ('princess', ...), ...]

# 不匹配词
print(wv.doesnt_match(['apple', 'banana', 'car', 'orange']))  # car

```
### 星期三
Tokenizer 原理（BPE 深度）
手机摸鱼：
BPE 步骤：
① 把所有词拆成字符：hello → h e l l o
② 统计所有相邻字符对的出现频率
③ 选择最高频的一对合并为一个新 token
④ 重复 N 次（N 是词表大小）

为什么好？未登录词（训练时没见过的词）可以被拆成已知的子词。
"unhappiness" → "un" + "happiness" → 模型能猜出意思。

> 💡 **Aha Moment**：BPE 解决了 NLP 中最头疼的问题——词表之外的词。传统的词级别 tokenizer 看到新词只能标为 [UNK]。但 BPE 把"unbelievable"拆成 "un" + "believe" + "able"——三个子词模型都见过，组合起来就能理解新词。这就是为什么现代 LLM 全部使用子词 tokenizer。

```python
  # 用 HuggingFace tokenizer 实验
  from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-chinese")
text = "我喜欢学习人工智能"
tokens = tokenizer.tokenize(text)
print(tokens)  # ['我', '喜', '欢', '学', '习', '人', '工', '智', '能']
ids = tokenizer.convert_tokens_to_ids(tokens)
print(ids)
restored = tokenizer.decode(ids)
print(restored)  # 我 喜 欢 学 习 人 工 智 能（空格分隔）

```
> ⚠️ **为什么中文 BERT 把每个字都拆开了？** 因为 BERT 中文版用的是字级别的 BPE（Character-level）。这不是 bug，是设计选择——中文"词"的边界模糊，"人工智能"是"人工"+"智能"还是"人"+"工"+"智能"？字级别避免了分词歧义。

### 星期四
BERT Fine-tune 文本分类（完整版）

> 🧠 **BERT 是什么？** Encoder-Only Transformer。它不生成文本，而是"理解"文本——给一个句子，输出每个词的高质量向量表示。Fine-tune = 在预训练 BERT 上面加一个小分类头，用你的数据微调一下 → 世界级的文本分类器。

```python
  from transformers import AutoTokenizer, AutoModelForSequenceClassification
  from transformers import Trainer, TrainingArguments, EarlyStoppingCallback
  from datasets import Dataset
  import numpy as np
  from sklearn.metrics import accuracy_score, f1_score

def compute_metrics(eval_pred):
logits, labels = eval_pred
preds = np.argmax(logits, axis=1)
return {"accuracy": accuracy_score(labels, preds),
"f1": f1_score(labels, preds, average='macro')}

model_name = "bert-base-chinese"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

def tokenize_fn(examples):
return tokenizer(examples["text"], padding=True, truncation=True, max_length=256)

# 假设已有 train_texts, train_labels, test_texts, test_labels
train_dataset = Dataset.from_dict({"text": train_texts, "label": train_labels})
test_dataset = Dataset.from_dict({"text": test_texts, "label": test_labels})
train_dataset = train_dataset.map(tokenize_fn, batched=True)
test_dataset = test_dataset.map(tokenize_fn, batched=True)

training_args = TrainingArguments(
output_dir="./bert-finetuned",
num_train_epochs=5,
per_device_train_batch_size=16,
per_device_eval_batch_size=64,
evaluation_strategy="epoch",    # 每个 epoch 评估一次
      save_strategy="epoch",          # 每个 epoch 保存
      load_best_model_at_end=True,    # 训练完加载最佳模型
      metric_for_best_model="f1",
      logging_dir="./logs",
      logging_steps=50,
      fp16=torch.cuda.is_available(), # 有 GPU 就用混合精度
  )

trainer = Trainer(
model=model,
args=training_args,
train_dataset=train_dataset,
eval_dataset=test_dataset,
compute_metrics=compute_metrics,
callbacks=[EarlyStoppingCallback(early_stopping_patience=2)]
)

trainer.train()
print(trainer.evaluate())
```
trainer.save_model("./bert-finetuned-best")

> 🎉 **你用不到 50 行代码完成了一个 BERT fine-tune 项目！** 这就是 HuggingFace 的力量——它把模型架构、tokenizer、训练循环全部封装好了，你只需要提供数据。但下周你要打开这个"黑盒子"，亲手实现 BERT 内部的核心——Transformer。

### 星期五
GPT-2 文本生成

> 🧠 **GPT-2 是什么？** Decoder-Only Transformer。和 BERT 相反——它不看全部输入，只看"之前"的内容，逐个预测下一个词。这就是 ChatGPT 的"祖先"——核心架构是一样的（都是 Decoder-Only），只是规模大了 1000 倍。

```python
  from transformers import GPT2LMHeadModel, GPT2Tokenizer

model = GPT2LMHeadModel.from_pretrained("uer/gpt2-chinese-cluecorpussmall")
tokenizer = GPT2Tokenizer.from_pretrained("uer/gpt2-chinese-cluecorpussmall")

def generate(prompt, max_length=100, temperature=0.8, top_p=0.9):
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(
**inputs,
max_length=max_length,
temperature=temperature,   # 控制随机性：低=保守，高=疯狂
          top_p=top_p,               # nucleus sampling
          do_sample=True,
          pad_token_id=tokenizer.eos_token_id,
          no_repeat_ngram_size=2,    # 避免重复
      )
      return tokenizer.decode(outputs[0], skip_special_tokens=True)

print(generate("人工智能的未来是"))

```
> 🎲 **temperature 和 top_p**：temperature=0 → 每次选概率最高的词（确定性，可能无聊）。temperature=1 → 按原始概率分布采样（自然）。temperature=2 → 概率分布被"拉平"，更随机（可能胡说八道）。top_p (nucleus sampling) 是当前最流行的采样策略——只从累积概率达到 p 的词中选，自动过滤"明显不对"的词。

### 星期六 · 3.5h
NLP 综合实战
选一个任务：新闻分类/情感分析/意图识别
完整流程：数据加载→预处理→Tokenizer→Trainer训练→评估→推理→部署
push 到 GitHub + README

> 🎉 **第 14 周完成！** 你现在能用 HuggingFace fine-tune BERT 做分类，用 GPT-2 生成文本，理解 tokenizer 的内部机制。更重要的是——下周你会亲手实现这些模型内部的核心：**Transformer**。不再"调包"，而是"造轮子"。

- [ ] 第14周完成检查
- [ ] 文本预处理 pipeline 能独立编写
- [ ] 词向量语义运算理解
- [ ] BERT fine-tune 完整流程跑通（含 early stopping + 最佳模型保存）
- [ ] GPT-2 生成能调 temperature/top_p 控制输出
### 第15周 · 主题：****★★**★** 手写 Transformer ****★★**★**


> 🏆 **这是整个 6 个月计划中最重要的 1 周。**
>
> 目标：用纯 PyTorch 从零手写一个 Transformer，
> 不使用任何第三方库的 Transformer 实现。
>
> 之前 14 周的一切——梯度下降、Autograd、nn.Module、LayerNorm、反向传播——都是为了这一周准备的。
> 之后的一切——Fine-tune、LoRA、Agent、RAG——都建立在你对 Transformer 的理解之上。
>
>
> ## 🗺️ The Big Picture：为什么 Transformer 改变了世界？
>
> 在 Transformer（2017）之前，NLP 的主流是 RNN/LSTM。它们的问题是：
> - **串行处理**：第 10 个词必须等前 9 个词处理完才能开始 → 无法并行 → 训练慢
> - **长距离遗忘**：第 1 个词和第 100 个词之间隔着 99 次乘法 → 梯度消失
>
> Transformer 的核心创新是 **Self-Attention（自注意力）**：
> - **并行处理**：所有词同时计算互相之间的关系 → GPU 吃满
> - **直接连接**：任意两个词之间只有 O(1) 的路径 → 没有长距离遗忘
>
> 结果？Transformer 可以扩展到前所未有的规模。GPT-3 (1750 亿参数) → ChatGPT → GPT-4 ——都是 Transformer。
>
> 这一周，你将从零实现这个架构的每一个部分。当你做完，你不会再用"调包侠"的眼光看大模型——你会看到 Attention、残差连接、LayerNorm 在每一层里协同工作。
>
> > ⚠️ ️ **调试铁律（保存下来！）**：
> > 每写完一个模块，立即 `print(x.shape)` 确认维度。
> > Transformer 99% 的 bug 都是维度不匹配。
> > 报错 `"mat1 and mat2 shapes cannot be multiplied"` 时，
> > 检查 view/transpose/permute 的维度变换是否正确。
> > 常用排查命令：
> > ```python
> > print(f"期望: (batch, seq, d_model), 实际: {x.shape}")
> > ```
>
> ### 🐛 Debugging Transformer：5 个常见错误及排查方法
>
> **错误 #1：维度不匹配**
> 症状：`RuntimeError: mat1 and mat2 shapes cannot be multiplied (a×b and c×d)`
> 排查：从 `forward` 的第一行开始逐行 print shape。99% 是 transpose/view 搞错了维度顺序。
>
> **错误 #2：忘记 Mask**
> 症状：Decoder 生成的答案"提前看到了"后面的词 → 训练 loss 极低但推理完全没用。
> 排查：确认 `tgt_mask` 是上三角矩阵（未来位置为 0），且在 softmax 前用 `masked_fill(mask==0, -inf)`。
>
> **错误 #3：LayerNorm 放错位置**
> 症状：训练不稳定，loss 震荡大。
> 排查：Post-LN（原论文）= `LayerNorm(x + Sublayer(x))`，Pre-LN（现代）= `x + Sublayer(LayerNorm(x))`。确认你在用哪种。
>
> **错误 #4：Positional Encoding 没加上**
> 症状：模型输出和词序无关（"狗咬人"和"人咬狗"输出一样）。
> 排查：检查 PE 是否真的被 `x + pe` 了。
>
> **错误 #5：训练/推理模式忘记切换**
> 症状：推理时结果不稳定。
> 排查：`model.eval()` + `torch.no_grad()` 都有吗？Dropout 在 eval 模式下关了吗？
>
> ### 第15周 · 星期一：Scaled Dot-Product Attention
> ---
> ### 手机摸鱼 · 上午 30 分钟
> 阅读主题：Attention 机制 —— Transformer 的灵魂
>
> 核心知识点（反复读直到能背）
>
> **1. Attention 的直觉**
>
> 你在读一句话："我昨天去了那家餐厅，食物很好吃。"
>
> 当你要理解"食物"这个词时，你自然会关注"餐厅"和"好吃"。
> 你不会关注"昨天"这种无关的词。
>
> Attention 就是让模型学会"关注什么"。
>
> > 🧠 **为什么这如此重要？**
> > RNN 处理"食物"时，它的 hidden state 里混杂了"我"、"昨天"、"去了"……所有前面的词都搅在一起。Attention 让"食物"直接看到"餐厅"和"好吃"，不看"昨天"——干净、直接、高效。
>
> **2. Query、Key、Value —— 三要素**
>
> > 📚 **图书馆检索类比（这是理解 Attention 的最佳类比！）**
> >
> > 你去图书馆找关于"Transformer"的书：
> >
> > 1. 你脑中有一个**问题**："哪些书和 Transformer 相关？" ← 这是 **Query (Q)**
> > 2. 每本书的书脊上有一个**标题**，让你快速判断相关性 ← 这是 **Key (K)**
> > 3. 选好书之后，你读的**内容**才是真正有价值的信息 ← 这是 **Value (V)**
> >
> > **Attention 的计算过程**：
> > - 用你的 Q（问题）去和每本书的 K（标题）做"匹配" → 得到相关度分数
> > - 相关度分数经过 softmax → 变成百分比（你把注意力分给哪些书）
> > - 用这些百分比作为权重，对 V（书的内容）加权求和 → 得到"综合理解"
> >
> > 在这个类比里：
> > - 如果 Q 和某个 K 非常匹配 → 注意力权重高 → 那本书的 V 被大量提取
> > - 如果不匹配 → 注意力权重≈0 → 那本书的 V 几乎被忽略

Query (Q)：我要查什么？（当前词在问：谁和我有关？）
Key   (K)：我是什么？（每个词在喊：我在这里！我长这样！）
Value (V)：我有什么信息？（每个词的内容）

注意力计算：用 Q 去"查询"每个 K，得到的"匹配分数"
作为权重，对 V 加权求和。

**3. Scaled Dot-Product Attention 公式（背下来！）**

Attention(Q, K, V) = softmax(QK^T / √d_k) × V

分解理解：
① Q @ K^T ：计算每对词之间的"相关程度"矩阵
(batch, seq_len, d_k) @ (batch, d_k, seq_len) → (batch, seq_len, seq_len)
结果矩阵的 [i][j] 位置 = 词 i 对词 j 的 attention 分数

② / √d_k ：缩放。为什么？
d_k 很大时，QK^T 的值很大 → softmax 后梯度接近 0 → 学不动
除以 √d_k 把方差拉回 1。

> 🔢 **为什么是 √d_k？（一个直观解释）**
> 假设 Q 和 K 的每个元素独立、均值 0 方差 1 → QK^T 的每个元素是 d_k 个随机变量的和 → 方差 = d_k → 标准差 = √d_k
> 除以 √d_k 相当于把方差"标准化"回 1，让 softmax 不饱和。
> 如果不除：d_k=64 → QK^T 的值范围 ±80 → softmax 几乎只有 0 和 1 → 梯度≈0 → 学不动。

③ softmax ：把分数变成"概率"（每行和为 1）
第 i 行的第 j 列 = 词 i 应该给词 j 多少"注意力"

④ @ V ：按注意力权重从 V 中提取信息
(batch, seq, seq) @ (batch, seq, d_v) → (batch, seq, d_v)

> 📐 **维度追踪 —— 用 ASCII 画出来（保存这张图！）：**
>
> 假设：batch=2, seq_len=4, d_k=4
>
> ```
> Step ①:  Q @ K^T
> Q:  (2, 4, 4)    @    K^T: (2, 4, 4)
>     batch─┘││         batch─┘││
>       seq─┘│            seq─┘│  (transposed: last two dims swapped)
>        d_k─┘             d_k─┘
>                        = (2, 4, 4)     ← (batch, seq_len, seq_len)
>                        scores[i,j] = 第i个Q词和第j个K词的相关度
> 
> Step ②:  / √d_k
> scores / √4 = scores / 2       ← 形状不变
> 
> Step ③:  softmax(dim=-1)
> 每行变成概率分布（和为1）        ← 形状不变
> 
> Step ④:  @ V
> (2, 4, 4) @ (2, 4, 4) = (2, 4, 4) ← 和 Q 形状一样！
> ```
>
> **关键观察**：输出形状 = Q 的形状。Attention 不改变维度——它只是按相关性重新"混合"了 V 的信息。

维度对照表（一定要记住！）

假设：batch=2, seq_len=4, d_model=8, num_heads=2
那么 d_k = d_model / num_heads = 4

Q: (2, 4, 4)    ← (batch, seq_len, d_k)
K: (2, 4, 4)
V: (2, 4, 4)

QK^T: (2, 4, 4) @ (2, 4, 4)^T = (2, 4, 4)
softmax(QK^T/√4): (2, 4, 4)   ← 每行和为 1
output: (2, 4, 4) @ (2, 4, 4) = (2, 4, 4)  ← 和 Q 形状一样！

> ✅ **Self-Check**（离开手机前）：
> 1. Q 和 K 的作用分别是什么？
> 2. 为什么要除以 √d_k？
> 3. softmax 沿哪个维度做？（dim=-1，即最后一个维度）

### 晚上电脑 · 2 小时
任务：手写 Scaled Dot-Product Attention！

```python
  import torch
  import torch.nn as nn
  import torch.nn.functional as F
  import math

class ScaledDotProductAttention(nn.Module):
"""手写注意力：Attention(Q,K,V) = softmax(QK^T/√d_k)V"""

def __init__(self, dropout=0.1):
          super().__init__()
          self.dropout = nn.Dropout(dropout)

def forward(self, Q, K, V, mask=None):
          """
          Q, K, V: (batch, n_heads, seq_len, d_k)
          mask: (batch, 1, seq_len, seq_len) or None
          """
          d_k = Q.size(-1)

# ① Q @ K^T / √d_k
          scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(d_k)
          # scores: (batch, n_heads, seq_len, seq_len)

# ② mask（可选：Decoder 需要遮住未来位置）
          if mask is not None:
              scores = scores.masked_fill(mask == 0, float('-inf'))

# ③ softmax
          attention_weights = F.softmax(scores, dim=-1)
          attention_weights = self.dropout(attention_weights)

# ④ 加权求和
          output = torch.matmul(attention_weights, V)
          return output, attention_weights

# ========== 验证 ==========
batch, seq_len, d_model, n_heads = 2, 4, 8, 2
d_k = d_model // n_heads  # 4

Q = torch.randn(batch, n_heads, seq_len, d_k)
K = torch.randn(batch, n_heads, seq_len, d_k)
V = torch.randn(batch, n_heads, seq_len, d_k)

attn = ScaledDotProductAttention()
output, weights = attn(Q, K, V)

print(f"输出形状: {output.shape}")     # (2, 2, 4, 4)
print(f"注意力权重形状: {weights.shape}")  # (2, 2, 4, 4)
print(f"每行权重和（应接近1）:\n{weights[0,0].sum(dim=-1)}")

```
> 🎉 **第一个模块完成！** Attention 是 Transformer 的心脏。你现在理解了 Q/K/V 的含义、为什么除以 √d_k、注意力权重怎么算。剩下的模块都是在这个基础上搭建的。

- [ ] 今日完成检查
- [ ] Attention 公式能默写：softmax(QK^T/√d_k)V
- [ ] 代码跑通，输出形状正确
- [ ] 理解 d_k 为什么是 d_model/num_heads
- [ ] 能用"图书馆检索"类比解释 Q/K/V
### 第15周 · 星期二：Multi-Head Attention
---
### 手机摸鱼
核心知识点

> 🧠 **为什么学这个？**
> 单头注意力：每个词只能用一种方式关注其他词。但语言是多维的——语法、语义、指代、情感...一个好的表示需要从多个"角度"同时关注。

**1. 为什么需要多头？**

单头注意力：每个词只能以一种方式"关注"其他词。
多头注意力：并行计算多个"注意力视角"。

> 🏛️ **"委员会"类比**：
> 一个只有 1 人的评审委员会（单头）评审论文时，只能看到论文的一个方面。
> 但如果有一个 8 人的委员会（8 头），每个人有不同的专业背景：
> - 头 1（语法专家）：关注主语-谓语-宾语关系
> - 头 2（语义专家）：关注同义词、近义词
> - 头 3（位置专家）：关注"前面提到的"指代关系
> - 头 4（情感专家）：关注情感词和修饰关系
> - 头 5-8：关注其他我们还不知道的模式（模型自己学出来的！）
>
> 最后，8 个人的意见被整合成一个综合评估——这就是 Multi-Head Attention。

比如：
头 1：关注语法关系（主语-谓语）
头 2：关注语义关系（同义词）
头 3：关注位置关系（前后文）
头 4：关注...

**2. Multi-Head Attention 的计算步骤**

① 将 Q, K, V 分别投影 h 次（h = num_heads）
Q → [Q₁, Q₂, ..., Qₕ]  （每个是 d_k = d_model/h 维）
K → [K₁, K₂, ..., Kₕ]
V → [V₁, V₂, ..., Vₕ]

② 每个头独立执行 Attention(Qᵢ, Kᵢ, Vᵢ)

③ 将所有头的输出拼接 → 再经一次线性投影

> 📐 **维度变换全景图**：
> 
> ```
> 输入:     (batch=2, seq=4, d_model=8)
> 投影(每个): → (2, 4, 8)  # W_Q, W_K, W_V 都是 (8,8) 的线性层
> split_heads:  → (2, 2, 4, 4)  # (batch, n_heads=2, seq, d_k=4)
> Attention:    → (2, 2, 4, 4)  # 每个头独立计算
> combine_heads:→ (2, 4, 8)     # 拼回 (batch, seq, d_model)
> W_O 投影:    → (2, 4, 8)      # 输出投影，形状不变
> ```
>
> **关键**：split_heads 不改变总参数量——只是把一个大矩阵切成 h 个小矩阵。每个头处理的特征维度更小（d_k = d_model/h），所以总计算量基本不变。

MultiHead(Q,K,V) = Concat(head₁, ..., headₕ) W_O

其中 headᵢ = Attention(QWᵢ^Q, KWᵢ^K, VWᵢ^V)

### 晚上电脑
```python
  class MultiHeadAttention(nn.Module):
      def __init__(self, d_model, n_heads, dropout=0.1):
          super().__init__()
          assert d_model % n_heads == 0, "d_model 必须能被 n_heads 整除"

self.d_model = d_model
          self.n_heads = n_heads
          self.d_k = d_model // n_heads

# 投影矩阵（注意：合并了所有头的投影，效率更高）
          self.W_Q = nn.Linear(d_model, d_model)
          self.W_K = nn.Linear(d_model, d_model)
          self.W_V = nn.Linear(d_model, d_model)
          self.W_O = nn.Linear(d_model, d_model)  # 输出投影

self.attention = ScaledDotProductAttention(dropout)

def split_heads(self, x):
          """x: (batch, seq_len, d_model)
             → (batch, n_heads, seq_len, d_k)"""
          batch, seq_len, _ = x.shape
          x = x.view(batch, seq_len, self.n_heads, self.d_k)
          return x.transpose(1, 2)  # (batch, n_heads, seq_len, d_k)

def combine_heads(self, x):
          """x: (batch, n_heads, seq_len, d_k)
             → (batch, seq_len, d_model)"""
          batch, _, seq_len, _ = x.shape
          x = x.transpose(1, 2)  # (batch, seq_len, n_heads, d_k)
          return x.reshape(batch, seq_len, self.d_model)

def forward(self, Q, K, V, mask=None):
          # 1. 线性投影
          Q = self.W_Q(Q)  # (batch, seq, d_model)
          K = self.W_K(K)
          V = self.W_V(V)

# 2. 拆分为多头
          Q = self.split_heads(Q)  # (batch, n_heads, seq, d_k)
          K = self.split_heads(K)
          V = self.split_heads(V)

# 3. 每个头独立做 Attention
          attn_out, attn_weights = self.attention(Q, K, V, mask)

# 4. 合并多头
          attn_out = self.combine_heads(attn_out)  # (batch, seq, d_model)

# 5. 输出投影
          return self.W_O(attn_out)

# ========== 验证 ==========
batch, seq_len, d_model, n_heads = 2, 4, 8, 2
x = torch.randn(batch, seq_len, d_model)

mha = MultiHeadAttention(d_model, n_heads)
output = mha(x, x, x)  # Self-Attention: Q=K=V=x
print(f"Multi-Head Attention 输出: {output.shape}")  # (2, 4, 8) ← 和输入形状一样！

```
> 🎉 **Multi-Head Attention 完成！** 注意到输出形状和输入完全一样吗？这正是 Transformer 能"层层堆叠"的关键——每层的输入输出维度一致，可以像积木一样往上摞。

- [ ] 今日完成检查
- [ ] 理解 split_heads / combine_heads 的维度变换
- [ ] Multi-Head Attention 输出和输入形状一致
- [ ] 能画出"输入 → 投影 → 拆头 → Attention → 拼头 → 输出"的数据流
### 第15周 · 星期三：Positional Encoding + Feed-Forward
---
### 手机摸鱼
核心知识点

**1. 为什么需要位置编码？**

Attention 本身是"无序"的——它对输入位置的排列不敏感。
但语言是有顺序的："狗咬人" vs "人咬狗"完全不同。

所以需要注入位置信息。

> 🗺️ **GPS 坐标类比（理解位置编码的最佳方式）**：
>
> 如果你要在地图上找"上海"的位置，你可以用"东经 121°，北纬 31°"来描述它。不同位置有不同的坐标组合。
>
> Positional Encoding 做的事情就是给每个词位置分配一个**独特的"坐标"**：
> - 位置 0 → [sin(0), cos(0), sin(0), cos(0)]
> - 位置 1 → [sin(ω₁), cos(ω₁), sin(ω₂), cos(ω₂)]
> - 位置 2 → [sin(2ω₁), cos(2ω₁), sin(2ω₂), cos(2ω₂)]
>
> 不同的频率（ω₁, ω₂, ...）就像不同的"坐标轴"，组合起来形成了每个位置的"指纹"。
> 两个相邻的位置（如 pos=5 和 pos=6），它们的"坐标"很接近——因为 sin/cos 是连续函数。
> 这使得模型能学到"距离"的概念。

**2. 正弦位置编码（Sinusoidal PE）**

PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))

其中 pos 是位置，i 是维度索引。

直觉：不同频率的正弦/余弦波编码了不同的位置模式。
位置相近的向量也相近（因为连续函数）。

> 💡 **Aha Moment**：为什么不用"可学习的"位置编码（像 BERT 那样）？正弦 PE 的最大优点是**外推**——训练时的 max_len=512，但推理时可以用 1024。可学习的 PE 不行——位置 513 的 embedding 根本不存在。这就是为什么有些模型（如 LLaMA）虽然用了可学习的（RoPE），但设计了特殊的旋转编码来支持外推。

优点：不需要学习参数，能外推到训练时没见过的长度。

**3. Feed-Forward Network (FFN)**

FFN(x) = ReLU(x @ W₁ + b₁) @ W₂ + b₂

或更现代的版本（LLaMA 用）：
FFN(x) = (SiLU(x @ W_gate) ⊙ (x @ W_up)) @ W_down

本质上是一个"两层的 MLP"，每个位置独立计算。
作用：增加模型的非线性和表达能力。

> 🏋️ **FFN 的类比**：如果 Attention 是"交流"（每个词和其他词交换信息），FFN 就是"思考"（每个词独立消化刚刚交流得到的信息）。"先交流（Attention），再思考（FFN）"——这就是 Transformer 每层的基本节奏。

### 晚上电脑
任务 1：手写 Positional Encoding

```python
  class SinusoidalPositionalEncoding(nn.Module):
      def __init__(self, d_model, max_len=5000):
          super().__init__()
          pe = torch.zeros(max_len, d_model)
          position = torch.arange(0, max_len).unsqueeze(1).float()
          div_term = torch.exp(
              torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model)
          )
          pe[:, 0::2] = torch.sin(position * div_term)  # 偶数维度用 sin
          pe[:, 1::2] = torch.cos(position * div_term)  # 奇数维度用 cos
          self.register_buffer('pe', pe.unsqueeze(0))   # (1, max_len, d_model)

def forward(self, x):
          # x: (batch, seq_len, d_model)
          return x + self.pe[:, :x.size(1), :]

```
> 🔑 **register_buffer 的作用**：PE 不是可训练参数，但需要在 `model.to(device)` 时一起移动。`register_buffer` 让 PE 像参数一样自动跟随模型移动，但不会被优化器更新。

任务 2：手写 Feed-Forward Network



```python
  class FeedForward(nn.Module):
      def __init__(self, d_model, d_ff, dropout=0.1):
          super().__init__()
          self.fc1 = nn.Linear(d_model, d_ff)    # 扩展：512 → 2048
          self.fc2 = nn.Linear(d_ff, d_model)    # 压缩：2048 → 512
          self.dropout = nn.Dropout(dropout)
          self.activation = nn.GELU()  # 或 ReLU()

def forward(self, x):
          return self.fc2(self.dropout(self.activation(self.fc1(x))))

```
> 📐 **FFN 的形状变化**：
> 输入 (batch, seq=10, d_model=512) → fc1 → (batch, 10, d_ff=2048) → GELU → dropout → fc2 → (batch, 10, 512)
> 先膨胀到 4 倍（提供大量"思考空间"），再压缩回来。这是 Transformer 中最重的部分——FFN 的参数约占整个 Transformer 的 2/3。

- [ ] 今日完成检查
- [ ] PE 公式能默写
- [ ] 理解为什么用 sin/cos（连续 → 能学到距离，能外推）
- [ ] FFN 的两层结构理解（膨胀→激活→压缩）
### 第15周 · 星期四：Encoder Layer + Encoder 完整组装
---
### 手机摸鱼
核心知识点

**1. Transformer Encoder Layer（一层）**

> 📊 **一层 Encoder 的 ASCII 结构图**：
> ```
> 输入 x
>   │
>   ├──────────────────┐
>   ▼                  │
> Multi-Head Attention │ (残差连接)
>   │                  │
>   ▼                  ▼
>   ├─── Add ──────────┘
>   ▼
> LayerNorm           ← 稳定训练
>   │
>   ├──────────────────┐
>   ▼                  │
> Feed-Forward Network │ (残差连接)
>   │                  │
>   ▼                  ▼
>   ├─── Add ──────────┘
>   ▼
> LayerNorm           ← 稳定训练
>   │
>   ▼
> 输出
> ```

伪代码：


```python
def encoder_layer(x):
         x = LayerNorm(x + MultiHeadAttention(x, x, x))
         x = LayerNorm(x + FeedForward(x))
         return x

```
**2. 残差连接（Residual Connection）的作用**

把输入"跳过"一层直接加到输出上：
output = LayerNorm(x + sublayer(x))

> 🛤️ **"高速公路"类比**：
> 想象你从北京开车到广州。正常路径是 G4 高速（层的前向计算）。现在在旁边修了一条"直达快车道"（残差连接），你可以完全不经过任何城市，直接到达广州。
>
> 对梯度来说也一样——反向传播时，梯度可以通过这条"快车道"直接从第 50 层跳到第 1 层，不被中间 49 层稀释。这就是为什么 100 层的 Transformer 还能训练。

为什么需要？
- 梯度可以直接流过残差路径（短路），缓解梯度消失
- 让深层网络至少不会比浅层更差（最坏情况 sublayer 输出 0，
残差连接保证至少输出原输入）

**3. 完整的 Transformer Encoder**

N 个 Encoder Layer 堆叠：
x → EncoderLayer₁ → EncoderLayer₂ → ... → EncoderLayerₙ → output

### 晚上电脑
```python
  class EncoderLayer(nn.Module):
      def __init__(self, d_model, n_heads, d_ff, dropout=0.1):
          super().__init__()
          self.self_attn = MultiHeadAttention(d_model, n_heads, dropout)
          self.feed_forward = FeedForward(d_model, d_ff, dropout)
          self.norm1 = nn.LayerNorm(d_model)
          self.norm2 = nn.LayerNorm(d_model)
          self.dropout = nn.Dropout(dropout)

def forward(self, x, mask=None):
          # 1. Self-Attention + 残差 + Norm
          attn_out = self.self_attn(x, x, x, mask)
          x = self.norm1(x + self.dropout(attn_out))

# 2. FFN + 残差 + Norm
          ff_out = self.feed_forward(x)
          x = self.norm2(x + self.dropout(ff_out))

return x

class TransformerEncoder(nn.Module):
def __init__(self, vocab_size, d_model, n_heads, d_ff, n_layers, dropout=0.1):
          super().__init__()
          self.embedding = nn.Embedding(vocab_size, d_model)
          self.pos_encoding = SinusoidalPositionalEncoding(d_model)
          self.layers = nn.ModuleList([
              EncoderLayer(d_model, n_heads, d_ff, dropout)
              for _ in range(n_layers)
          ])
          self.dropout = nn.Dropout(dropout)

def forward(self, x, mask=None):
          # Token Embedding + Positional Encoding
          x = self.embedding(x) * math.sqrt(self.embedding.embedding_dim)
          x = self.pos_encoding(x)
          x = self.dropout(x)

# 逐层通过 Encoder
          for layer in self.layers:
              x = layer(x, mask)

return x

# ⚠️ 架构注释：这是 Post-LN（原论文风格）
#    写法：y = LayerNorm(x + Sublayer(x))
#    现代 LLM 用 Pre-LN：y = x + Sublayer(LayerNorm(x))
#    Pre-LN 训练更稳定，不需要 warmup。
#    面试常问两者的区别——在这里建立第一印象。

# ========== 验证：用随机输入测试 forward ==========
vocab_size, d_model, n_heads, d_ff, n_layers = 1000, 512, 8, 2048, 6
batch, seq_len = 2, 10

encoder = TransformerEncoder(vocab_size, d_model, n_heads, d_ff, n_layers)
dummy_input = torch.randint(0, vocab_size, (batch, seq_len))  # 随机 token IDs

output = encoder(dummy_input)
print(f"Encoder 输出形状: {output.shape}")  # (2, 10, 512)
print(f"参数量: {sum(p.numel() for p in encoder.parameters()):,}")

```
> 🎉 **完整的 Transformer Encoder 已经跑通了！** 你刚刚实现了 BERT 的核心架构——BERT 就是一堆 Encoder Layer 堆起来的。区别只是 BERT 用 12 层、d_model=768、在超大语料上预训练过。但架构和你写的**一模一样**。

- [ ] 今日完成检查
- [ ] Encoder Layer 结构能画出来（Attention→Add&Norm→FFN→Add&Norm）
- [ ] 完整 Encoder 能 forward 跑通
- [ ] 理解残差连接的梯度短路作用
### 第15周 · 星期五：Decoder + 完整 Transformer
---
### 手机摸鱼
核心知识点

**1. Decoder 和 Encoder 的区别**

Encoder：双向看（每个词能看到所有其他词）
Decoder：单向看（生成第 t 个词时，只能看到前 t-1 个词）

Decoder 比 Encoder 多一层 Cross-Attention：
- Self-Attention（Masked）：只看当前和之前的位置
- Cross-Attention：用 Decoder 的 Q 去查 Encoder 输出的 K, V

> 🔑 **Cross-Attention 的关键**：Q 来自 Decoder（"我要生成什么？"），K 和 V 来自 Encoder（"源语言说了什么？"）。这样就建立了"翻译"的桥梁——Decoder 的每个位置都能"查询"Encoder 的所有位置。

**2. Masked Self-Attention**

用一个上三角矩阵 mask：
[1, 0, 0, 0]  ← 第 1 个词只能看自己
[1, 1, 0, 0]  ← 第 2 个词能看 1-2
[1, 1, 1, 0]
[1, 1, 1, 1]

在 softmax 前，把 mask=0 的位置设为 -inf：
scores.masked_fill(mask == 0, float('-inf'))

softmax(-inf) = 0 → 这些位置的注意力权重为 0。

> 💡 **Aha Moment**：为什么训练时 Decoder 也只需要一次 forward？（不是自回归一个一个生成？）因为Teacher Forcing——训练时你已经有正确答案，直接把整串目标 token 喂给 Decoder，用 Mask 确保每个位置只看前面的。这样整个序列可以并行计算，训练速度是自回归的 seq_len 倍。

今日思考题
- 为什么 Decoder 在训练时也只需要一次 forward？
（因为 Masked Self-Attention + Teacher Forcing，
训练时输入是真实的前 t-1 个 token，不需要自回归生成）

### 晚上电脑
```python
  class DecoderLayer(nn.Module):
      def __init__(self, d_model, n_heads, d_ff, dropout=0.1):
          super().__init__()
          self.self_attn = MultiHeadAttention(d_model, n_heads, dropout)
          self.cross_attn = MultiHeadAttention(d_model, n_heads, dropout)
          self.feed_forward = FeedForward(d_model, d_ff, dropout)
          self.norm1 = nn.LayerNorm(d_model)
          self.norm2 = nn.LayerNorm(d_model)
          self.norm3 = nn.LayerNorm(d_model)
          self.dropout = nn.Dropout(dropout)

def forward(self, x, enc_output, src_mask=None, tgt_mask=None):
          # 1. Masked Self-Attention（只能看当前及之前位置）
          attn_out = self.self_attn(x, x, x, tgt_mask)
          x = self.norm1(x + self.dropout(attn_out))

# 2. Cross-Attention（用 Decoder 的 Q 查 Encoder 的 K,V）
          attn_out = self.cross_attn(x, enc_output, enc_output, src_mask)
          x = self.norm2(x + self.dropout(attn_out))

# 3. FFN
          ff_out = self.feed_forward(x)
          x = self.norm3(x + self.dropout(ff_out))

return x

```
> 📐 **Decoder Layer 的三层结构**：
> ① Self-Attention（自己和自己交流，但只能看过去）
> ② Cross-Attention（和 Encoder 交流，Q 来自自己，K/V 来自 Encoder）
> ③ FFN（消化刚才的交流结果）

- [ ] 今日完成检查
- [ ] Decoder Layer 三层结构理解（Self-Attn → Cross-Attn → FFN）
- [ ] 理解 Masked Self-Attention 的作用（训练时并行，推理时自回归）
### 第15周 · 星期六：★★★ 终极组装 ★★★
### 14:00-17:00 完整 Transformer（Encoder + Decoder）+ 测试

> 🏗️ **终极组装开始！** 你过去 5 天写的每一个模块——Attention、Multi-Head、Positional Encoding、FFN、Encoder Layer、Decoder Layer——现在要像拼积木一样组合成完整的 Transformer。ARE YOU READY?

```python
  class Transformer(nn.Module):
      def __init__(self, src_vocab_size, tgt_vocab_size,
                   d_model, n_heads, d_ff, n_layers, dropout=0.1):
          super().__init__()
          self.encoder = TransformerEncoder(
              src_vocab_size, d_model, n_heads, d_ff, n_layers, dropout)
          self.decoder_embedding = nn.Embedding(tgt_vocab_size, d_model)
          self.decoder_pos = SinusoidalPositionalEncoding(d_model)
          self.decoder_layers = nn.ModuleList([
              DecoderLayer(d_model, n_heads, d_ff, dropout)
              for _ in range(n_layers)
          ])
          self.fc_out = nn.Linear(d_model, tgt_vocab_size)
          self.dropout = nn.Dropout(dropout)

def forward(self, src, tgt, src_mask=None, tgt_mask=None):
          # Encoder
          enc_output = self.encoder(src, src_mask)

# Decoder
          x = self.decoder_embedding(tgt) * math.sqrt(d_model)
          x = self.decoder_pos(x)
          x = self.dropout(x)

for layer in self.decoder_layers:
x = layer(x, enc_output, src_mask, tgt_mask)

return self.fc_out(x)  # (batch, tgt_len, tgt_vocab_size)

def generate(self, src, max_len, start_token, end_token):
          """推理模式：自回归生成"""
          self.eval()
          # Encode 源序列（只做一次）
          with torch.no_grad():
              enc_output = self.encoder(src)

# 逐 token 生成
          generated = [start_token]
          for _ in range(max_len):
              tgt = torch.tensor([generated]).to(src.device)
              # 构建因果 mask
              tgt_mask = self._generate_square_subsequent_mask(len(generated))
              # Decoder forward
              output = self.forward(src, tgt, tgt_mask=tgt_mask)
              # 取最后一个位置的预测
              next_token = output[0, -1].argmax().item()
              generated.append(next_token)
              if next_token == end_token:
                  break

return generated

```
验证清单（逐一确认）：
- [ ] Encoder 输入 (2, 10)，输出 (2, 10, 512) ✓
- [ ] Decoder 输入 (2, 8) + Encoder 输出，输出 (2, 8, tgt_vocab_size) ✓
- [ ] 所有层参数正确计数
- [ ] generate() 能自回归生成 token 序列

> 🎇 **你做到了。** 你面前的代码——从 Scaled Dot-Product Attention 到完整的 Encoder-Decoder Transformer——就是 **Vaswani et al. (2017) "Attention Is All You Need"** 的核心实现。
> 
> 当然，工业级的 Transformer 还有更多细节（Pre-LN、混合精度、分布式训练），但架构的核心——你已经完全掌握了。

- ⭐ 把这个 Transformer 类和本周所有模块的代码 push 到 GitHub！
17:00-17:30 复盘
本周你面前（不是背，是亲手写！）了：
- [ ] Scaled Dot-Product Attention
- [ ] Multi-Head Attention
- [ ] Positional Encoding
- [ ] Feed-Forward Network
- [ ] Encoder Layer → Encoder
- [ ] Decoder Layer
- [ ] 完整 Transformer（Encoder + Decoder）
- [ ] generate() 自回归推理

> ## 🚀 Now What? —— 你从这个起点能去往何方？
>
> 你刚刚手写的 Transformer 是**整个现代 AI 的基石**。从这里开始，每一条路都通向一个令人兴奋的方向：
>
> **BERT** = 你写的 Encoder × 12~24 层 + 海量预训练数据 → 理解语言
> **GPT** = 你写的 Decoder × 12~96 层 + 海量预训练数据 → 生成语言
> **T5 / BART** = 你写的完整 Encoder-Decoder → 翻译、摘要
> **LLaMA** = GPT 架构 + Pre-LN + RoPE + SwiGLU → 开源大模型
> **ChatGPT** = GPT + RLHF（人类反馈强化学习）→ 对话助手
> **Vision Transformer (ViT)** = 把图片切成 patch，当成"词"输入 Encoder → 图像理解
> **CLIP** = 图片 Encoder + 文本 Encoder → 图文匹配
>
> 你不再是一个"调包侠"。你知道了 Attention 的每个矩阵乘法、LayerNorm 的每个均值和方差、残差连接如何保障深层网络训练。
>
> **这是你整个学习旅程的"毕业项目"。恭喜！🎓**

- [ ] 第15周完成检查
- [ ] 完整 Transformer 能 forward 跑通
- [ ] 维度全部核对正确
- [ ] 代码 push 到 GitHub
### 第16周 · 主题：NLP 进阶 + 微调概念入门


> 最后一周！前两周你从零手写了 Transformer，现在你用工业级工具（HuggingFace、PEFT）做"外面的事"——但你心里知道每个工具内部在做什么。

### 星期一
Decoder 回顾 + GPT-2 Fine-tuning（HF Trainer）

> 用你手写 Transformer 的眼光重新看 GPT-2——你会发现它的架构就是你写的 Decoder 堆了 12 层。`causal_mask`（因果 mask）就是你的 `tgt_mask`，`cross_attn` 被去掉了（Decoder-Only）。

### 星期二
P-Tuning v2 概念 + 简单实验

> P-Tuning：不在原模型上改参数，而是在输入前面加一些可学习的"虚拟 token"。只训练这些虚拟 token 的 embedding，模型参数完全冻结 → 每个任务只需要存几十 KB 的"提示词 embedding"。

### 星期三
LoRA 概念理解（低秩分解的直觉）+ PEFT 库入门
LoRA 核心思想：不在原权重矩阵上训练，而是在旁边加两个小矩阵 A 和 B，
只训练 A 和 B（参数量是原来的 1/1000）。
W_new = W_original + B × A（其中 A 和 B 的秩远小于 W）

> 🔑 **LoRA 为什么有效？** 想象你要修改一幅画。与其重画整幅画（全量 fine-tune），不如在上面加几笔（低秩更新）。LoRA 的假设是：fine-tune 时的参数更新是"低秩"的——可以用两个很小的矩阵来近似。效果：原来需要训练 1750 亿参数，现在只需要训练几百万个 → 一张消费级显卡就能 fine-tune LLaMA。

### 星期四
完整训练一个 GPT-2 Small 文本生成

### 星期五
复习 + 整理所有 NLP 代码

### 星期六
阶段三综合复盘

> 🏁 **最后的终极验收**：
> 
> **凌晨 3 点把你叫醒，你能做到吗？**
> 
1. 手写一遍 Transformer forward（白板默写！不查代码！）
   x = embedding(tokens) + positional_encoding
   for layer in layers:
       x = LayerNorm(x + MultiHeadAttention(x, x, x))  # Encoder
       x = LayerNorm(x + FFN(x))
   # Decoder 类似，多一层 Cross-Attention
2. 标注每个 tensor 的维度
   Q: (batch, seq, d_model) → split → (batch, n_heads, seq, d_k)
   scores: (batch, n_heads, seq, seq) → softmax → weights
   output: (batch, n_heads, seq, d_k) → combine → (batch, seq, d_model)
3. 整理本周所有代码到 GitHub
4. 更新 Obsidian

- [ ] 第16周完成检查
- [ ] GPT-2 fine-tune 成功
- [ ] 理解 LoRA 的低秩分解原理
- [ ] Transformer 能闭眼默写（白板推导！）
### 阶段三结束 · 终极验收


> 🎊 **你已完成整个计划中最核心的 162 小时！**
>
> 回顾这 9 周：
> - 第 8 周：手写梯度下降 → 线性回归/逻辑回归（ML 的基石）
> - 第 9 周：K-Means + L1/L2 + 特征工程 + Kaggle（ML 工具箱）
> - 第 10 周：Tensor → Autograd → nn.Module → 训练循环（PyTorch 入门）
> - 第 11 周：手写 Softmax/LayerNorm + CNN（PyTorch 进阶）
> - 第 12 周：手写反向传播 + Dropout/BN/LN + AMP（深度学习基本功）
> - 第 13 周：CNN/LSTM/GRU + GPU 管理（深度学习实战）
> - 第 14 周：NLP 完整工具链 + BERT/GPT-2 fine-tune（NLP 入门）
> - 第 15 周：★★★ 从零手写完整 Transformer ★★★（巅峰之作）
> - 第 16 周：LoRA + P-Tuning + 综合复盘（工业级微调）
>
> **你不再是初学者了。** 你理解了从梯度下降到 Transformer 的整条链路。
> 面试官问"Transformer 内部怎么工作"——你不用背答案，你亲手写过每一行代码。

- [ ] 能手写完整的 Transformer forward
Attention(Q,K,V) = softmax(QK^T/√d_k)V
MultiHead → Add&Norm → FFN → Add&Norm
- [ ] 能独立写完训练循环（DataLoader → forward → loss → backward → step）
- [ ] 能用 HuggingFace fine-tune BERT/GPT-2
- [ ] 理解 LoRA 的核心思想
- [ ] sklearn ML Pipeline + PyTorch DL Pipeline 都做过实战

下一步：阶段四 · Agent 开发（LangChain + LangGraph + RAG）

> 🔜 在阶段四，你将用 Transformer 构建智能 Agent——让 LLM 学会"调用工具、搜索知识、执行多步推理"。你在阶段三写的 Transformer，就是你即将构建的 Agent 系统的"大脑"。

### END OF 阶段三·下


> 🎓 **Congratulations!** 如果这是大学课程，这 162 小时相当于"机器学习 + 深度学习 + NLP"三个学期的内容。你以自学的方式完成了它——这种自律和学习能力，比任何证书都更有价值。进入阶段四，让 Transformer 真正"活"起来。
