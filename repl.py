import webmacs
import os
import pprint

class EvalExpressionPrompt(webmacs.minibuffer.Prompt):
    label = "M-: "
    # complete_options = {
    #     "match": Prompt.FuzzyMatch,
    #     "complete-empty": True,
    # }
    history = webmacs.minibuffer.prompt.PromptHistory()

    # def completer_model(self):
    #     model = QStringListModel(self)
    #     model.setStringList(sorted(k for k, v in COMMANDS.items()
    #                                if v.visible))
    #     return model

@webmacs.commands.define_command("eval-expression")
def eval_expression(ctx):
    """
    Prompt for a python expression to execute
    """
    prompt = EvalExpressionPrompt(ctx)
    value = ctx.minibuffer.do_prompt(prompt)
    try:
        # TODO: truncate output so there isn't too many lines
        ctx.minibuffer.show_info(pprint.pformat(eval(value, {"webmacs":webmacs, "os":os})))
    except:
        # TODO: print traceback
        pass

webmacs.keymaps.keymap("global").define_key("M-:", "eval-expression")
