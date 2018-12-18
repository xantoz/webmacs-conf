from webmacs.keymaps import keymap
from webmacs.commands import define_command

derp = __import__("webmacs.commands.global", fromlist=['']) # Don't name modules like keywords...
@define_command("describe-key-briefly")
def describe_binding_briefly(ctx):
    "Like emacs"
    called_with = ctx.minibuffer.do_prompt(derp.BindingPrompt(ctx))
    if called_with:
        ctx.minibuffer.show_info(
            "{key} runs the command {command} (keymap {keymap})".format(**called_with)
        )

keymap("global").define_key("C-h c", "describe-key-briefly")
keymap("global").define_key("C-h F", "describe-command")
keymap("global").define_key("C-h f", "describe-command") # TODO: binding at "C-h f" that allows to list actual python functions (need a REPL first for this to make sense)
