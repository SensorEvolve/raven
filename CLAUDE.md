# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Vague2k** is a VS Code color theme extension — a port of the [Vague2k Neovim theme](https://github.com/vague2k/vague.nvim) with a true-black background (`#050301`) from the original Raven theme. The entire codebase is a single JSON theme file plus extension metadata.

## Building & Publishing

```bash
# Install vsce (VS Code Extension CLI) if not already installed
npm install -g @vscode/vsce

# Package the extension into a .vsix file
vsce package

# Publish to VS Code Marketplace (requires publisher auth)
vsce publish
```

There are no build steps, tests, or linting — the theme is pure JSON.

## Architecture

The entire theme lives in one file:

**`themes/vague2k-color-theme.json`** — Three sections:
1. **`colors`** (lines ~5–327) — VS Code UI element colors (~200+ assignments: sidebar, tabs, editor gutter, terminal ANSI, git decorations, etc.)
2. **`tokenColors`** (lines ~329–934) — TextMate grammar-based syntax highlighting (~60+ rules using `scope` selectors)
3. **`semanticTokenColors`** (lines ~936–964) — Modern semantic token overrides (language server-aware, takes precedence over tokenColors)

**`package.json`** — Extension manifest. The `contributes.themes` array registers the theme with VS Code.

## Color Palette

All colors come from the Vague2k palette (ported from Neovim). When editing, use these consistently:

| Name       | Hex       | Primary Use                              |
|------------|-----------|------------------------------------------|
| bg         | `#050301` | Editor/terminal background (Raven black) |
| surface    | `#141415` | Panels, menus, widgets                   |
| inactiveBg | `#1c1c24` | Overlays, selections, dropdowns          |
| line       | `#252530` | Indent guides, line highlight            |
| visual     | `#333738` | Selection background                     |
| search     | `#405065` | Find match highlight                     |
| comment    | `#606079` | Comments, muted/inactive text            |
| operator   | `#90a0b5` | Operators, punctuation                   |
| fg         | `#cdcdcd` | Primary foreground                       |
| property   | `#c3c3d5` | Object properties, JSON keys             |
| constant   | `#aeaed1` | Constants, booleans, HTML attributes     |
| parameter  | `#bb9dbd` | Parameters, decorators                   |
| type       | `#9bb4bc` | Types, classes, tab active border        |
| builtin    | `#b4d4cf` | Builtins, cursor, links, markdown code   |
| keyword    | `#6e94b2` | Keywords, storage types, CSS @ rules     |
| hint       | `#7e98e8` | Info diagnostics, button hover           |
| func       | `#c48282` | Functions, methods                       |
| string     | `#e8b589` | Strings, markdown headings               |
| number     | `#e0a363` | Numbers, CSS selectors, markdown bold    |
| error      | `#d8647e` | Errors, `return`, HTML tags, git deleted |
| warning    | `#f3be7c` | Warnings, delta                          |
| plus       | `#7fa563` | Git added, diff inserted                 |

## Versioning

Version is set in `package.json`. Bump it before packaging/publishing. The README badge still references 1.0.0 but the actual version is tracked in `package.json`.
