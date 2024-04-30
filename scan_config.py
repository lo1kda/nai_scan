scan_nai_config = {
    # 必要设置
    'Repeated_execution': True,  # 无限循环执行
    "Silent_run": False, # 静默运行，没啥用
    "Proxy_url": "http://pom.pom.pom:pom",  # 代理池链接
    "Threading": 9999,  # 线程数，开的越高，扫的越快，需要机器性能允许

    # 扫出来的线报推送到哪，三选一即可
    ## TG
    "TG_BOT_TOKEN": "",  # TG 推送的机器人Token，在TG找 @BotFather 创建一个机器人，BotFather给你的机器人token
    "TG_USER_ID": "",  # TG 推送的目标，可以是频道id、群id、个人id，获取id方法参考 https://laowangblog.com/howt-to-get-userid-and-chatid-of-telegram.html
    "TG_API_HOST": "",  # TG推送反代，填了就不用填下面的htp代理和sock5代理，什么是反代参考 https://imnerd.org/telegram-api-proxy.html
    "TG_PROXY_HTTP": "",  # TG http代理，填了就不用填推送反代和socks5代理，就是clash/v2rayN/sing-box/...这些软件给你的http代理端口，实在不懂自己百度吧
    "TG_PROXY_SOCK5": "",  # TG sock5代理，填了就不用填上面的http代理和推送反代，就是clash/v2rayN/sing-box/...这些软件给你的sock5代理端口，实在不懂自己百度吧

    ## PUSH_PLUS
    "PUSH_PLUS_TOKEN": "",  # Pushpuls 的推送Token，参考官方教程 https://pushplus.plus/doc/guide/demo.html
    "PUSH_PLUS_USER": "",  # Pushpuls 微信推送的群组编码，参考官方教程 https://pushplus.plus/doc/guide/demo.html

    ## 企业微信
    "QYWX_KEY": ""  # 企业微信，参考官方教程 https://work.weixin.qq.com/api/doc/90000/90136/91770

    # 不用修改的设置
    "Verify_Token": "POMPOM",  # 不用改
    "Cookie_access": "2", # 不用改
    "Shop_number": "2",  # 不用改
    "Proxy_mode": "2",  # 不用改
    "Proxy_count": 5,  # 不用改
    "Proxy_sleep": 1,  # 不用改
    "Retry_count": 5,  # 不用改
    "Draw_summary": False,  # 不用改
    "Lottery_summary": False,  # 不用改
    "Push_shop_link": False,  # 不用改
}

# 不要删掉
scan_nai_debug={}
