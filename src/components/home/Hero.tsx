import { useState } from "react";
import Button from "../common/Button";
import Input from "../common/Input";

type Repository = {
  name: string;
  owner: string;
  description: string;
  stars: number;
  forks: number;
  language: string;
};


export default function Hero() {

  const [repoUrl, setRepoUrl] = useState("");
  const [result, setResult] = useState<Repository | null>(null);

  const handleAnalyze = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          repo: repoUrl,
        }),
      });

      const data = await response.json();

      console.log(data);

      setResult(data);

    } catch (error) {
      console.error(error);
    }
  };

  return (
    <section className="mx-auto flex min-h-[80vh] max-w-5xl flex-col items-center justify-center px-6 text-center">
      <p className="mb-6 text-lg font-bold leading-8 text-purple-600 text-lg rounded-full bg-violet-100 px-4 py-2">
        ✨ AI-powered Repository Analysis
      </p>

      <h1 className="mb-6 text-6xl font-extrabold tracking-tight text-slate-900">
        Review GitHub Repositories Like a Senior Engineer
      </h1>

      <p className="mb-10 max-w-2xl text-lg leading-8 text-slate-600">
        Analyze any public GitHub repository for bugs,
        security issues, performance bottlenecks,
        and best practices in seconds.
      </p>

      <div className="flex w-full max-w-3xl items-center gap-4">
        <Input
          value={repoUrl}
          onChange={(e) => setRepoUrl(e.target.value)}
          placeholder="https://github.com/facebook/react"
        />

        <Button onClick={handleAnalyze}>
          Analyze Repository →
        </Button>
      </div>
      {result && (
        <div className="mt-8 w-full max-w-3xl rounded-xl border border-slate-200 bg-white p-6 shadow-md">
          <h2 className="text-2xl font-bold">
            {result.owner}/{result.name}
          </h2>

          <p className="mt-3 text-slate-600">
            {result.description}
          </p>

          <div className="mt-5 flex flex-wrap gap-6 text-lg">
            <span>⭐ {result.stars}</span>
            <span>🍴 {result.forks}</span>
            <span>💻 {result.language}</span>
          </div>
        </div>
      )}

    </section>
  );
}