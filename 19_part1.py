input = open("19.txt").read()
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

workflows, parts = [lines.split("\n") for lines in input.split("\n\n")]

x, m, a, s = list("xmas")
parts = [eval(part.replace("=", ":")) for part in parts]
workflows = {line.split("{")[0]: line.split("{")[1][:-1].split(",") for line in workflows}

def consider(workflow, part):
    for rule in workflow[:-1]:
        test, result = rule.split(":")
        if eval(f"{part[test[0]]}{test[1:]}"):
            return result
    
    return workflow[-1]

print

result = 0
for part in parts:
    cur_workflow_name = "in"
    while cur_workflow_name != "R" and cur_workflow_name != "A":
        cur_workflow_name = consider(workflows[cur_workflow_name], part)
    if cur_workflow_name == "A":
        result += sum(part.values())

print(result)   
