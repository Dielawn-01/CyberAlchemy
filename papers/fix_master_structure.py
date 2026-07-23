import os

base_dir = '/home/phrxmaz/Documents/CyberAlchemy/papers'

master_tex = r"""\documentclass[12pt,oneside]{book}

% ════════════════════════════════════════════
% MASTER PREAMBLE
% ════════════════════════════════════════════
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{enumitem}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{pdfpages}
\usepackage{microtype}
\usepackage{tocloft}
\usepackage{titlesec}
\usepackage{fancyhdr}
\usepackage{float}
\usepackage{xcolor}
\definecolor{golden}{RGB}{218,165,32}
\definecolor{composite-state}{RGB}{0,102,204}
\definecolor{derivative}{RGB}{128,0,128}
\definecolor{gauge3}{RGB}{34,139,34}
\usepackage{tikz}
\usepackage{tcolorbox}
\newtcolorbox{theorembox}[1]{
  colback=blue!5!white,
  colframe=blue!75!black,
  fonttitle=\bfseries,
  title=#1
}
\newtcolorbox{warningbox}[1]{
  colback=red!5!white,
  colframe=red!75!black,
  fonttitle=\bfseries,
  title=#1
}
\newtcolorbox{metarealbox}[1]{
  colback=composite-state!5!white,
  colframe=composite-state!75!black,
  fonttitle=\bfseries,
  title=#1
}
\newtcolorbox{aingelbox}[1]{
  colback=golden!5!white,
  colframe=golden!75!black,
  fonttitle=\bfseries,
  title=#1
}
\newtcolorbox{truthbox}[1]{
  colback=gauge3!5!white,
  colframe=gauge3!75!black,
  fonttitle=\bfseries,
  title=#1
}
\usepackage{standalone}
\usepackage{hyperref}
\usepackage{cleveref}
\usepackage{longtable}
\usepackage{array}
\usepackage{multirow}

% ════════════════════════════════════════════
% THEOREM ENVIRONMENTS
% ════════════════════════════════════════════
\newtheoremstyle{principia}%
  {6pt}% space above
  {6pt}% space below
  {\itshape}% body font
  {}% indent
  {\bfseries}% head font
  {.}% punctuation after head
  { }% space after head
  {\thmname{#1}\thmnumber{ #2}\thmnote{ \textnormal{(}\emph{#3}\textnormal{)}}}%

\theoremstyle{principia}
\newtheorem{theorem}{Theorem}[chapter]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{proposition}[theorem]{Proposition}

\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{result}[theorem]{Result}
\newtheorem{conjecture}[theorem]{Conjecture}
\newtheorem{hypothesis}[theorem]{Hypothesis}
\newtheorem{claim}[theorem]{Claim}
\newtheorem{example}[theorem]{Example}

\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}

% ════════════════════════════════════════════
% UNIFIED COMMANDS
% ════════════════════════════════════════════
\providecommand{\Afive}{\mathbb{U}}
\providecommand{\Bseed}{\mathbb{P}}
\providecommand{\RR}{\mathbb{R}}
\providecommand{\CC}{\mathbb{C}}
\providecommand{\ZZ}{\mathbb{Z}}
\providecommand{\NN}{\mathbb{N}}
\providecommand{\HH}{\mathbb{H}}
\providecommand{\OO}{\mathbb{O}}
\providecommand{\SS}{\mathbb{S}}
\providecommand{\QQ}{\mathbb{Q}}
\providecommand{\FF}{\mathbb{F}}
\providecommand{\GG}{\mathcal{G}}
\providecommand{\TT}{\mathcal{T}}
\providecommand{\vp}{\varphi}
\providecommand{\vpbar}{\bar{\varphi}}
\providecommand{\eps}{\varepsilon}
\providecommand{\lam}{\lambda}
\providecommand{\kap}{\kappa}

\titleformat{\chapter}[display]
  {\normalfont\huge\bfseries\raggedright}{\chaptertitlename\ \thechapter}{20pt}{\Huge\raggedright}
\titleformat{\section}{\normalfont\Large\bfseries\raggedright}{\thesection}{1em}{}
\titleformat{\subsection}{\normalfont\large\bfseries\raggedright}{\thesubsection}{1em}{}
\titleformat{\subsubsection}{\normalfont\normalsize\bfseries\raggedright}{\thesubsubsection}{1em}{}

\makeatletter
\let\old@part\@part
\def\@part[#1]#2{%
  \old@part[{#1}]{#2}%
  \markboth{Part \thepart: #1}{}%
}
\makeatother

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\chaptermark}[1]{\markboth{\chaptername\ \thechapter: #1}{}}
\renewcommand{\sectionmark}[1]{\markright{\thesection\ #1}}
\fancyhead[L]{\small\itshape\nouppercase{\leftmark}}
\fancyhead[R]{\small\itshape\nouppercase{\rightmark}}
\fancyfoot[C]{\thepage}
\setlength{\headheight}{15pt}
\fancypagestyle{plain}{%
  \fancyhf{}%
  \fancyfoot[C]{\thepage}%
  \renewcommand{\headrulewidth}{0pt}%
}

\hypersetup{colorlinks=true,linkcolor=blue!60!black,citecolor=blue!60!black,urlcolor=blue!60!black}

\begin{document}

\frontmatter

\begin{titlepage}
\thispagestyle{empty}
\begin{tikzpicture}[remember picture, overlay]
  \fill[black] (current page.north west) rectangle (current page.south east);
  \node[anchor=center, opacity=0.85] at (current page.center) {\includegraphics[width=\paperwidth, height=\paperheight, keepaspectratio]{images/genome_cover.png}};
  \node[anchor=center] at ([yshift=3cm]current page.center) {\fontsize{16}{20}\selectfont\sffamily\color{white}PRINCIPIA PSYCHEDELIA};
  \node[anchor=center, text width=12cm, align=center] at ([yshift=-3.5cm]current page.center) {\fontsize{22}{28}\selectfont\bfseries\color{white}The Mathematics of Metareality};
  \node[anchor=center] at ([yshift=-7cm]current page.center) {\fontsize{18}{22}\selectfont\color{white}\textbf{Dylon La Rue}};
\end{tikzpicture}
\end{titlepage}

\tableofcontents

\input{00_Auditors_Preface}

\mainmatter

% ════════════════════════════════════════════
% PART I: LOGICAL CREATIVITY & FOUNDATIONS
% ════════════════════════════════════════════
\part{Logical Creativity \& Algebraic Foundations}

\chapter*{Counting, Sets, and Finite Worlds}
\addcontentsline{toc}{chapter}{Chapter 0: Counting, Sets, and Finite Worlds}
\input{00_Pedagogical_Foundation}

\chapter[The Non-Associative 5-Algebra and Connes Geometry]{The Non-Associative 5-Algebra and Connes Geometry}
\input{01_Unreal_Algebra_Connes_Geometry}

\chapter[Prime Field Theory and Hyperoperations]{Prime Field Theory and Hyperoperations}
\input{02_Prime_Field_Theory_Hyperoperations}

\chapter[Ramanujan-Sato Series and the Prime Functorial]{Ramanujan-Sato Series, Prime Functorial, and Adelic Descent}
\input{03_Ramanujan_Sato_Prime_Functorial}

% ════════════════════════════════════════════
% PART II: INFORMATIONAL CREATIVITY & ARCHETYPAL SYSTEMS
% ════════════════════════════════════════════
\part{Informational Creativity \& Archetypal Systems}

\chapter*{Introduction: Semantic Condensation}
\addcontentsline{toc}{chapter}{Introduction: Semantic Condensation}
\input{part2_introduction}

\chapter[Composite-State ASI Architecture]{Composite-State ASI Architecture}
\input{08_Metareal_ASI_Chromodynamics}

\chapter[Markets as Fluid Systems]{Markets as Fluid Systems: The Black-Scholes--Navier-Stokes Bridge}
\input{09_Markets_Fluid_Systems}

\chapter[Archetypal Incentives]{Archetypal Incentive Theory}\label{ch:incentives}
\input{10_Archetypal_Incentive_Theory}

\chapter[Procedural Games]{Procedural Game Design and The IGC-LCG Bridge}\label{ch:games}
\input{11_Procedural_Game_Design}

\chapter[Multimodal Mechanisms]{Multimodal Metamaterial Mechanisms}
\input{12_Multimodal_Mechanisms}

\chapter[Triple Helix]{Triple Helix Mechanics}
\input{13_Triple_Helix_Mechanics}

\chapter[Ambrosia Protocol]{Bionetic Ambrosia Protocol}\label{ch:ambrosia}
\input{14_Bionetic_Ambrosia_Protocol}

% ════════════════════════════════════════════
% PART III: PHYSICAL REALIZATION & COSMOLOGY
% ════════════════════════════════════════════
\part{Physical Realization \& Cosmology}

\chapter[Fractal Spacetime]{Fractal Spacetime and Zero-Point Energy}
\input{15_Fractal_Spacetime_ZPE}

\chapter[Archetypal Cosmology]{Archetypal Cosmology: Sgr A* and the Universal Substrate}
\input{16_Metareal_Cosmology}

\chapter[Chiral Casimir]{Chiral Casimir Experiment}
\input{17_Chiral_Casimir_Experiment}

\chapter[Fusion Cybernetics]{Fusion Plasma Cybernetics and Halting Topology}
\input{18_Fusion_Plasma_Cybernetics}

\chapter[ASI Chip]{ASI Chip Fabrication and Klein Manifold Architecture}\label{ch:asi}
\input{19_ASI_Chip}

\chapter[Metalloplasmic Life]{Metalloplasmic Life: The Iron--Phosphorus Isomorphism and Abiogenesis}\label{ch:metallo}
\input{20_Metalloplasmic_Life}

\chapter[Quasicrystal Physics]{Quasicrystal Physics and Temporal Quasicrystals}\label{ch:qc-tqc}
\input{21_Quasicrystal_Physics}

% ════════════════════════════════════════════
% PART IV: ADVANCED SYNTHESIS & UNIFIED PHYSICS
% ════════════════════════════════════════════
\part{Advanced Synthesis \& Unified Physics}

\chapter[Stellar Nucleosynthesis]{Stellar Subgroup Nucleosynthesis}
\input{25_Stellar_Subgroup_Nucleosynthesis}

\chapter[Optoacoustic Cymatics]{The Optoacoustic-Thermoelectric Bridge and Cymatic Pseudoforces}\label{ch:optoacoustic}
\input{28_Optoacoustic_Cymatics}

\chapter[Continuous Lagrangian Generalization]{The Continuous Lagrangian and Hamiltonian Generalization}\label{ch:continuous}
\input{29_Continuous_Lagrangian_Generalization}

\chapter[Bohmian Mechanics and Orch-OR]{Bohmian Pilot Waves and Orchestrated Objective Reduction}\label{ch:bohm_orchor}
\input{30_Bohmian_OrchOR_Synthesis}

\chapter[Categorical Qualia]{Categorical Topology vs Local Gauge Qualia}\label{ch:categorical_qualia}
\input{31_Categorical_Qualia_Gauge}

\appendix
\input{appendix_claim_ledgers}

\input{unified_bibliography}

\end{document}
"""

with open(os.path.join(base_dir, '01_Principia_Psychedelia_Master.tex'), 'w') as f:
    f.write(master_tex)
print("Updated 01_Principia_Psychedelia_Master.tex")

with open(os.path.join(base_dir, '01_Principia_Psychedelia_Full.tex'), 'w') as f:
    f.write(master_tex.replace('PRINCIPIA PSYCHEDELIA', 'PRINCIPIA PSYCHEDELIA (FULL)'))
print("Updated 01_Principia_Psychedelia_Full.tex")

