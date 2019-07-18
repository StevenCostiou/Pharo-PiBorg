#!/usr/bin/env python
import PicoBorgRev
import sys

PBR = PicoBorgRev.PicoBorgRev()
PBR.Init()
PBR.ResetEpo()

power = float(sys.argv[1])
addr = int(sys.argv[2])

sys.stdout.write(str(power) + " " + str(addr))

try:
        if addr == 1:
                sys.stdout.write("power to motor 1")
                PBR.SetMotor1(power)
        
        if addr == 2:
                sys.stdout.write("power to motor 2")
                PBR.SetMotor2(power)
except err:
        sys.stdout.write(str(err))

