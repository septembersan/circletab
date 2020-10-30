
" The VimL/VimScript code is included in this sample plugin to demonstrate the
" two different approaches but it is not required you use VimL. Feel free to
" delete this code and proceed without it.

command! TabRollBack call RollBackTab()

" augroup NvimTabRollBack
"     au!
"     " au TabEnter * call GdbHandleEvent("on_tab_enter")
"     au TabLeave * call GdbHandleEvent("on_tab_leave")
"     " au BufEnter * call GdbHandleEvent("on_buf_enter")
"     " au BufLeave * call GdbHandleEvent("on_buf_leave")
"     " au TabClosed * call GdbHandleTabClosed()
"     " au VimLeavePre * call GdbHandleVimLeavePre()
" augroup END
