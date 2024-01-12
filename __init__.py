import os
import sys
sys.path.append(os.path.dirname(__file__))
from fooocus import  FooocusKSampler




NODE_CLASS_MAPPINGS = {
    "Fooocus_KSample": FooocusKSampler,

}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SDXLPromptStyler": "Fooocus KSample",
}


__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

print("\033[0m\033[95mFooocus采样器\033[0m \033[32m加载成功，有bug请及时反馈！！\033[0m")