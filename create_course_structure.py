#!/usr/bin/env python3
"""
Data Science Course Directory Structure Creator
This script creates a complete, systematic directory structure for a data science course.
"""

import os
import json

def create_directory(path):
    """Create directory if it doesn't exist"""
    try:
        os.makedirs(path, exist_ok=True)
        print(f"✓ Created directory: {path}")
    except Exception as e:
        print(f"✗ Error creating {path}: {e}")

def create_file(filepath, content=""):
    """Create a file with optional content"""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Created file: {filepath}")
    except Exception as e:
        print(f"✗ Error creating {filepath}: {e}")

def create_readme(filepath, title, description=""):
    """Create a README.md file with title and description"""
    content = f"""# {title}

{description}

## Overview

This section covers {title.lower()}.

## Contents

- README.md (this file) - Overview and learning objectives
- notebook.ipynb - Interactive exercises and examples

## Learning Objectives

By the end of this section, you will be able to:
- [ ] Objective 1
- [ ] Objective 2
- [ ] Objective 3

## Prerequisites

- Basic understanding of previous sections
- Python programming basics

## Resources

- Additional reading materials
- External links and references

## Next Steps

Continue to the next section to build upon these concepts.
"""
    create_file(filepath, content)

def create_notebook(filepath, title):
    """Create a basic Jupyter notebook structure"""
    notebook_content = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {title}\n",
                    "\n",
                    "Welcome to this interactive notebook!\n",
                    "\n",
                    "## Learning Objectives\n",
                    "\n",
                    "In this notebook, you will:\n",
                    "- Learn key concepts\n",
                    "- Practice with examples\n",
                    "- Apply your knowledge\n",
                    "\n",
                    "---"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## Setup\n",
                    "\n",
                    "First, let's import the necessary libraries:"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Import necessary libraries\n",
                    "import pandas as pd\n",
                    "import numpy as np\n",
                    "import matplotlib.pyplot as plt\n",
                    "import seaborn as sns\n",
                    "\n",
                    "# Set up plotting\n",
                    "plt.style.use('default')\n",
                    "sns.set_palette('husl')"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## Content\n",
                    "\n",
                    "Add your content here..."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Your code here"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    create_file(filepath, json.dumps(notebook_content, indent=2))

