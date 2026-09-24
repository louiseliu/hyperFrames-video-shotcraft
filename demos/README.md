# demos/ — 镜头卡参考实现源码

多数镜头卡会在"参考实现"中指向本目录；必须先读卡片，再按其明确路径定位准确的
demo 文件，不能只凭卡名假设目录结构。这里的组件是调校过的 HyperFrames 实现——
**用卡先读准确源码**（SKILL.md 理念 5）。

## HyperFrames HTML 格式

每个 demo 都有一个 `index.html` 文件，是独立的 HyperFrames 合成：

```html
<div data-composition-id="DemoName"
     data-start="0" data-duration="5.6"
     data-fps="30" data-width="1920" data-height="1080">
  <!-- 场景元素 -->
</div>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<script>
  window.__timelines = window.__timelines || {};
  const tl = gsap.timeline({ paused: true });
  // 动画逻辑...
  window.__timelines["DemoName"] = tl;
</script>
```

预览和渲染：

```bash
cd demos/<category>/<demo-name>
npx hyperframes preview    # 浏览器预览
npx hyperframes render --output out.mp4  # 渲染 MP4
```

## 两类共享依赖

- `_fixtures/motion.js` — 缓动表 E / seg / lerp / 确定性 rand /
  DesignStage CSS 辅助函数。motion-lab 系 demo 使用。
- `_fixtures/Fixtures.tsx`（旧格式参考） — 灰阶假 UI 场景件。
- `_fixtures/PageCam2D.tsx`（旧格式参考） — 2.5D 页面相机坐标数学，
  仅依赖 hyperframes。

## Motion 系 demo（2026-08 并入的 48 张卡）

这批卡使用 480×270 设计坐标（`.design-stage` div 等比放大到合成分辨率），
参数表数值都在此坐标系下标定，改合成分辨率不需要动参数。

动画全部由归一化 t（0→1）驱动计算，无真随机，逐帧确定性渲染。
在 HyperFrames 中使用 GSAP `onUpdate` 回调实现：

```js
const state = { t: 0 };
tl.to(state, {
  t: 1, duration: DUR, ease: "none",
  onUpdate: () => {
    const t = state.t;
    // 动效逻辑
  }
}, 0);
```

## 真实视频素材（ClipCard，assets/lib/ClipCard.html）

把一段视频包进圆角"卡片"，让运镜骨架驱动真实 footage。
在 HyperFrames 中使用 `<video>` 元素 + GSAP 变换实现。

## 测试与验证

1. **渲染冒烟**：`npx hyperframes render` 渲染各 demo 验证不崩。
2. **视觉检查**：`npx hyperframes inspect` 检查布局问题。
3. **对比验证**：`npx hyperframes validate` 运行 WCAG 对比度审计。

## 旧格式参考

原始的 `.tsx` 文件保留在各 demo 目录中作为参考。这些使用 React + Remotion
的旧格式，其中的动画时序和缓动参数是经过调校的权威来源。新的 `index.html`
文件是从这些 TSX 翻译而来的 HyperFrames 原生格式。
