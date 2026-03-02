
import ctypes
import os
import platform
import sys

class _2nd_stage:

    def set_wallpaper(self,image_path: str) -> bool:

        if platform.system() != "Windows":
            print("Wallpaper change is only supported on Windows.")
            return False

        if not os.path.isfile(image_path):
            print(f"Image not found: {image_path}")
            return False

        SPI_SETDESKWALLPAPER = 20
        SPIF_UPDATEINIFILE = 1
        SPIF_SENDCHANGE = 2

        result = ctypes.windll.user32.SystemParametersInfoW(
            SPI_SETDESKWALLPAPER,
            0,
            image_path,
            SPIF_UPDATEINIFILE | SPIF_SENDCHANGE
        )

        return bool(result)


    def main(self):
        # Example: wallpaper.jpg in same folder
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "wallpaper.jpg")

        success = self.set_wallpaper(image_path)

        if success:
            print("Demo payload executed: wallpaper changed.")
        else:
            print("Demo payload failed.")


if __name__ == "__main__":
    try:
        secstage = _2nd_stage()
        secstage.main()

    except Exception as e:
        print(f"Error : {e}")
        
    finally:    
        sys.exit()