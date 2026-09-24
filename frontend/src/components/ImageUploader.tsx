
import { useRef, useState } from "react";

interface ImageUploaderProps {
  onSearch: (file: File) => void;
}

export default function ImageUploader({ onSearch }: ImageUploaderProps) {
  const [file, setFile] = useState<File | null>(null);
  const [preview, setPreview] = useState<string | null>(null);
  const [dragging, setDragging] = useState(false);

  const inputRef = useRef<HTMLInputElement>(null);

  const selectFile = (selectedFile: File) => {
    if (!selectedFile.type.startsWith("image/")) {
      return;
    }

    setFile(selectedFile);
    setPreview(URL.createObjectURL(selectedFile));
  };

  const handleFileChange = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    const selectedFile = event.target.files?.[0];

    if (selectedFile) {
      selectFile(selectedFile);
    }
  };

  const handleDrop = (event: React.DragEvent<HTMLDivElement>) => {
    event.preventDefault();
    setDragging(false);

    const droppedFile = event.dataTransfer.files[0];

    if (droppedFile) {
      selectFile(droppedFile);
    }
  };

  return (
    <div className="space-y-6">

      {/* Upload zone */}
      <div
        onDragOver={(event) => {
          event.preventDefault();
          setDragging(true);
        }}
        onDragLeave={() => setDragging(false)}
        onDrop={handleDrop}
        onClick={() => inputRef.current?.click()}
        className={`cursor-pointer rounded-xl border-2 border-dashed p-10 text-center transition ${
          dragging
            ? "border-blue-500 bg-blue-500/10"
            : "border-gray-700 hover:border-gray-500"
        }`}
      >
        <input
          ref={inputRef}
          type="file"
          accept="image/*"
          onChange={handleFileChange}
          className="hidden"
        />

        <div className="text-4xl">🖼️</div>

        <p className="mt-4 font-medium">
          Glissez une image ici
        </p>

        <p className="mt-2 text-sm text-gray-500">
          ou cliquez pour sélectionner une image
        </p>
      </div>

      {/* Preview */}
      {preview && (
        <div className="overflow-hidden rounded-xl border border-gray-800">
          <img
            src={preview}
            alt="Aperçu"
            className="max-h-80 w-full object-contain"
          />
        </div>
      )}

      {/* Search button */}
      <button
        onClick={() => file && onSearch(file)}
        disabled={!file}
        className="w-full rounded-xl bg-blue-600 px-6 py-3 font-medium transition hover:bg-blue-500 disabled:cursor-not-allowed disabled:opacity-40"
      >
        Rechercher des images similaires
      </button>
    </div>
  );
}

