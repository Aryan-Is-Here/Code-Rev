import type { ChangeEvent } from "react";

interface InputProps {
  placeholder: string;
  value: string;
  onChange: (e: ChangeEvent<HTMLInputElement>) => void;
}

export default function Input({
  placeholder,
  value,
  onChange,
}: InputProps) {
  return (
    <input
      type="text"
      placeholder={placeholder}
      value={value}
      onChange={onChange}
      className="flex-1 w-full rounded-lg border border-slate-300 px-4 py-3 outline-none transition focus:border-blue-600"
    />
  );
}