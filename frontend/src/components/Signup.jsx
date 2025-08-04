import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

const SwapIcon = () => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    className="h-6 w-6 text-white"
    fill="none"
    viewBox="0 0 24 24"
    stroke="currentColor"
    strokeWidth={2}
  >
    <path
      strokeLinecap="round"
      strokeLinejoin="round"
      d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"
    />
  </svg>
);

const Signup = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();
  const [isSwapped, setIsSwapped] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess("");
    setIsLoading(true);

    try {
      const response = await fetch(
        `${import.meta.env.VITE_API_BASE_URL}/users`,
        // '/api/users',
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email, password }),
        }
      );

      if (!response.ok) {
        const errData = await response.json();
        throw new Error(errData.detail || "Signup failed. Please try again.");
      }

      setSuccess("Account created! Redirecting to login...");
      setTimeout(() => navigate("/login"), 2000);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="bg-gray-900 min-h-screen flex items-center justify-center p-4">
      <div className="relative w-full max-w-4xl flex bg-gray-800 rounded-2xl shadow-2xl overflow-hidden">
        <button
          onClick={() => setIsSwapped(!isSwapped)}
          className="hidden md:flex absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 z-20 bg-teal-500 hover:bg-teal-600 rounded-full p-3 transition-transform duration-300 hover:scale-110"
          aria-label="Swap panels"
        >
          <SwapIcon />
        </button>
        <div
          className={`hidden md:block w-1/2 bg-cover bg-center p-12 text-white transition-transform duration-700 ease-in-out ${
            isSwapped ? "translate-x-full" : ""
          }`}
          style={{
            backgroundImage:
              "url('https://images.unsplash.com/photo-1618335829737-2228915674e0?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&q=80')",
          }}
        >
          <div
            className={`flex flex-col justify-center h-full transition-opacity duration-500 ${
              isSwapped ? "opacity-0" : "opacity-100"
            }`}
          >
            <div className="bg-black bg-opacity-40 p-8 rounded-lg backdrop-blur-sm">
              <h1 className="text-4xl font-bold leading-tight">
                Join the Future of Code Quality
              </h1>
              <p className="text-teal-300 mt-2 font-semibold">
                Sign up to start analyzing your code with the power of AI.
              </p>
            </div>
          </div>
        </div>
        <div
          className={`w-full md:w-1/2 p-8 md:p-12 transition-transform duration-700 ease-in-out ${
            isSwapped ? "-translate-x-full" : ""
          }`}
        >
          <h2 className="text-3xl font-bold text-white mb-2">Create Account</h2>
          <p className="text-gray-400 mb-8">
            Get started in just a few clicks.
          </p>

          {error && (
            <p className="bg-red-900/50 border border-red-700 text-red-300 p-3 rounded-lg text-center mb-4">
              {error}
            </p>
          )}
          {success && (
            <p className="bg-green-900/50 border border-green-700 text-green-300 p-3 rounded-lg text-center mb-4">
              {success}
            </p>
          )}

          <form onSubmit={handleSubmit} className="space-y-6">
            <div>
              <label className="block text-gray-400 mb-2" htmlFor="email">
                Email Address
              </label>
              <input
                type="email"
                id="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="w-full p-3 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-teal-500 text-white transition"
                required
              />
            </div>
            <div>
              <label className="block text-gray-400 mb-2" htmlFor="password">
                Password
              </label>
              <input
                type="password"
                id="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="w-full p-3 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-teal-500 text-white transition"
                required
              />
            </div>
            <button
              type="submit"
              disabled={isLoading || !!success}
              className="w-full bg-teal-500 text-white font-bold py-3 rounded-lg hover:bg-teal-600 transition-colors duration-300 disabled:bg-gray-600 disabled:cursor-not-allowed"
            >
              {isLoading ? "Creating Account..." : "Sign Up"}
            </button>
          </form>

          <p className="text-center text-gray-400 mt-8">
            Already have an account?{" "}
            <Link
              to="/login"
              className="text-teal-400 hover:underline font-semibold"
            >
              Login
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
};

export default Signup;
