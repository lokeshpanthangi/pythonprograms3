
mon = {"user1", "user2", "user3", "user4", "user5"}
tue = {"user2", "user4", "user6", "user7", "user8"}
wed = {"user1", "user3", "user6", "user9", "user10"}

all_users = []
for u in mon:
    if u not in all_users:
        all_users.append(u)
for u in tue:
    if u not in all_users:
        all_users.append(u)
for u in wed:
    if u not in all_users:
        all_users.append(u)
print(f"Total unique visitors across all days: {len(all_users)}")


ret_tue = []
for u in tue:
    if u in mon:
        ret_tue.append(u)
print(f"Returning visitors on Tuesday: {sorted(ret_tue)}")

new_mon = []
for u in mon:
    new_mon.append(u)
new_tue = []
for u in tue:
    if u not in mon:
        new_tue.append(u)
new_wed = []
for u in wed:
    if u not in mon and u not in tue:
        new_wed.append(u)

print(f"New visitors on Monday: {sorted(new_mon)}")
print(f"New visitors on Tuesday: {sorted(new_tue)}")
print(f"New visitors on Wednesday: {sorted(new_wed)}")

loyal = []
for u in mon:
    if u in tue and u in wed:
        loyal.append(u)
print(f"Loyal visitors (all three days): {sorted(loyal)}")

overlap_mon_tue = []
for u in mon:
    if u in tue:
        overlap_mon_tue.append(u)
overlap_tue_wed = []
for u in tue:
    if u in wed:
        overlap_tue_wed.append(u)
overlap_mon_wed = []
for u in mon:
    if u in wed:
        overlap_mon_wed.append(u)
        
print(f"Overlap Monday-Tuesday: {sorted(overlap_mon_tue)}")
print(f"Overlap Tuesday-Wednesday: {sorted(overlap_tue_wed)}")
print(f"Overlap Monday-Wednesday: {sorted(overlap_mon_wed)}")
