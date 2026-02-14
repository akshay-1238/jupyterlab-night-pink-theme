# JupyterLab Night Pink Theme

A beautiful dark theme for JupyterLab inspired by VS Code's Night Pink theme. Features a dark purple-pink color scheme that's easy on the eyes during long coding sessions.

## Features

- 🎨 Beautiful pink and purple color palette
- 🌙 Dark theme optimized for low-light environments
- 💅 Carefully crafted syntax highlighting
- ⚡ Smooth and consistent UI elements
- 🔍 Enhanced code readability

## Preview

The theme features:
- Deep purple-pink background colors (#1a0f1f base)
- Vibrant pink accents (#ff6ec7)
- Carefully selected syntax highlighting colors
- Smooth scrollbars and UI elements
- Custom cell borders and active indicators

## Prerequisites

- JupyterLab >= 4.0.0
- Node.js >= 18
- npm or yarn

## Installation

### Development Installation

1. **Clone or create the theme directory:**
```bash
cd jupyterlab-night-pink-theme
```

2. **Install dependencies:**
```bash
npm install
# or
jlpm install
```

3. **Build the extension:**
```bash
npm run build
# or
jlpm build
```

4. **Install the extension:**
```bash
jupyter labextension install .
```

5. **Rebuild JupyterLab:**
```bash
jupyter lab build
```

6. **Start JupyterLab:**
```bash
jupyter lab
```

### Using the Theme

1. Once JupyterLab starts, go to **Settings → Theme**
2. Select **JupyterLab Night Pink** from the theme dropdown
3. Enjoy your new theme!

## Development

### Watching for Changes

For development, you can watch for changes and automatically rebuild:

```bash
# In one terminal, watch the source files
npm run watch
# or
jlpm watch

# In another terminal, run JupyterLab in watch mode
jupyter lab --watch
```

### Customizing Colors

The main color definitions are in `style/variables.css`. You can customize:

- **Background colors**: `--jp-layout-color0` through `--jp-layout-color4`
- **Brand/accent colors**: `--jp-brand-color0` through `--jp-brand-color4`
- **Syntax highlighting**: `--jp-mirror-editor-*` variables
- **UI elements**: Various other CSS variables

After making changes, rebuild the extension:

```bash
npm run build
jupyter lab build
```

## Extracting Colors from VS Code Themes

If you want to extract colors from the actual VS Code Night Pink theme or any other VS Code theme:

1. **Find the theme in VS Code:**
   - In VS Code, press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
   - Type "Developer: Generate Color Theme From Current Settings"
   - This will create a JSON file with all current theme colors

2. **Or locate the theme file:**
   - VS Code themes are typically in: `~/.vscode/extensions/`
   - Look for the theme extension folder (e.g., `samrc.night-pink-x.x.x`)
   - Open `themes/` directory and find the `.json` file
   - Copy the color values you need

3. **Map VS Code colors to JupyterLab variables:**
   - `editor.background` → `--jp-layout-color0`
   - `editor.foreground` → `--jp-content-font-color0`
   - `editorLineNumber.foreground` → `--jp-ui-font-color2`
   - Syntax token colors → `--jp-mirror-editor-*` variables

## File Structure

```
jupyterlab-night-pink-theme/
├── src/
│   └── index.ts           # Main TypeScript plugin file
├── style/
│   ├── index.css          # Main stylesheet with theme rules
│   ├── index.js           # Style module loader
│   └── variables.css      # CSS variables (colors, fonts, etc.)
├── package.json           # Package configuration
├── tsconfig.json          # TypeScript configuration
└── README.md             # This file
```

## Publishing (Optional)

To publish your theme to npm and make it available for others:

1. **Update package.json** with your details:
   - Change `name`, `author`, `repository`, etc.

2. **Build the production version:**
```bash
npm run build:prod
```

3. **Publish to npm:**
```bash
npm publish
```

4. **Users can then install with:**
```bash
pip install jupyterlab-night-pink-theme
```

## Troubleshooting

### Theme doesn't appear in the list
- Make sure you ran `jupyter lab build`
- Check for errors in the browser console (F12)
- Verify the extension is installed: `jupyter labextension list`

### Changes not showing up
- Clear your browser cache
- Run `jupyter lab build --dev-build=False --minimize=False`
- Restart JupyterLab

### Build errors
- Ensure you have Node.js >= 18
- Try removing `node_modules` and reinstalling: `rm -rf node_modules && npm install`
- Check that JupyterLab is version 4.0 or higher: `jupyter lab --version`

## Color Palette Reference

| Element | Color | Hex Code |
|---------|-------|----------|
| Background (darkest) | Deep Purple | `#1a0f1f` |
| Background (dark) | Dark Purple | `#241729` |
| Accent/Brand | Pink | `#ff6ec7` |
| Text (primary) | Light Pink | `#f0e6f6` |
| Keywords | Pink | `#ff6ec7` |
| Strings | Pink Red | `#ff79c6` |
| Comments | Blue Gray | `#6272a4` |
| Functions | Green | `#50fa7b` |

## Credits

- Inspired by VS Code's Night Pink theme by SamRC
- Built using JupyterLab's theme extension template
- Color palette influenced by Dracula and pink theme aesthetics

## License

BSD-3-Clause

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Share your customizations

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Look for similar issues on GitHub
3. Create a new issue with details about your environment

## Credits

This theme is based on the [Night Pink VS Code theme](https://github.com/samRC/night-pink) by SamRC, licensed under the MIT License.

Color scheme © 2021 SamRC - Used under MIT License (see LICENSE_NIGHT_PINK.txt)

JupyterLab theme implementation © 2026 Akshay Balani
