interface AnalysisCardProps {
  analysis: {
    summary: string;
    strengths: string[];
    improvements: string[];
    score: number;
  };
}

export default function AnalysisCard({
  analysis,
}: AnalysisCardProps) {
  return (
    <div className="mt-8 w-full max-w-3xl rounded-xl border border-slate-200 bg-white p-6 shadow-md">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold">
          AI Analysis
        </h2>

        <span className="rounded-full bg-green-100 px-4 py-2 text-lg font-bold text-green-700">
          {analysis.score}/100
        </span>
      </div>

      <p className="mt-5 text-slate-600">
        {analysis.summary}
      </p>

      <div className="mt-6">
        <h3 className="font-semibold text-green-700">
          Strengths
        </h3>

        <ul className="mt-2 list-disc space-y-1 pl-5">
          {analysis.strengths.map((strength) => (
            <li key={strength}>{strength}</li>
          ))}
        </ul>
      </div>

      <div className="mt-6">
        <h3 className="font-semibold text-red-700">
          Improvements
        </h3>

        <ul className="mt-2 list-disc space-y-1 pl-5">
          {analysis.improvements.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}