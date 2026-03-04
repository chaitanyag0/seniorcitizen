"use client";

import { motion } from "framer-motion";
import { UploadCloud } from "lucide-react";
import { useState } from "react";

export function UploadCard() {
  const [progress, setProgress] = useState(0);

  return (
    <div className="glass rounded-2xl p-6">
      <div className="flex items-center gap-2 text-lg font-medium">
        <UploadCloud size={20} /> Drag & Drop Secure Upload
      </div>
      <p className="mt-2 text-sm text-slate-500 dark:text-slate-300">PDF, JPG, PNG, DOCX • encrypted before storage</p>
      <button
        className="mt-4 rounded-xl bg-indigo-600 px-4 py-2 text-sm text-white"
        onClick={() => setProgress((prev) => (prev >= 100 ? 0 : prev + 25))}
      >
        Simulate Upload
      </button>
      <div className="mt-4 h-2 rounded-full bg-slate-200 dark:bg-slate-800">
        <motion.div
          className="h-2 rounded-full bg-emerald-500"
          animate={{ width: `${progress}%` }}
          transition={{ type: "spring", stiffness: 120, damping: 18 }}
        />
      </div>
    </div>
  );
}
