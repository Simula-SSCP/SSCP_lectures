# Cable Equation History - Jupyter Notebook Markdown Slides

This folder contains markdown versions of the cable equation history presentation, designed for direct use in Jupyter notebook markdown cells.

## Contents

### Slide Files (Markdown)
- `slide_01_title.md` - Title and introduction
- `slide_02_early_diffusion.md` - Lord Kelvin's early diffusion models (1850s)
- `slide_03_heaviside_contribution.md` - Heaviside's contribution (Late 1870s)
- `slide_04_telegrapher_equations.md` - The telegrapher's equations
- `slide_05_significance_impact.md` - Historical significance and impact
- `slide_06_modern_applications.md` - Modern applications and legacy

### Figures Folder
- `figures/lord_kelvin.jpg` - Portrait of Lord Kelvin
- `figures/oliver_heaviside.jpg` - Portrait of Oliver Heaviside
- `figures/telegraph_cable.jpg` - Historical telegraph cable operations
- `figures/cable_map.jpg` - Historical submarine cable network map

## Usage Instructions

### Method 1: Copy-Paste Individual Slides
1. Open each `.md` file
2. Copy the entire content
3. Create a new markdown cell in your Jupyter notebook
4. Paste the content
5. Run the cell to render the slide

### Method 2: Load Files Programmatically
```python
# In a code cell
with open('slide_01_title.md', 'r') as f:
    slide_content = f.read()

from IPython.display import Markdown, display
display(Markdown(slide_content))
```

### Method 3: Create Complete Notebook
```python
import os
from IPython.display import Markdown, display

# Get all slide files
slide_files = sorted([f for f in os.listdir('.') if f.startswith('slide_') and f.endswith('.md')])

# Display all slides
for slide_file in slide_files:
    with open(slide_file, 'r') as f:
        content = f.read()
    print(f"\\n{'='*60}")
    print(f"FILE: {slide_file}")
    print('='*60)
    display(Markdown(content))
```

## File Organization

### Recommended Directory Structure:
```
your_notebook_folder/
├── your_notebook.ipynb
├── slide_01_title.md
├── slide_02_early_diffusion.md
├── slide_03_heaviside_contribution.md
├── slide_04_telegrapher_equations.md
├── slide_05_significance_impact.md
├── slide_06_modern_applications.md
└── figures/
    ├── lord_kelvin.jpg
    ├── oliver_heaviside.jpg
    ├── telegraph_cable.jpg
    └── cable_map.jpg
```

## Features

### Mathematical Equations
- Uses LaTeX syntax for mathematical notation
- Renders properly in Jupyter markdown cells
- MathJax support for complex equations

### Images
- Relative paths to figures folder
- Responsive sizing with width attributes
- Alt text for accessibility

### Formatting
- Clean markdown syntax
- Tables for organized information
- Headers for clear structure
- Emphasis and styling for key points

## Customization

### Modifying Content
- Edit any `.md` file to customize content
- Maintain markdown syntax for proper rendering
- Update image paths if you reorganize files

### Adding Slides
- Create new `.md` files following the naming convention
- Add corresponding figures to the figures folder
- Update this README if needed

## Troubleshooting

### Images Not Displaying
- Check that figures folder is in the correct location
- Verify image file names match those referenced in markdown
- Ensure relative paths are correct

### Equations Not Rendering
- Make sure you're using markdown cells (not code cells)
- Check LaTeX syntax in equations
- Verify MathJax is enabled in your Jupyter environment

### Formatting Issues
- Ensure proper markdown syntax
- Check for missing line breaks between sections
- Verify table formatting is correct

## Educational Context

These slides are designed for:
- **Audience:** Graduate students (Master's and PhD level)
- **Subject:** Computational Biology
- **Focus:** Historical development and mathematical foundations
- **Style:** Clean, academic presentation suitable for lecture use

## License

Created for educational use in computational biology graduate courses. Historical images and content used for educational purposes.

