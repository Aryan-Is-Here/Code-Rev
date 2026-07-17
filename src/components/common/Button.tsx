import type { ReactNode } from "react";

interface ButtonProps {
  children: ReactNode;
  onClick?: () => void;
}

export default function Button({ 
  children,
  onClick,
 }: ButtonProps) {
  return (
    <button
      onClick={onClick}
      className="rounded-lg bg-blue-600 px-8 py-3 font-semibold text-white transition hover:bg-blue-700"
    >
      {children}
    </button>
  );
} 