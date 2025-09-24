import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(16, 20))
ax.set_xlim(0, 10)
ax.set_ylim(0, 25)
ax.axis('off')

# Define colors for different levels
colors = {
    'root': '#2E86AB',
    'main': '#A23B72', 
    'sub': '#F18F01',
    'file': '#C73E1D'
}

# Title
ax.text(5, 24, 'Data Science Course Directory Structure', 
        fontsize=20, fontweight='bold', ha='center')

# Root level folders and their positions
folders = [
    # (name, x, y, level)
    ('foundations/', 1, 22, 'main'),
    ('working-with-data/', 1, 19, 'main'),
    ('data-analysis/', 1, 16, 'main'),
    ('advanced-analysis/', 1, 13, 'main'),
    ('intro-to-ml/', 1, 10, 'main'),
    ('ml-in-practice/', 1, 7, 'main'),
    ('communicating-insights/', 1, 4, 'main'),
    ('projects/', 1, 1.5, 'main'),
    ('assets/', 6, 1.5, 'main'),
]

# Sub folders
sub_folders = [
    # foundations
    ('what-is-ds/', 3, 22.5, 'sub'),
    ('python-basics/', 3, 22, 'sub'),
    ('tools-for-ds/', 3, 21.5, 'sub'),
    
    # working-with-data
    ('data-formats/', 3, 19.5, 'sub'),
    ('cleaning/', 3, 19, 'sub'),
    ('exploration/', 3, 18.5, 'sub'),
    ('visualization/', 3, 18, 'sub'),
    
    # data-analysis
    ('statistics/', 3, 16.5, 'sub'),
    ('hypothesis-testing/', 3, 16, 'sub'),
    ('feature-engineering/', 3, 15.5, 'sub'),
    
    # advanced-analysis
    ('correlation-vs-causation/', 3, 13.5, 'sub'),
    ('multivariate-analysis/', 3, 13, 'sub'),
    ('time-series/', 3, 12.5, 'sub'),
    ('intro-to-predictive-analysis/', 3, 12, 'sub'),
    
    # intro-to-ml
    ('ml-basics/', 3, 10.5, 'sub'),
    ('regression-models/', 3, 10, 'sub'),
    ('classification-models/', 3, 9.5, 'sub'),
    
    # ml-in-practice
    ('model-evaluation/', 3, 7.5, 'sub'),
    ('cross-validation/', 3, 7, 'sub'),
    ('overfitting-regularization/', 3, 6.5, 'sub'),
    
    # communicating-insights
    ('dashboarding/', 3, 4.5, 'sub'),
    ('data-in-business/', 3, 4, 'sub'),
    ('capstone-story/', 3, 3.5, 'sub'),
    
    # projects
    ('analyze-your-survey/', 3, 2, 'sub'),
    ('movie-data-story/', 3, 1.5, 'sub'),
    ('simple-ml-predictor/', 3, 1, 'sub'),
    
    # assets
    ('illustrations/', 7.5, 2, 'sub'),
    ('datasets/', 7.5, 1.5, 'sub'),
    ('templates/', 7.5, 1, 'sub'),
]

# Files (showing some examples)
files = [
    ('README.md', 5, 22.5, 'file'),
    ('notebook.ipynb', 5, 22.3, 'file'),
    ('assets/', 5, 22.1, 'file'),
]

# Draw connections (lines)
def draw_connection(x1, y1, x2, y2, style='solid'):
    ax.plot([x1, x2], [y1, y2], 'k-', linewidth=1, alpha=0.6, linestyle=style)

# Draw main folder connections
for name, x, y, level in folders:
    if name != 'assets/' and name != 'projects/':
        draw_connection(0.5, y, x-0.1, y)

# Draw sub folder connections
for name, x, y, level in sub_folders:
    parent_y = None
    if 'what-is-ds' in name or 'python-basics' in name or 'tools-for-ds' in name:
        parent_y = 22
    elif 'data-formats' in name or 'cleaning' in name or 'exploration' in name or 'visualization' in name:
        parent_y = 19
    elif 'statistics' in name or 'hypothesis-testing' in name or 'feature-engineering' in name:
        parent_y = 16
    elif 'correlation' in name or 'multivariate' in name or 'time-series' in name or 'predictive' in name:
        parent_y = 13
    elif 'ml-basics' in name or 'regression' in name or 'classification' in name:
        parent_y = 10
    elif 'model-evaluation' in name or 'cross-validation' in name or 'overfitting' in name:
        parent_y = 7
    elif 'dashboarding' in name or 'data-in-business' in name or 'capstone' in name:
        parent_y = 4
    elif 'analyze' in name or 'movie' in name or 'simple-ml' in name:
        parent_y = 1.5
    elif 'illustrations' in name or 'datasets' in name or 'templates' in name:
        parent_y = 1.5
        draw_connection(6.5, parent_y, x-0.1, y)
        continue
    
    if parent_y:
        draw_connection(1.8, parent_y, x-0.1, y)

# Draw folder boxes
def draw_folder_box(name, x, y, level):
    width = len(name) * 0.08 + 0.3
    height = 0.25
    
    # Create fancy box
    box = FancyBboxPatch((x, y-height/2), width, height,
                        boxstyle="round,pad=0.02",
                        facecolor=colors[level],
                        edgecolor='black',
                        linewidth=1,
                        alpha=0.8)
    ax.add_patch(box)
    
    # Add text
    text_color = 'white' if level in ['main', 'root'] else 'black'
    ax.text(x + width/2, y, name, 
            fontsize=8 if level == 'sub' else 10,
            fontweight='bold' if level == 'main' else 'normal',
            ha='center', va='center',
            color=text_color)

# Draw all folders
for name, x, y, level in folders:
    draw_folder_box(name, x, y, level)

for name, x, y, level in sub_folders:
    draw_folder_box(name, x, y, level)

# Add legend
legend_elements = [
    plt.Rectangle((0, 0), 1, 1, facecolor=colors['main'], label='Main Directories'),
    plt.Rectangle((0, 0), 1, 1, facecolor=colors['sub'], label='Sub Directories'),
]
ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(0.98, 0.98))

# Add description
description = """
This directory structure organizes the Data Science course content into logical modules:
• Foundations: Core concepts and basic tools
• Working with Data: Data handling, cleaning, and exploration
• Data Analysis: Statistical analysis and feature engineering
• Advanced Analysis: Complex analysis techniques
• Intro to ML: Basic machine learning concepts
• ML in Practice: Practical ML implementation
• Communicating Insights: Presenting results
• Projects: Hands-on practical projects
• Assets: Supporting materials and resources
"""

ax.text(0.5, 0.5, description, fontsize=10, ha='left', va='top',
        bbox=dict(boxstyle="round,pad=0.5", facecolor='lightgray', alpha=0.8))

plt.tight_layout()
plt.savefig('data_science_course_structure.png', dpi=300, bbox_inches='tight')
plt.show()

print("Directory structure visualization created successfully!")
print("\nActual directory structure created in your workspace:")
print("├── foundations/")
print("├── working-with-data/") 
print("├── data-analysis/")
print("├── advanced-analysis/")
print("├── intro-to-ml/")
print("├── ml-in-practice/")
print("├── communicating-insights/")
print("├── projects/")
print("└── assets/")