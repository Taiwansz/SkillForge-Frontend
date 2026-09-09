import type { Config } from "tailwindcss";

const tokLangPreset = {
  theme: {
    extend: {
      colors: {
        tok: {
          silver: "#D9DADC",
          wine: "#4A1824",
          yellow: "#FFD324",
          paper: "#F7F7F4",
          night: "#130B10",
          surface: "#211219",
          raised: "#2B1820",
          muted: "#AEB2B8"
        }
      },
      borderRadius: { tok: "18px", "tok-lg": "28px" },
      fontFamily: {
        display: ["Arial Black", "Helvetica Neue", "Arial", "sans-serif"],
        mono: ["IBM Plex Mono", "JetBrains Mono", "ui-monospace", "monospace"]
      }
    }
  }
} satisfies Config;

export default tokLangPreset;
