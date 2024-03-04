import random, time

BAR = chr(9608)

def progressbar():
    bytesdownloaded = 0
    downloadsize = 4090
    while bytesdownloaded < downloadsize:
        bytesdownloaded += random.randint(0, 10)
        barstr = get_bar_str(bytesdownloaded, downloadsize)
        print(barstr, end="", flush=True)
        time.sleep(0.1)
        print('\b' * len(barstr), end='', flush=True)

def get_bar_str(progress, total, barSize=40):
    probar = ""
    probar += "["
    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    numberofbars = int((progress / total) * barSize)
    probar += BAR * numberofbars 
    probar += " " * (barSize - numberofbars)
    probar += "]"
    percent_complete = round(progress / total * 100, 1)
    probar += "  " + str(percent_complete) + "%"
    probar += " " + str(progress) + "/" + str(total)
    return probar

if __name__ == "__main__":
    progressbar()