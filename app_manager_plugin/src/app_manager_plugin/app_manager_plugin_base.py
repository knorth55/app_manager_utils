class AppManagerPlugin(object):
    def __init__(self):
        pass

    @classmethod
    def app_manager_start_plugin(cls, app, ctx, plugin_args):
        return ctx

    @classmethod
    def app_manager_stop_plugin(cls, app, ctx, plugin_args):
        return ctx
