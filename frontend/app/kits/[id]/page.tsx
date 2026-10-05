export default function KitPage({ params }: { params: { id: string } }) {
  return (
    <section>
      <h1 className="text-2xl font-bold">Study Kit {params.id}</h1>
      <p className="mt-2 text-sm text-slate-600">TODO Phase 3/4: tabs — Summary, Concepts, MCQs, Flashcards.</p>
    </section>
  );
}
