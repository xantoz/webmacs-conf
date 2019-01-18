import webmacs
from webmacs.keymaps import keymap
from webmacs.commands import define_command

derp = __import__("webmacs.commands.global", fromlist=['']) # Don't name modules like keywords...

@define_command("describe-key-briefly")
def describe_binding_briefly(ctx):
    "Like emacs"
    called_with = ctx.minibuffer.do_prompt(derp.BindingPrompt(ctx))
    if called_with:
        ctx.minibuffer.show_info(
            "{key} runs the command {command} (keymap: {keymap})".format(**called_with)
        )


class WhereIsCommandsListPrompt(derp.CommandsListPrompt):
    label = "Where is command: "
    history = webmacs.minibuffer.prompt.PromptHistory()


@define_command("where-is")
def where_is(ctx):
    "Print short notice of where command is bound"
    command = ctx.minibuffer.do_prompt(WhereIsCommandsListPrompt(ctx))
    if not command:
        return
    command_bindings = list("{} (keymap: {})".format(k, kmapname)
                            for kmapname, kmap in webmacs.keymaps.KEYMAPS.items()
                            for k, v in kmap.all_bindings() if v == command)
    if command_bindings:
        ctx.minibuffer.show_info("{} is on: {}".format(command, ", ".join(command_bindings)))
    else:
        ctx.minibuffer.show_info("{} is not on any key".format(command))


keymap("global").define_key("C-h c", "describe-key-briefly")
keymap("global").define_key("C-h F", "describe-command")
keymap("global").define_key("C-h f", "describe-command") # TODO: binding at "C-h f" that allows to list actual python functions (need a REPL first for this to make sense)
keymap("global").define_key("C-h w", "where-is")
