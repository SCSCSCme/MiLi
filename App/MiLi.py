import wx
import os

def on_button_click(event):
    wx.MessageBox(message="You Click Button. Hello World!", caption='Info', style=wx.OK | wx.ICON_INFORMATION)

app=wx.App()
frame = wx.Frame(parent=None, title='Test', size=(1280, 720))

def on_new_project(event):
            dlg = wx.TextEntryDialog(
                frame,
                message="请输入项目文件夹名称：",
                caption="新建项目"
            )
                    
            if dlg.ShowModal() == wx.ID_OK:
                folder_name = dlg.GetValue().strip()
                if not folder_name:
                    wx.MessageBox("❌ 文件夹名称不能为空", "错误", wx.OK | wx.ICON_WARNING)
                    return

                try:
                    if os.path.exists(folder_name):
                        wx.MessageBox(f"❌ 文件夹已存在：{folder_name}", "错误", wx.OK | wx.ICON_ERROR)
                        return

                    os.makedirs(folder_name)
                    wx.MessageBox(f"✅ 项目文件夹已创建：\n{folder_name}", "成功", wx.OK | wx.ICON_INFORMATION)
                   
                    project_version = 1.0
                    with open(f'{folder_name}/pConfig.json', 'w') as file:
                        file.write('{\n')
                        file.write(f'    name: {folder_name},\n')
                        file.write(f'    version: {project_version}\n')
                        file.write('}')
                except Exception as e:
                    wx.MessageBox(f"❌ 创建失败：\n{str(e)}", "错误", wx.OK | wx.ICON_ERROR)
                    dlg.Destroy()

panel = wx.Panel(frame)

new_project = wx.Button(parent=panel, label='New Project')
new_project.Bind(wx.EVT_BUTTON, on_new_project)

box_sizer = wx.BoxSizer(wx.VERTICAL)
box_sizer.Add(new_project, 0, wx.ALL | wx.CENTER, 1)

panel.SetSizer(box_sizer)

frame.Centre()
frame.Show()
app.MainLoop()
