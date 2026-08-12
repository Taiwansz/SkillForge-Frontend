import type { CSSProperties } from "react";

type ThLoopLogoProps = {
  compact?: boolean;
  className?: string;
  priority?: boolean;
  style?: CSSProperties;
  theme?: "dark" | "light";
};

export function ThLoopLogo({
  compact = false,
  className,
  priority = false,
  style,
  theme = "dark",
}: ThLoopLogoProps) {
  const assets = {
    dark: {
      compact: "/brand/twin-chamber-light.svg",
      full: "/brand/thloop-continuous-core-light.svg",
    },
    light: {
      compact: "/brand/twin-chamber-dark.svg",
      full: "/brand/thloop-continuous-core-dark.svg",
    },
  } as const;
  const src = compact ? assets[theme].compact : assets[theme].full;

  return (
    <img
      alt={compact ? "" : "ThLoop"}
      aria-hidden={compact || undefined}
      className={className}
      decoding="async"
      fetchPriority={priority ? "high" : "auto"}
      height={compact ? 132 : 186}
      src={src}
      style={{ display: "block", height: "auto", maxWidth: "100%", ...style }}
      width={compact ? 251 : 854}
    />
  );
}
