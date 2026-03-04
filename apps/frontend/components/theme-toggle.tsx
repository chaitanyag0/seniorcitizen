"use client";

import { Moon, Sun } from "lucide-react";
import { useEffect, useState } from "react";

import { loadTheme, toggleTheme } from "@/lib/theme";

export function ThemeToggle() {
  const [dark, setDark] = useState(false);

  useEffect(() => {
    loadTheme();
    setDark(document.documentElement.classList.contains("dark"));
  }, []);

  return (
    <button
      className="rounded-full border border-slate-300 px-3 py-2 dark:border-slate-700"
      onClick={() => {
        toggleTheme();
        setDark(document.documentElement.classList.contains("dark"));
      }}
    >
      {dark ? <Sun size={16} /> : <Moon size={16} />}
    </button>
  );
}
