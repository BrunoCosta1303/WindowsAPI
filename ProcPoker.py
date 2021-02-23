import ctypes
import win32gui

k_handler = ctypes.WinDLL("Kernel32.dll")
u_handler = ctypes.WinDLL("User32.dll")
PROCESS_ALL_ACCESS = ( 0x000F0000 | 0x0010000 | 0xFFF) 

# Get's the handle for the active windows
def winEnumHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible( hwnd ):
        print (hex(hwnd), win32gui.GetWindowText( hwnd ))

win32gui.EnumWindows( winEnumHandler, None )


# Choosing hwnd(Handler for operations)
lpWindowName = ctypes.c_char_p(input("So... Are you just going to stare at the prompt ?").encode('utf-8'))
hWnd = u_handler.FindWindowA(None, lpWindowName)
if hWnd == 0: 
    print("Error Code: {0} - Ain't no handles for you to grab, mate!".format(k_handler.GetLastError()))
    exit(1)
else:   
    print("You've been handled XD")    

#Getting PID (For further change - set just one function to list'em all)
lpdwProcessId = ctypes.c_ulong()
response = u_handler.GetWindowThreadProcessId(hWnd, ctypes.byref(lpdwProcessId))
if response ==0:
    print("Error Code: {0} - Are u sure bro ? Try Again!".format(k.handler.GetLastError()))
    exit(1)
else: 
    print("We're good on PIDS")

#Closes processes 
dwDesiredAccess = PROCESS_ALL_ACCESS
bInheritHandle = False
dwProcessId = lpdwProcessId
hprocess = k_handler.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId)
if hprocess <= 0:
    print("Error Code: {0} - Maybe you wanna go outside, catch up with your family a litle... Instead of be running stuff without permition...".format(k_handler.GetLastError()))
    exit(1)
else: 
    print("Oraite, mate! Killing the poor bastard")
u_exitCode = 0x1
response = k_handler.TerminateProcess(hprocess, u_exitCode)
if hprocess <= 0:
    print("Error Code: {0} - Oak's words echoes in your head...".format(k_handler.GetLastError())) 
else:
    print("Killed")
