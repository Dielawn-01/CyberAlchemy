import React, { useState, useEffect } from 'react';
import { Backpack, Sparkles, Zap, Award, Hexagon, Fingerprint } from 'lucide-react';
import './index.css';

function App() {
  const [resonance, setResonance] = useState(0);
  const [dialogue, setDialogue] = useState("Hello! I'm your Aura Companion. Ready to tune the network?");
  const [artifacts, setArtifacts] = useState([
    { id: 1, title: 'Seed of Chronos', icon: <Fingerprint size={28} />, earned: true },
    { id: 2, title: 'Void Shard', icon: <Hexagon size={28} />, earned: false },
    { id: 3, title: 'Quantum Spark', icon: <Sparkles size={28} />, earned: false },
    { id: 4, title: 'Gold Badge', icon: <Award size={28} />, earned: false },
  ]);

  const [isTuning, setIsTuning] = useState(false);

  const handleTune = () => {
    if (isTuning || resonance >= 100) return;
    setIsTuning(true);
    setDialogue("Calculating Klein transitions...");
    
    // Simulate complex background processing (ZKPCR validation)
    let currentResonance = resonance;
    const interval = setInterval(() => {
      currentResonance += Math.floor(Math.random() * 15) + 5;
      if (currentResonance >= 100) {
        currentResonance = 100;
        clearInterval(interval);
        
        // Unlock new artifact
        setTimeout(() => {
          setDialogue("Resonance achieved! You earned a new artifact!");
          setArtifacts(prev => prev.map(a => 
            !a.earned && currentResonance === 100 ? { ...a, earned: true } : a
          ));
          setIsTuning(false);
          
          // Reset after a bit for demo purposes
          setTimeout(() => {
            setResonance(0);
            setDialogue("Ready for the next frequency tuning?");
          }, 4000);
        }, 1000);
      }
      setResonance(currentResonance);
    }, 400);
  };

  return (
    <div className="app-container">
      <header className="header glass-panel">
        <div className="header-title">
          <Sparkles color="var(--success-color)" size={32} />
          <h1>Aura OS</h1>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <Backpack color="var(--text-muted)" size={24} />
          <span style={{ color: 'var(--text-muted)', fontWeight: 600 }}>Sync Level: {Math.floor(resonance)}%</span>
        </div>
      </header>

      <main className="main-content">
        
        {/* Main Avatar Section */}
        <section className="glass-panel" style={{ padding: '3rem 2rem', display: 'flex', flexDirection: 'column', height: '100%' }}>
          <div className="avatar-section">
            <div className="avatar-orb"></div>
            <div className="avatar-dialogue">
              "{dialogue}"
            </div>
          </div>
          
          <div className="resonance-meter">
            <h3 style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem' }}>
              <Zap color="var(--accent-color)" size={20} />
              Resonance Core
            </h3>
            <div className="resonance-bar-container">
              <div 
                className="resonance-bar" 
                style={{ width: `${resonance}%` }}
              ></div>
            </div>
          </div>

          <div className="controls-section">
            <button 
              className="action-btn" 
              onClick={handleTune}
              disabled={isTuning || resonance >= 100}
              style={{ opacity: (isTuning || resonance >= 100) ? 0.5 : 1 }}
            >
              {isTuning ? "Tuning Frequency..." : "Align Frequencies"}
            </button>
            <button className="action-btn secondary">
              Analyze State
            </button>
          </div>
        </section>

        {/* Backpack Sidebar Section */}
        <aside className="glass-panel backpack-section">
          <div className="backpack-header">
            <Backpack color="var(--accent-light)" size={24} />
            <h2>My Backpack</h2>
          </div>
          <p style={{ fontSize: '0.9rem', color: 'var(--text-muted)' }}>
            Collect artifacts by proving your knowledge to the network!
          </p>
          
          <div className="backpack-grid">
            {artifacts.map((artifact) => (
              <div 
                key={artifact.id} 
                className="artifact-card"
                style={{ 
                  opacity: artifact.earned ? 1 : 0.3,
                  filter: artifact.earned ? 'none' : 'grayscale(100%)'
                }}
              >
                <div className="artifact-icon-wrapper">
                  {artifact.icon}
                </div>
                <span className="artifact-title">{artifact.title}</span>
                <span style={{ fontSize: '0.7rem', color: 'var(--success-color)' }}>
                  {artifact.earned ? 'Verified' : 'Locked'}
                </span>
              </div>
            ))}
          </div>
        </aside>

      </main>
    </div>
  );
}

export default App;