def main():
    """Main function to create the complete directory structure"""
    print("🚀 Creating Data Science Course Directory Structure...\n")
    
    # Get current directory
    base_path = os.getcwd()
    
    # Course structure definition
    course_structure = {
        "foundations": {
            "what-is-ds": "What is Data Science",
            "python-basics": "Python Basics",
            "tools-for-ds": "Tools for Data Science"
        },
        "working-with-data": {
            "data-formats": "Data Formats",
            "cleaning": "Data Cleaning",
            "exploration": "Data Exploration", 
            "visualization": "Data Visualization"
        },
        "data-analysis": {
            "statistics": "Statistics",
            "hypothesis-testing": "Hypothesis Testing",
            "feature-engineering": "Feature Engineering"
        },
        "advanced-analysis": {
            "correlation-vs-causation": "Correlation vs Causation",
            "multivariate-analysis": "Multivariate Analysis",
            "time-series": "Time Series Analysis",
            "intro-to-predictive-analysis": "Introduction to Predictive Analysis"
        },
        "intro-to-ml": {
            "ml-basics": "Machine Learning Basics",
            "regression-models": "Regression Models",
            "classification-models": "Classification Models"
        },
        "ml-in-practice": {
            "model-evaluation": "Model Evaluation",
            "cross-validation": "Cross Validation",
            "overfitting-regularization": "Overfitting and Regularization"
        },
        "communicating-insights": {
            "dashboarding": "Dashboarding",
            "data-in-business": "Data in Business",
            "capstone-story": "Capstone Story"
        }
    }
    
    # Create main course directories with content
    for module, lessons in course_structure.items():
        print(f"\n📁 Creating module: {module}")
        module_path = os.path.join(base_path, module)
        create_directory(module_path)
        
        for lesson, title in lessons.items():
            print(f"  📂 Creating lesson: {lesson}")
            lesson_path = os.path.join(module_path, lesson)
            create_directory(lesson_path)
            
            # Create README.md
            readme_path = os.path.join(lesson_path, "README.md")
            create_readme(readme_path, title)
            
            # Create notebook.ipynb
            notebook_path = os.path.join(lesson_path, "notebook.ipynb")
            create_notebook(notebook_path, title)
            
            # Create assets folder for what-is-ds
            if lesson == "what-is-ds":
                assets_path = os.path.join(lesson_path, "assets")
                create_directory(assets_path)
    
    # Create projects directory
    print(f"\n📁 Creating projects directory")
    projects_path = os.path.join(base_path, "projects")
    create_directory(projects_path)
    
    projects = ["analyze-your-survey", "movie-data-story", "simple-ml-predictor"]
    for project in projects:
        project_path = os.path.join(projects_path, project)
        create_directory(project_path)
    
    # Create assets directory
    print(f"\n📁 Creating assets directory")
    assets_path = os.path.join(base_path, "assets")
    create_directory(assets_path)
    
    asset_subdirs = ["illustrations", "datasets", "templates"]
    for subdir in asset_subdirs:
        subdir_path = os.path.join(assets_path, subdir)
        create_directory(subdir_path)
    
    print(f"\n✅ Course structure created successfully!")
    print(f"\n📊 Summary:")
    print(f"   - 7 main modules created")
    print(f"   - 23 lessons with README.md and notebook.ipynb files")
    print(f"   - 3 project directories")
    print(f"   - 1 assets directory with 3 subdirectories")
    print(f"   - 1 special assets folder in what-is-ds")
    
    print(f"\n📍 All files created in: {base_path}")
    
    # Display tree structure
    print(f"\n🌳 Directory structure created:")
    print("├── foundations/")
    print("│   ├── what-is-ds/")
    print("│   │   ├── README.md")
    print("│   │   ├── notebook.ipynb")  
    print("│   │   └── assets/")
    print("│   ├── python-basics/")
    print("│   │   ├── README.md")
    print("│   │   └── notebook.ipynb")
    print("│   └── tools-for-ds/")
    print("│       ├── README.md")
    print("│       └── notebook.ipynb")
    print("│")
    print("├── working-with-data/")
    print("│   ├── data-formats/")
    print("│   │   ├── README.md")
    print("│   │   └── notebook.ipynb")
    print("│   ├── cleaning/")
    print("│   │   ├── README.md")
    print("│   │   └── notebook.ipynb")
    print("│   ├── exploration/")
    print("│   │   ├── README.md")
    print("│   │   └── notebook.ipynb")
    print("│   └── visualization/")
    print("│       ├── README.md")
    print("│       └── notebook.ipynb")
    print("│")
    print("├── data-analysis/")
    print("│   ├── statistics/")
    print("│   │   ├── README.md")
    print("│   │   └── notebook.ipynb")
    print("│   ├── hypothesis-testing/")
    print("│   │   ├── README.md")
    print("│   │   └── notebook.ipynb")
    print("│   └── feature-engineering/")
    print("│       ├── README.md")
    print("│       └── notebook.ipynb")
    print("│")
    print("├── advanced-analysis/")
    print("│   ├── correlation-vs-causation/")
    print("│   │   ├── README.md")
    print("│   │   └── notebook.ipynb")
    print("│   ├── multivariate-analysis/")
    print("│   │   ├── README.md")
    print("│   │   └── notebook.ipynb")
    print("│   ├── time-series/")
    print("│   │   ├── README.md")
    print("│   │   └── notebook.ipynb")
    print("│   └── intro-to-predictive-analysis/")
    print("│       ├── README.md")
    print("│       └── notebook.ipynb")
    print("│")
    print("├── intro-to-ml/")
    print("│   ├── ml-basics/")
    print("│   │   ├── README.md")
    print("│   │   └── notebook.ipynb")
    print("│   ├── regression-models/")
    print("│   │   ├── README.md")
    print("│   │   └── notebook.ipynb")
    print("│   └── classification-models/")
    print("│       ├── README.md")
    print("│       └── notebook.ipynb")
    print("│")
    print("├── ml-in-practice/")
    print("│   ├── model-evaluation/")
    print("│   │   ├── README.md")
    print("│   │   └── notebook.ipynb")
    print("│   ├── cross-validation/")
    print("│   │   ├── README.md")
    print("│   │   └── notebook.ipynb")
    print("│   └── overfitting-regularization/")
    print("│       ├── README.md")
    print("│       └── notebook.ipynb")
    print("│")
    print("├── communicating-insights/")
    print("│   ├── dashboarding/")
    print("│   │   ├── README.md")
    print("│   │   └── notebook.ipynb")
    print("│   ├── data-in-business/")
    print("│   │   ├── README.md")
    print("│   │   └── notebook.ipynb")
    print("│   └── capstone-story/")
    print("│       ├── README.md")
    print("│       └── notebook.ipynb")
    print("│")
    print("├── projects/")
    print("│   ├── analyze-your-survey/")
    print("│   ├── movie-data-story/")
    print("│   └── simple-ml-predictor/")
    print("│")
    print("└── assets/")
    print("    ├── illustrations/")
    print("    ├── datasets/")
    print("    └── templates/")

if __name__ == "__main__":
    main()