from webmacs.keymaps import keymap
from webmacs.commands import register_prompt_opener_commands, webjump

# Binding from conkeror
keymap("global").define_key("C-x C-v", "go-to-alternate-url")

# Hack to make 'g' and 'C-x C-f' behave like conkeror (no text)
register_prompt_opener_commands(
    "find-url",
    webjump.wj_prompt(""),
    "Prompt to open a URL or a webjump (conkeror style)",
)
keymap("webbuffer").define_key("g", "find-url")
keymap("global").define_key("C-x C-f", "find-url-new-buffer")

