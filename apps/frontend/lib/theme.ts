"use client";

export function toggleTheme(): void {
  const root = document.documentElement;
  root.classList.toggle("dark");
  localStorage.setItem("theme", root.classList.contains("dark") ? "dark" : "light");
}

export function loadTheme(): void {
  const saved = localStorage.getItem("theme");
  if (saved === "dark") document.documentElement.classList.add("dark");
}
