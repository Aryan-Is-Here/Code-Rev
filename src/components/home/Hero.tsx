import { useState } from "react";
import Button from "../common/Button";
import Input from "../common/Input";


export default function Hero() {

  const [repoUrl, setRepoUrl] = useState("");
  const [result, setResult] = useState("");

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

      setResult(data.message);
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
        <div className="mt-8 rounded-lg bg-green-100 p-4 text-green-800">
          {result}
        </div>
      )}

    </section>
  );
}