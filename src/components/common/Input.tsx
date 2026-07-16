interface InputProps {
  placeholder: string;
}

export default function Input({ placeholder }: InputProps) {
  return (
    <input
      type="text"
      placeholder={placeholder}
      className="w-full rounded-lg border border-slate-300 px-4 py-3 outline-none transition focus:border-blue-600"
    />
  );
}