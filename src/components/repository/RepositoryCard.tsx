import type { Repository } from "../../types/repository";
import { formatNumber } from "../../utils/format";

interface RepositoryCardProps {
  repository: Repository;
}

export default function RepositoryCard({
  repository,
}: RepositoryCardProps) {
  return (
    <div className="mt-8 w-full max-w-3xl rounded-xl border border-slate-200 bg-white p-6 shadow-md">

      {/* Header */}
      <div className="flex items-center gap-4">
        <img
          src={repository.avatar}
          alt={repository.owner}
          className="h-16 w-16 rounded-full border"
        />

        <div>
          <h2 className="text-2xl font-bold">
            {repository.owner}/{repository.name}
          </h2>

          <a
            href={repository.html_url}
            target="_blank"
            rel="noreferrer"
            className="text-sm text-blue-600 hover:underline"
          >
            View on GitHub →
          </a>
        </div>
      </div>

      {/* Description */}
      <p className="mt-5 text-slate-600">
        {repository.description}
      </p>

      {/* Last Updated */}
      <p className="mt-2 text-sm text-slate-500">
        Last updated:{" "}
        {new Date(repository.updated_at).toLocaleDateString()}
      </p>

      {/* Stats */}
      <div className="mt-5 flex flex-wrap gap-6 text-lg">
        <span>⭐ {formatNumber(repository.stars)}</span>
        <span>🍴 {formatNumber(repository.forks)}</span>
        <span>💻 {repository.language}</span>
      </div>

      {/* Languages */}
      <div className="mt-6 flex flex-wrap gap-2">
        {repository.languages.map((language) => (
          <span
            key={language}
            className="rounded-full bg-blue-100 px-3 py-1 text-sm font-medium text-blue-700"
          >
            {language}
          </span>
        ))}
      </div>

    </div>
  );
}