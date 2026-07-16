import Button from "../common/Button";
import Input from "../common/Input";

export default function Hero() {
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

      <div className="flex w-full max-w-2xl gap-4 font-semibold text-lg">
        <Input placeholder="https://github.com/facebook/react" />

        <Button>
          Analyze Repository →
        </Button>
      </div>

    </section>
  );
}