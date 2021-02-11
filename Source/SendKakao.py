import time, win32con, win32api, win32gui
import os
# kakaotalk chat room title
roomTitle = "[공중파]중계방"

# send text
def sendText(text):
    hwndMain = win32gui.FindWindow(None, roomTitle)
    hwndEdit = win32gui.FindWindowEx(hwndMain, None, "RichEdit50W", None)

    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    sendReturn(hwndEdit)

# send "\n"
def sendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(1)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

def enterRoom():
    hwnd = win32gui.FindWindow(None, "카카오톡")
    hwndChild = win32gui.FindWindowEx(hwnd, None, "EVA_ChildWindow", None)
    hwndEdit01 = win32gui.FindWindowEx(hwndChild, None, "EVA_Window", None)
    hwndEdit02 = win32gui.FindWindowEx(hwndChild, hwndEdit01, "EVA_Window", None)
    hwndEdit02_01 = win32gui.FindWindowEx(hwndEdit02, None, "Edit", None)

    win32api.SendMessage(hwndEdit02_01, win32con.WM_SETTEXT, 0, roomTitle)
    time.sleep(1)  # 안정성 위해 필요
    sendReturn(hwndEdit02_01)
    time.sleep(1)

def openKakao():
    os.system(r'"C:\Program Files (x86)\Kakao\KakaoTalk\KakaoTalk.exe"')
    time.sleep(1)

