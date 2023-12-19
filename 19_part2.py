test = """\
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}\
"""

import copy

input = open("19.txt").read()

workflows= [[line.split("{") for line in lines.split("\n")] for lines in input.split("\n\n")][0]

workflows = {line[0]: line[1][:-1].split(",") for line in workflows}

start_parts = {"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}

result = 0
queue = [["in", start_parts]]
while queue:
    workflow_name, parts = queue.pop(0)

    if workflow_name == "A":        
        result += (parts['x'][1] - parts['x'][0] + 1) * \
                  (parts['m'][1] - parts['m'][0] + 1) * \
                  (parts['a'][1] - parts['a'][0] + 1) * \
                  (parts['s'][1] - parts['s'][0] + 1)
        continue
    
    if workflow_name == "R":
        continue

    for rule in workflows[workflow_name][:-1]:
        test, sendto = rule.split(":")
        part = parts[test[0]]
        part_lower = part[0]
        part_upper = part[1]
        cutoff = int(test[2:])
        if test[1] == "<":
            # Purely below cutoff
            if part_upper < cutoff:
                # Put back into queue with the new workflow
                queue.append([sendto, parts])
                break
            
            # Half below half above
            elif part_lower < cutoff and part_upper >= cutoff:
                new_parts = copy.deepcopy(parts)
                new_parts[test[0]] = [part_lower, cutoff - 1]
                parts[test[0]] = [cutoff, part_upper]
                queue.append([sendto, new_parts])
        else:
            # Purely above cutoff
            if part_lower > cutoff:
                # Put right back into queue with the new workflow
                queue.append([sendto, parts])
                break
            
            # Half below half above
            elif part_lower <= cutoff and part_upper > cutoff:
                new_parts = copy.deepcopy(parts)
                new_parts[test[0]] = [cutoff + 1, part_upper]
                parts[test[0]] = [part_lower, cutoff]
                queue.append([sendto, new_parts])
    else:
        # If the loop didn't break (i.e. if some part of the original parts never got sent away)
        queue.append([workflows[workflow_name][-1], parts])

print(result)   
