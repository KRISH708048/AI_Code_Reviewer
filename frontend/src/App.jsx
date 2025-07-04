import React, { useState } from 'react';
import Header from './components/Header';
import DashBoard from './components/DashBoard';

function App() {
    return (
        <div className="bg-gray-900 min-h-screen text-gray-200 font-sans flex flex-col w-full h-screen">
            <Header />
            <DashBoard />
        </div>
    );
}

export default App;