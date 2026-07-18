import type { Repository } from "../../types/repository";

interface RepositoryCardProps {
  repository: Repository;
}

export default function RepositoryCard({
  repository,
}: RepositoryCardProps) {
  return (
    <div className="mt-8 w-full max-w-3xl rounded-xl border border-slate-200 bg-white p-6 shadow-md">
      <h2 className="text-2xl font-bold">
        {repository.owner}/{repository.name}
      </h2>

      <p className="mt-3 text-slate-600">
        {repository.description}
      </p>

      <div className="mt-5 flex flex-wrap gap-6 text-lg">
        <span>⭐ {repository.stars}</span>
        <span>🍴 {repository.forks}</span>
        <span>💻 {repository.language}</span>
      </div>
    </div>
  );
}