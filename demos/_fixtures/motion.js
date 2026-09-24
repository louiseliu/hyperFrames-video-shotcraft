// Motion 动效公共件 —— 源自 motion-lab 孵化轮沉淀的 48 张卡共用：
// 缓动表 E / 分段进度 seg / 插值 lerp / 确定性伪随机 rand / DesignStage CSS 辅助。
// 全部是纯函数，由 GSAP timeline 驱动，满足 HyperFrames 确定性渲染要求。

const E = {
  linear: (t) => t,
  inQuad: (t) => t * t,
  outQuad: (t) => t * (2 - t),
  inOutQuad: (t) => (t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t),
  inCubic: (t) => t * t * t,
  outCubic: (t) => 1 - Math.pow(1 - t, 3),
  inOutCubic: (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2),
  outQuart: (t) => 1 - Math.pow(1 - t, 4),
  outQuint: (t) => 1 - Math.pow(1 - t, 5),
  inQuart: (t) => t * t * t * t,
  outExpo: (t) => (t === 1 ? 1 : 1 - Math.pow(2, -10 * t)),
  inExpo: (t) => (t === 0 ? 0 : Math.pow(2, 10 * t - 10)),
  outBack: (t, s = 1.70158) => 1 + (s + 1) * Math.pow(t - 1, 3) + s * Math.pow(t - 1, 2),
  inBack: (t, s = 1.70158) => (s + 1) * t * t * t - s * t * t,
  outElastic: (t) =>
    t === 0 ? 0 : t === 1 ? 1 : Math.pow(2, -10 * t) * Math.sin((t * 10 - 0.75) * ((2 * Math.PI) / 3)) + 1,
  spring: (t, bounce = 0.25) => {
    const w = 8 + 8 * (1 - bounce);
    return 1 - Math.exp(-6 * t) * Math.cos(w * t * bounce * 2.2);
  },
};

const lerp = (t, a, b) => a + (b - a) * t;

// 分段进度：t 在 [t0,t1] 内归一化后过 ease，越界钳位——所有动效的时间轴原语
const seg = (t, t0, t1, ease = E.linear) =>
  ease(Math.min(1, Math.max(0, (t - t0) / (t1 - t0))));

// 确定性伪随机（同种子跨帧/跨渲染可复现）
const rand = (seed) => {
  const x = Math.sin(seed * 127.1 + 311.7) * 43758.5453;
  return x - Math.floor(x);
};

// GSAP CustomEase 映射表：将 E 缓动名转为 GSAP ease 字符串
const GSAP_EASE_MAP = {
  linear: "none",
  inQuad: "power1.in",
  outQuad: "power1.out",
  inOutQuad: "power1.inOut",
  inCubic: "power2.in",
  outCubic: "power2.out",
  inOutCubic: "power2.inOut",
  outQuart: "power3.out",
  outQuint: "power4.out",
  inQuart: "power3.in",
  outExpo: "expo.out",
  inExpo: "expo.in",
  outBack: "back.out(1.7)",
  inBack: "back.in(1.7)",
  outElastic: "elastic.out(1, 0.3)",
  spring: "back.out(1.4)",
};

// 设计坐标容器 CSS：内容按 w×h 作画，等比放大铺满合成分辨率。
// 在 HyperFrames HTML 中，用作 .design-stage 样式的参数。
function designStageCSS(compWidth = 1920, w = 480, h = 270, raster = 'scale') {
  const scale = compWidth / w;
  if (raster === 'zoom') {
    return `position:absolute;left:0;top:0;width:${w}px;height:${h}px;overflow:hidden;zoom:${scale};`;
  }
  return `position:absolute;left:0;top:0;width:${w}px;height:${h}px;overflow:hidden;transform:scale(${scale});transform-origin:top left;`;
}
