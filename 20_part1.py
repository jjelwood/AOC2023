input = open("20.txt").read()
test1 = """\
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a\
"""
test2 = """\
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output\
"""

modules = {}
pulses = []
rxs = 0

class Module:
    def __init__(self, func, name, outs):
        self.func = func
        self.name = name
        self.outs = outs
        self.recieveds = {}
        self.isOn = False
    
    def sendSignal(self, isHigh):
        for out in self.outs:
            if out in modules:
                modules[out].recieveds[self.name] = isHigh
            pulses.append((out, isHigh))
    
    def pulse(self, isHigh):
        if self.name == "rx" and not isHigh:
            rxs += 1
        if self.func == "%":
            if not isHigh:
                if self.isOn:
                    self.sendSignal(False)
                else:
                    self.sendSignal(True)
                self.isOn = not self.isOn
        elif self.func == "&":
            if all(self.recieveds.values()):
                self.sendSignal(False)
            else:
                self.sendSignal(True)

for line in input.split("\n"):
    info = line.replace(",", "").split()
    if line.startswith("broadcaster"):
        broadcast_pulses = [(name, False) for name in info[2:]]
        continue
    func = line[0]
    name = info[0][1:]
    outs = info[2:]
    modules[name] = Module(func, name, outs)

# Set up memory
for name, module in modules.items():
    for out in module.outs:
        if out in modules:
            modules[out].recieveds[name] = False

# lows = 0
# highs = 0
presses = 0

while rxs == 0:
    if presses % 100000 == 0:
        print(presses)
    # lows += 1
    pulses = broadcast_pulses.copy()
    while pulses:
        name, isHigh = pulses.pop(0)
        # if isHigh:
        #     highs += 1
        # else:
        #     lows += 1
        if name in modules:
            modules[name].pulse(isHigh)
    presses += 1

# print(lows * highs)
print(rxs)