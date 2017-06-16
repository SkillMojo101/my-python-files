##This is just a prototype demonstration of how a simple
##personal assisstant is built, with the aid of two modules
##(wolfram module and wikipedia module).
##Most of the code is just GUI with the wxPython library.

import wx
import wikipedia
import wolframalpha

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, pos=wx.DefaultPosition, size=wx.Size(450, 110), 
        style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN,
        title="PyA")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel, label="Hello, I am PyA! Your SLOW Personal Assistant. How can I help?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400, 30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()
        
    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        #print "OnEnter"
        try:
            #Wolfram
            app_id = "J8URQW-98EAUPHG7G"
            client = wolframalpha.Client(app_id)
            res = client.query(input)
            answer = next(res.results).text
            print answer

        except:
            #Wiki
            #input.split(' ') #split by spaces
            #input = " ".join(input[2:]) #rejoin except for the first two words
            print wikipedia.summary(input)#, sentences = 2)
            
if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
