import "./globals.css";

import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "SentinelLocker",
  description: "Government-grade digital document locker"
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
