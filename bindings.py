from webmacs.keymaps import keymap

keymap("global").define_key("C-x Right", "next-buffer")
keymap("global").define_key("C-x Left", "previous-buffer")

# # Like emacs or conkeror (upstream?)
keymap("global").define_key("C-x 5 2", "make-window")
keymap("global").define_key("C-x 5 0", "close-window")
