import FeatureCard from "./FeatureCard";

const features = [
  {
    id: "bug-detection",
    icon: "🐞",
    title: "Bug Detection",
    description: "Automatically detect logic errors and potential bugs."
  },
  {
    id: "security-review",
    icon: "🔒",
    title: "Security Review",
    description: "Find common security vulnerabilities."
  },
  {
    id: "performance-optimization",
    icon: "⚡",
    title: "Performance",
    description: "Identify inefficient code patterns."
  },
  {
    id: "learning-mode",
    icon: "📚",
    title: "Learning Mode",
    description: "Understand why each improvement is suggested."
  }
];

export default function Features() {
  return (
    <section className="mx-auto max-w-6xl px-6 py-20">
      <h2 className="mb-10 text-center text-4xl font-bold">
        Everything You Need For Better Code
      </h2>

      <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-4">
        {features.map((feature) => (
          <FeatureCard
            key={feature.id}
            icon={feature.icon}
            title={feature.title}
            description={feature.description}
          />
        ))}
      </div>
    </section>
  );
}