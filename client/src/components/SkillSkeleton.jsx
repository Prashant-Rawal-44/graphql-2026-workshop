export default function SkillSkeleton() {
  return (
    <div className="skill-card skeleton-card">
      <div className="skeleton-shimmer" style={{width:'60%',height:'18px',borderRadius:'4px',marginBottom:'8px'}} />
      <div className="skeleton-shimmer" style={{width:'35%',height:'12px',borderRadius:'4px',marginBottom:'12px'}} />
      <div className="skeleton-shimmer" style={{width:'100%',height:'10px',borderRadius:'4px',marginBottom:'6px'}} />
      <div className="skeleton-shimmer" style={{width:'80%',height:'10px',borderRadius:'4px',marginBottom:'16px'}} />
      <div className="skeleton-shimmer" style={{width:'100%',height:'6px',borderRadius:'3px',marginBottom:'12px'}} />
      <div className="skeleton-shimmer" style={{width:'100%',height:'34px',borderRadius:'6px'}} />
    </div>
  );
}
