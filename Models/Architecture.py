import torch
import torch.nn as nn
import torchvision.models as models

class ResNet50Classifier(nn.Module):
    def __init__(self, num_classes=2, pretrained=True):
        super(ResNet50Classifier, self).__init__()

        # Charger le modèle ResNet-50 pré-entraîné sur ImageNet
        self.backbone = models.resnet50(pretrained=pretrained)

        # Remplacer la dernière couche entièrement connectée (fc) par une nouvelle adaptée au nombre de classes
        self.backbone.fc = nn.Linear(in_features=self.backbone.fc.in_features,
                                     out_features=num_classes)

    def forward(self, x):
        return self.backbone(x)

# Test rapide du modèle (facultatif)
if __name__ == "__main__":
    model = ResNet50Classifier(num_classes=3)
    print(model)

    # Dummy input (batch de 4 images RGB 224x224)
    x = torch.randn(4, 3, 224, 224)
    output = model(x)

    print("Shape de sortie :", output.shape)  # Doit être [4, 3] si num_classes=3
