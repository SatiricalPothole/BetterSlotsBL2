import unrealsdk
from Mods import ModMenu
   
class BetterSlots(ModMenu.SDKMod):
    Name: str = "BetterSlotsBL2"
    Author: str = "SatiricalPothole"
    Description: str = "A mod to make slots easier and more fun to use, roll 10 times simultaneously or use all your cash to roll as many time as you can in once go."
    Version: str = "1.0.0"
    SupportedGames: ModMenu.Game = ModMenu.Game.BL2
    Types: ModMenu.ModTypes = ModMenu.ModTypes.Utility
    SaveEnabledState: ModMenu.EnabledSaveType = ModMenu.EnabledSaveType.LoadWithSettings

def Enable(self) -> None:
    super().Enable()
    unrealsdk.Log("I ARISE!")

def Disable(self) -> None:  # noqa: N802
    unrealsdk.Log("I FALL!")
    super().Disable()
   
ModMenu.RegisterMod(BetterSlots())
