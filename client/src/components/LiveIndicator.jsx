export default function LiveIndicator({ connected = true }) {
  return (
    <div className={`live-indicator ${connected ? 'live' : 'disconnected'}`}>
      <span className="live-dot" />
      <span>{connected ? 'Live' : 'Offline'}</span>
    </div>
  );
}
