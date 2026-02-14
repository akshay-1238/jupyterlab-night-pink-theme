# Quick Setup Guide for JupyterLab Night Pink Theme

## What You've Built

You now have a complete JupyterLab theme extension with:
- Custom Night Pink color scheme (dark purple-pink theme)
- Professional syntax highlighting
- Polished UI elements
- Ready to install and use

## Installation Steps

### 1. Prerequisites Check

First, make sure you have the required software:

```bash
# Check Node.js version (need 18+)
node --version

# Check JupyterLab version (need 4.0+)
jupyter lab --version

# If you don't have jlpm, install it
npm install -g jlpm
```

### 2. Install the Theme

Navigate to your theme directory and run:

```bash
cd jupyterlab-night-pink-theme

# Install dependencies
jlpm install

# Build the theme
jlpm build

# Install as JupyterLab extension
jupyter labextension install .

# Rebuild JupyterLab
jupyter lab build
```

### 3. Activate the Theme

```bash
# Start JupyterLab
jupyter lab
```

Then in JupyterLab:
1. Go to **Settings** menu → **Theme**
2. Select **JupyterLab Night Pink**
3. The theme will apply immediately!

## Customizing the Theme

### Changing Colors

Edit `style/variables.css` to modify colors. Here are the main ones:

```css
/* Main background - Change this for overall darkness */
--jp-layout-color0: #1a0f1f;

/* Pink accent - Change this for the main accent color */
--jp-brand-color1: #ff5bb8;

/* Text color - Change this for readability */
--jp-ui-font-color0: #f0e6f6;
```

### After Making Changes

```bash
# Rebuild the theme
jlpm build

# Rebuild JupyterLab
jupyter lab build

# Restart JupyterLab
```

## Using VS Code Night Pink Colors

### Option 1: Extract from VS Code Extension

If you have VS Code Night Pink installed:

1. Find the extension folder:
   - Windows: `%USERPROFILE%\.vscode\extensions\`
   - Mac/Linux: `~/.vscode/extensions/`

2. Look for folder like `samrc.night-pink-x.x.x`

3. Open `themes/night-pink-color-theme.json`

4. Copy colors to your `variables.css`

### Option 2: Use VS Code's Built-in Tool

1. In VS Code with Night Pink theme active:
   - Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
   - Type: "Developer: Generate Color Theme From Current Settings"
   - This creates a JSON file with all colors

2. Map the colors:
   ```
   VS Code                    →  JupyterLab Variable
   ───────────────────────────────────────────────────
   editor.background          →  --jp-layout-color0
   editor.foreground          →  --jp-content-font-color0
   editorLineNumber.foreground →  --jp-ui-font-color2
   activityBar.background     →  --jp-layout-color1
   ```

### Option 3: Common Night Pink-style Colors

If you don't have access to the theme, here's a typical pink theme palette:

```css
/* Dark purple-pink backgrounds */
--jp-layout-color0: #1a0f1f;  /* Darkest */
--jp-layout-color1: #241729;  /* Dark */
--jp-layout-color2: #2d1f33;  /* Medium */
--jp-layout-color3: #3a2842;  /* Light */

/* Pink accents */
--jp-brand-color0: #ff6ec7;   /* Light pink */
--jp-brand-color1: #ff5bb8;   /* Pink */
--jp-brand-color2: #ff48a9;   /* Dark pink */

/* Syntax colors */
--jp-mirror-editor-keyword-color: #ff6ec7;    /* Keywords - pink */
--jp-mirror-editor-string-color: #ff79c6;     /* Strings - pink-red */
--jp-mirror-editor-comment-color: #6272a4;    /* Comments - gray-blue */
--jp-mirror-editor-def-color: #50fa7b;        /* Functions - green */
--jp-mirror-editor-number-color: #f1fa8c;     /* Numbers - yellow */
--jp-mirror-editor-variable-color: #f0e6f6;   /* Variables - light pink */
```

## Development Workflow

For active development (auto-rebuild on changes):

### Terminal 1 - Watch Source Files
```bash
cd jupyterlab-night-pink-theme
jlpm watch
```

### Terminal 2 - Watch JupyterLab
```bash
jupyter lab --watch
```

Now changes to CSS/TypeScript files will auto-rebuild!

## Troubleshooting

### "Extension not found"
```bash
# Check if installed
jupyter labextension list

# If not listed, reinstall
jupyter labextension install .
jupyter lab build
```

### "Theme not appearing in menu"
```bash
# Clear cache and rebuild
jupyter lab clean
jupyter lab build --dev-build=False
```

### "Build errors"
```bash
# Clean everything and start fresh
jlpm clean:all
rm -rf node_modules
jlpm install
jlpm build
jupyter lab build
```

### "Colors not updating"
1. Make sure you edited `style/variables.css`
2. Run `jlpm build`
3. Run `jupyter lab build`
4. Hard refresh browser (Ctrl+Shift+R or Cmd+Shift+R)
5. If still not working, clear browser cache

## Sharing Your Theme

### Method 1: GitHub Repository

1. Create a GitHub repository
2. Upload your theme files
3. Others can clone and install:
   ```bash
   git clone https://github.com/yourusername/jupyterlab-night-pink-theme
   cd jupyterlab-night-pink-theme
   jlpm install && jlpm build
   jupyter labextension install .
   ```

### Method 2: Publish to npm

1. Update `package.json` with your information
2. Create an npm account at npmjs.com
3. Login: `npm login`
4. Publish: `npm publish`
5. Others install with: `pip install jupyterlab-night-pink-theme`

## Tips for Best Results

1. **Test in different lighting conditions** - Your theme should work in both bright and dark environments

2. **Check contrast ratios** - Use tools like WebAIM Contrast Checker to ensure text is readable

3. **Test with different file types** - Python, Markdown, JSON, etc. should all look good

4. **Consider colorblind users** - Avoid relying only on color to convey information

5. **Keep it consistent** - Use your color palette systematically across all UI elements

## Next Steps

Now that you have a working theme:

1. ✅ Customize colors to your preference
2. ✅ Test with your typical workflow
3. ✅ Share with friends or the community
4. ✅ Consider publishing to npm
5. ✅ Create variations (light mode, different accent colors)

Happy theming! 🎨✨
