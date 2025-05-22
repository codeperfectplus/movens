from datetime import datetime

project = 'movens'
release = '1.0.7'
templates_path = ['_templates']
source_suffix = ".rst"
master_doc = "index"
year = datetime.now().year
copyright = "{} Py-Contributors".format(year)
extensions = ['sphinx.ext.autosectionlabel']
releases_github_path = "Py-Contributors/filemover"
autosectionlabel_prefix_document = True
html_static_path = ['_static']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv']
html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'] }



# -- General Configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',          # Automatically document from docstrings
    'sphinx.ext.todo',             # Support for todo notes
    'sphinx.ext.coverage',         # Check documentation coverage
    'sphinx.ext.viewcode',         # Add links to highlighted source code
    'sphinx.ext.autosectionlabel', # Automatically reference sections
    'sphinx.ext.githubpages',      # Publish HTML docs on GitHub Pages
]

# Prefix document path to section labels to avoid ambiguity
autosectionlabel_prefix_document = True

# PDF generation (requires an external tool)
pdf_documents = [
    ('index', 'SystemGuard_Documentation', 'SystemGuard Docs', 'SystemGuard Team')
]

# GitHub Releases Integration
releases_github_path = "codeperfectplus/systemguard"
releases_unstable_prehistory = True  # Treat pre-v1.0 releases as unstable

# Custom templates path
templates_path = ['_templates']

# Specify the source file format
source_suffix = ".rst"

# Main document (entry point)
master_doc = "index"

# Patterns to exclude from the build process
exclude_patterns = [
    '_build', 
    'Thumbs.db', 
    '.DS_Store', 
    '.venv'
]

# -- HTML Output Configuration ------------------------------------------------
# Specify the theme for HTML output
html_theme = 'pydata_sphinx_theme'  # Alternative themes: 'sphinx_rtd_theme', 'alabaster'

# Paths for custom static files (e.g., CSS stylesheets)
html_static_path = ['_static']

# Theme options for pydata_sphinx_theme
html_theme_options = {
    "show_prev_next": True,             # Enable next/previous buttons
    "navigation_depth": 4,              # Control TOC depth, increase to show more levels
    "collapse_navigation": True,         # Collapsible sidebar navigation
    "navbar_align": "content",           # Center-align navbar content
    "show_nav_level": 2,                 # Show second-level headings in the navbar
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/codeperfectplus/systemguard",
            "icon": "fab fa-github",
            "type": "fontawesome"
        },
        {
            "name": "Releases",
            "url": "https://github.com/codeperfectplus/systemguard/releases",
            "icon": "fas fa-tag",
            "type": "fontawesome"
        }
    ],
    "use_edit_page_button": True,
   
}

# Provide context for "Edit on GitHub" button
html_context = {
    "github_user": "codeperfectplus",
    "github_repo": "systemguard",
    "github_version": "production",
    "doc_path": "docs",
}

# Configure sidebars
html_sidebars = {
    '**': [
        'globaltoc.html',    # Global table of contents
        'relations.html',    # Links to next/previous pages
        'sourcelink.html',   # Link to view source code
        'searchbox.html'     # Search box
    ]
}

# Configure sidebars for documentation
html_sidebars = {
    '**': [
        'globaltoc.html',    # Global table of contents
        'relations.html',    # Links to next/previous pages
        'sourcelink.html',   # Link to view source code
        'searchbox.html',     # Search box        
    ]
}


# Additional CSS for improved navbar styling
html_css_files = [
    'custom.css'  # Custom CSS file for additional styling
]