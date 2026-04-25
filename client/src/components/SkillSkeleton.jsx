// ─── SkillSkeleton ────────────────────────────────────────────────────────────
// Placeholder rendered while GetSkills is in-flight.
// Uses the .skeleton-shimmer utility for the animated gradient sweep.
// Great for your talk: demonstrates Apollo loading state primitives.

export default function SkillSkeleton() {
  return (
    <div className="glass-card p-5 flex flex-col gap-4 overflow-hidden">

      {/* Category badge skeleton */}
      <div className="flex items-center justify-between">
        <div className="skeleton-shimmer h-6 w-24 rounded-lg" />
      </div>

      {/* Title skeleton */}
      <div className="skeleton-shimmer h-4 w-3/4 rounded-md" />

      {/* Level area skeleton */}
      <div className="space-y-2.5">
        <div className="flex justify-between items-center">
          <div className="skeleton-shimmer h-2.5 w-10 rounded" />
          <div className="skeleton-shimmer h-6 w-8 rounded" />
        </div>
        <div className="skeleton-shimmer h-1.5 w-full rounded-full" />
      </div>

      {/* Button skeleton */}
      <div className="skeleton-shimmer h-9 w-full rounded-xl mt-auto" />
    </div>
  );
}
