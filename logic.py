subjects = []
i = 0
n = int(input("enter the number of subjects that you want to target : "))
while(i<n):
    sub_name = input(f"enter the name of subject {i+1} : ")
    subjects.append(sub_name)
    i+=1

print(subjects)

print("please enter the difficulty-level of each subject")
print("1 to 3 (3->hard and 1->easy)")
difficulty = []
i = 0
while(i<n):
    difficulty_level = int(input(f"enter the difficulty level of each subject{i+1} : "))
    difficulty.append(difficulty_level)
    i+=1

print(difficulty)

i = 0
sub_diffLevel = {}
while(i<n):
    sub_diffLv = {subjects[i] : difficulty[i]}
    sub_diffLevel.update(sub_diffLv)
    i+=1
print(sub_diffLevel)

sorted_sub_diffLv = sorted(sub_diffLevel.items(), key=lambda x: x[1], reverse=True)
print(sorted_sub_diffLv)

study_hours = int(input("enter the number of hours you want to study : "))
total_weight = sum(sub_diffLevel.values())
for key, value in sub_diffLevel.items():
    time_for_sub = (value / total_weight) * study_hours
    print(f"time allocated for {key} = {time_for_sub:.2f} hours")