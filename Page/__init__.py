from selenium.webdriver.common.by import By

"""初始页面"""

# 启动页面_教程_进入爱优品
access_love_youpin = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/ip_ll_enter')
# 始终允许按钮
allow_button = (By.ID,'com.android.packageinstaller:id/permission_allow_button')

"""我要卖功能"""

# 我的按钮
my_button = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/lfi_tv_my')
# 我要卖
I_want_to_sell = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/lfi_ll_sell')
# 马上登录
immediately_register = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/fm_rl_login')
# 快速注册
celerity_register = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/lt_tv_register')
# 登录页面_账户
register_acctount = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/al_et_user')
# 登录页面_密码
register_passwod = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/al_et_pwd')
# 登录页面_确定页面
register_confirm = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/al_ll_login')
# 我的_列表（一组）
my_list = (By.CLASS_NAME,'android.widget.TextView')
# 退出当前账号
quit_accounts = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/fm_ll_out_login')
# 点击确定按钮
confirm_quit = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/dc_right')
# 返回按钮
return_button = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/lt_rl_left')
