import webmacs
import os
import pprint
import traceback
import importlib

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
    if not value:
        return
    try:
        # TODO: truncate output so there isn't too many lines
        ctx.minibuffer.show_info(pprint.pformat(eval(value, {
            "webmacs": webmacs,
            "os": os,
            "init": __import__('init'),
            "reload": importlib.reload,
            "pprint": pprint.pprint,
        })))
    except:
        trace = traceback.format_exc()
        ctx.minibuffer.show_info(trace)
        print(trace)
        pass

webmacs.keymaps.keymap("global").define_key("M-:", "eval-expression")
