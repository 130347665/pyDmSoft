import ctypes
import os
from comtypes.client import CreateObject
import win32com.client
class DM():
    def __init__(self,DmRegPath=None,DMPath=None) -> None:
        self.dm = None
        if DmRegPath is None and DMPath is None:
            print("不使用免註冊")
            self.dm = win32com.client.Dispatch('dm.dmsoft')
        elif DmRegPath is not None and DMPath is not None:
            print("使用免註冊調用")
            self.dm = self.免註冊調用(DmRegPath,DMPath)
            
        else:
            raise Exception("請傳入兩個參數或者不傳入參數")
        if not self.dm:
            raise Exception("DM初始化失敗")
        
            
    def 免註冊調用(self,DmRegPath,DMPath):
        try:
            dm = win32com.client.Dispatch('dm.dmsoft')
        except:
            dms = ctypes.windll.LoadLibrary(DmRegPath)
            location_dmreg = DMPath
            dms.SetDllPathW(location_dmreg, 0)
            dm = CreateObject('dm.dmsoft')
        return dm
    def SetPath(self, path):
        return self.dm.SetPath(path)

    def Ocr(self, x1, y1, x2, y2, color, sim):
        return self.dm.Ocr(x1, y1, x2, y2, color, sim)

    def FindStr(self, x1, y1, x2, y2, str, color, sim):
        return self.dm.FindStr(x1, y1, x2, y2, str, color, sim)

    def GetResultCount(self, str):
        return self.dm.GetResultCount(str)

    def GetResultPos(self, str, index):
        return self.dm.GetResultPos(str, index)

    def StrStr(self, s, str):
        return self.dm.StrStr(s, str)

    def SendCommand(self, cmd):
        return self.dm.SendCommand(cmd)

    def UseDict(self, index):
        return self.dm.UseDict(index)

    def GetBasePath(self):
        return self.dm.GetBasePath()

    def SetDictPwd(self, pwd):
        return self.dm.SetDictPwd(pwd)

    def OcrInFile(self, x1, y1, x2, y2, pic_name, color, sim):
        return self.dm.OcrInFile(x1, y1, x2, y2, pic_name, color, sim)

    def Capture(self, x1, y1, x2, y2, file):
        return self.dm.Capture(x1, y1, x2, y2, file)

    def KeyPress(self, vk):
        return self.dm.KeyPress(vk)

    def KeyDown(self, vk):
        return self.dm.KeyDown(vk)

    def KeyUp(self, vk):
        return self.dm.KeyUp(vk)

    def LeftClick(self):
        return self.dm.LeftClick()

    def RightClick(self):
        return self.dm.RightClick()

    def MiddleClick(self):
        return self.dm.MiddleClick()

    def LeftDoubleClick(self):
        return self.dm.LeftDoubleClick()

    def LeftDown(self):
        return self.dm.LeftDown()

    def LeftUp(self):
        return self.dm.LeftUp()

    def RightDown(self):
        return self.dm.RightDown()

    def RightUp(self):
        return self.dm.RightUp()

    def MoveTo(self, x, y):
        return self.dm.MoveTo(x, y)

    def MoveR(self, rx, ry):
        return self.dm.MoveR(rx, ry)

    def GetColor(self, x, y):
        return self.dm.GetColor(x, y)

    def GetColorBGR(self, x, y):
        return self.dm.GetColorBGR(x, y)

    def RGB2BGR(self, rgb_color):
        return self.dm.RGB2BGR(rgb_color)

    def BGR2RGB(self, bgr_color):
        return self.dm.BGR2RGB(bgr_color)

    def UnBindWindow(self):
        return self.dm.UnBindWindow()

    def CmpColor(self, x, y, color, sim):
        return self.dm.CmpColor(x, y, color, sim)

    def ClientToScreen(self, hwnd):
        return self.dm.ClientToScreen(hwnd)

    def ScreenToClient(self, hwnd):
        return self.dm.ScreenToClient(hwnd)

    def ShowScrMsg(self, x1, y1, x2, y2, msg, color):
        return self.dm.ShowScrMsg(x1, y1, x2, y2, msg, color)

    def SetMinRowGap(self, row_gap):
        return self.dm.SetMinRowGap(row_gap)

    def SetMinColGap(self, col_gap):
        return self.dm.SetMinColGap(col_gap)

    def FindColor(self, x1, y1, x2, y2, color, sim, dir):
        return self.dm.FindColor(x1, y1, x2, y2, color, sim, dir)

    def FindColorEx(self, x1, y1, x2, y2, color, sim, dir):
        return self.dm.FindColorEx(x1, y1, x2, y2, color, sim, dir)

    def SetWordLineHeight(self, line_height):
        return self.dm.SetWordLineHeight(line_height)

    def SetWordGap(self, word_gap):
        return self.dm.SetWordGap(word_gap)

    def SetRowGapNoDict(self, row_gap):
        return self.dm.SetRowGapNoDict(row_gap)

    def SetColGapNoDict(self, col_gap):
        return self.dm.SetColGapNoDict(col_gap)

    def SetWordLineHeightNoDict(self, line_height):
        return self.dm.SetWordLineHeightNoDict(line_height)

    def SetWordGapNoDict(self, word_gap):
        return self.dm.SetWordGapNoDict(word_gap)

    def GetWordResultCount(self, str):
        return self.dm.GetWordResultCount(str)

    def GetWordResultPos(self, str, index):
        return self.dm.GetWordResultPos(str, index)

    def GetWordResultStr(self, str, index):
        return self.dm.GetWordResultStr(str, index)

    def GetWords(self, x1, y1, x2, y2, color, sim):
        return self.dm.GetWords(x1, y1, x2, y2, color, sim)

    def GetWordsNoDict(self, x1, y1, x2, y2, color):
        return self.dm.GetWordsNoDict(x1, y1, x2, y2, color)

    def SetShowErrorMsg(self, show):
        return self.dm.SetShowErrorMsg(show)

    def GetClientSize(self, hwnd):
        return self.dm.GetClientSize(hwnd)

    def MoveWindow(self, hwnd, x, y):
        return self.dm.MoveWindow(hwnd, x, y)

    def GetColorHSV(self, x, y):
        return self.dm.GetColorHSV(x, y)

    def GetAveRGB(self, x1, y1, x2, y2):
        return self.dm.GetAveRGB(x1, y1, x2, y2)

    def GetAveHSV(self, x1, y1, x2, y2):
        return self.dm.GetAveHSV(x1, y1, x2, y2)

    def GetForegroundWindow(self):
        return self.dm.GetForegroundWindow()

    def GetForegroundFocus(self):
        return self.dm.GetForegroundFocus()

    def GetMousePointWindow(self):
        return self.dm.GetMousePointWindow()

    def GetPointWindow(self, x, y):
        return self.dm.GetPointWindow(x, y)

    def EnumWindow(self, parent, title, class_name, filter):
        return self.dm.EnumWindow(parent, title, class_name, filter)

    def GetWindowState(self, hwnd, flag):
        return self.dm.GetWindowState(hwnd, flag)

    def GetWindow(self, hwnd, flag):
        return self.dm.GetWindow(hwnd, flag)

    def GetSpecialWindow(self, flag):
        return self.dm.GetSpecialWindow(flag)

    def SetWindowText(self, hwnd, text):
        return self.dm.SetWindowText(hwnd, text)

    def SetWindowSize(self, hwnd, width, height):
        return self.dm.SetWindowSize(hwnd, width, height)

    def GetWindowRect(self, hwnd):
        return self.dm.GetWindowRect(hwnd)

    def GetWindowTitle(self, hwnd):
        return self.dm.GetWindowTitle(hwnd)

    def GetWindowClass(self, hwnd):
        return self.dm.GetWindowClass(hwnd)

    def SetWindowState(self, hwnd, flag):
        return self.dm.SetWindowState(hwnd, flag)

    def CreateFoobarRect(self, hwnd, x, y, w, h):
        return self.dm.CreateFoobarRect(hwnd, x, y, w, h)

    def CreateFoobarRoundRect(self, hwnd, x, y, w, h, rw, rh):
        return self.dm.CreateFoobarRoundRect(hwnd, x, y, w, h, rw, rh)

    def CreateFoobarEllipse(self, hwnd, x, y, w, h):
        return self.dm.CreateFoobarEllipse(hwnd, x, y, w, h)

    def CreateFoobarCustom(self, hwnd, x, y, pic, trans_color, sim):
        return self.dm.CreateFoobarCustom(hwnd, x, y, pic, trans_color, sim)

    def FoobarFillRect(self, hwnd, x1, y1, x2, y2, color):
        return self.dm.FoobarFillRect(hwnd, x1, y1, x2, y2, color)

    def FoobarDrawText(self, hwnd, x, y, w, h, text, color, align):
        return self.dm.FoobarDrawText(hwnd, x, y, w, h, text, color, align)

    def FoobarDrawPic(self, hwnd, x, y, pic, trans_color):
        return self.dm.FoobarDrawPic(hwnd, x, y, pic, trans_color)

    def FoobarUpdate(self, hwnd):
        return self.dm.FoobarUpdate(hwnd)

    def FoobarLock(self, hwnd):
        return self.dm.FoobarLock(hwnd)

    def FoobarUnlock(self, hwnd):
        return self.dm.FoobarUnlock(hwnd)

    def FoobarSetFont(self, hwnd, font_name, size, flag):
        return self.dm.FoobarSetFont(hwnd, font_name, size, flag)

    def FoobarTextRect(self, hwnd, x, y, w, h):
        return self.dm.FoobarTextRect(hwnd, x, y, w, h)

    def FoobarPrintText(self, hwnd, text, color):
        return self.dm.FoobarPrintText(hwnd, text, color)

    def FoobarClearText(self, hwnd):
        return self.dm.FoobarClearText(hwnd)

    def FoobarTextLineGap(self, hwnd, gap):
        return self.dm.FoobarTextLineGap(hwnd, gap)

    def Play(self, file):
        return self.dm.Play(file)

    def FaqCapture(self, x1, y1, x2, y2, quality, delay, time):
        return self.dm.FaqCapture(x1, y1, x2, y2, quality, delay, time)

    def FaqRelease(self, handle):
        return self.dm.FaqRelease(handle)

    def FaqSend(self, server, handle, request_type, time_out):
        return self.dm.FaqSend(server, handle, request_type, time_out)

    def Beep(self, fre, delay):
        return self.dm.Beep(fre, delay)

    def FoobarClose(self, hwnd):
        return self.dm.FoobarClose(hwnd)

    def MoveDD(self, dx, dy):
        return self.dm.MoveDD(dx, dy)

    def FaqGetSize(self, handle):
        return self.dm.FaqGetSize(handle)

    def LoadPic(self, pic_name):
        return self.dm.LoadPic(pic_name)

    def FreePic(self, pic_name):
        return self.dm.FreePic(pic_name)

    def GetScreenData(self, x1, y1, x2, y2):
        return self.dm.GetScreenData(x1, y1, x2, y2)

    def FreeScreenData(self, handle):
        return self.dm.FreeScreenData(handle)

    def WheelUp(self):
        return self.dm.WheelUp()

    def WheelDown(self):
        return self.dm.WheelDown()

    def SetMouseDelay(self, type, delay):
        return self.dm.SetMouseDelay(type, delay)

    def SetKeypadDelay(self, type, delay):
        return self.dm.SetKeypadDelay(type, delay)

    def GetEnv(self, index, name):
        return self.dm.GetEnv(index, name)

    def SetEnv(self, index, name, value):
        return self.dm.SetEnv(index, name, value)

    def SendString(self, hwnd, str):
        return self.dm.SendString(hwnd, str)

    def DelEnv(self, index, name):
        return self.dm.DelEnv(index, name)

    def GetPath(self):
        return self.dm.GetPath()

    def SetDict(self, index, dict_name):
        return self.dm.SetDict(index, dict_name)

    def FindPic(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir):
        return self.dm.FindPic(x1, y1, x2, y2, pic_name, delta_color, sim, dir)

    def FindPicEx(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir):
        return self.dm.FindPicEx(x1, y1, x2, y2, pic_name, delta_color, sim, dir)

    def SetClientSize(self, hwnd, width, height):
        return self.dm.SetClientSize(hwnd, width, height)

    def ReadInt(self, hwnd, addr, type):
        return self.dm.ReadInt(hwnd, addr, type)

    def ReadFloat(self, hwnd, addr):
        return self.dm.ReadFloat(hwnd, addr)

    def ReadDouble(self, hwnd, addr):
        return self.dm.ReadDouble(hwnd, addr)

    def FindInt(self, hwnd, addr_range, int_value_min, int_value_max, type):
        return self.dm.FindInt(hwnd, addr_range, int_value_min, int_value_max, type)

    def FindFloat(self, hwnd, addr_range, float_value_min, float_value_max):
        return self.dm.FindFloat(hwnd, addr_range, float_value_min, float_value_max)

    def FindDouble(self, hwnd, addr_range, double_value_min, double_value_max):
        return self.dm.FindDouble(hwnd, addr_range, double_value_min, double_value_max)

    def FindString(self, hwnd, addr_range, string_value, type):
        return self.dm.FindString(hwnd, addr_range, string_value, type)

    def GetModuleBaseAddr(self, hwnd, module_name):
        return self.dm.GetModuleBaseAddr(hwnd, module_name)

    def MoveToEx(self, x, y, w, h):
        return self.dm.MoveToEx(x, y, w, h)

    def MatchPicName(self, pic_name):
        return self.dm.MatchPicName(pic_name)

    def AddDict(self, index, dict_info):
        return self.dm.AddDict(index, dict_info)

    def EnterCri(self):
        return self.dm.EnterCri()

    def LeaveCri(self):
        return self.dm.LeaveCri()

    def WriteInt(self, hwnd, addr, type, v):
        return self.dm.WriteInt(hwnd, addr, type, v)

    def WriteFloat(self, hwnd, addr, v):
        return self.dm.WriteFloat(hwnd, addr, v)

    def WriteDouble(self, hwnd, addr, v):
        return self.dm.WriteDouble(hwnd, addr, v)

    def WriteString(self, hwnd, addr, type, v):
        return self.dm.WriteString(hwnd, addr, type, v)

    def AsmAdd(self, asm_ins):
        return self.dm.AsmAdd(asm_ins)

    def AsmClear(self):
        return self.dm.AsmClear()

    def AsmCall(self, hwnd, mode):
        return self.dm.AsmCall(hwnd, mode)

    def FindMultiColor(self, x1, y1, x2, y2, first_color, offset_color, sim, dir):
        return self.dm.FindMultiColor(x1, y1, x2, y2, first_color, offset_color, sim, dir)

    def FindMultiColorEx(self, x1, y1, x2, y2, first_color, offset_color, sim, dir):
        return self.dm.FindMultiColorEx(x1, y1, x2, y2, first_color, offset_color, sim, dir)

    def Assemble(self, base_addr, is_64bit):
        return self.dm.Assemble(base_addr, is_64bit)

    def DisAssemble(self, asm_code, base_addr, is_64bit):
        return self.dm.DisAssemble(asm_code, base_addr, is_64bit)

    def SetWindowTransparent(self, hwnd, v):
        return self.dm.SetWindowTransparent(hwnd, v)

    def ReadData(self, hwnd, addr, len):
        return self.dm.ReadData(hwnd, addr, len)

    def WriteData(self, hwnd, addr, data):
        return self.dm.WriteData(hwnd, addr, data)

    def FindData(self, hwnd, addr_range, data):
        return self.dm.FindData(hwnd, addr_range, data)

    def SetPicPwd(self, pwd):
        return self.dm.SetPicPwd(pwd)

    def Log(self, info):
        return self.dm.Log(info)

    def FindStrE(self, x1, y1, x2, y2, str, color, sim):
        return self.dm.FindStrE(x1, y1, x2, y2, str, color, sim)

    def FindColorE(self, x1, y1, x2, y2, color, sim, dir):
        return self.dm.FindColorE(x1, y1, x2, y2, color, sim, dir)

    def FindPicE(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir):
        return self.dm.FindPicE(x1, y1, x2, y2, pic_name, delta_color, sim, dir)

    def FindMultiColorE(self, x1, y1, x2, y2, first_color, offset_color, sim, dir):
        return self.dm.FindMultiColorE(x1, y1, x2, y2, first_color, offset_color, sim, dir)

    def SetExactOcr(self, exact_ocr):
        return self.dm.SetExactOcr(exact_ocr)

    def ReadString(self, hwnd, addr, type, len):
        return self.dm.ReadString(hwnd, addr, type, len)

    def FoobarTextPrintDir(self, hwnd, dir):
        return self.dm.FoobarTextPrintDir(hwnd, dir)

    def OcrEx(self, x1, y1, x2, y2, color, sim):
        return self.dm.OcrEx(x1, y1, x2, y2, color, sim)

    def SetDisplayInput(self, mode):
        return self.dm.SetDisplayInput(mode)

    def GetTime(self):
        return self.dm.GetTime()

    def GetScreenWidth(self):
        return self.dm.GetScreenWidth()

    def GetScreenHeight(self):
        return self.dm.GetScreenHeight()

    def BindWindowEx(self, hwnd, display, mouse, keypad, public_desc, mode):
        return self.dm.BindWindowEx(hwnd, display, mouse, keypad, public_desc, mode)

    def GetDiskSerial(self, index):
        return self.dm.GetDiskSerial(index)

    def Md5(self, str):
        return self.dm.Md5(str)

    def GetMac(self):
        return self.dm.GetMac()

    def ActiveInputMethod(self, hwnd, id):
        return self.dm.ActiveInputMethod(hwnd, id)

    def CheckInputMethod(self, hwnd, id):
        return self.dm.CheckInputMethod(hwnd, id)

    def FindInputMethod(self, id):
        return self.dm.FindInputMethod(id)

    def GetCursorPos(self):
        return self.dm.GetCursorPos()

    def BindWindow(self, hwnd, display, mouse, keypad, mode):
        return self.dm.BindWindow(hwnd, display, mouse, keypad, mode)

    def FindWindow(self, class_name, title_name):
        return self.dm.FindWindow(class_name, title_name)

    def GetScreenDepth(self):
        return self.dm.GetScreenDepth()

    def SetScreen(self, width, height, depth):
        return self.dm.SetScreen(width, height, depth)

    def ExitOs(self, type):
        return self.dm.ExitOs(type)

    def GetDir(self, type):
        return self.dm.GetDir(type)

    def GetOsType(self):
        return self.dm.GetOsType()

    def FindWindowEx(self, parent, class_name, title_name):
        return self.dm.FindWindowEx(parent, class_name, title_name)

    def SetExportDict(self, index, dict_name):
        return self.dm.SetExportDict(index, dict_name)

    def GetCursorShape(self):
        return self.dm.GetCursorShape()

    def DownCpu(self, type, rate):
        return self.dm.DownCpu(type, rate)

    def GetCursorSpot(self):
        return self.dm.GetCursorSpot()

    def SendString2(self, hwnd, str):
        return self.dm.SendString2(hwnd, str)

    def FaqPost(self, server, handle, request_type, time_out):
        return self.dm.FaqPost(server, handle, request_type, time_out)

    def FaqFetch(self):
        return self.dm.FaqFetch()

    def FetchWord(self, x1, y1, x2, y2, color, word):
        return self.dm.FetchWord(x1, y1, x2, y2, color, word)

    def CaptureJpg(self, x1, y1, x2, y2, file, quality):
        return self.dm.CaptureJpg(x1, y1, x2, y2, file, quality)

    def FindStrWithFont(self, x1, y1, x2, y2, str, color, sim, font_name, font_size, flag):
        return self.dm.FindStrWithFont(x1, y1, x2, y2, str, color, sim, font_name, font_size, flag)

    def FindStrWithFontE(self, x1, y1, x2, y2, str, color, sim, font_name, font_size, flag):
        return self.dm.FindStrWithFontE(x1, y1, x2, y2, str, color, sim, font_name, font_size, flag)

    def FindStrWithFontEx(self, x1, y1, x2, y2, str, color, sim, font_name, font_size, flag):
        return self.dm.FindStrWithFontEx(x1, y1, x2, y2, str, color, sim, font_name, font_size, flag)

    def GetDictInfo(self, str, font_name, font_size, flag):
        return self.dm.GetDictInfo(str, font_name, font_size, flag)

    def SaveDict(self, index, file):
        return self.dm.SaveDict(index, file)

    def GetWindowProcessId(self, hwnd):
        return self.dm.GetWindowProcessId(hwnd)

    def GetWindowProcessPath(self, hwnd):
        return self.dm.GetWindowProcessPath(hwnd)

    def LockInput(self, lock):
        return self.dm.LockInput(lock)

    def GetPicSize(self, pic_name):
        return self.dm.GetPicSize(pic_name)

    def GetID(self):
        return self.dm.GetID()

    def CapturePng(self, x1, y1, x2, y2, file):
        return self.dm.CapturePng(x1, y1, x2, y2, file)

    def CaptureGif(self, x1, y1, x2, y2, file, delay, time):
        return self.dm.CaptureGif(x1, y1, x2, y2, file, delay, time)

    def ImageToBmp(self, pic_name, bmp_name):
        return self.dm.ImageToBmp(pic_name, bmp_name)

    def FindStrFast(self, x1, y1, x2, y2, str, color, sim):
        return self.dm.FindStrFast(x1, y1, x2, y2, str, color, sim)

    def FindStrFastEx(self, x1, y1, x2, y2, str, color, sim):
        return self.dm.FindStrFastEx(x1, y1, x2, y2, str, color, sim)

    def FindStrFastE(self, x1, y1, x2, y2, str, color, sim):
        return self.dm.FindStrFastE(x1, y1, x2, y2, str, color, sim)

    def EnableDisplayDebug(self, enable_debug):
        return self.dm.EnableDisplayDebug(enable_debug)

    def CapturePre(self, file):
        return self.dm.CapturePre(file)

    def RegEx(self, code, Ver, ip):
        return self.dm.RegEx(code, Ver, ip)

    def GetMachineCode(self):
        return self.dm.GetMachineCode()

    def SetClipboard(self, data):
        return self.dm.SetClipboard(data)

    def GetClipboard(self):
        return self.dm.GetClipboard()

    def GetNowDict(self):
        return self.dm.GetNowDict()

    def Is64Bit(self):
        return self.dm.Is64Bit()

    def GetColorNum(self, x1, y1, x2, y2, color, sim):
        return self.dm.GetColorNum(x1, y1, x2, y2, color, sim)

    def EnumWindowByProcess(self, process_name, title, class_name, filter):
        return self.dm.EnumWindowByProcess(process_name, title, class_name, filter)

    def GetDictCount(self, index):
        return self.dm.GetDictCount(index)

    def GetLastError(self):
        return self.dm.GetLastError()

    def GetNetTime(self):
        return self.dm.GetNetTime()

    def EnableGetColorByCapture(self, en):
        return self.dm.EnableGetColorByCapture(en)

    def CheckUAC(self):
        return self.dm.CheckUAC()

    def SetUAC(self, uac):
        return self.dm.SetUAC(uac)

    def DisableFontSmooth(self):
        return self.dm.DisableFontSmooth()

    def CheckFontSmooth(self):
        return self.dm.CheckFontSmooth()

    def SetDisplayAcceler(self, level):
        return self.dm.SetDisplayAcceler(level)

    def FindWindowByProcess(self, process_name, class_name, title_name):
        return self.dm.FindWindowByProcess(process_name, class_name, title_name)

    def FindWindowByProcessId(self, process_id, class_name, title_name):
        return self.dm.FindWindowByProcessId(process_id, class_name, title_name)

    def ReadIni(self, section, key, file):
        return self.dm.ReadIni(section, key, file)

    def WriteIni(self, section, key, v, file):
        return self.dm.WriteIni(section, key, v, file)

    def RunApp(self, path, mode):
        return self.dm.RunApp(path, mode)

    def delay(self, mis):
        return self.dm.delay(mis)

    def FindWindowSuper(self, spec1, flag1, type1, spec2, flag2, type2):
        return self.dm.FindWindowSuper(spec1, flag1, type1, spec2, flag2, type2)

    def ExcludePos(self, all_pos, type, x1, y1, x2, y2):
        return self.dm.ExcludePos(all_pos, type, x1, y1, x2, y2)

    def FindNearestPos(self, all_pos, type, x, y):
        return self.dm.FindNearestPos(all_pos, type, x, y)

    def SortPosDistance(self, all_pos, type, x, y):
        return self.dm.SortPosDistance(all_pos, type, x, y)

    def FindPicMem(self, x1, y1, x2, y2, pic_info, delta_color, sim, dir):
        return self.dm.FindPicMem(x1, y1, x2, y2, pic_info, delta_color, sim, dir)

    def FindPicMemEx(self, x1, y1, x2, y2, pic_info, delta_color, sim, dir):
        return self.dm.FindPicMemEx(x1, y1, x2, y2, pic_info, delta_color, sim, dir)

    def FindPicMemE(self, x1, y1, x2, y2, pic_info, delta_color, sim, dir):
        return self.dm.FindPicMemE(x1, y1, x2, y2, pic_info, delta_color, sim, dir)

    def AppendPicAddr(self, pic_info, addr, size):
        return self.dm.AppendPicAddr(pic_info, addr, size)

    def WriteFile(self, file, content):
        return self.dm.WriteFile(file, content)

    def Stop(self, id):
        return self.dm.Stop(id)

    def SetDictMem(self, index, addr, size):
        return self.dm.SetDictMem(index, addr, size)

    def GetNetTimeSafe(self):
        return self.dm.GetNetTimeSafe()

    def ForceUnBindWindow(self, hwnd):
        return self.dm.ForceUnBindWindow(hwnd)

    def ReadIniPwd(self, section, key, file, pwd):
        return self.dm.ReadIniPwd(section, key, file, pwd)

    def WriteIniPwd(self, section, key, v, file, pwd):
        return self.dm.WriteIniPwd(section, key, v, file, pwd)

    def DecodeFile(self, file, pwd):
        return self.dm.DecodeFile(file, pwd)

    def KeyDownChar(self, key_str):
        return self.dm.KeyDownChar(key_str)

    def KeyUpChar(self, key_str):
        return self.dm.KeyUpChar(key_str)

    def KeyPressChar(self, key_str):
        return self.dm.KeyPressChar(key_str)

    def KeyPressStr(self, key_str, delay):
        return self.dm.KeyPressStr(key_str, delay)

    def EnableKeypadPatch(self, en):
        return self.dm.EnableKeypadPatch(en)

    def EnableKeypadSync(self, en, time_out):
        return self.dm.EnableKeypadSync(en, time_out)

    def EnableMouseSync(self, en, time_out):
        return self.dm.EnableMouseSync(en, time_out)

    def DmGuard(self, en, type):
        return self.dm.DmGuard(en, type)

    def FaqCaptureFromFile(self, x1, y1, x2, y2, file, quality):
        return self.dm.FaqCaptureFromFile(x1, y1, x2, y2, file, quality)

    def FindIntEx(self, hwnd, addr_range, int_value_min, int_value_max, type, step, multi_thread, mode):
        return self.dm.FindIntEx(hwnd, addr_range, int_value_min, int_value_max, type, step, multi_thread, mode)

    def FindFloatEx(self, hwnd, addr_range, float_value_min, float_value_max, step, multi_thread, mode):
        return self.dm.FindFloatEx(hwnd, addr_range, float_value_min, float_value_max, step, multi_thread, mode)

    def FindDoubleEx(self, hwnd, addr_range, double_value_min, double_value_max, step, multi_thread, mode):
        return self.dm.FindDoubleEx(hwnd, addr_range, double_value_min, double_value_max, step, multi_thread, mode)

    def FindStringEx(self, hwnd, addr_range, string_value, type, step, multi_thread, mode):
        return self.dm.FindStringEx(hwnd, addr_range, string_value, type, step, multi_thread, mode)

    def FindDataEx(self, hwnd, addr_range, data, step, multi_thread, mode):
        return self.dm.FindDataEx(hwnd, addr_range, data, step, multi_thread, mode)

    def EnableRealMouse(self, en, mousedelay, mousestep):
        return self.dm.EnableRealMouse(en, mousedelay, mousestep)

    def EnableRealKeypad(self, en):
        return self.dm.EnableRealKeypad(en)

    def SendStringIme(self, str):
        return self.dm.SendStringIme(str)

    def FoobarDrawLine(self, hwnd, x1, y1, x2, y2, color, style, width):
        return self.dm.FoobarDrawLine(hwnd, x1, y1, x2, y2, color, style, width)

    def FindStrEx(self, x1, y1, x2, y2, str, color, sim):
        return self.dm.FindStrEx(x1, y1, x2, y2, str, color, sim)

    def IsBind(self, hwnd):
        return self.dm.IsBind(hwnd)

    def SetDisplayDelay(self, t):
        return self.dm.SetDisplayDelay(t)

    def GetDmCount(self):
        return self.dm.GetDmCount()

    def DisableScreenSave(self):
        return self.dm.DisableScreenSave()

    def DisablePowerSave(self):
        return self.dm.DisablePowerSave()

    def SetMemoryHwndAsProcessId(self, en):
        return self.dm.SetMemoryHwndAsProcessId(en)

    def FindShape(self, x1, y1, x2, y2, offset_color, sim, dir):
        return self.dm.FindShape(x1, y1, x2, y2, offset_color, sim, dir)

    def FindShapeE(self, x1, y1, x2, y2, offset_color, sim, dir):
        return self.dm.FindShapeE(x1, y1, x2, y2, offset_color, sim, dir)

    def FindShapeEx(self, x1, y1, x2, y2, offset_color, sim, dir):
        return self.dm.FindShapeEx(x1, y1, x2, y2, offset_color, sim, dir)

    def FindStrS(self, x1, y1, x2, y2, str, color, sim):
        return self.dm.FindStrS(x1, y1, x2, y2, str, color, sim)

    def FindStrExS(self, x1, y1, x2, y2, str, color, sim):
        return self.dm.FindStrExS(x1, y1, x2, y2, str, color, sim)

    def FindStrFastS(self, x1, y1, x2, y2, str, color, sim):
        return self.dm.FindStrFastS(x1, y1, x2, y2, str, color, sim)

    def FindStrFastExS(self, x1, y1, x2, y2, str, color, sim):
        return self.dm.FindStrFastExS(x1, y1, x2, y2, str, color, sim)

    def FindPicS(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir):
        return self.dm.FindPicS(x1, y1, x2, y2, pic_name, delta_color, sim, dir)

    def FindPicExS(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir):
        return self.dm.FindPicExS(x1, y1, x2, y2, pic_name, delta_color, sim, dir)

    def ClearDict(self, index):
        return self.dm.ClearDict(index)

    def GetMachineCodeNoMac(self):
        return self.dm.GetMachineCodeNoMac()

    def GetClientRect(self, hwnd):
        return self.dm.GetClientRect(hwnd)

    def EnableFakeActive(self, en):
        return self.dm.EnableFakeActive(en)

    def GetScreenDataBmp(self, x1, y1, x2, y2):
        return self.dm.GetScreenDataBmp(x1, y1, x2, y2)

    def EncodeFile(self, file, pwd):
        return self.dm.EncodeFile(file, pwd)

    def GetCursorShapeEx(self, type):
        return self.dm.GetCursorShapeEx(type)

    def FaqCancel(self):
        return self.dm.FaqCancel()

    def IntToData(self, int_value, type):
        return self.dm.IntToData(int_value, type)

    def FloatToData(self, float_value):
        return self.dm.FloatToData(float_value)

    def DoubleToData(self, double_value):
        return self.dm.DoubleToData(double_value)

    def StringToData(self, string_value, type):
        return self.dm.StringToData(string_value, type)

    def SetMemoryFindResultToFile(self, file):
        return self.dm.SetMemoryFindResultToFile(file)

    def EnableBind(self, en):
        return self.dm.EnableBind(en)

    def SetSimMode(self, mode):
        return self.dm.SetSimMode(mode)

    def LockMouseRect(self, x1, y1, x2, y2):
        return self.dm.LockMouseRect(x1, y1, x2, y2)

    def SendPaste(self, hwnd):
        return self.dm.SendPaste(hwnd)

    def IsDisplayDead(self, x1, y1, x2, y2, t):
        return self.dm.IsDisplayDead(x1, y1, x2, y2, t)

    def GetKeyState(self, vk):
        return self.dm.GetKeyState(vk)

    def CopyFile(self, src_file, dst_file, over):
        return self.dm.CopyFile(src_file, dst_file, over)

    def IsFileExist(self, file):
        return self.dm.IsFileExist(file)

    def DeleteFile(self, file):
        return self.dm.DeleteFile(file)

    def MoveFile(self, src_file, dst_file):
        return self.dm.MoveFile(src_file, dst_file)

    def CreateFolder(self, folder_name):
        return self.dm.CreateFolder(folder_name)

    def DeleteFolder(self, folder_name):
        return self.dm.DeleteFolder(folder_name)

    def GetFileLength(self, file):
        return self.dm.GetFileLength(file)

    def ReadFile(self, file):
        return self.dm.ReadFile(file)

    def WaitKey(self, key_code, time_out):
        return self.dm.WaitKey(key_code, time_out)

    def DeleteIni(self, section, key, file):
        return self.dm.DeleteIni(section, key, file)

    def DeleteIniPwd(self, section, key, file, pwd):
        return self.dm.DeleteIniPwd(section, key, file, pwd)

    def EnableSpeedDx(self, en):
        return self.dm.EnableSpeedDx(en)

    def EnableIme(self, en):
        return self.dm.EnableIme(en)

    def Reg(self, code, Ver):
        return self.dm.Reg(code, Ver)

    def SelectFile(self):
        return self.dm.SelectFile()

    def SelectDirectory(self):
        return self.dm.SelectDirectory()

    def LockDisplay(self, lock):
        return self.dm.LockDisplay(lock)

    def FoobarSetSave(self, hwnd, file, en, header):
        return self.dm.FoobarSetSave(hwnd, file, en, header)

    def EnumWindowSuper(self, spec1, flag1, type1, spec2, flag2, type2, sort):
        return self.dm.EnumWindowSuper(spec1, flag1, type1, spec2, flag2, type2, sort)

    def DownloadFile(self, url, save_file, timeout):
        return self.dm.DownloadFile(url, save_file, timeout)

    def EnableKeypadMsg(self, en):
        return self.dm.EnableKeypadMsg(en)

    def EnableMouseMsg(self, en):
        return self.dm.EnableMouseMsg(en)

    def RegNoMac(self, code, Ver):
        return self.dm.RegNoMac(code, Ver)

    def RegExNoMac(self, code, Ver, ip):
        return self.dm.RegExNoMac(code, Ver, ip)

    def SetEnumWindowDelay(self, delay):
        return self.dm.SetEnumWindowDelay(delay)

    def FindMulColor(self, x1, y1, x2, y2, color, sim):
        return self.dm.FindMulColor(x1, y1, x2, y2, color, sim)

    def GetDict(self, index, font_index):
        return self.dm.GetDict(index, font_index)

    def GetBindWindow(self):
        return self.dm.GetBindWindow()

    def FoobarStartGif(self, hwnd, x, y, pic_name, repeat_limit, delay):
        return self.dm.FoobarStartGif(hwnd, x, y, pic_name, repeat_limit, delay)

    def FoobarStopGif(self, hwnd, x, y, pic_name):
        return self.dm.FoobarStopGif(hwnd, x, y, pic_name)

    def FreeProcessMemory(self, hwnd):
        return self.dm.FreeProcessMemory(hwnd)

    def ReadFileData(self, file, start_pos, end_pos):
        return self.dm.ReadFileData(file, start_pos, end_pos)

    def VirtualAllocEx(self, hwnd, addr, size, type):
        return self.dm.VirtualAllocEx(hwnd, addr, size, type)

    def VirtualFreeEx(self, hwnd, addr):
        return self.dm.VirtualFreeEx(hwnd, addr)

    def GetCommandLine(self, hwnd):
        return self.dm.GetCommandLine(hwnd)

    def TerminateProcess(self, pid):
        return self.dm.TerminateProcess(pid)

    def GetNetTimeByIp(self, ip):
        return self.dm.GetNetTimeByIp(ip)

    def EnumProcess(self, name):
        return self.dm.EnumProcess(name)

    def GetProcessInfo(self, pid):
        return self.dm.GetProcessInfo(pid)

    def ReadIntAddr(self, hwnd, addr, type):
        return self.dm.ReadIntAddr(hwnd, addr, type)

    def ReadDataAddr(self, hwnd, addr, len):
        return self.dm.ReadDataAddr(hwnd, addr, len)

    def ReadDoubleAddr(self, hwnd, addr):
        return self.dm.ReadDoubleAddr(hwnd, addr)

    def ReadFloatAddr(self, hwnd, addr):
        return self.dm.ReadFloatAddr(hwnd, addr)

    def ReadStringAddr(self, hwnd, addr, type, len):
        return self.dm.ReadStringAddr(hwnd, addr, type, len)

    def WriteDataAddr(self, hwnd, addr, data):
        return self.dm.WriteDataAddr(hwnd, addr, data)

    def WriteDoubleAddr(self, hwnd, addr, v):
        return self.dm.WriteDoubleAddr(hwnd, addr, v)

    def WriteFloatAddr(self, hwnd, addr, v):
        return self.dm.WriteFloatAddr(hwnd, addr, v)

    def WriteIntAddr(self, hwnd, addr, type, v):
        return self.dm.WriteIntAddr(hwnd, addr, type, v)

    def WriteStringAddr(self, hwnd, addr, type, v):
        return self.dm.WriteStringAddr(hwnd, addr, type, v)

    def Delays(self, min_s, max_s):
        return self.dm.Delays(min_s, max_s)

    def FindColorBlock(self, x1, y1, x2, y2, color, sim, count, width, height):
        return self.dm.FindColorBlock(x1, y1, x2, y2, color, sim, count, width, height)

    def FindColorBlockEx(self, x1, y1, x2, y2, color, sim, count, width, height):
        return self.dm.FindColorBlockEx(x1, y1, x2, y2, color, sim, count, width, height)

    def OpenProcess(self, pid):
        return self.dm.OpenProcess(pid)

    def EnumIniSection(self, file):
        return self.dm.EnumIniSection(file)

    def EnumIniSectionPwd(self, file, pwd):
        return self.dm.EnumIniSectionPwd(file, pwd)

    def EnumIniKey(self, section, file):
        return self.dm.EnumIniKey(section, file)

    def EnumIniKeyPwd(self, section, file, pwd):
        return self.dm.EnumIniKeyPwd(section, file, pwd)

    def SwitchBindWindow(self, hwnd):
        return self.dm.SwitchBindWindow(hwnd)

    def InitCri(self):
        return self.dm.InitCri()

    def SendStringIme2(self, hwnd, str, mode):
        return self.dm.SendStringIme2(hwnd, str, mode)

    def EnumWindowByProcessId(self, pid, title, class_name, filter):
        return self.dm.EnumWindowByProcessId(pid, title, class_name, filter)

    def GetDisplayInfo(self):
        return self.dm.GetDisplayInfo()

    def EnableFontSmooth(self):
        return self.dm.EnableFontSmooth()

    def OcrExOne(self, x1, y1, x2, y2, color, sim):
        return self.dm.OcrExOne(x1, y1, x2, y2, color, sim)

    def SetAero(self, en):
        return self.dm.SetAero(en)

    def FoobarSetTrans(self, hwnd, trans, color, sim):
        return self.dm.FoobarSetTrans(hwnd, trans, color, sim)

    def EnablePicCache(self, en):
        return self.dm.EnablePicCache(en)

    def FaqIsPosted(self):
        return self.dm.FaqIsPosted()

    def LoadPicByte(self, addr, size, name):
        return self.dm.LoadPicByte(addr, size, name)

    def MiddleDown(self):
        return self.dm.MiddleDown()

    def MiddleUp(self):
        return self.dm.MiddleUp()

    def FaqCaptureString(self, str):
        return self.dm.FaqCaptureString(str)

    def VirtualProtectEx(self, hwnd, addr, size, type, old_protect):
        return self.dm.VirtualProtectEx(hwnd, addr, size, type, old_protect)

    def SetMouseSpeed(self, speed):
        return self.dm.SetMouseSpeed(speed)

    def GetMouseSpeed(self):
        return self.dm.GetMouseSpeed()

    def EnableMouseAccuracy(self, en):
        return self.dm.EnableMouseAccuracy(en)

    def SetExcludeRegion(self, type, info):
        return self.dm.SetExcludeRegion(type, info)

    def EnableShareDict(self, en):
        return self.dm.EnableShareDict(en)

    def DisableCloseDisplayAndSleep(self):
        return self.dm.DisableCloseDisplayAndSleep()

    def Int64ToInt32(self, v):
        return self.dm.Int64ToInt32(v)

    def GetLocale(self):
        return self.dm.GetLocale()

    def SetLocale(self):
        return self.dm.SetLocale()

    def ReadDataToBin(self, hwnd, addr, len):
        return self.dm.ReadDataToBin(hwnd, addr, len)

    def WriteDataFromBin(self, hwnd, addr, data, len):
        return self.dm.WriteDataFromBin(hwnd, addr, data, len)

    def ReadDataAddrToBin(self, hwnd, addr, len):
        return self.dm.ReadDataAddrToBin(hwnd, addr, len)

    def WriteDataAddrFromBin(self, hwnd, addr, data, len):
        return self.dm.WriteDataAddrFromBin(hwnd, addr, data, len)

    def SetParam64ToPointer(self):
        return self.dm.SetParam64ToPointer()

    def GetDPI(self):
        return self.dm.GetDPI()

    def SetDisplayRefreshDelay(self, t):
        return self.dm.SetDisplayRefreshDelay(t)

    def IsFolderExist(self, folder):
        return self.dm.IsFolderExist(folder)

    def GetCpuType(self):
        return self.dm.GetCpuType()

    def ReleaseRef(self):
        return self.dm.ReleaseRef()

    def SetExitThread(self, en):
        return self.dm.SetExitThread(en)

    def GetFps(self):
        return self.dm.GetFps()

    def VirtualQueryEx(self, hwnd, addr, pmbi):
        return self.dm.VirtualQueryEx(hwnd, addr, pmbi)

    def AsmCallEx(self, hwnd, mode, base_addr):
        return self.dm.AsmCallEx(hwnd, mode, base_addr)

    def GetRemoteApiAddress(self, hwnd, base_addr, fun_name):
        return self.dm.GetRemoteApiAddress(hwnd, base_addr, fun_name)

    def ExecuteCmd(self, cmd, current_dir, time_out):
        return self.dm.ExecuteCmd(cmd, current_dir, time_out)

    def SpeedNormalGraphic(self, en):
        return self.dm.SpeedNormalGraphic(en)

    def UnLoadDriver(self):
        return self.dm.UnLoadDriver()

    def GetOsBuildNumber(self):
        return self.dm.GetOsBuildNumber()

    def HackSpeed(self, rate):
        return self.dm.HackSpeed(rate)

    def GetRealPath(self, path):
        return self.dm.GetRealPath(path)

    def ShowTaskBarIcon(self, hwnd, is_show):
        return self.dm.ShowTaskBarIcon(hwnd, is_show)

    def AsmSetTimeout(self, time_out, param):
        return self.dm.AsmSetTimeout(time_out, param)

    def DmGuardParams(self, cmd, sub_cmd, param):
        return self.dm.DmGuardParams(cmd, sub_cmd, param)

    def GetModuleSize(self, hwnd, module_name):
        return self.dm.GetModuleSize(hwnd, module_name)

    def IsSurrpotVt(self):
        return self.dm.IsSurrpotVt()

    def GetDiskModel(self, index):
        return self.dm.GetDiskModel(index)

    def GetDiskReversion(self, index):
        return self.dm.GetDiskReversion(index)

    def EnableFindPicMultithread(self, en):
        return self.dm.EnableFindPicMultithread(en)

    def GetCpuUsage(self):
        return self.dm.GetCpuUsage()

    def GetMemoryUsage(self):
        return self.dm.GetMemoryUsage()

    def Hex32(self, v):
        return self.dm.Hex32(v)

    def Hex64(self, v):
        return self.dm.Hex64(v)

    def GetWindowThreadId(self, hwnd):
        return self.dm.GetWindowThreadId(hwnd)

    def DmGuardExtract(self, type, path):
        return self.dm.DmGuardExtract(type, path)

    def DmGuardLoadCustom(self, type, path):
        return self.dm.DmGuardLoadCustom(type, path)

    def SetShowAsmErrorMsg(self, show):
        return self.dm.SetShowAsmErrorMsg(show)

    def GetSystemInfo(self, type, method):
        return self.dm.GetSystemInfo(type, method)

    def SetFindPicMultithreadCount(self, count):
        return self.dm.SetFindPicMultithreadCount(count)

    def FindPicSim(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir):
        return self.dm.FindPicSim(x1, y1, x2, y2, pic_name, delta_color, sim, dir)

    def FindPicSimEx(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir):
        return self.dm.FindPicSimEx(x1, y1, x2, y2, pic_name, delta_color, sim, dir)

    def FindPicSimMem(self, x1, y1, x2, y2, pic_info, delta_color, sim, dir):
        return self.dm.FindPicSimMem(x1, y1, x2, y2, pic_info, delta_color, sim, dir)

    def FindPicSimMemEx(self, x1, y1, x2, y2, pic_info, delta_color, sim, dir):
        return self.dm.FindPicSimMemEx(x1, y1, x2, y2, pic_info, delta_color, sim, dir)

    def FindPicSimE(self, x1, y1, x2, y2, pic_name, delta_color, sim, dir):
        return self.dm.FindPicSimE(x1, y1, x2, y2, pic_name, delta_color, sim, dir)

    def FindPicSimMemE(self, x1, y1, x2, y2, pic_info, delta_color, sim, dir):
        return self.dm.FindPicSimMemE(x1, y1, x2, y2, pic_info, delta_color, sim, dir)

    def SetInputDm(self, input_dm, rx, ry):
        return self.dm.SetInputDm(input_dm, rx, ry)

        
        

if __name__ == "__main__":
    m_dm = DM()
    print(m_dm.Reg('xxxx','xxx'))
        
    
    