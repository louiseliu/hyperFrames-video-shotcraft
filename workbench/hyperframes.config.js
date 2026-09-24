// HyperFrames CLI configuration for workbench
// Manages composition preview and render export
import { existsSync } from "node:fs";
import path from "node:path";

const proj = path.resolve(
  process.cwd(),
  existsSync(path.resolve(process.cwd(), "proj", "workbench.ts")) ? "proj" : "proj-stub",
);

export default {
  videoImageFormat: 'jpeg',
  overwriteOutput: true,
  chromiumOpenGlRenderer: 'angle',
  concurrency: 4,
  resolve: {
    alias: {
      "@proj": proj,
      "@demos": path.resolve(process.cwd(), "demosrc"),
    },
  },
};
