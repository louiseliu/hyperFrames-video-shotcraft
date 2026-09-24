#!/usr/bin/env python3
"""Generate demos/typography/*/index.html from ported animation logic."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TYPO = ROOT / "demos" / "typography"

MOTION = r"""
const E = {
  linear: t => t,
  inQuad: t => t * t,
  outQuad: t => t * (2 - t),
  inOutQuad: t => (t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t),
  inCubic: t => t * t * t,
  outCubic: t => 1 - Math.pow(1 - t, 3),
  inOutCubic: t => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2),
  outQuart: t => 1 - Math.pow(1 - t, 4),
  outQuint: t => 1 - Math.pow(1 - t, 5),
  inQuart: t => t * t * t * t,
  outExpo: t => (t === 1 ? 1 : 1 - Math.pow(2, -10 * t)),
  inExpo: t => (t === 0 ? 0 : Math.pow(2, 10 * t - 10)),
  outBack: (t, s = 1.70158) => 1 + (s + 1) * Math.pow(t - 1, 3) + s * Math.pow(t - 1, 2),
  inBack: (t, s = 1.70158) => (s + 1) * t * t * t - s * t * t,
  outElastic: t => t === 0 ? 0 : t === 1 ? 1 : Math.pow(2, -10 * t) * Math.sin((t * 10 - 0.75) * ((2 * Math.PI) / 3)) + 1,
  spring: (t, bounce = 0.25) => { const w = 8 + 8 * (1 - bounce); return 1 - Math.exp(-6 * t) * Math.cos(w * t * bounce * 2.2); },
};
const lerp = (t, a, b) => a + (b - a) * t;
const seg = (t, t0, t1, ease = E.linear) => ease(Math.min(1, Math.max(0, (t - t0) / (t1 - t0))));
const rand = seed => { const x = Math.sin(seed * 127.1 + 311.7) * 43758.5453; return x - Math.floor(x); };
"""

G = """const G = { bg:'#ececea', panel:'#f7f7f6', line:'#dcdcda', bar:'#c2c2c0', ink:'#2f2f2f', mid:'#8f8f8d', card:'#ffffff', border:'#d8d8d6', side:'#3a3a3a', sideBar:'#5a5a58' };"""

FRAME_HELPERS = r"""
function frameAt(state, totalFrames) {
  return Math.min(totalFrames - 1, Math.round(state.t * (totalFrames - 1)));
}
function interp(frame, [a, b], [va, vb], opts = {}) {
  let t = (frame - a) / (b - a);
  if (opts.clamp !== false) t = Math.max(0, Math.min(1, t));
  if (t <= 0) return va;
  if (t >= 1) return vb;
  if (opts.ease === 'outCubic') t = E.outCubic(t);
  else if (opts.ease === 'inCubic') t = E.inCubic(t);
  else if (opts.ease === 'inOutCubic') t = E.inOutCubic(t);
  else if (opts.ease === 'outQuad') t = E.outQuad(t);
  else if (opts.ease === 'inQuad') t = E.inQuad(t);
  else if (opts.ease === 'outQuart') t = E.outQuart(t);
  else if (opts.ease === 'inOutQuad') t = E.inOutQuad(t);
  else if (opts.ease === 'outQuint') t = E.outQuint(t);
  else if (opts.ease === 'outExpo') t = E.outExpo(t);
  else if (opts.ease === 'inExpo') t = E.inExpo(t);
  else if (opts.ease === 'outBack') t = E.outBack(t);
  else if (opts.ease === 'inBack') t = E.inBack(t);
  else if (opts.ease === 'outElastic') t = E.outElastic(t);
  else if (opts.ease === 'poly5') { t = 1 - Math.pow(1 - t, 5); }
  else if (opts.ease === 'poly4') { t = 1 - Math.pow(1 - t, 4); }
  return va + (vb - va) * t;
}
"""


def shell(comp_id, dur_sec, fps, css, body, script, bg="#0a0b10", design=True):
    w, h = 1920, 1080
    stage_css = """
    .design-stage {
      position: absolute; left: 0; top: 0;
      width: 480px; height: 270px;
      overflow: hidden;
      transform: scale(4);
      transform-origin: top left;
    }""" if design else ""
    stage_open = '<div class="design-stage">' if design else ""
    stage_close = "</div>" if design else ""
    bg_rule = f'background: {bg};' if design else f'background: {bg};'
    return f"""<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    [data-composition-id="{comp_id}"] {{
      {bg_rule}
      overflow: hidden;
      position: relative;
      width: {w}px;
      height: {h}px;
    }}
    {stage_css}
    {css}
  </style>
