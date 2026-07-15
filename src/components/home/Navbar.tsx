export default function Navbar() {
  return (
    <nav className="flex items-center justify-between border-b border-slate-200 px-10 py-5">
      <h1 className="text-2xl font-bold text-slate-900">
        code-rev
      </h1>

      <div className="flex gap-8">
        <a
          href="#"
          className="text-slate-600 transition hover:text-blue-600"
        >
          Docs
        </a>

        <a
          href="#"
          className="text-slate-600 transition hover:text-blue-600"
        >
          GitHub
        </a>

        <a
          href="#"
          className="text-slate-600 transition hover:text-blue-600"
        >
          About
        </a>
      </div>
    </nav>
  );
}