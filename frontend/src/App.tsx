
import { useState } from "react";
import ImageUploader from "./components/ImageUploader";
import { searchImage, type SearchResult } from "../services/api";

function App() {
  const [results, setResults] = useState<SearchResult[]>([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async (file: File) => {
    try {
      setLoading(true);
      const data = await searchImage(file);
      setResults(data);
    } catch (error) {
      console.error("Erreur lors de la recherche :", error);
    } finally {
      setLoading(false);
    }
  };

   const API_URL = import.meta.env.VITE_API_URL;
  return (
    <main className="min-h-screen bg-gray-950 text-white px-6 py-12">
      <div className="mx-auto max-w-6xl">

        {/* Header */}
        <header className="mb-12 text-center">
          <h1 className="text-4xl font-bold tracking-tight">
            AI Image Search
          </h1>

          <p className="mt-3 text-gray-400">
            Trouvez des images similaires grâce à l'intelligence artificielle.
          </p>
        </header>

        {/* Upload */}
        <section className="mx-auto max-w-2xl rounded-2xl border border-gray-800 bg-gray-900 p-8">
          <ImageUploader onSearch={handleSearch} />
        </section>

        {/* Loading */}
        {loading && (
          <div className="mt-10 text-center text-gray-400">
            Recherche des images similaires...
          </div>
        )}

        {/* Results */}
        {results.length > 0 && !loading && (
          <section className="mt-12">

            <h2 className="mb-6 text-2xl font-semibold">
              Images similaires
            </h2>

            <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-5">
              {results.map((result) => (
                <article
                  key={result.index}
                  className="overflow-hidden rounded-xl border border-gray-800 bg-gray-900"
                >
                  <img
                    src={`${API_URL}${result.image_url}`}
                    alt={result.label}
                    className="h-48 w-full object-cover"
                  />

                  <div className="p-4">
                    <h3 className="font-medium">
                      {result.label}
                    </h3>

                    <p className="mt-2 text-sm text-gray-400">
                      Similarité :{" "}
                      {(result.similarity * 100).toFixed(1)}%
                    </p>
                  </div>
                </article>
              ))}
            </div>

          </section>
        )}

      </div>
    </main>
  );
}

export default App;

