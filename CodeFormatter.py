import os
import sys
import subprocess
import time
import pyautogui


def autoFormatTheCode(fileName):
    pyautogui.press('shiftleft')
    pyautogui.press('shiftleft')
    pyautogui.write(fileName)
    time.sleep(1)

    pyautogui.press('return')
    time.sleep(1)
    pyautogui.hotkey('optionleft', 'command', 'l')
    time.sleep(1)
    pyautogui.press('return')


def runKtlintFix(fileName):
    subprocess.run(["ktlint", "-F", fileName])
    pyautogui.hotkey('command', 'w')


try:
    inputFileName = sys.argv[1]
    time.sleep(3)
    for root, dirs, files in os.walk(inputFileName):
        for file in files:
            if (".java" in file):
                fileName = os.path.join(root, file)
                print("Started optimising on " + fileName)
                time.sleep(1)
                autoFormatTheCode(fileName)

            elif (".kt" in file):
                fileName = os.path.join(root, file)
                print("Started optimising on " + fileName)
                time.sleep(1)
                autoFormatTheCode(fileName)
                runKtlintFix(fileName)
except:
    print("Missing or wrong path")
