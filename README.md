# Galaksi Global Website

[![CI](https://github.com/azuzun/WEB1_Final/actions/workflows/ci.yml/badge.svg)](https://github.com/azuzun/WEB1_Final/actions/workflows/ci.yml)

A responsive, single-page company website for Galaksi Global Gemicilik Lojistik. The site introduces the company's logistics services and provides direct telephone and email contact options.

Live site: [azuzun.github.io/WEB1_Final](https://azuzun.github.io/WEB1_Final/)

## Overview

This repository contains a dependency-free static website built with HTML and CSS. The interface and content are in Turkish. The deployable files are placed at the repository root so that local preview and GitHub Pages deployment are straightforward.

The original website code and visual design have been preserved. Repository-level documentation, organization, tests, and automation were added around it.

## Key Features

- Responsive single-page company presentation
- Sea, road, air, intermediary transport, and warehousing service sections
- About, service, value proposition, quote, and contact sections
- Direct `tel:` and `mailto:` contact links
- Sticky navigation and smooth in-page scrolling
- Local image assets with no external runtime dependency

## Technologies Used

| Technology | Purpose |
| --- | --- |
| HTML5 | Page structure and content |
| CSS3 | Layout, responsive design, and presentation |
| Python 3 standard library | Repository tests and local preview server |
| GitHub Actions | Automated validation for pushes and pull requests |

## Project Architecture

The browser loads one HTML document, one stylesheet, and local image assets. The site has no application backend, database, JavaScript runtime, or build step.

```text
Browser
  └── index.html
      ├── assets/css/galaksi-global.css
      └── assets/images/*

Repository quality checks
  ├── Makefile
  ├── tests/test_site.py
  └── .github/workflows/ci.yml
```

## Installation Requirements

- Git
- Python 3.10 or newer
- A modern web browser

No package installation is required.

## Installation Instructions

```bash
git clone https://github.com/azuzun/WEB1_Final.git
cd WEB1_Final
```

## Usage Instructions

Start a local server:

```bash
make serve
```

Open [http://localhost:8000](http://localhost:8000) in a browser. Stop the server with `Ctrl+C`.

If `make` is unavailable, run:

```bash
python3 -m http.server 8000
```

Because this is a static website, `index.html` can also be opened directly in a browser. A local server is recommended because it matches production URL behavior more closely.

## Example Input and Output

The project is an informational website rather than a command-line program. Its main interactions are:

| User action | Result |
| --- | --- |
| Select a navigation item | Scrolls to the matching page section |
| Select **Teklif Alın** | Opens the quote contact section |
| Select a telephone number | Opens the device's configured calling application |
| Select an email address | Opens the device's configured email application |

## Testing Instructions

Run all repository tests:

```bash
make test
```

Or use Python directly:

```bash
python3 -m unittest discover -s tests -v
```

The tests validate the existing code without changing it. They check document basics, required sections, unique IDs, image alternative text, in-page links, contact links, local HTML/CSS assets, and balanced CSS blocks.

GitHub Actions runs the same checks on pushes and pull requests targeting `main`.

## Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── assets/
│   ├── css/
│   │   └── galaksi-global.css
│   └── images/
│       ├── backgrounds/
│       │   └── services-bg-2.jpg
│       ├── galaksi-global-logo-cropped.png
│       └── vehicleAi.png
├── docs/
│   └── brand/
│       ├── galaksi-global-logo.pdf
│       └── logo-source.png
├── tests/
│   └── test_site.py
├── .editorconfig
├── .gitignore
├── CONTRIBUTING.md
├── Makefile
├── README.md
└── index.html
```

Deployable files are kept at the root. Original brand source files are preserved under `docs/brand/`, separate from runtime assets.

## Technical Challenges and Solutions

| Challenge | Repository-level solution |
| --- | --- |
| The deployable website was nested several directories below the repository root. | Moved the complete site and its assets together to the root without editing their contents. |
| The repository contained a byte-identical duplicate of the vehicle image. | Kept the referenced copy and removed only the unreferenced duplicate. |
| Brand source files were mixed with deployable site files. | Preserved them in `docs/brand/`. |
| The project had no documentation or repeatable validation. | Added a complete README, contribution guidance, standard-library tests, and CI. |
| The original PDF filename caused Unicode normalization differences across operating systems. | Renamed it to a portable lowercase ASCII filename. |

## Future Improvements

The following are recommendations only; they are not implemented in the current code:

- Add a semantic `<main>` landmark and a single `<h1>` page heading.
- Add a meta description and social-sharing metadata.
- Improve keyboard focus styling and add a skip-to-content link.
- Replace the unfinished address placeholder after verified address information is available.
- Optimize large PNG assets after visual approval.
- Add browser-level responsive and accessibility tests if the site evolves.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the local workflow and review checklist.

## License

No open-source license has been selected. Until the repository owner chooses and adds a license, the source remains protected by default copyright rules and may not be reused without permission.
