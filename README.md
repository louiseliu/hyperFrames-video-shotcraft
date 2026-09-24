<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/brand/logo-mark-reverse.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/brand/logo-mark.svg">
  <img alt="hyperFrames-video-shotcraft logo" src="./assets/brand/logo-mark.svg" width="112" height="112">
</picture>

<h1>hyperFrames-video-shotcraft</h1>

[![GitHub stars](https://img.shields.io/github/stars/louiseliu/hyperFrames-video-shotcraft)](https://github.com/louiseliu/hyperFrames-video-shotcraft/stargazers)

**An agent skill for crafting cinematic product videos with HyperFrames: 157 shot recipe cards · 214 styles · 218 HTML compositions · a production-ready template**

[English](README.md) | [中文](README_CN.md) | [日本語](README_JA.md)

</div>

**hyperFrames-video-shotcraft** is an AI agent skill that turns Claude Code or Codex into a
motion-design studio: point it at your product and it storyboards, animates, and
sound-designs a cinematic promo, marketing, launch, or demo video with
[HyperFrames](https://hyperframes.heygen.com/) — real page captures, 2.5D camera moves,
beat-synced cuts, and film-grade SFX included.

## ✨ Features

- **157 shot recipe cards** with full parameters, timing, and easing
- **218 HTML compositions** powered by HyperFrames + GSAP
- **Production-ready template** — Ink Press (36.2s, 1920×1080, 30fps, 10 shots)
- **Motion workbench** — browser-based timeline editor for post-delivery editing
- **One-click film themes** — Ink Press, Modern Light, Midnight, Sage, Coral, Iris, Deep Ocean, Obsidian Violet, Vintage Kraft. [Theme guide](template/THEMES.md)
- **JianYing (CapCut CN) export** — editable draft with per-shot clips, captions, and audio tracks. [Guide](references/jianying-export.md)

## 🚀 Quick start

**The most direct way: hand the repo link to your agent.**
In Claude Code / Codex or a similar agent, just say:

```text
Install this skill for me: https://github.com/louiseliu/hyperFrames-video-shotcraft
```

The agent will clone the repo and link it into your skills directory. Or install
with the [skills](https://skills.sh/) CLI / manually:

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

Then make requests like:

```text
Use hyperFrames-video-shotcraft to create a promo for my desktop product.
Use the deck-deal-flyin and row-embed shot cards to present this feature.
Design a product close-up inspired by spotlight-hero-card.
```

If no shot card is specified, the skill introduces the built-in video template
first and asks whether to use it; you can also browse shots in the `gallery/` directory before starting.

## 📼 Video template: Ink Press

The skill ships with **Ink Press** — a validated, complete promo template:
36.2 seconds, 1920×1080, 30fps, 10 shots in a paper-ink-amber style, with 2.5D
real-page camera moves, title cards, transitions, and a fully pinned cinematic
SFX pass:

https://github.com/user-attachments/assets/4cf5af51-98f3-4af2-8ab2-7267f470513d

▶️ [Watch in HD on YouTube](https://youtu.be/iShab28B_ak)

To use it, just tell your agent:

```text
Use hyperFrames-video-shotcraft to make a promo for my product with the Ink Press template.
```

The agent swaps in your product's screenshots, copy, and branding to reproduce
the same quality — the fastest, most reliable path to a finished film.

> More templates are on the way.

### Headless / CI notes

Rendering on a headless Linux box (tested: 2 cores, Node 22) hits three walls
worth knowing:

1. **Concurrency cap** — `hyperframes inspect --at/render` fails with "Maximum for
   --concurrency is 2" on low-core machines. Fix: pass `--concurrency=1`.
2. **Old Headless removal** — recent Chrome/Chromium dropped old headless mode;
   pointing HyperFrames at system chromium fails to launch. Fix: use a
   chrome-headless-shell binary instead of full Chrome.
3. **Blocked CDN** — if hyperframes.heygen.com is unreachable, the automatic
   headless-shell download is rejected. Fix:
   `--browser-executable=<path-to-local chrome-headless-shell>`.

With these three flags, frame renders from the bundled template work.

## 📦 What's included

| Content | Description |
| --- | --- |
| 157 shot recipe cards | Purpose, energy, suggested duration, parameters, implementation notes, and known pitfalls |
| 218 HTML compositions | Covering 214 styles with HyperFrames HTML + GSAP implementations |
| HyperFrames implementations | Tuned HTML + GSAP demos containing the actual easing and timing parameters for each card |
| Complete video template | A validated 36.2-second, 1920×1080, 30fps product promo with 10 shots |
| Components and assets | 2.5D page camera, captions, flash cuts, digit rolls, SFX, and capture scripts |
| Production methodology | Capture, visual direction, storyboarding, sound design, beat sync, and final QA |
| JianYing project export | Load the film into JianYing (CapCut CN) for further editing — per-shot speed, captions, and audio all editable (verified on macOS 11.2) |
| Motion workbench | Browser timeline editor opened after delivery: split the film into tracks, edit exposed shot properties, retime, drag in any of the 216 demo motions, export via HyperFrames |

The toolkit primarily targets web and desktop product promos, while individual
shot cards can also be used in feature demos, brand films, launch videos, and
other motion projects.

## 🗂 Repository structure

```text
hyperFrames-video-shotcraft/
├── SKILL.md                 # Agent entry point and core production rules
├── references/
│   ├── pipeline.md          # End-to-end production workflow
│   ├── shots/               # 157 shot recipe cards in 10 functional categories
│   ├── sequences/           # Reusable full-video structures and sequence patterns
│   ├── aesthetic-rules.md   # Visual QA criteria
│   ├── music-beat-sync.md   # BGM analysis and beat-sync methodology
│   ├── sound-design.md      # Sound-design guidance and examples
│   ├── jianying-export.md   # JianYing (CapCut CN) project-export guide
│   └── workbench.md         # Motion workbench: manifest contract + editability rules
├── demos/                   # HyperFrames reference implementations (same categories)
├── gallery/                 # Static motion-preview Gallery
├── template/                # Runnable complete video template
├── jianying-export/         # JianYing draft installers (mac tested / win untested)
├── workbench/               # Post-delivery motion workbench (Vite + HyperFrames Player)
└── assets/
    ├── lib/                 # Reusable HyperFrames components
    ├── scripts/             # Page-asset capture scripts
    └── audio/               # Audio assets
        ├── bgm/             # 5 BGM options
        └── sfx/<category>/  # 149 SFX across 16 scene categories
```

For the complete workflow and implementation requirements, see [SKILL.md](SKILL.md),
the [production pipeline](references/pipeline.md), and the
[visual QA criteria](references/aesthetic-rules.md).

## 🔊 Audio and asset notes

Audio files under `assets/audio/` may be used according to their respective license terms.
See [ATTRIBUTION.md](assets/audio/ATTRIBUTION.md) for sources and license details.

SFX are organized into 16 scene/material categories (`transition` `impact` `riser`
`camera` `ui` `text` `paper` `film` `light` `data` `scifi` `mech` `glass` `fluid`
`crowd` `counter`) — **pick the category first, then the timbre**. See
[sound-design.md](references/sound-design.md) for the category index and per-file usage.

Product screenshots bundled with the template are demonstration assets. Replace them with
screenshots from the target product before publishing, and verify whether any product,
customer, or personal data needs to be anonymized.

## 🙏 Acknowledgements

Many shot recipes in this library were distilled by studying the motion language
of outstanding official product films — including promos from **ClickUp,
Perplexity, Slack, Notion, Figma, Framer, Bear, Raycast, Pitch, Miro, Superhuman,
and Loom**. The cards document motion techniques (timing, easing, choreography)
re-implemented from scratch; no footage, artwork, or brand assets from these
films are included in this repository. All trademarks belong to their respective
owners, and none of these companies are affiliated with or endorse this project.
Per-batch sourcing notes for the 48 cards added in 2026-08 live in
[references/shots/ATTRIBUTION.md](references/shots/ATTRIBUTION.md).

Special thanks to:

- **[HyperFrames](https://hyperframes.heygen.com/)** — the HTML-based video framework
  that powers every demo and template here. Note that HyperFrames has its own
  [license](https://github.com/heygen-com/hyperframes/blob/main/LICENSE.md)
  (free for individuals and small teams; companies may need a paid license).
- **[Mixkit](https://mixkit.co/)** — source of the SFX and music assets bundled
  under their free commercial license.
- The game-feel and animation communities whose published principles (e.g.
  Vlambeer's screenshake talks, classic animation timing) inform several cards.
- **Claude Code** — this library itself was built, iterated, and QA'd with an
  AI coding agent, using the same workflow the skill teaches.

## ⭐ Star history

[![Star History Chart](https://api.star-history.com/svg?repos=louiseliu/hyperFrames-video-shotcraft&type=Date)](https://star-history.com/#louiseliu/hyperFrames-video-shotcraft&Date)
