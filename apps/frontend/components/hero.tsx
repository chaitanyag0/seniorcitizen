"use client";

import { motion } from "framer-motion";

export function Hero() {
  return (
    <motion.section
      initial={{ opacity: 0, y: 24 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6 }}
      className="glass rounded-3xl p-8 shadow-2xl"
    >
      <p className="text-sm uppercase tracking-[0.3em] text-indigo-500">SentinelLocker</p>
      <h1 className="mt-4 text-4xl font-semibold leading-tight md:text-6xl">
        World-class secure digital document vault
      </h1>
      <p className="mt-4 max-w-2xl text-slate-600 dark:text-slate-300">
        Zero-trust architecture, end-to-end encryption, biometric-ready MFA and AI-powered retrieval.
      </p>
    </motion.section>
  );
}
