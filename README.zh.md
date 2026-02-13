[English](README.md) | [繁體中文](README.zh.md)

# theme-factory

一個 Claude Code 技能，提供 10 組精選的專業色彩與字型主題，可套用於任何成品 -- 簡報、文件、報告、HTML 著陸頁等。也可以即時產生自訂主題。

## 說明

1. 顯示 `assets/theme-showcase.pdf`，讓使用者視覺瀏覽全部 10 組預設主題
2. 讓使用者選擇主題（或要求自訂主題）
3. 從 `references/` 讀取主題規格，取得精確的 hex 色碼和字型配對
4. 將所選主題一致地套用到目標成品

## 功能特色

- 10 組精心設計的色彩與字型主題
- 每組主題包含：色彩調色盤（hex 色碼）、標題與內文字型配對
- 支援自訂主題：根據描述即時產生新主題
- 可套用於簡報、文件、報告、網頁等各種成品

## 可用主題

| # | 主題名稱 | 風格 |
|---|----------|------|
| 1 | Ocean Depths | 專業、沉穩的海洋風格 |
| 2 | Sunset Boulevard | 溫暖、鮮豔的日落色調 |
| 3 | Forest Canopy | 自然、沉穩的大地色系 |
| 4 | Modern Minimalist | 乾淨、現代的灰階風格 |
| 5 | Golden Hour | 濃郁、溫暖的秋季調色盤 |
| 6 | Arctic Frost | 清涼、清爽的冬季風格 |
| 7 | Desert Rose | 柔和、精緻的沙漠色調 |
| 8 | Tech Innovation | 大膽、現代的科技美學 |
| 9 | Botanical Garden | 清新、有機的花園色彩 |
| 10 | Midnight Galaxy | 戲劇性、宇宙感的深色調 |

## 安裝

```bash
git clone https://github.com/joneshong-skills/theme-factory.git ~/.claude/skills/theme-factory
```

## 使用方式

安裝後，直接要求 Claude 套用主題：

- *「幫我的簡報套用 Ocean Depths 主題」*
- *「顯示所有可用主題」*
- *「建立一個暖色系粉彩主題給我的著陸頁」*
- *「用 Tech Innovation 主題設計這份報告」*
- *「產生主題」*
- *「品牌主題設計」*

## 專案結構

```
theme-factory/
├── SKILL.md                        # 技能定義及工作流程
├── README.md                       # 英文說明
├── README.zh.md                    # 繁體中文說明（本檔案）
├── LICENSE.txt                     # Apache 2.0 授權
├── assets/
│   └── theme-showcase.pdf          # 全部 10 組主題的視覺展示
├── references/
│   ├── arctic-frost.md             # 主題規格：Arctic Frost
│   ├── botanical-garden.md         # 主題規格：Botanical Garden
│   ├── desert-rose.md              # 主題規格：Desert Rose
│   ├── forest-canopy.md            # 主題規格：Forest Canopy
│   ├── golden-hour.md              # 主題規格：Golden Hour
│   ├── midnight-galaxy.md          # 主題規格：Midnight Galaxy
│   ├── modern-minimalist.md        # 主題規格：Modern Minimalist
│   ├── ocean-depths.md             # 主題規格：Ocean Depths
│   ├── sunset-boulevard.md         # 主題規格：Sunset Boulevard
│   └── tech-innovation.md          # 主題規格：Tech Innovation
└── scripts/                        # （保留供未來自動化使用）
```

## 授權

Apache 2.0 -- 參見 [LICENSE.txt](LICENSE.txt)
