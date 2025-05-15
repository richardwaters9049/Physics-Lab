'use client';

import { useState } from 'react';
import { Button } from '@/components/ui/button';

export default function HomePage() {
  const [gridSize, setGridSize] = useState(10);
  const [response, setResponse] = useState(null);

  async function runSimulation() {
    const res = await fetch('http://localhost:8000/simulate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ grid_size: gridSize, time_steps: 20, source_position: [5, 5] }),
    });
    const data = await res.json();
    setResponse(data);
  }

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">🧪 Run Electromagnetic Simulation</h1>
      <div className="mb-4">
        <label className="block">Grid Size: {gridSize}</label>
        <input
          type="range"
          min="5"
          max="50"
          value={gridSize}
          onChange={e => setGridSize(Number(e.target.value))}
        />
      </div>
      <Button onClick={runSimulation}>Run</Button>
      {response && (
        <pre className="mt-4 bg-gray-100 p-2 rounded">{JSON.stringify(response, null, 2)}</pre>
      )}
    </div>
  );
}