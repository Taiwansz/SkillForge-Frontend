import type { Config } from "tailwindcss";

const thloopPreset: Partial<Config> = {
  theme: {
    extend: {
      colors: {
        thloop: {
          black: "#0A0A0A",
          paper: "#F0EDE6",
          gold: "#C8B560",
          chassis: "#2A2A2A",
          smoke: "#5C5C5C",
        },
        background: "var(--tl-bg)",
        surface: "var(--tl-surface)",
        foreground: "var(--tl-text)",
        accent: "var(--tl-accent)",
      },
      fontFamily: {
        display: ["Space Grotesk", "Arial", "sans-serif"],
        mono: ["IBM Plex Mono", "JetBrains Mono", "ui-monospace", "monospace"],
      },
      borderRadius: {
        tl: "0.5rem",
      },
      transitionTimingFunction: {
        thloop: "cubic-bezier(0.16, 1, 0.3, 1)",
      },
    },
  },
};

export default thloopPreset;
