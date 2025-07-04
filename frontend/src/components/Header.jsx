import React from 'react';

const Header = () => {
  return (
    <header className="bg-gray-800/80 backdrop-blur-sm border-b border-gray-700 sticky top-0 z-10">
      <nav className=" mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center">
            <h1 className="text-2xl font-bold">
              <span className="
                bg-gradient-to-r from-teal-400 via-cyan-400 to-sky-500 
                bg-clip-text text-transparent
              ">
                AI Code Reviewer
              </span>
              <span className="text-teal-400">.</span>
            </h1>
          </div>
        </div>
      </nav>
    </header>
  );
};

export default Header;