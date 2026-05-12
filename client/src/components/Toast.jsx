import { motion } from 'framer-motion';

export default function Toast({ message, onDone }) {
  return (
    <motion.div
      className="toast"
      initial={{ x: 120, opacity: 0 }}
      animate={{ x: 0, opacity: 1 }}
      exit={{ x: 120, opacity: 0 }}
      transition={{ type: 'spring', stiffness: 200, damping: 20 }}
      onAnimationComplete={(_def) => {
        if (_def.opacity === 0) onDone();
      }}
    >
      {message}
    </motion.div>
  );
}
