import { Hero } from "@/components/hero";
import { ThemeToggle } from "@/components/theme-toggle";
import { UploadCard } from "@/components/upload-card";

export default function HomePage() {
  return (
    <main className="mx-auto min-h-screen max-w-6xl p-6 md:p-10">
      <div className="mb-6 flex justify-end">
        <ThemeToggle />
      </div>
      <Hero />
      <section className="mt-6 grid gap-6 md:grid-cols-2">
        <UploadCard />
        <div className="glass rounded-2xl p-6">
          <h2 className="text-xl font-semibold">AI Smart Search</h2>
          <p className="mt-2 text-sm text-slate-500 dark:text-slate-300">
            Semantic tags, auto-categorization, and voice query retrieval for instant access.
          </p>
        </div>
      </section>
    </main>
  );
}
