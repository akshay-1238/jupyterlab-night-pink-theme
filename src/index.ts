import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { IThemeManager } from '@jupyterlab/apputils';

/**
 * A plugin for the Night Pink theme.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'jupyterlab-night-pink-theme:plugin',
  description: 'A Night Pink theme for JupyterLab',
  requires: [IThemeManager],
  activate: (app: JupyterFrontEnd, manager: IThemeManager) => {
    const style = 'jupyterlab-night-pink-theme/index.css';

    manager.register({
      name: 'JupyterLab Night Pink',
      isLight: false,
      themeScrollbars: true,
      load: () => manager.loadCSS(style),
      unload: () => Promise.resolve(undefined)
    });
  },
  autoStart: true
};

export default plugin;
