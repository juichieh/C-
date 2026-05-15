# Banana Civilization Simulator (Private MVP)

> 文字 MUD / 文明模擬最小可行版本（MVP），僅採用原創文字內容，**不包含任何官方圖片、音樂或侵權素材**。

## 專案目標
將「蘑菇世界」風格世界觀轉化為可長期擴充的文字文明模擬：
- 派系外交與衝突
- 資源經濟（特別是香蕉經濟）
- NPC 記憶與關係狀態
- 世界事件日誌

## MVP 功能（目前版本）
- Terminal 執行的 **10 回合**世界模擬
- 四大陣營：
  - 蘑菇王國
  - 庫巴軍團
  - 耀西農業區
  - 大金剛部落
- 核心資源：`coins`, `food`, `wood`, `bananas`, `military`
- 每回合自動觸發事件池中的事件並更新世界狀態
- 每回合輸出日誌（含 emoji 與派系敘事）

## 快速開始
```bash
cd banana-civilization-simulator
python3 src/main.py
```

## 專案結構
```text
banana-civilization-simulator/
├─ README.md
├─ docs/
│  ├─ mvp-design.md
│  ├─ world-rules.md
│  └─ next-steps.md
├─ data/
│  ├─ factions.json
│  ├─ npcs.json
│  ├─ resources.json
│  └─ events.json
├─ prompts/
│  └─ npc-event-generator.md
├─ src/
│  └─ main.py
└─ logs/
   └─ world-log-example.txt
```

## 注意
- 本專案僅作私人實驗用途。
- 世界觀參考你提到的《瑪利歐文明模擬遊戲.pdf》，目前先以可執行 MVP 落地；待你提供文件後可再做精準對齊。
