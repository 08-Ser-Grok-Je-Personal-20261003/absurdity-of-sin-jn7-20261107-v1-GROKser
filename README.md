# 你看见罪是多么荒谬了吗？ · 讲章学习站

## 🔗 三个链接

| | 链接 |
|---|---|
| 📦 **GitHub 仓库** | **<https://github.com/08-Ser-Grok-Je-Personal-20261003/absurdity-of-sin-jn7-20261107-v1-GROKser>** |
| 🌐 **GitHub Pages** | **<https://08-ser-grok-je-personal-20261003.github.io/absurdity-of-sin-jn7-20261107-v1-GROKser/>** |
| 🌐 **Surge** | **<https://absurdity-of-sin-jn7-20261107-v1-grokser.surge.sh>** |

> 诗歌：圣诗第4首、韵诗11篇、韵诗7篇、韵诗第1篇、圣诗第9首（只列编号，不含歌词）
> 读经：**箴言第5章**　证经：**约翰福音 7:45–52**
> 题目：**你看见罪是多么荒谬了吗？**
> 一、他们对差役的回应　二、他们对尼哥底母的回应

这是一个多页静态讲章学习站，全部用简体中文，按欧陆改革宗传统编写：三项联合信条（海德堡要理问答、比利时信条、多特信经）加三大普世信经。

- 纯静态，不用 CDN，使用系统中文字体。
- 亮色／深色、玻璃拟态、可折叠目录、响应式布局。
- 主线：罪的荒谬是人宁可扭曲真理也不肯降服基督；恩典是基督为这样的罪人受审，并赐新心使人听见、悔改。
- 页面用相对链接，放在仓库根目录或 GitHub Pages 子路径下都可以打开。

版本：**v1（2026-11-07）**，变更见 [CHANGELOG.md](CHANGELOG.md)。

## 页面一览

**核心页面（顶部导航）**

| 文件 | 内容 |
|---|---|
| `index.html` | 首页：一句话总结、最感动的3点、学习路径 |
| `sermon.html` | **讲章**：全局到局部；两点；七个视角；四个闭环；约7:52释经警戒 |
| `background.html` | 背景·地图：作者与年代的不同看法、职分界限、示意图（耶路撒冷／圣殿局部，加利利含迦特希弗） |
| `discussion.html` | 13 道讨论题与答案分析 |
| `memory.html` | 记忆：一句话、三点、听查判改、导图、流程、总表、闪卡 |
| `creeds.html` | 三大信经干净阅读与背诵 |
| `compare.html` | 三大信经对比：不是三种福音 |
| `worship.html` | 诗歌只列编号；韵诗暂按篇号附诗篇和合本；箴言第5章全文 |

**参考资料（菜单「页面」中）**

| 文件 | 内容 |
|---|---|
| `tfu.html` | 信条精选（原文）：海德堡问1–11、21、60、65、86、108–109、112；比利时信条7、14–15；多特 I.5–6 与 III/IV 相关条。威斯敏斯特仅意译 |
| `extension.html` | 十处经文对照、闭环应用、辩正清单 |
| `hc.html` `bc.html` `cd.html` | 海德堡要理问答、比利时信条、多特信经全文 |
| `sources.html` | 资料来源与逐字核对报告 |
| `404.html` | 未找到页面 |

## 目录结构

```
├── *.html                 # 生成结果（连同 assets/ 即可部署）
├── assets/style.css       # 亮／暗、玻璃拟态、响应式、动画
├── assets/app.js          # 主题、可折叠目录、背诵、翻转卡片
├── content/*.html         # 源：front-matter + HTML + {{宏}}
├── data/
│   ├── bop.json           # ccifellowship.org 的信经／信条文本
│   ├── cuv_used.json      # 本站用到的和合本章节
│   └── source_pages/      # 信经简介等被引用页面的存档
├── tools/
│   ├── build.py           # 生成器（引句必须是原文子串）
│   ├── maps.py            # 示意图与导图、流程
│   ├── verify.py          # 在线重抓并逐字比对
│   ├── qa.py linkcheck.py # 375／768／1280 与深色；站内链接
│   ├── fetch/             # 重新抓取信条与和合本
│   └── deploy_surge.sh    # 部署到 surge（用本机已登录账号，不存密码）
└── reports/               # verify 与 qa 的结果（截图不入库）
```

## 如何修改内容

1. 编辑 `content/*.html`。开头是 front-matter（`title` `h1` `lead` `badges`，以 `---` 结束）。
2. **信经与信条不要手打**，用宏注入。构建时会断言引句是来源原文的子串：

| 宏 | 作用 |
|---|---|
| `{{bible:约7:45-52\|hl=46}}` / `{{bq:约7:46}}` | 和合本经文块 / 行内引句 |
| `{{hc:112}}` `{{hcm:21}}` `{{hcq:21\|片段}}` | 海德堡问答 |
| `{{bc:14}}` `{{bcq:14\|片段}}` | 比利时信条 |
| `{{cd:34.4}}` `{{cdq:34.4\|片段}}` | 多特信经（`34` 表示第三、四项） |
| `{{crq:apostles\|片段}}` | 三大信经引句 |
| `{{ccq:源键\|片段}}` | 已存档页面的引句 |
| `{{map:galilee}}` | `galilee` `mindmap` `paths` `loop-redemptive` `triad` |

3. 生成：`python3 tools/build.py`（Python 3.10+，`beautifulsoup4`）。
4. 检查：

   ```bash
   python3 tools/verify.py
   python3 tools/build.py
   python3 tools/linkcheck.py
   python3 tools/qa.py
   ```

5. 重新抓取（可选）：在 `_src` 中运行 `tools/fetch/` 下的脚本。`_src/` 已列入 `.gitignore`，原始抓取缓存不入库。

## 部署

**GitHub Pages**（仓库根目录，已含 `.nojekyll`）：

```bash
gh api -X POST repos/08-Ser-Grok-Je-Personal-20261003/absurdity-of-sin-jn7-20261107-v1-GROKser/pages \
  -f 'source[branch]=main' -f 'source[path]=/'
```

**Surge**（使用本机已经登录的账号，仓库里不写密码或令牌）：

```bash
npx surge whoami
tools/deploy_surge.sh
```

默认域名：`absurdity-of-sin-jn7-20261107-v1-grokser.surge.sh`。

## 资料来源与诚实说明

- 三大信经、海德堡要理问答、比利时信条、多特信经的中文全部来自 [ccifellowship.org](https://ccifellowship.org)，由 `tools/verify.py` 在线核对（见 `sources.html`）。
- 信经对比页若引用站内简介或恩约教会「我们的信仰」中的句子，同样只引用已抓取页面里的原句。
- 经文：和合本（getbible.net `cus`）。
- 地图是手绘示意图，不是比例图，也不是考古测绘图。
- **未抓取、只作转述的内容**都在 `sources.html` 标明：威斯敏斯特标准（仅意译）、成书年代、职分与节期、迦特希弗的精确遗址、约7:52的希腊文时态讨论。不把未打开的注释页写成引文。
- 诗歌只列编号。韵诗篇号对应诗篇是假定，不代表已核对某一教会的诗本。

## 许可

站点自写内容供教会与个人学习。信经和信条文本的版权与使用条件以 ccifellowship.org 为准；和合本为公有领域。
