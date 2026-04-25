// ─── Toast ────────────────────────────────────────────────────────────────────
// Slide-in notification rendered when a subscription event arrives.
// Wrapped in <AnimatePresence> in App.jsx so exit animations fire on unmount.

import { motion } from 'framer-motion';

export default function Toast({ message }) {
  return (
    <motion.div
      initial={{ opacity: 0, x: 72, scale: 0.9 }}
      animate={{ opacity: 1, x:  0, scale: 1   }}
      exit={{    opacity: 0, x: 72, scale: 0.9 }}
      transition={{ type: 'spring', stiffness: 300, damping: 26 }}
      className="glass-card pointer-events-auto px-4 py-3 max-w-xs"
      style={{
        borderColor: 'rgba(0,245,255,0.22)',
        background:  'rgba(0,245,255,0.05)',
      }}
    >
      <p className="font-mono text-sm text-cyan-300">{message}</p>
    </motion.div>
  );
}
