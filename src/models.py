import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from efficientnet_pytorch import EfficientNet

from vit_pytorch.cait import CaiT
import _testimportmultiple
# from tlt.utils import load_pretrained_weights
import timm
import math


class BaseModel(nn.Module):
    def __init__(self, num_classes):
        super().__init__()

        self.conv1 = nn.Conv2d(3, 32, kernel_size=7, stride=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, stride=1)
        self.dropout1 = nn.Dropout(0.25)
        self.dropout2 = nn.Dropout(0.25)
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(128, num_classes)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)

        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)

        x = self.conv3(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout2(x)

        x = self.avgpool(x)
        x = x.view(-1, 128)
        return self.fc(x)

class pretrainedModel(nn.Module):
    def __init__(self, num_classes=18):
        super().__init__()

        self.net = timm.create_model('swin_base_patch4_window7_224', pretraind=True, num_classes=num_classes)
    
    def forward(self,x):
        x=self.net(x)

        return x

# Custom Model Template
class MyModel(nn.Module):
    def __init__(self, name, class_num, pretrained_path=None) -> None:
        self.name = name
        # super.__init__(self, name, class_num)
        super(MyModel, self).__init__()
        print("load model... class num is", class_num)
        if name == 'test':
            self.model = BaseModel(class_num)
        elif name == "swin":
            self.model = pretrainedModel(class_num)
        elif name == "renet18":
            self.model = torchvision.models.renet18(pretrained=True)
            self.model.fc = torch.nn.Linear(
                in_features=512, out_features=class_num, bias=True,
            )
        elif name == "mobilenetv2":
            self.model = timm.create_model('mobilenetv2_100', pretrained=True)
            # print(self.model)
            self.model.classifier = torch.nn.Linear(
                in_features=1280, out_features=class_num, bias=True
            )
            self.init_weight(self.model.classifier)
        elif name == "efficientnet-b0":
            self.model = EfficientNet.from_pretrained(
                "efficientnet-b0", num_classes=class_num
            )
        elif name == "efficientnet-b2":
            self.model = EfficientNet.from_pretrained(
                "efficientnet-b2", num_classes=class_num
            )
        elif name == "efficientnet-b4":
            self.model = EfficientNet.from_pretrained(
                "efficientnet-b4", num_classes=class_num
            )
            self.reset_parameters(self.model._fc)
        elif name == "efficientnet-b7":
            self.model = EfficientNet.from_pretrained(
                "efficientnet-b7", num_classes=class_num
            )
            self.reset_parameters(self.model._fc)
        elif name == "BiT":
            self.model = timm.create_model(
                "resnetv2_101x1_bitm", pretrained=True, num_classes=class_num,
            )
        elif name == 'ViT':
            self.model = timm.create_model('vit_base_patch16_224', pretrained=True, num_classes=class_num)
        elif name == "deit":
            self.model = torch.hub.load(
                "facebookresearch/deit:main",
                "deit_base_patch16_224",
                pretrained=True,
            )
            self.model.head = torch.nn.Linear(
                in_features=768, out_features=class_num, bias=True
            )
            torch.nn.init.xavier_normal_(self.model.head.weight)
            stdv = 1.0 / math.sqrt(self.model.head.weight.size(1))
            self.model.head.bias.data.uniform_(-stdv, stdv)
        elif name == "CaiT":
            # https://github.com/lucidrains/vit-pytorch
            self.model = CaiT(
                image_size=224,
                patch_size=32,
                num_classes=class_num,
                dim=1024,
                depth=12,  # depth of transformer for patch to patch attention only
                cls_depth=2,  # depth of cross attention of CLS tokens to patch
                heads=16,
                mlp_dim=2048,
                dropout=0.1,
                emb_dropout=0.1,
                layer_dropout=0.05,  # randomly dropout 5% of the layers
            )
        # elif name == 'NFNet-F1':
            # model_F1 = pretrained_nfnet('pretrained/F1_haiku.npz')
        if pretrained_path:
            self.model.load_state_dict(torch.load(pretrained_path))
            print('load custom pretrained model!!', pretrained_path)
        
        
    def reset_parameters(self, layer):
        bound = 1 / math.sqrt(layer.weight.size(1))
        torch.nn.init.xavier_uniform_(layer.weight)
        # torch.nn.init.uniform_(layer.weight, -bound, bound)
        if layer.bias is not None:
            torch.nn.init.uniform_(layer.bias, -bound, bound)
    

    def init_weight(self, layer):
        torch.nn.init.xavier_uniform_(layer.weight)
        stdv = 1.0 / math.sqrt(layer.weight.size(1))
        layer.bias.data.uniform_(-stdv, stdv)


# model = MyModel('CaiT',18)
# print(model)
# print(list(model.parameters()))
