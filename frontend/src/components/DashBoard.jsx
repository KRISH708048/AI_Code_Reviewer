import React, { useState } from "react";
import CodeInput from "./CodeInput"
import AnalysisResult from './AnalysisResult';

const DashBoard = () => {
  const [analysisResult, setAnalysisResult] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isPdfLoading, setIsPdfLoading] = useState(false);
  const [error, setError] = useState("");

  const handleAnalyze = async (type, payload) => {
    if (
      !payload ||
      (type === "text" && !payload.code) ||
      (type === "file" && !payload.file)
    ) {
      setError(
        type === "text" ? "Please paste some code." : "Please select a file."
      );
      return;
    }

    setError("");
    setIsLoading(true);
    setAnalysisResult(null);

    try {
      let response;
      if (type === "text") {
        const apiPayload = {
          code: payload.code,
          language: payload.language,
          user: { id: "1", email: "demo@example.com" },
        };
        response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/analyze/json`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(apiPayload),
        });
      } else {
        const formData = new FormData();
        formData.append("file", payload.file);
        formData.append("language", payload.language);
        formData.append("user", JSON.stringify({ id: "1", email: "demo" }));
        response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/analyze/file`, {
          method: "POST",
          body: formData,
        });
      }

      if (!response.ok) {
        const errData = await response.json();
        throw new Error(
          errData.detail || "An unknown error occurred during analysis."
        );
      }

      const resultData = await response.json();
      setAnalysisResult(resultData);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  const handleDownloadPdf = async () => {
    if (!analysisResult) return;

    setIsPdfLoading(true);
    setError("");

    try {
      const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/analyze/pdf`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(analysisResult),
      });

      if (!response.ok) {
        throw new Error("Failed to generate PDF report.");
      }

      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `code_review_${new Date().toISOString().slice(0, 10)}.pdf`;
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
      a.remove();
    } catch (err) {
      setError(err.message);
    } finally {
      setIsPdfLoading(false);
    }
  };
  return (
    <main className="flex-grow flex flex-col md:flex-row p-4 md:p-8 gap-8 mx-auto w-full min-h-0">
      <div className="w-full md:w-1/2 flex flex-col min-h-0">
        <CodeInput onAnalyze={handleAnalyze} isLoading={isLoading} />
      </div>
      <div className="w-full md:w-1/2 flex flex-col min-h-0">
        <AnalysisResult
          result={analysisResult}
          error={error}
          isLoading={isLoading}
          isPdfLoading={isPdfLoading}
          onDownloadPdf={handleDownloadPdf}
        />
      </div>
    </main>
  );
};

export default DashBoard;
