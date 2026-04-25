/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      // ── Neon palette ─────────────────────────────────────────────────────
      colors: {
        neon: {
          cyan:   '#00f5ff',
          purple: '#bf00ff',
          green:  '#00ff88',
          orange: '#ff6b00',
          yellow: '#ffbe00',
          pink:   '#ff006e',
        },
      },

      // ── Typography ───────────────────────────────────────────────────────
      fontFamily: {
        mono: ['"JetBrains Mono"', '"Fira Code"', 'ui-monospace', 'monospace'],
        sans: ['Inter', 'ui-sans-serif', 'system-ui'],
      },

      // ── Custom animations ────────────────────────────────────────────────
      animation: {
        shimmer:      'shimmer 2.5s linear infinite',
        'pulse-slow': 'pulse 3s ease-in-out infinite',
        float:        'float 4s ease-in-out infinite',
        'spin-slow':  'spin 3s linear infinite',
      },
      keyframes: {
        shimmer: {
          '0%':   { backgroundPosition: '-1000px 0' },
          '100%': { backgroundPosition:  '1000px 0' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%':      { transform: 'translateY(-8px)' },
        },
      },
    },
  },
  plugins: [],
};
