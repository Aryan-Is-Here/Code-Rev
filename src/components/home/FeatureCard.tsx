import type { ReactNode } from "react";

interface FeatureCardProps {
  icon: ReactNode;
  title: string;
  description: string;
}

export default function FeatureCard({
  icon,
  title,
  description,
}: FeatureCardProps) {
  return (
    <div className="rounded-2xl border border-slate-200 p-8 transition-all duration-300 hover:-translate-y-2 hover:border-blue-300 hover:shadow-xl">
      <div className="mb-4 flex justify-center text-4xl">{icon}</div>

      <h3 className="mb-2 text-center text-xl font-semibold">
        {title}
      </h3>

      <p className="text-slate-600 text-center">
        {description}
      </p>
    </div>
  );
}