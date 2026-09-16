type ThPayLogoProps = {
  theme?: 'dark-on-light' | 'light-on-dark';
  compact?: boolean;
  className?: string;
};

export function ThPayLogo({
  theme = 'dark-on-light',
  compact = false,
  className,
}: ThPayLogoProps) {
  const src = compact
    ? theme === 'light-on-dark'
      ? '/brand/connector-t-light.svg'
      : '/brand/connector-t-dark.svg'
    : theme === 'light-on-dark'
      ? '/brand/thpay-primary-light.svg'
      : '/brand/thpay-primary-dark.svg';

  return (
    <img
      src={src}
      alt={compact ? 'THP' : 'ThPay'}
      className={className}
      draggable={false}
    />
  );
}
