// ─── LiveIndicator ────────────────────────────────────────────────────────────
// Fixed badge showing WebSocket subscription status.
// The pulsing dot is a simple visual cue that the WS connection is active.

import { motion } from 'framer-motion';

export default function LiveIndicator() {
  return (
    <div className="fixed top-4 right-4 z-50">
      <div
        className="glass-card flex items-center gap-2 px-3 py-1.5"
        style={{ borderColor: 'rgba(0,255,136,0.18)' }}
      >
        {/* Pulsing dot */}
        <motion.span
          animate={{ scale: [1, 1.55, 1], opacity: [1, 0.45, 1] }}
          transition={{ duration: 1.6, repeat: Infinity, ease: 'easeInOut' }}
          className="block w-2 h-2 rounded-full"
          style={{
            background: '#00ff88',
            boxShadow:  '0 0 8px #00ff88, 0 0 18px rgba(0,255,136,0.4)',
          }}
        />
        <span className="font-mono text-[0.6rem] tracking-[0.3em] text-gray-400 uppercase">
          Live
        </span>
      </div>
    </div>
  );
}
