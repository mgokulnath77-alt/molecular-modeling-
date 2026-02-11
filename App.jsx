import React, { useState } from 'react';
import { BeakerIcon, CloudArrowUpIcon, ChartBarIcon, DocumentTextIcon, CpuChipIcon } from '@heroicons/react/24/outline';

const App = () => {
  const [step, setStep] = useState(1);

  const steps = [
    { id: 1, name: 'Start', icon: <BeakerIcon className="w-5 h-5"/> },
    { id: 2, name: 'Upload', icon: <CloudArrowUpIcon className="w-5 h-5"/> },
    { id: 3, name: 'Docking', icon: <CpuChipIcon className="w-5 h-5"/> },
    { id: 4, name: 'Analysis', icon: <ChartBarIcon className="w-5 h-5"/> },
    { id: 5, name: 'Report', icon: <DocumentTextIcon className="w-5 h-5"/> },
  ];

  return (
    <div className="flex min-h-screen">
      {/* Sidebar */}
      <nav className="w-20 lg:w-64 glass-card m-4 flex flex-col items-center py-8">
        <h1 className="text-2xl font-bold mb-10 text-cyan-400 hidden lg:block">COX-2 Lab</h1>
        <div className="space-y-6">
          {steps.map((s) => (
            <button 
              key={s.id}
              onClick={() => setStep(s.id)}
              className={`flex items-center space-x-4 p-3 rounded-xl transition-all ${step === s.id ? 'bg-cyan-500 shadow-lg scale-105' : 'hover:bg-white/10 text-gray-400'}`}
            >
              {s.icon}
              <span className="hidden lg:block">{s.name}</span>
            </button>
          ))}
        </div>
      </nav>

      {/* Main Content */}
      <main className="flex-1 p-8">
        {/* Header */}
        <header className="mb-10">
          <h2 className="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-white to-gray-400">
            COX-2 & Ibuprofen Interaction
          </h2>
          <p className="text-gray-400 mt-2">Team 3 | Computational Evaluation for Arthritis Treatment</p>
        </header>

        {/* Step Content: Upload Simulation */}
        {step === 2 && (
          <div className="glass-card p-10 max-w-2xl mx-auto border-dashed border-2 border-cyan-500/50">
            <div className="flex flex-col items-center">
              <CloudArrowUpIcon className="w-16 h-16 text-cyan-400 animate-bounce" />
              <h3 className="text-xl mt-4">Drag and Drop PDB Files</h3>
              <p className="text-gray-500 text-sm">Upload COX-2 receptor for analysis</p>
              <button className="mt-6 px-8 py-3 neon-button rounded-full font-semibold">
                Select Protein File
              </button>
            </div>
          </div>
        )}

        {/* Step Content: Results Simulation */}
        {step === 4 && (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="glass-card p-6">
              <p className="text-sm text-gray-400">Binding Energy</p>
              <h4 className="text-3xl font-bold text-cyan-400">-8.4 kcal/mol</h4>
            </div>
            <div className="glass-card p-6">
              <p className="text-sm text-gray-400">H-Bonds</p>
              <h4 className="text-3xl font-bold text-green-400">3 Established</h4>
            </div>
            <div className="glass-card p-6">
              <p className="text-sm text-gray-400">Stability</p>
              <h4 className="text-3xl font-bold text-purple-400">Optimal</h4>
            </div>
            
            {/* Interaction Diagram Table */}
            <div className="col-span-1 md:col-span-3 glass-card overflow-hidden">
               <div className="p-4 bg-white/5 border-b border-white/10 font-semibold">Interactions Table</div>
               <table className="w-full text-left">
                  <thead className="text-gray-400 text-sm border-b border-white/10">
                    <tr>
                      <th className="p-4">Residue</th>
                      <th className="p-4">Interaction</th>
                      <th className="p-4">Distance</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr className="border-b border-white/5 hover:bg-white/5">
                      <td className="p-4 text-cyan-300 font-mono">ARG120</td>
                      <td className="p-4">Hydrogen Bond</td>
                      <td className="p-4">2.8 Å</td>
                    </tr>
                    <tr className="hover:bg-white/5">
                      <td className="p-4 text-cyan-300 font-mono">TYR355</td>
                      <td className="p-4">van der Waals</td>
                      <td className="p-4">3.4 Å</td>
                    </tr>
                  </tbody>
               </table>
            </div>
          </div>
        )}
      </main>
    </div>
  );
};

export default App;