---
title: About
date: 2024-12-08
author: Granth Agarwal
---

# Markdown Articles Web Application

## Overview

This is a Flask-based web application designed to render and display Markdown articles with frontmatter metadata. The application provides a simple, elegant interface for publishing and reading blog-style articles.

## Features

- Dynamic Markdown article rendering
- Frontmatter metadata support
- Responsive and minimalist design
- Code syntax highlighting
- Automatic article sorting by date

## Dependencies

- Flask
- markdown2
- PyYAML
- Pygments

## Key Components

### Article Parsing
- Supports YAML frontmatter in Markdown files
- Extracts metadata such as title, date, and author
- Converts Markdown to HTML with syntax highlighting

### Routes
- `/`: Displays list of articles sorted by date
- `/article/<slug>`: Renders individual articles by their slug

## Markdown File Format

Articles should be written in Markdown with YAML frontmatter:

```markdown
---
title: My Article Title
date: 2024-01-15
author: John Doe
---

Article content here...
```

## Setup and Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Place Markdown files in the `articles/` directory
4. Run the application: `python app.py`

## Customization

- Modify `templates/base.html` for global layout changes
- Adjust styling in templates using Tailwind CSS classes
- Extend `app.py` to add more routes or functionality

## Contact

Maintainer: [Granth Agarwal](https://gtithub.com/hey-granth)

Email: [heygranth@gmail.com](mailto:heygranth@gmail.com)