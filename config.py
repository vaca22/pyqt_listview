


is_proxy = True
app_name_config="订单导出助手 v2.3.1"

def init_config():
    global app_name_config
    global is_proxy
    if is_proxy:
        app_name_config="订单导出助手 v2.3.1"
    else:
        app_name_config="订单导出助手 v2.3"