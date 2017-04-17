# Determine Winner and winning lead

max_lead = -1
out_lead = 0
a, b = 0, 0
for _ in range(int(raw_input().strip())):
    p1, p2 = map(int, raw_input().split())
    a += p1
    b += p2
    lead = a - b
    if abs(lead) > max_lead:
        max_lead = abs(lead)
        out_lead = lead
if out_lead < 0:
    print("2 %d" % -out_lead)
else:
    print("1 %d" % out_lead)

