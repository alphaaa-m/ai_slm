import Link from "next/link";

const links = [
  { href: "/", label: "Dashboard" },
  { href: "/planner", label: "Planner" },
  { href: "/documents", label: "Documents" },
  { href: "/tutor", label: "Tutor" },
  { href: "/progress", label: "Progress" },
  { href: "/login", label: "Login" },
];

export function Nav() {
  return (
    <header className="border-b bg-white">
      <nav className="mx-auto flex max-w-5xl items-center gap-4 px-4 py-3">
        <Link href="/" className="font-bold">
          AI StudyOS
        </Link>
        <div className="flex gap-3 text-sm">
          {links.map((l) => (
            <Link key={l.href} href={l.href} className="text-slate-600 hover:text-slate-900">
              {l.label}
            </Link>
          ))}
        </div>
        <span className="ml-auto rounded bg-slate-100 px-2 py-1 text-xs text-slate-500">Phase 0 skeleton</span>
      </nav>
    </header>
  );
}
