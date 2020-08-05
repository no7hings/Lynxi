# coding:utf-8
import imp

fn_, path, desc = imp.find_module('setup', [r'E:\myworkspace\td\lynxi\toolkit\windows\arnold_cmd_render\source'])

print fn_, path, desc

mod = imp.load_module('setup', fn_, path, desc)

print dir(mod)

mod.run()
