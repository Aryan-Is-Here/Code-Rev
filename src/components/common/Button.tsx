import type { ReactNode } from "react";

interface ButtonProps {
  children: ReactNode;
}

export default function Button({ children }: ButtonProps) {
  return (
    <button className="rounded-lg bg-blue-600 px-10 py-3 font-semibold text-white transition hover:bg-blue-700">
      {children}
    </button>
  );
} 