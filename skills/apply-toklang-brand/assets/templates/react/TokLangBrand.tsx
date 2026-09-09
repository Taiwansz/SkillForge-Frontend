import type { CSSProperties, ImgHTMLAttributes } from "react";

type BrandVariant = "stacked" | "extended" | "mark";
type BrandTheme = "light" | "dark";

const assets: Record<BrandVariant, Record<BrandTheme, string>> = {
  stacked: {
    light: "/brand/logos/toklang-stacked-light.svg",
    dark: "/brand/logos/toklang-stacked-dark.svg"
  },
  extended: {
    light: "/brand/logos/toklang-extended-light.svg",
    dark: "/brand/logos/toklang-extended-dark.svg"
  },
  mark: {
    light: "/brand/marks/toklang-flow-light.svg",
    dark: "/brand/marks/toklang-flow-dark.svg"
  }
};

export function TokLangBrand({
  variant = "extended",
  theme = "light",
  alt = "TokLang",
  ...props
}: ImgHTMLAttributes<HTMLImageElement> & {
  variant?: BrandVariant;
  theme?: BrandTheme;
}) {
  return <img src={assets[variant][theme]} alt={alt} {...props} />;
}

export function CompressionMetric({ before, after }: { before: number; after: number }) {
  const savings = before > 0 ? Math.round((1 - after / before) * 100) : 0;
  const style = { "--tok-saving": `${savings}%` } as CSSProperties;
  return (
    <section className="tok-metric" style={style} aria-label={`${savings}% de economia de tokens`}>
      <span>{before} tokens</span><i aria-hidden="true" /><strong>{after} tokens</strong><b>{savings}%</b>
    </section>
  );
}
