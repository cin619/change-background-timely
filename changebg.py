import os
import re
import win32api
import win32gui
import win32con
import time


def set_wallpaper(bmp_path):
    # 打开指定注册表路径
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    # 最后的参数:2拉伸,0居中,6适应,10填充,0平铺
    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    # 最后的参数:1表示平铺,拉伸居中等都是0
    win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # 刷新桌面
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,bmp_path, win32con.SPIF_SENDWININICHANGE)


path = 'C:\\Users\\bmp\\'   # 图片路径
now =time.strftime('%H')
if __name__ == '__main__':
    if now == "00":
        set_wallpaper(path + 'pm12.bmp')
    elif now == "01":
        set_wallpaper(path + 'am1.bmp')
    elif now == "02":
        set_wallpaper(path + 'am2.bmp')
    elif now == "03":
        set_wallpaper(path + 'am3.bmp')
    elif now == "04":
        set_wallpaper(path + 'am4.bmp')
    elif now == "05":
        set_wallpaper(path + 'am5.bmp')
    elif now == "06":
        set_wallpaper(path + 'am6.bmp')
    elif now == "07":
        set_wallpaper(path + 'am7.bmp')
    elif now == "08":
        set_wallpaper(path + 'am8.bmp')
    elif now == "09":
        set_wallpaper(path + 'am9.bmp')
    elif now == "10":
        set_wallpaper(path + 'am10.bmp')
    elif now == "11":
        set_wallpaper(path + 'am11.bmp')
    elif now == "12":
        set_wallpaper(path + 'am12.bmp')
    elif now == "13":
        set_wallpaper(path + 'pm1.bmp')
    elif now == "14":
        set_wallpaper(path + 'pm2.bmp')
    elif now == "15":
        set_wallpaper(path + 'pm3.bmp')
    elif now == "16":
        set_wallpaper(path + 'pm4.bmp')
    elif now == "17":
        set_wallpaper(path + 'pm5.bmp')
    elif now == "18":
        set_wallpaper(path + 'pm6.bmp')
    elif now == "19":
        set_wallpaper(path + 'pm7.bmp')
    elif now == "20":
        set_wallpaper(path + 'pm8.bmp')
    elif now == "21":
        set_wallpaper(path + 'pm9.bmp')
    elif now == "22":
        set_wallpaper(path + 'pm10.bmp')
    elif now == "23":
        set_wallpaper(path + 'pm11.bmp')
