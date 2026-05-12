import { useQuery } from '@apollo/client';
import { AnimatePresence } from 'framer-motion';
import { GET_SKILLS } from '../graphql/queries';
import SkillCard from './SkillCard';
import SkillSkeleton from './SkillSkeleton';

export default function SkillGrid({ selectedCategory }) {
  const { data, loading, error } = useQuery(GET_SKILLS, {
    variables: selectedCategory ? { category: selectedCategory } : {},
  });

  if (error) return (
    <div className="error-msg">
      <p>GraphQL Error: {error.message}</p>
      <p style={{fontSize:'0.8rem',opacity:0.6}}>Is the server running? cd server && npm run dev</p>
    </div>
  );

  if (loading) return (
    <div className="skill-grid">
      {Array.from({ length: 8 }).map((_, i) => <SkillSkeleton key={i} />)}
    </div>
  );

  return (
    <div className="skill-grid">
      <AnimatePresence mode="popLayout">
        {data?.getSkills.map(skill => (
          <SkillCard key={skill.id} skill={skill} />
        ))}
      </AnimatePresence>
    </div>
  );
}
