# LongTREC Beamer Template Documentation

## Overview
This beamer template has been created to match the design of the provided HTML slides. It includes all the key visual elements, color schemes, and layouts from the original design, adapted for LaTeX beamer presentations.

## Files Included
- `beamerthemeLongTREC.sty`: The main theme file containing all style definitions
- `example.tex`: An example presentation showcasing all slide types
- `example_no_images.tex`: A version that works without logo images

## Required Images
For the full template to work properly, you'll need to add the following images to the `images/` directory:
- `longtrec_logo.png`: The LongTREC logo
- `eu_logo.png`: The European Union logo
- `dna_background.png`: A DNA-themed background image (optional)

## Color Scheme
The template uses the following color scheme:
- Primary blue: #0047AB
- Secondary darker blue: #003380
- Accent orange: #FF8C00
- Text colors: White (on blue backgrounds), dark gray (#333) on white backgrounds

## Slide Types
The template includes the following slide types:

### 1. Title/Cover Slide
```latex
\begin{frame}[plain]
  \titlepage
\end{frame}
```

### 2. Table of Contents Slide
```latex
\tocframe
```

### 3. Section Divider Slide
```latex
\sectionframe{Section Title}{Optional subtitle text}
```

### 4. Content Slide
```latex
\begin{frame}
  \frametitle{Slide Title}
  
  \begin{columns}[T]
    \begin{column}{\textwidth}
      {\usebeamercolor[fg]{structure}\usebeamerfont{block title}Content Heading}
      
      \begin{itemize}
        \item Bullet point 1
        \item Bullet point 2
      \end{itemize}
    \end{column}
  \end{columns}
\end{frame}
```

### 5. Data Visualization Slide
```latex
\dataframe{Slide Title}{
  % Chart/visualization content here
  \begin{tikzpicture}
    % TikZ code for visualization
  \end{tikzpicture}
}{
  % Description text here
  The chart demonstrates the \textbf{\textcolor{longtrec-blue}{key points}}:
  
  \begin{itemize}
    \item Point 1
    \item Point 2
  \end{itemize}
}
```

### 6. Thank You Slide
```latex
\thankyouframe{Contact information text}{Website URL}{Email address}
```

## Customization
You can customize the template by modifying the `beamerthemeLongTREC.sty` file:
- Colors can be adjusted in the color definitions section
- Font sizes can be modified in the font settings section
- Layout elements can be adjusted in their respective template definitions

## Compilation
Compile your presentation using pdflatex:
```
pdflatex your_presentation.tex
```

## Notes on Visual Fidelity
The template closely matches the original HTML slides with the following considerations:
- Gradients are implemented using TikZ shading
- Custom bullet points use orange circles
- Headers and footers match the original design
- The aspect ratio is set to 16:9 (aspectratio=169) to match modern presentations

## Improvements
The beamer template includes several improvements over the HTML version:
- Consistent styling across all slide types
- Better typography control through LaTeX
- Easier content management through separation of content and design
- Built-in support for mathematical formulas and academic content
