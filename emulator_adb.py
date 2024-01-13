import os,time
try:
 import threading,subprocess,base64,cv2,random
 import numpy as np
except:
  os.system("pip install --force-reinstall --no-cache opencv-python==4.5.5.64")
  os.system("pip install numpy")
import threading,subprocess,base64,cv2,random
import numpy as np
from datetime import datetime
from com.dtmilano.android.viewclient import ViewClient


class Auto:
    def __init__(self,handle):
        self.handle = handle
    def screen_capture(self,name):
        os.system(f"adb -s {self.handle} exec-out screencap -p > {name}.png ")
    def click(self,x,y):
        os.system(f"adb -s {self.handle} shell input tap {x} {y}")
    def find(self,img='',template_pic_name=False,threshold=0.99):
        if template_pic_name == False:
            self.screen_capture(self.handle)
            template_pic_name = self.handle+'.png'
        else:
            self.screen_capture(template_pic_name)
        img = cv2.imread(img)
        img2 = cv2.imread(template_pic_name)
        result = cv2.matchTemplate(img,img2,cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)
        test_data = list(zip(*loc[::-1]))
        return test_data
    def sendText(self, text: str) -> None:
        os.system(f"adb -s {self.handle} shell input text '{text}'")
    def deleteText(self) -> None:
        os.system(f"adb -s {self.handle} shell input keyevent KEYCODE_DEL")
    def enter(self) -> None:
        os.system(f"adb -s {self.handle} shell input keyevent 66")

def GetDevices():
        devices = subprocess.check_output("adb devices")
        p = str(devices).replace("b'List of devices attached","").replace('\\r\\n',"").replace(" ","").replace("'","").replace('b*daemonnotrunning.startingitnowonport5037**daemonstartedsuccessfully*Listofdevicesattached',"")
        if len(p) > 0:
            listDevices = p.split("\\tdevice")
            listDevices.pop()
            return listDevices
        else:
            return 0
        
