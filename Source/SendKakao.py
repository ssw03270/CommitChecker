import time, win32con, win32api, win32gui

# kakaotalk chat room title
roomTitle = "RommTitle"

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

