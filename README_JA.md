<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/brand/logo-mark-reverse.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/brand/logo-mark.svg">
  <img alt="hyperFrames-video-shotcraft logo" src="./assets/brand/logo-mark.svg" width="112" height="112">
</picture>

<h1>hyperFrames-video-shotcraft</h1>

[![GitHub stars](https://img.shields.io/github/stars/louiseliu/hyperFrames-video-shotcraft)](https://github.com/louiseliu/hyperFrames-video-shotcraft/stargazers)

**HyperFrames で映画のような製品動画を制作するためのエージェントスキル：157 種類のショットレシピカード · 214 種類のスタイル · 218 HTML コンポジション · 実制作に対応したテンプレート**

[English](README.md) | [中文](README_CN.md) | [日本語](README_JA.md)

</div>

**hyperFrames-video-shotcraft** は、Claude Code や Codex をモーションデザインスタジオに
変える AI エージェントスキルです。製品を指定するだけで、ストーリーボード、アニメーション、
サウンドデザインを行い、[HyperFrames](https://hyperframes.heygen.com/) を使って映画のようなプロモーション、
マーケティング、ローンチ、デモ動画を制作します。実際のページキャプチャ、2.5D カメラワーク、
ビートに同期したカット、映画品質の SFX も含まれます。


## ✨ 特徴

- **157 種類のショットレシピカード**——パラメータ、タイミング、イージング完備
- **218 HTML コンポジション**——HyperFrames + GSAP ベース
- **検証済みテンプレート**——Ink Press（36.2 秒、1920×1080、30fps、10 ショット）
- **モーションワークベンチ**——ブラウザベースのタイムラインエディタ、納品後も編集可能
- **ワンクリックテーマ切替**——紙質 / モダンライト / ミッドナイト / セージ / コーラル / アイリス / ディープオーシャン / オブシディアンバイオレット / ヴィンテージクラフト。[テーマガイド](template/THEMES.md)
- **剪映エクスポート**——ショット、字幕、音声トラック付き編集可能ドラフト。[ガイド](references/jianying-export.md)

## 🚀 クイックスタート

**最も簡単な方法は、リポジトリのリンクをエージェントに渡すことです。**
Claude Code、Codex、または同様のエージェントで、次のように伝えます。

```text
Install this skill for me: https://github.com/louiseliu/hyperFrames-video-shotcraft
```

エージェントがリポジトリをクローンし、スキルディレクトリにリンクします。または、
[skills](https://skills.sh/) CLI を使うか、手動でインストールします。

```bash
npx skills add louiseliu/hyperFrames-video-shotcraft
```

```bash
git clone https://github.com/louiseliu/hyperFrames-video-shotcraft.git
cd hyperFrames-video-shotcraft
ln -s "$(pwd)" ~/.claude/skills/hyperFrames-video-shotcraft   # Claude Code
# or
ln -s "$(pwd)" ~/.codex/skills/hyperFrames-video-shotcraft    # Codex
```

インストール後は、次のように依頼できます。

```text
Use hyperFrames-video-shotcraft to create a promo for my desktop product.
Use the deck-deal-flyin and row-embed shot cards to present this feature.
Design a product close-up inspired by spotlight-hero-card.
```

ショットカードを指定しない場合、スキルは最初に内蔵の動画テンプレートを
紹介し、それを使うか確認します。作業を始める前に

## 📼 動画テンプレート：Ink Press

スキルには、検証済みの完全なプロモーションテンプレート **Ink Press** が付属します。
長さ 36.2 秒、1920×1080、30fps、紙・インク・アンバー調の 10 ショットで構成され、2.5D の
実ページカメラワーク、タイトルカード、トランジション、細部まで調整された映画品質の
SFX が含まれます。

https://github.com/user-attachments/assets/4cf5af51-98f3-4af2-8ab2-7267f470513d

▶️ [YouTube で HD 版を見る](https://youtu.be/iShab28B_ak)

使用するには、エージェントに次のように伝えるだけです。

```text
Use hyperFrames-video-shotcraft to make a promo for my product with the Ink Press template.
```

エージェントが製品のスクリーンショット、コピー、ブランド要素に差し替えて
同じ品質を再現します。完成した動画を得るための、最も速く確実な方法です。

> 今後、さらに多くのテンプレートが追加される予定です。

### Headless / CI に関する注意事項

ヘッドレスの Linux サーバー（検証環境：2 コア、Node 22）でレンダリングする際、
次の 3 つの問題に遭遇します。いずれもフラグ 1 つで解決できます。

1. **並列数の上限** — 低コアのマシンでは `hyperframes inspect --at/render` が
   "Maximum for --concurrency is 2" というエラーで失敗します。対処:
   `--concurrency=1` を指定します。
2. **旧 Headless モードの廃止** — 最近の Chrome/Chromium は旧 headless モードを
   廃止したため、HyperFrames にシステムの chromium を指定すると起動に失敗します。
   対処: フル版 Chrome ではなく chrome-headless-shell バイナリを使用します。
3. **CDN への接続遮断** — hyperframes.heygen.com に到達できない環境では、
   headless-shell の自動ダウンロードが失敗します。対処:
   `--browser-executable=<ローカルの chrome-headless-shell のパス>` を指定します。

この 3 つのフラグを設定すれば、同梱テンプレートのレンダリングが動作します。

## 📦 収録内容

| 内容 | 説明 |
| --- | --- |
| 157 種類のショットレシピカード | 目的、エネルギー、推奨時間、パラメータ、実装上の注意点、既知の落とし穴 |
| 214 本のモーションプレビュー | 214 種類のスタイルを網羅し、オンライン Gallery で検索と絞り込みが可能 |
| HyperFrames 実装 | 各カードの実際のイージングとタイミングパラメータを含む、調整済みの TSX デモ |
| 完全な動画テンプレート | 検証済みの 36.2 秒、1920×1080、30fps、10 ショットの製品プロモーション |
| コンポーネントとアセット | 2.5D ページカメラ、キャプション、フラッシュカット、数字ロール、SFX、キャプチャスクリプト |
| 制作手法 | キャプチャ、ビジュアルディレクション、ストーリーボード、サウンドデザイン、ビート同期、最終 QA |
| 剪映プロジェクト書き出し | 完成映像を剪映（CapCut 中国版）で継続編集——ショット変速・字幕・音声トラックを編集可（macOS 11.2 実機検証済み） |
| モーションワークベンチ | 納品後に開くブラウザのタイムラインエディタ：映像をトラックに分解、公開されたショット属性の編集、再タイミング、216 個の demo モーションのドラッグ投入、HyperFrames 書き出し |

このツールキットは主に Web およびデスクトップ製品のプロモーションを対象としていますが、
各ショットカードは機能デモ、ブランド映像、ローンチ動画、
その他のモーション制作にも利用できます。

## 🗂 リポジトリ構成

```text
hyperFrames-video-shotcraft/
├── SKILL.md                 # Agent entry point and core production rules
├── references/
│   ├── pipeline.md          # End-to-end production workflow
│   ├── shots/               # 157 shot recipe cards
│   ├── sequences/           # Reusable full-video structures and sequence patterns
│   ├── aesthetic-rules.md   # Visual QA criteria
│   ├── music-beat-sync.md   # BGM analysis and beat-sync methodology
│   ├── sound-design.md      # Sound-design guidance and examples
│   ├── jianying-export.md   # JianYing (CapCut CN) project-export guide
│   └── workbench.md         # Motion workbench: manifest contract + editability rules
├── demos/                   # HyperFrames reference implementations for shot cards
├── gallery/                 # Static motion-preview Gallery
├── template/                # Runnable complete video template
├── jianying-export/         # JianYing draft installers (mac tested / win untested)
├── workbench/               # Post-delivery motion workbench (Vite + HyperFrames Player)
└── assets/
    ├── lib/                 # Reusable HyperFrames components
    ├── scripts/             # Page-asset capture scripts
    └── audio/               # 音声アセット
        ├── bgm/             # BGM 候補 5 曲
        └── sfx/<カテゴリ>/  # 効果音 149 個、シーン別 16 カテゴリ
```

完全なワークフローと実装要件については、[SKILL.md](SKILL.md)、
[制作パイプライン](references/pipeline.md)、および
[ビジュアル QA 基準](references/aesthetic-rules.md)を参照してください。

## 🔊 音声とアセットに関する注意事項

`assets/audio/` にある音声ファイルは、それぞれのライセンス条件に従って使用できます。
出典とライセンスの詳細については、[ATTRIBUTION.md](assets/audio/ATTRIBUTION.md)を参照してください。

効果音はシーン／素材ごとに 16 カテゴリへ分類されています（`transition` `impact`
`riser` `camera` `ui` `text` `paper` `film` `light` `data` `scifi` `mech` `glass`
`fluid` `crowd` `counter`）。**まずカテゴリを決め、次に音色を選ぶ**のが基本です。
カテゴリ索引とファイルごとの用途は
[sound-design.md](references/sound-design.md) を参照してください。

テンプレートに含まれる製品スクリーンショットはデモ用アセットです。公開前に
対象製品のスクリーンショットへ差し替え、製品、顧客、または個人に関するデータを
匿名化する必要があるか確認してください。

## 🙏 謝辞

本プロジェクトは [**@Vincentwei1021（Wei Yihao）**](https://github.com/Vincentwei1021) による
[**video-shotcraft**](https://github.com/Vincentwei1021/video-shotcraft) のフォークであり、
Remotion から HyperFrames へ移行したものです。オリジナルプロジェクトの優れたショットレシピカード
体系、制作手法、サウンドデザインフレームワークが本プロジェクトの基盤となっています。
Apache 2.0 ライセンスの下で公開されており、元の著作権表示は [LICENSE](LICENSE) ファイルに
保持されています。

このライブラリの多くのショットレシピは、優れた公式製品動画のモーション表現を
研究してまとめたものです。対象には **ClickUp、Perplexity、Slack、Notion、
Figma、Framer、Bear、Raycast、Pitch、Miro、Superhuman、Loom** のプロモーションが
含まれます。カードには、ゼロから再実装したモーション技法
（タイミング、イージング、振り付け）を記載しています。これらの動画の映像、アートワーク、
ブランドアセットはリポジトリに含まれません。すべての商標は各所有者に帰属し、
各社は本プロジェクトと提携しておらず、また本プロジェクトを推奨していません。
2026-08 に追加した 48 枚のカードのバッチ別ソース情報は
[references/shots/ATTRIBUTION.md](references/shots/ATTRIBUTION.md) を参照してください。

特に以下のプロジェクトとコミュニティに感謝します。

- **[@Vincentwei1021](https://github.com/Vincentwei1021)** — オリジナルの
  [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) プロジェクトの
  作者です。ショットレシピカード体系、制作パイプライン、手法のすべてがこの優れた作品に
  由来しています。
- **[HyperFrames](https://hyperframes.heygen.com/)** — すべてのデモとテンプレートを支える
  HTML ベースの動画フレームワークです。HyperFrames には独自の
  [ライセンス](https://github.com/heygen-com/hyperframes/blob/main/LICENSE.md)
  がある点に注意してください（個人と小規模チームは無料、企業は有料ライセンスが必要な場合があります）。
- **[Mixkit](https://mixkit.co/)** — 無料の商用ライセンスで収録されている
  SFX と音楽アセットの提供元です。
- 複数のカードに影響を与えた、ゲームフィールとアニメーションのコミュニティが公開する原則
  （Vlambeer のスクリーンシェイクに関する講演、古典的なアニメーションのタイミングなど）。
- **Claude Code** — このライブラリ自体も、スキルが教えるものと同じワークフローを使い、
  AI コーディングエージェントによって構築、反復改善、QA されました。

## ⭐ Star 履歴

[![Star History Chart](https://api.star-history.com/svg?repos=louiseliu/hyperFrames-video-shotcraft&type=Date)](https://star-history.com/#louiseliu/hyperFrames-video-shotcraft&Date)