class EmulatorWorker(threading.Thread):
    def __init__(self, device_name: str, proxy: str) -> None:
        super().__init__()
        self.device = device_name
        self.proxy = proxy

    def config_proxy(self, adb_auto: Auto, locating_img_path: str) -> None:
        proxy = self.proxy.split(":")
        print(proxy)
        while True:
            try:
                point = adb_auto.find(locating_img_path)
                if point > [(0,0)]:
                    adb_auto.click(point[0][0], point[0][1])
                    time.sleep(5)
                    point_2 = adb_auto.find("./images/proxy-host-label.png")
                    point_3 = adb_auto.find("./images/proxy-port-label.png")
                    point_4 = adb_auto.find("./images/proxy-username-label.png")
                    point_5 = adb_auto.find("./images/proxy-password-label.png")
                    point_6 = adb_auto.find("./images/start-proxy.png")
                    if point_2 > [(0,0)]:
                        adb_auto.click(point_2[0][0]+348, point_2[0][1])
                        adb_auto.click(point_2[0][0]+348, point_2[0][1])
                        adb_auto.deleteText()
                        time.sleep(0.5)
                        adb_auto.sendText(proxy[0])
                        time.sleep(1)
                    if point_3 > [(0,0)]:
                        adb_auto.click(point_3[0][0]+348, point_3[0][1])
                        adb_auto.click(point_3[0][0]+348, point_3[0][1])
                        adb_auto.deleteText()
                        time.sleep(0.5)
                        adb_auto.sendText(proxy[1])
                        time.sleep(1)
                    if point_4 > [(0,0)]:
                        adb_auto.click(point_4[0][0]+348, point_4[0][1])
                        adb_auto.click(point_4[0][0]+348, point_4[0][1])
                        adb_auto.deleteText()
                        time.sleep(0.5)
                        adb_auto.sendText(proxy[2])
                        time.sleep(1)
                    if point_5 > [(0,0)]:
                        adb_auto.click(point_5[0][0]+348, point_5[0][1])
                        adb_auto.click(point_5[0][0]+348, point_5[0][1])
                        adb_auto.deleteText()
                        time.sleep(0.5)
                        adb_auto.sendText(proxy[3])
                        time.sleep(1)
                    if point_6 > [(0,0)]:
                        adb_auto.click(point_6[0][0], point_6[0][1])
                        time.sleep(3)
                        point_7 = adb_auto.find("./images/start-proxy-service.png")
                        print('point_7', point_7)
                        if point_7 > [(0,0)]:
                            print(point_7)
                            adb_auto.click(point_7[0][0], point_7[0][1])
                            time.sleep(1)
                    break
            except Exception as err:
                print("Lỗi khi config proxy:", err)


    def startApp(self, adb_auto: Auto, app_img_path: str) -> None:
        while True:
            try:
                img_point = adb_auto.find(app_img_path)
                if img_point > [(0,0)]:
                    adb_auto.click(img_point[0][0], img_point[0][1])
                break
            except Exception as e:
                print("Err", e)


    def searchLiveStream(self, adb_auto: Auto, search_img_path: str, page_name: str, live_tag_img_path_1: str, live_tag_img_path_2: str) -> bool:
        while True:
            try:
                img_point = adb_auto.find(search_img_path)
                print('img_point', img_point)
                print(search_img_path)
                if img_point > [(0,0)]:
                    adb_auto.click(img_point[0][0], img_point[0][1])

                    time.sleep(2)
                    adb_auto.sendText(page_name)
                    adb_auto.enter()

                    time.sleep(2)
                    live_img_point_1 = adb_auto.find(live_tag_img_path_1)
                    live_img_point_2 = adb_auto.find(live_tag_img_path_2)
                    print('live_img_point_1', live_img_point_1)
                    print('live_img_point_2', live_img_point_2)

                    # Because There are 2 live-image tags, need to check twice
                    if live_img_point_1 > [(0, 0)]:
                        adb_auto.click(live_img_point_1[0][0], live_img_point_1[0][1])
                        return True # Search livestream successfully!
                    if live_img_point_2 > [(0, 0)]:
                        adb_auto.click(live_img_point_2[0][0], live_img_point_2[0][1])
                        return True # Search livestream successfully!

            except Exception as e:
                print(e)
                return False
            
            return False
        
    def interactLiveStream(self, adb_auto: Auto, captcha_img_path: str) -> None:

        device, serialno = ViewClient.connectToDeviceOrExit()
        device.takeSnapshot().crop((100, 50, 500, 600)).save('./myscreencap.png', 'PNG')


        # count = 0
        # while True:
        #     captcha_img_point = adb_auto.find(captcha_img_path)
        #     if captcha_img_point > [(0, 0)]:
        #         print(f'Captcha xuất hiện khi count = {count}')
        #     count+=1


            

        #     # Check captcha appear every 10 seconds
        #     time.sleep(10)

    def run(self):
        try:
            adb_auto = Auto(self.device)

            proxy_app_path = "./images/proxy-app-1.png"

            print('--------------------')
            print(f"Device {self.device} started")

            # Config proxy for the emulator
            self.config_proxy(adb_auto, proxy_app_path)
            time.sleep(2)

            

        except Exception as e:
            print(e)
    
def start_worker(worker_index, proxy):
    time.sleep(0.5)
    device_name = GetDevices()[worker_index]    
    worker = EmulatorWorker(device_name, proxy)
    worker.run()

def main():
    thread_count = len(GetDevices())
    print('thread_count', thread_count)

    proxies = []
    p_count = 0
    with open('./resources/proxy-101-200.txt') as f:
        proxies = f.read().split('\n')

    for i in range(thread_count):
        worker_index = i
        threading.Thread(target=start_worker, args=(worker_index, proxies[p_count])).start()
        p_count += 1

if __name__=="__main__": 
    main()