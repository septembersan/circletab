# import neovim as vim
import pynvim as vim
# https://pynvim.readthedocs.io/en/latest/usage/remote-plugins.html
'''
:call dein#recache_runtimepath()
:UpdateRemotePlugins
'''

@vim.plugin
class CircleTab(object):
    def __init__(self, vim):
        self.vim = vim
        self._stack_tabpagesnr = []
        self._flag = False


    @vim.function('RollBackTab')
    def roll_back_tab(self, args):
        self._flag = True
        if len(self._stack_tabpagesnr) < 1:
            return
        nr = self._stack_tabpagesnr.pop()
        self.vim.command(f'tabn {nr}')

    @vim.autocmd('TabLeave', sync=True)
    def on_tab_leave(self):
        if self._flag and len(self._stack_tabpagesnr) != 0:
            self._flag = False
            return
        self._stack_tabpagesnr.append(self.vim.current.tabpage.number)
        # self.vim.command(f'echo "leave" {self._stack_tabpagesnr}')
