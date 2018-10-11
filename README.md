# GuiGenerateTestIVRConfig
## 由来
每次联调接口需要配置TestIVR的配置文件，每次都很麻烦，像这次联调200+个接口，简直要疯，用python写了一个gui的工具，可以提高工作效率

## 打包
```shell
pyinstaller -F -i config.ico -w GUI_generateTestIVRConf.py
```