</head>
<body>
  <div
    data-composition-id="{comp_id}"
    data-start="0"
    data-duration="{dur_sec}"
    data-fps="{fps}"
    data-width="{w}"
    data-height="{h}"
  >
    {stage_open}
    {body}
    {stage_close}
  </div>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
  <script>
    window.__timelines = window.__timelines || {{}};
    {MOTION}
    {G}
    {FRAME_HELPERS}
    {script}
  </script>
</body>
</html>
"""


def write(rel_dir, content):
    p = TYPO / rel_dir / "index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    print("wrote", p.relative_to(ROOT))


def gen_brace_expand():
    write("brace-expand", shell(
        "BraceExpand", 114 / 30, 30, "",
        """<div id="root" style="position:absolute;inset:0;background:#0a0b10;"></div>""",
        """
const tl = gsap.timeline({ paused: true });
const DUR = 114 / 30;
const HALF = 148;
const FONT = '-apple-system,system-ui,sans-serif';
const root = document.getElementById('root');
const state = { t: 0 };
tl.to(state, { t: 1, duration: DUR, ease: 'none', onUpdate: () => {
  const t = state.t;
  const on = t >= 0.07 ? 1 : 0;
  const ex = seg(t, 0.13, 0.34, E.outBack);
  const sc = lerp(ex, 0.6, 1);
  const x = HALF * ex * sc;
  const ls = lerp(seg(t, 0.42, 0.62, E.inOutQuad), 1, 2.6);
  root.innerHTML = `<div style="position:absolute;left:50%;top:50%;width:0;height:0">
    <div style="position:absolute;left:0;top:0;transform:translate(-50%,-50%);overflow:hidden;height:60px;display:flex;align-items:center;justify-content:center;width:${Math.max(0, x * 2 - 34)}px;opacity:${on}">
      <div style="font-weight:800;font-size:38px;font-family:${FONT};color:#fff;white-space:nowrap;letter-spacing:${ls}px;transform:scale(${sc})">Your title</div>
    </div>
    <div style="position:absolute;left:0;top:0;font-weight:800;font-size:44px;font-family:${FONT};color:#fff;transform:translate(-50%,-50%) translateX(${-x}px) scale(${sc});opacity:${on}">{</div>
    <div style="position:absolute;left:0;top:0;font-weight:800;font-size:44px;font-family:${FONT};color:#fff;transform:translate(-50%,-50%) translateX(${x}px) scale(${sc});opacity:${on}">}</div>
  </div>`;
}}, 0);
window.__timelines['BraceExpand'] = tl;
"""))


def gen_scramble():
    write("scramble", shell(
        "Scramble", 96 / 30, 30, "",
        """<div id="row" style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:#07080c;font-family:'SF Mono',Menlo,monospace;font-size:34px;letter-spacing:2px;"></div>""",
        """
const tl = gsap.timeline({ paused: true });
const DUR = 96 / 30;
const TEXT = 'TEMPLATE MOTION DEMO';
const POOL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#$%&*+=<>/\\\\';
const CHARS = [...TEXT];
const row = document.getElementById('row');
const state = { t: 0 };
tl.to(state, { t: 1, duration: DUR, ease: 'none', onUpdate: () => {
  const t = state.t;
  const frame = Math.floor(t * 96);
  row.innerHTML = CHARS.map((ch, i) => {
    let content = ch, color = '#3d4560', textShadow = 'none';
    if (ch !== ' ') {
      const lockAt = 0.25 + (i / CHARS.length) * 0.6 + rand(i * 7) * 0.06;
      if (t < 0.06) content = ' ';
      else if (t < lockAt) content = POOL[Math.floor(rand(i * 131 + Math.floor(frame / 2)) * POOL.length)];
      else {
        const flash = 1 - seg(t, lockAt, lockAt + 0.1);
        color = flash > 0.4 ? '#dff3ff' : '#e8eaf0';
        textShadow = `0 0 ${flash * 18}px rgba(120,200,255,${flash})`;
      }
    }
    return `<span style="min-width:0.62em;text-align:center;color:${color};text-shadow:${textShadow}">${content === ' ' ? '\\u00a0' : content}</span>`;
  }).join('');
}}, 0);
window.__timelines['Scramble'] = tl;
"""))


def main():
    gen_brace_expand()
    gen_scramble()
    print("done partial — extend script for remaining demos")


if __name__ == "__main__":
    main()
