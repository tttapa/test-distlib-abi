import distlib.wheel
print("distlib:  ", distlib.wheel.ABI)
import packaging.tags
print("packaging:", next(packaging.tags.sys_tags()).abi)
